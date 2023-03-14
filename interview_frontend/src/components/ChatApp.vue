<template>
    <main class="main" :class="{ 'loading': loading }">
      <ChatLoading v-if="loading"></ChatLoading>
      <div class="message-list-container">
        <message-list :messages="messages" class="message-list" />
      </div>
      <div class="message-input-container">
        <message-input @message-added="onMessageAdded" @evaluate="onEvaluate" class="message-input" />
      </div>
    </main>
  </template>
  
  <style scoped> 
  .main {
    flex: 1;
    display: flex;
    flex-direction: column;
    pointer-events: auto;
  }
  
.main.loading {
  pointer-events: none;
}

  .message-list-container {
    flex: 1;
    overflow-y: auto; /* add scrollbar when message list exceeds container height */
    max-width: 40rem;
    max-height: calc(100vh - 20rem); /* set maximum height */
    margin: 0 auto;
    padding: 1rem;
  }
  
  .message-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  
  .message-input-container {
    position: sticky;
    bottom: 0;
    z-index: 1; /* ensure message input is above message list */
    padding: 1rem;
    background-color: #fff;
  }
  
  .message-input {
    width: 100%;
  }
  </style>  
  
  <script>
  import axios from "axios";
  import MessageList from "./MessageList.vue";
  import MessageInput from "./MessageInput.vue";
  import ChatLoading from './ChatLoading.vue';

  export default {
    data() {
      return {
        messages: [],
        loading: false,
      };
    },
    mounted() {
      const searchParams = new URLSearchParams(this.$route.query)
      this.token = searchParams.get('token')
      this.loading = true; 
      axios
        .post(`/api/chat/${this.token}`, {}, {
            headers: {
            "Content-Type": "application/json"
            }
        })
        .then((response) => {
          if(Array.isArray(response.data)) {
            this.messages.push(...response.data);
          } else {
            this.messages.push(response.data);
          }
          this.loading = false; 
        })
        .catch((error) => {
          console.error(error);
          this.loading = false; 
        });
    },
    components: {
      MessageList,
      MessageInput,
      ChatLoading,
    },
    methods: {
      onMessageAdded(message) {
        const searchParams = new URLSearchParams(this.$route.query)
        this.token = searchParams.get('token')
        this.messages.push(message);
        this.loading = true; 
        axios
          .post(`/api/chat/${this.token}`, message)
          .then((response) => {
            this.messages.push(response.data);
            this.loading = false; 
          })
          .catch((error) => {
            console.error(error);
            this.loading = false; 
          });
      },
      onEvaluate() {
        const searchParams = new URLSearchParams(this.$route.query)
        this.token = searchParams.get('token')
        this.loading = true; 
        axios
          .post(`/api/evaluate/${this.token}`)
          .then((response) => {
            this.messages.push(response.data);
            this.loading = false; 
         })
          .catch((error) => {
            console.error(error);
            this.loading = false; 
          });
      },
    },
  };
  </script>  