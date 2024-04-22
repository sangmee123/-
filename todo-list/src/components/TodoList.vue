<template lang="pug"> 
div
    TodoListItem(
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
    todos: {
      type: Array,
      default: () => [],
    },
    onUpdate: Function,
    onDelete: Function,
  },
  methods: {
    // handleCheck(isCheck) {
    //   this.$emit('handleCheck', isCheck)
    // },
  },
}
</script>

<style lang="stylus"></style>
