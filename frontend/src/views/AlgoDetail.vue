<template>

  <div v-html="codeHtml">
    <!-- {{ codeHtml }} -->
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'AlgoDetail',
    data() {
      return {
        selectedProblem: JSON.parse(localStorage.getItem('localproblem')),
        codeHtml: ''
      }
    },
    methods: {
      getSource() {

        // 1. CORS 에러로 인해 Django 서버로 데이터를 보내 처리 후 다시 vue로 받는 방법
        // console.log(this.selectedProblem)
        // let probNum = this.selectedProblem.id
        // axios.get(`http://edugieungp.xvjby8f4xg.ap-northeast-2.elasticbeanstalk.com/api/v1/problems/${probNum}`)
        // .then(res => {
        //   this.codeHtml = res.data
        // })
        // .catch(err => {
        //   console.log(err)
        // })

        // 2. vue.config.js 파일의 proxy 도메인 일치 후 vue 내부에서 처리하는 방법
        // let probNum = this.selectedProblem.id
        axios.get({
          baseURL: `https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py`,
          // headers: {'X-Custom-Header': 'foobar'}
        })
        .then(res => {
          // this.codeHtml = res.data
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })

      }
      // getdata: function (data) {
      //   console.log(data)
      //   this.codeHtml = data
      // }
    },
    mounted() {
      this.getSource()
      // var request = require("request");

      // function getpage(link, callback) {
      //   request({
      //     url: link,
      //   }, function (error, response, body) {
      //     let start = 0
      //     let end = 0
      //     for (let i = 0; i < body.length; i++) {
      //       if (body[i] === '<' && body[i + 1] === 't' && body[i + 2] === 'a' && body[i + 3] === 'b' && body[i +
      //         4] === 'l') {
      //         start = i
      //       }
      //       if (body[i] === '/' && body[i + 1] === 't' && body[i + 2] === 'a' && body[i + 3] === 'b' && body[i +
      //         4] === 'l') {
      //         end = i + 8
      //         let table_ele = ''
      //         for (i = start; i < end; i++) {
      //           table_ele = table_ele + body[i]
      //         }
      //         callback(table_ele)
      //       }
      //     }
      //   })
      // }
      // getpage("https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py", this.getdata)
      // var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
      // function reqListener () {
      //   console.log(3)
      //   console.log(this.responseText);
      // }

      // var oReq = new XMLHttpRequest();
      // oReq.addEventListener("load", reqListener);
      // oReq.open("GET", "https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py");
      // oReq.send();
    }
  }
</script>

<style>

</style>