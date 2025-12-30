<script setup lang="ts">
import { computed, nextTick, ref, watch } from 'vue'
import { streamChat } from '@/api/chat'

interface Message {
  role: 'user' | 'bot'
  text: string
}

const messages = ref<Message[]>([])
const messagesRef = ref<HTMLElement | null>(null)
const sessionId = Math.random().toString(36).substring(2, 15)
const input = ref('')
const isStreaming = ref(false)
let controller: AbortController | null = null

const isAtBottom = computed(() => {
  if (!messagesRef.value) return true
  const el = messagesRef.value
  return el.scrollHeight - el.scrollTop - el.clientHeight < 50
})

const scrollToBottom = () => {
  nextTick(() => messagesRef.value && (messagesRef.value.scrollTop = messagesRef.value.scrollHeight))
}

const updateBotMsg = (text: string) => {
  const lastMsg = messages.value[messages.value.length - 1]
  if (lastMsg?.role === 'bot') {
    lastMsg.text += text
  }
}

const send = async () => {
  if (!input.value) return

  const question = input.value
  controller = new AbortController()
  isStreaming.value = true

  messages.value.push({ role: 'user', text: question }, { role: 'bot', text: '' })
  if (isAtBottom.value) scrollToBottom()

  try {
    await streamChat(
      { sessionId, question, provider: 'openai' },
      (chunk: string) => {
        updateBotMsg(chunk.split('\n\n').join(''))
        scrollToBottom()
        isStreaming.value = false
      },
      controller.signal
    )
  } catch (err) {
    updateBotMsg('ChatBot is busy.\nPlease try again later.')
    console.error(err)
    isStreaming.value = false
  }
  input.value = ''
}

const stopStream = () => {
  controller?.abort()
  isStreaming.value = false
}

watch(messages, scrollToBottom, { deep: true })
</script>

<template>
  <div class="chat" :style="{ '--chat-height': messages.length ? '100%' : 'auto' }">
    <div ref="messagesRef" class="messages" :style="{ '--padding': messages.length ? '12px' : '0' }">
      <div v-for="(m, i) in messages" :key="i" :class="`msg ${m.role}`">
        <div class="avatar">
          <img v-if="m.role === 'user'" src="@/assets/user-avatar.svg" alt="User Avatar" />
          <img v-else src="@/assets/bot-avatar.svg" alt="Bot Avatar" />
        </div>
        <div class="msg-content">
          {{ m.text }}
          <span v-if="isStreaming && m.role === 'bot' && !m.text" class="cursor">|</span>
        </div>
      </div>
    </div>

    <div class="question">
      <input v-model="input" v-focus-slash :disabled="isStreaming" @keyup.enter="send"
        placeholder="Ask about the story..." autofocus />
      <kbd v-show="!isStreaming && !input">/</kbd>
      <button v-show="!isStreaming && input" class="send-button" @click="send">&#8593;</button>
      <button v-show="isStreaming" class="stop-button" @click="stopStream">&#9632;</button>
    </div>
  </div>
</template>

<style lang="scss">
.chat {
  width: 100%;
  height: var(--chat-height);
  display: flex;
  flex-direction: column;
}

.messages {
  flex: 1;
  overflow-y: auto;
  padding: var(--padding);
}

.msg {
  margin-bottom: 8px;
  display: flex;
  align-items: flex-start;
  gap: 12px;

  &.user,
  &.bot {
    display: flex;
    align-items: center;

    .msg-content {
      white-space: pre-wrap;
      padding: 12px 24px;
      max-width: 70%;
      border-radius: 30px;
      word-wrap: break-word;
      font-size: 1.2em;
      width: fit-content;
    }
  }

  &.user {
    margin-left: auto;
    justify-content: flex-end;

    .msg-content {
      background-color: var(--color-background-mute);
      text-align: right;
    }

    .avatar {
      order: 2;
    }
  }

  &.bot {

    .msg-content {
      background-color: var(--color-background-mute);
      text-align: left;
    }

    .avatar {
      transform: rotate(180deg);
    }
  }


  .avatar {
    flex-shrink: 0;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    overflow: hidden;
  }
}

.question {
  padding: 12px 24px;
  width: 100%;
  border-radius: 35px;
  background-color: var(--color-background-mute);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;

  input {
    flex: 1;
    width: 100%;
    padding: 10px;
    font-size: 1.2em;
    background-color: transparent;
    border: none;
    color: var(--color-text);

    &::placeholder {
      color: var(--color-border);
    }

    &:focus {
      outline: none;
    }
  }

  kbd {
    background-color: var(--color-background);
    border-radius: 4px;
    padding: 4px 8px;
    font-size: 0.9em;
    color: var(--color-text);
    margin-right: 4px;
  }

  .stop-button,
  .send-button {
    margin-left: auto;
    background-color: var(--color-text);
    border: none;
    color: var(--color-background);
    font-size: 1.2em;
    border-radius: 50%;
    width: 38px;
    height: 38px;
    cursor: pointer;

    &:hover {
      background-color: var(--color-border-hover);
    }
  }
}

.cursor {
  animation: blink 1s infinite;
}

@keyframes blink {
  50% {
    opacity: 0;
  }
}
</style>
