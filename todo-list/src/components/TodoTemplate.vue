<template lang="pug">
div
  .title To do List
  TodoInsert(:onCreate="onCreate")

  q-scroll-area(style="height: 24rem;")
      TodoList(:todos="todos", :onUpdate="onUpdate" :onDelete="onDelete")
</template>

<script>
import TodoInsert from '../components/TodoInsert.vue'
import TodoList from '../components/TodoList.vue'

export default {
  name: 'TodoApp',
  components: {
    TodoInsert,
    TodoList,
  },
  data() {
    return {
      todos: [
        { id: 0, content: 'vue 공부하기' },
        { id: 1, content: '퇴근하기' },
        { id: 2, content: '블로그 글 남기기' },
        { id: 3, content: '점심 먹기' },
      ],
    }
  },
  methods: {
    onCreate(text) {
      const todo = {
        id: this.todos.length + 1,
        content: text,
      }
      this.todos.push(todo)
    },
    onUpdate(id, text) {
      this.todos[id].content = text
      console.log('todos', this.todos)
    },
    onDelete(id) {
      this.todos = this.todos.filter(todo => todo.id !== id)
    },
  },
}
</script>

<style lang="stylus">
.title
    background: #F6D8CE;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    height: 4rem;
    font-size: 1.5rem;
    font-weight: bold;
    border-radius: 0.3rem 0.3rem 0 0;
</style>
