import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  base: '/news-archive/', // Set the base path for GitHub Pages
  build: {
    outDir: 'build', // Default build folder (can be 'dist' if you're using that)
  },
})
