<template>
  <div>
    <h1>Login Page</h1>
    <form @submit.prevent="login">
      <input type="text" v-model="username" placeholder="Username" required />
      <input type="password" v-model="password" placeholder="Password" required />
      <button type="submit">Login</button>
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
    async login() {
      try {
        const response = await axios.post("http://127.0.0.1:5000/login", {
          username: this.username,
          password: this.password,
        });

        alert(response.data.message);
      } catch {
        alert("Invalid credentials");
      }
    },
  },
};
</script>
