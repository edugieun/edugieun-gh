<template>
  <li @click="onProblemSelect(problem)">{{ problem.prob_diff }} // {{ problem.prob_name }}</li>
</template>

<script>
  export default {
    name: 'AlgoListItem',

    props: {
      problem: {
        type: Object
      }
    },
    methods: {
      onProblemSelect(problem) {
        this.$emit('problemSelect', problem)
      }
    }
  }
</script>

<style>

</style>