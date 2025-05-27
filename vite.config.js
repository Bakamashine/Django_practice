import { defineConfig } from 'vite'
import path from 'path'
import djangoVite from 'django-vite'

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
