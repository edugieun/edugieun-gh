<template>
    <div>
      <h1>Algorithm Page</h1>
      <algo-list :problems="problems" @problemSelect="onProblemSelect"></algo-list>
    </div>
</template>

<script>
import axios from 'axios'
import AlgoList from '../components/AlgoList'
import router from '../router'

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
    },
    onProblemSelect(problem) {
      this.$emit('problemSelect', problem)
      router.push({ path: `/algorithm/problem/${problem.code_url}`})
    }
  },
  mounted() {
    this.getproblems()
  }
}
</script>

<style>

</style>