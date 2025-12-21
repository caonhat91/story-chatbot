<script setup lang="ts">
import { computed, nextTick, ref, watch } from 'vue'
import { streamChat } from '@/api/chat'

const messages = ref<Array<{ role: string, text: string }>>([]);
const messagesRef = ref<HTMLElement | null>(null);
const sessionId = Math.random().toString(36).substring(2, 15);
const input = ref('')
let controller: AbortController | null = null
const isStreaming = ref(false)

const isAtBottom = computed(() => {
  if (!messagesRef.value) return true
  const el = messagesRef.value
  return el.scrollHeight - el.scrollTop - el.clientHeight < 50
});

function scrollToBottom() {
  nextTick(() => {
    if (messagesRef.value) {
      messagesRef.value.scrollTop =
        messagesRef.value.scrollHeight
    }
  })
}

const send = () => {
  const question = input.value;
  if (!question) return;

  controller = new AbortController();
  isStreaming.value = true;

  messages.value.push({ role: "user", text: question });
  messages.value.push({ role: "bot", text: "" });

  if (isAtBottom.value) {
    scrollToBottom();
  }

  const payload = {
    sessionId,
    question,
    history: messages.value.map(m => [m.role, m.text])
  };

  streamChat(payload, (chunk: string) => {
    const lines = chunk.split("\n\n")
    const lastIdx = messages.value.map(m => m.role).lastIndexOf('bot');

    for (const line of lines) {
      if (line.startsWith("data:")) {
        const json = line.replace("data:", "").trim()
        const data = JSON.parse(json)
        if (lastIdx >= 0 && messages.value[lastIdx]) {
          messages.value[lastIdx].text += data.token
        }
      }
    }

    scrollToBottom();
    isStreaming.value = false;
  }, controller.signal).catch((err) => {
    const lastIdx = messages.value.map(m => m.role).lastIndexOf('bot');
    if (lastIdx >= 0 && messages.value[lastIdx]) {
      messages.value[lastIdx].text += 'ChatBot is busy.';
    }
    setTimeout(() => {
      if (lastIdx >= 0 && messages.value[lastIdx]) {
        messages.value[lastIdx].text += '\nPlease try again later.';
      }
    }, 100);
    console.error(err);
    isStreaming.value = false;
  });

  input.value = "";
};

const stopStream = () => {
  if (!controller) {
    return;
  }
  controller.abort();
  isStreaming.value = false;
};

watch(messages, scrollToBottom, { deep: true });
</script>

<template>
  <div class="chat">
    <div class="messages" ref="messagesRef">
      <div v-for="(m, i) in messages" :key="i" :class="'msg ' + (m.role === 'user' ? 'user' : 'bot')">
        <div class="avatar">
          <img v-if="m.role === 'user'" src="@/assets/user-avatar.svg" alt="User Avatar" />
          <img v-else src="@/assets/bot-avatar.svg" alt="Bot Avatar" />
        </div>
        <div class="msg-content">
          {{ m.text }}
          <span v-if="isStreaming && m.role === 'bot' && !m.text" class="cursor">▍</span>
        </div>
      </div>
    </div>

    <div class="question">
      <input v-model="input" v-focus-slash :disabled="isStreaming" @keyup.enter="send"
        placeholder="Ask about the story..." autofocus />
      <kbd v-if="!isStreaming">/</kbd>
      <button v-if="isStreaming" class="stop-button" @click="stopStream">&#9632;</button>
    </div>
  </div>
</template>

<style lang="scss">
.chat {
  margin: auto;
  width: 100%;
  max-width: 80vw;
  min-height: 60vh;
  display: flex;
  flex-direction: column;
}

.messages {
  flex: 1;
  overflow-y: auto;
  padding: 12px;
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

  .stop-button {
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
