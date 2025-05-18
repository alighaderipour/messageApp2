import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  plugins: [vue()],
  root: "./",
  build: {
    rollupOptions: {
      input: "index.html",
    },
  },
  resolve: {
    alias: {
      "@": "/src",
    },
  },
});
