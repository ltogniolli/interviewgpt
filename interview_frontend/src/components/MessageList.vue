<template>
    <div class="message-list">
      <div v-for="message in messages" :key="message.id" :class="{ 'user-message': message.role === 'user', 'assistant-message': message.role === 'assistant' }">
        <div class="message-content">{{ message.content }}</div>
      </div>
    </div>
  </template>
  
  <style>
  .message-list {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }
  
  .user-message {
    align-self: flex-end;
    background-color: #ddeeff;
    color: #333;
    border-radius: 1rem 1rem 0 1rem;
    padding: 0.5rem 1rem;
    max-width: 60%;
    font-family: sans-serif;
    font-size: 1rem;
    line-height: 1.5;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  }
  
  .assistant-message {
    align-self: flex-start;
    background-color: #fff;
    color: #333;
    border-radius: 1rem 1rem 1rem 0;
    padding: 0.5rem 1rem;
    max-width: 60%;
    font-family: sans-serif;
    font-size: 1rem;
    line-height: 1.5;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
  }
  html, body {
    overflow: hidden;
  }
  </style>  
  
  <script>
  export default {
    props: {
      messages: {
        type: Array,
        required: true,
      },
    },
  };
  </script>  