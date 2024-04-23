<template lang="pug"> 
div
    TodoListItem(
      :isPastDate="isPastDate"
      v-for="item in todos" 
      :key="item.id" 
      :item="item" 
      :onUpdate="onUpdate" 
      :onDelete="onDelete" 
    )
</template>

<script>
import TodoListItem from './TodoListItem.vue'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  props: {
    isPastDate: Boolean,
    todos: {
      type: Array,
      default: () => [],
    },
    onUpdate: Function,
    onDelete: Function,
  },
}
</script>

<style lang="stylus"></style>
