const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  outputDir: '../interview_backend/static', 
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000/',
        ws: false,
        changeOrigin: false
      }
    }
  }
})
