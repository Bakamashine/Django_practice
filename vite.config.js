import { defineConfig } from 'vite'
import path from 'path'

export default defineConfig({
  base: '/static/',
  build: {
    outDir: 'static/dist',
    manifest: true,
    emptyOutDir: true,
    rollupOptions: {
      input: path.resolve(__dirname, 'src/main.js'), // Adjust entrypoint if needed
    },
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
  server: {
    cors: true,
    //   watch: {
    //     usePolling: true
    //   }
  },
})
