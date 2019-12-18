<template>

  <div v-html="codeHtml">
    {{ codeHtml }}
  </div>
</template>

<script>
  export default {
    name: 'AlgoDetail',
    data() {
      return {
        selectedProblem: JSON.parse(localStorage.getItem('localproblem')),
        codeHtml: 'ad'
      }
    },
    methods: {
      getdata: function (data) {
        console.log(data)
        this.codeHtml = data
      }
    },
    mounted() {
      var request = require("request");

      function getpage(link, callback) {
        request({
          url: link,
        }, function (error, response, body) {
          let start = 0
          let end = 0
          for (let i = 0; i < body.length; i++) {
            if (body[i] === '<' && body[i + 1] === 't' && body[i + 2] === 'a' && body[i + 3] === 'b' && body[i +
              4] === 'l') {
              start = i
            }
            if (body[i] === '/' && body[i + 1] === 't' && body[i + 2] === 'a' && body[i + 3] === 'b' && body[i +
              4] === 'l') {
              end = i + 8
              let table_ele = ''
              for (i = start; i < end; i++) {
                table_ele = table_ele + body[i]
              }
              callback(table_ele)
            }
          }
        })
      }
      getpage("https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py", this.getdata)


      // let table_ele = ''
      // request({
      //   url: this.selectedProblem.code_url,
      // }, function (error, response, body) {
      //   let start = 0
      //   let end = 0
      //   // console.log(body)
      //   for (let i = 0; i < body.length; i++) {
      //     if (body[i] === '<' && body[i + 1] === 't' && body[i + 2] === 'a' && body[i + 3] === 'b' && body[i +4] === 'l') {
      //       start = i
      //     }
      //     if (body[i] === '/' && body[i + 1] === 't' && body[i + 2] === 'a' && body[i + 3] === 'b' && body[i +4] === 'l') {
      //       end = i + 8
      //       // let table_ele = ''
      //       for (i = start; i < end; i++) {
      //         table_ele = table_ele + body[i]
      //       }
      //       // console.log(table_ele)
      //       // console.log(this.codeHtml)
      //       // this.codeHtml = table_ele
      //       this.codeSave(3)

      //       break
      //     }
      //   }
      // })
    }
  }
</script>

<style>

</style>