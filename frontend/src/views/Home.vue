<template>
  <div class="home">
    <h1>test</h1>
    <img alt="Vue logo" src="../assets/logo.png">
  </div>
</template>

<script>
  import axios from 'axios'
  // import fetch from 'node-fetch'
  export default {
    name: 'Home',
    methods: {
      getSource() {
        axios.get('https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py')
        .then(res => {
          console.log(res.data)
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
    mounted() {
      this.getSource()
    }
  }
</script>