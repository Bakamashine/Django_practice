import { defineConfig } from 'vite'
import path from 'path'
export default defineConfig({
  base: '/static/',
  resolve: {
          alias: {
                  '@': path.resolve("./static")
          }
  },
  build: {
    manifest: "manifest.json",
    outDir: path.resolve("./assets"),
    assetsDir: "django-assets",
    rollupOptions: {
           input: path.resolve("./static/js/main.js")
    },
  },
})
