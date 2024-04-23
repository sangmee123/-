<template lang="pug">
.todoApp
  TodoTemplate
</template>

<script>
import Calendar from '../components/Calendar.vue'
import TodoTemplate from '../components/TodoTemplate.vue'

export default {
  name: 'TodoApp',
  components: {
    Calendar,
    TodoTemplate,
  },
}
</script>

<style lang="stylus">
.todoApp
  text-align: center;
  margin-top: 5rem;
</style>
