import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    port: 4000,
    open: true,
    cors: true
  },
  build: {
    outDir: 'dist',
    sourcemap: true
  }
});