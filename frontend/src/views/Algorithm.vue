<template>
    <div>
      <h1>Algorithm Page</h1>
      <algo-list :problems="problems"></algo-list>
    </div>
</template>

<script>
import axios from 'axios'
import AlgoList from '../components/AlgoList'

export default {
  name: 'Algorithm',
  components: {
    AlgoList,
  },
  data() {
    return {
      problems: [],
    }
  },
  methods: {
    getproblems() {
      axios.get('http://127.0.0.1:8000/api/v1/problems/')
      .then(res => {
        this.problems = res.data
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  mounted() {
    this.getproblems()
  }
}
</script>

<style>

</style>