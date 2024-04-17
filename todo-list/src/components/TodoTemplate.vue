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
import axios from 'axios'

export default {
  name: 'TodoApp',
  components: {
    TodoInsert,
    TodoList,
  },
  data() {
    return {
      todos: [],
    }
  },
  mounted() {
    // 컴포넌트가 마운트될 때 getTodo 메서드 호출
    this.getTodo()
  },
  methods: {
    getTodo() {
      axios
        .get('/api/lists')
        .then(response => {
          this.todos = response.data
        })
        .catch(error => {
          alert('데이터를 불러올 수 없습니다.')
          console.log(error)
        })
        .finally(() => {
          console.log('항상 마지막에 실행')
        })
    },
    onCreate(text) {
      const newTodoItem = { content: text }
      axios
        .post('/api/add_todo', newTodoItem)
        .then(() => console.log('데이터 추가 완료', newTodoItem))
        .catch(error => console.log(error))
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
