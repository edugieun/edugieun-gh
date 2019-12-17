<template>
  <div>
    {{ problem }}
  </div>
</template>

<script>
  export default {
    name: 'AlgoDetail',
    data() {
    return {
      problem: this.$route.params.problem,
    }
  },
  }
</script>

<style>

</style>