module.exports = {
  publicPath: '/edugieun-gh/',
  devServer: {
    proxy: {
      '/':{
        target: 'https://github.com/'
      }
    }
  },
}