import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import Login from "@/views/Login.vue"; // Ensure this file exists

const routes = [
  { path: "/", component: Home },
  { path: "/home", component: Home }, // Ensure this exists
  { path: "/login", component: Login },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
