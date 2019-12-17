<template>
  <div class="algo-list">
    <h1>AlgoList</h1>
    <select v-model="difficulty" @click="sortedProblem">
      <option value="all">All</option>
      <option value="D1">D1</option>
      <option value="D2">D2</option>
      <option value="D3">D3</option>
    </select>

    <ol v-if="difficulty === 'all'">
      <algo-list-item v-for="problem in problems" :key="problem.id" :problem="problem" @problemSelect="onProblemSelect"></algo-list-item>
    </ol>
    <ol v-else>
      <algo-list-item v-for="problem in sorted_problems" :key="problem.id" :problem="problem" @problemSelect="onProblemSelect"></algo-list-item>
    </ol>

  </div>
</template>

<script>
  import AlgoListItem from './AlgoListItem'
  export default {
    name: 'AlgoList',
    components: {
      AlgoListItem,
    },
    data: function() {
      return {
        difficulty: 'all',
        sorted_problems: [],
      }
    },
    props: {
      problems: {
        type: Array,
      }
    },
    methods: {
      sortedProblem: function(){
        this.sorted_problems = this.problems.filter(problem => problem.prob_diff == this.difficulty)
      },
      onProblemSelect(problem) {
        this.$emit('problemSelect', problem)
      }
    },


  }
</script>

<style>

</style>