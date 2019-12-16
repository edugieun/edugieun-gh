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
      <li v-for="problem in problems" :key="problem.id">
        <div> {{ problem.prob_name }} // {{problem.prob_diff }}</div>
      </li>
    </ol>
    <ol v-else>
      <li v-for="problem in sorted_problems" :key="problem.id">
        <div> {{ problem.prob_name }} // {{problem.prob_diff }}</div>
      </li>
    </ol>

  </div>
</template>

<script>
  export default {
    name: 'AlgoList',
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
      }
    },


  }
</script>

<style>

</style>