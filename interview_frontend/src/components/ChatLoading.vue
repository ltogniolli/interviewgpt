<template>
  <div class="loading">
    <div class="spinner"></div>
  </div>
</template>

<style scoped>
.loading {
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(255, 255, 255, 0.7); 
  pointer-events: none; 
}

.spinner {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  border: 5px solid #ccc;
  border-top-color: #555;
  animation: spinner 1s linear infinite;
}

@keyframes spinner {
  to {transform: rotate(360deg);}
}
</style>