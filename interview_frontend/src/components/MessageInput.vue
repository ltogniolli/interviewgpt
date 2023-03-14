<template>
    <div class="message-input">
      <textarea v-model="inputText" class="input-box" placeholder="Digite sua resposta aqui"></textarea>
      <div class="button-container">
        <button class="send-button" @click="addMessage">Enviar</button>
        <button class="evaluate-button" @click="evaluateMessages">Avaliar</button>
      </div>
    </div>
  </template>
  
  <style scoped>
  .message-input {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 1rem;
  }
  
  .input-box {
    flex: 1;
    height: 5rem;
    padding: 1rem;
    font-family: sans-serif;
    font-size: 1rem;
    line-height: 1.5;
    border: 1px solid #ddd;
    border-radius: 0.5rem;
    resize: vertical; 
  }
  
  .send-button {
    background-color: #5cb85c;
    color: #fff;
    font-family: sans-serif;
    font-size: 1rem;
    border: none;
    border-radius: 0.5rem;
    padding: 0.5rem 1rem;
    cursor: pointer;
    transition: background-color 0.2s ease-in-out;
  }
  
  .send-button:hover {
    background-color: #4cae4c;
  }

  .evaluate-button {
    background-color: #d9534f;
    color: #fff;
    font-family: sans-serif;
    font-size: 1rem;
    border: none;
    border-radius: 0.5rem;
    padding: 0.5rem 1rem;
    cursor: pointer;
    transition: background-color 0.2s ease-in-out;
  }

  .evaluate-button:hover {
    background-color: #c9302c;
  }

  .button-container {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
</style>
  
  
  <script>
  export default {
    data() {
      return {
        inputText: "",
      };
    },
    methods: {
      addMessage() {
        if (this.inputText.trim() === "") {
            return;
        }
        this.$emit("message-added", {
          role: "user",
          content: this.inputText,
        });
        this.inputText = "";
      },
      evaluateMessages() {        
        this.$emit("evaluate");
      },
    },
  };
  </script>  