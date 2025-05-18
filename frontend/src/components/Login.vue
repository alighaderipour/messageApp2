<template>
    <div>
      <form @submit.prevent="login">
        <input type="text" v-model="username" placeholder="Username" />
        <input type="password" v-model="password" placeholder="Password" />
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return { username: '', password: '' };
    },
    methods: {
      async login() {
        try {
          const response = await axios.post('/api/login', { username: this.username, password: this.password });
          alert(response.data.message);
        } catch {
          alert("Invalid credentials");
        }
      }
    }
  };
  </script>
  