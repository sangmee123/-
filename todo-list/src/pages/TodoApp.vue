<template lang="pug">
.todoApp
  TodoTemplate
</template>

<script>
import Login from './Login.vue'
import TodoTemplate from '../components/TodoTemplate.vue'

export default {
  name: 'TodoApp',
  components: {
    Login,
    TodoTemplate,
  },
}
</script>

<style lang="stylus" scoped>
.todoApp
  text-align: center;
  margin-top: 3rem;
</style>
