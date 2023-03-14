<template>
  <div class="component-content">
    <label for="opening">Vaga:</label>
    <select id="opening" v-model="selectedOpening">
      <option value="">Selecione uma opção</option>
      <option v-for="opening in openings" :key="opening.id" :value="opening.id">{{ opening.description }}</option>
    </select>
    <br>
    <label for="name">Nome:</label>
    <input type="text" id="name" v-model="name">
    <button @click="register">Registrar</button>
  </div>
</template>

<style>
.component-content {
  max-width: 600px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 1rem;
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

select,
input {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
  margin-bottom: 1rem;
  width: 100%;
}

button {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  cursor: pointer;
}

button:hover {
  background-color: #0069d9;
}
</style>


  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        openings: [],
        selectedOpening: '',
        name: ''
      }
    },
    async mounted() {
      try {
        const response = await axios.get('/api/openings')
        this.openings = response.data
      } catch (error) {
        console.error(error)
      }
    },
    methods: {
      async register() {
        try {
          if (!this.name || !this.selectedOpening)
            return
          const response = await axios.post('/api/new_session', {
            name: this.name,
            openingId: this.selectedOpening
          })
  
          const token = response.data.token
  
          this.$router.push(`/chat?token=${token}`)
        } catch (error) {
          console.error(error)
        }
      }
    }
  }
  </script>  