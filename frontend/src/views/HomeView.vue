<script setup lang="ts">
import ChatUI from '@/components/ChatUI.vue';
</script>

<template>
  <main>
    <h1>Story Chatbot</h1>
    <h3>Ask questions about the story</h3>
    <ChatUI />
  </main>
</template>

<style scoped>
main {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;

  h1 {
    font-size: 3em;
    margin-bottom: 0;
  }

  h3 {
    margin-top: 4px;
    margin-bottom: 20px;
    color: var(--color-border-hover);
  }
}
</style>