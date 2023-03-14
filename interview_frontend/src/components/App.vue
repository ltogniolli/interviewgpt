<template>
    <div class="chat-app">
      <header class="header">
        <h1>Interview GPT</h1>
      </header>
      <router-view />
      <footer class="footer">
        <p>&copy; 2023 Interview GPT</p>
      </footer>
    </div>
</template>

<style>
  .chat-app {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 100vh;
    font-family: sans-serif;
    font-size: 1rem;
    line-height: 1.5;
    background-color: #f2f2f2;
    color: #333;
    overflow: hidden; /* hide main page scrollbar */
  }
  
  .header {
    background-color: #2196f3;
    color: #fff;
    padding: 1rem;
  }
  
  .header h1 {
    margin: 0;
  }  .footer {
    background-color: #ddd;
    padding: 1rem;
    text-align: center;
  }
  </style>  
  