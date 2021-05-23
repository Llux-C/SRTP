module.exports = {
    devServer:{
        open:true,
        host:"0.0.0.0",
        port:8888,
        proxy: {  //配置跨域
            '/api': {
              target: 'http://127.0.0.1:5000',
              changOrigin: true,  //允许跨域
              pathRewrite: {
                '^/api': '' 
              }
            },
    }
}
}