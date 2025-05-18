<template>
    <div>
      <form @submit.prevent="register">
        <input type="text" v-model="username" placeholder="Username" required />
        <input type="password" v-model="password" placeholder="Password" required />
        <button type="submit">Register</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        username: "",
        password: "",
      };
    },
    methods: {
      async register() {
        try {
          const response = await axios.post("http://127.0.0.1:5000/register", {
            username: this.username,
            password: this.password,
          });
  
          alert(response.data.message);
        } catch {
          alert("Username already exists");
        }
      },
    },
  };
  </script>
  