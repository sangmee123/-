<template lang="pug">
TodoTemplate.boxSize 
</template>

<script>
import TodoTemplate from '../components/TodoTemplate.vue'

export default {
  name: 'TodoApp',
  components: {
    TodoTemplate,
  },
}
</script>

<style lang="stylus">
.boxSize
  width: 35rem;
  border-radius: 0.3rem 0.3rem 0 0;
  box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
  margin: auto;
  margin-top: 6rem;
</style>
