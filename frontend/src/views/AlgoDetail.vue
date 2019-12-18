<template>
  <div>
    {{ selectedProblem }}
  </div>
  
</template>

<script scoped>
  export default {
    name: 'AlgoDetail',
    data() {
      return {
        selectedProblem: JSON.parse(localStorage.getItem('localproblem'))
      }
    },
    mehtods: {
    },
    mounted() {
      // const request = require('request')
      // const selectedProblem = JSON.parse(localStorage.getItem('localproblem'))
      // console.log(3)
      // let xhr = new XMLHttpRequest()
      // xhr.open("GET", 'https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py', false)
      // xhr.send()
      // console.log(xhr.load('https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py'))
      // console.log(xhr)}
      }
  }
</script>

<style>

</style>