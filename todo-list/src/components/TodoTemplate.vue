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
    this.onRead()
  },
  methods: {
    onRead() {
      axios
        .get('/api/lists')
        .then(response => {
          this.todos = response.data
          console.log('현재 todos', this.todos)
        })
        .catch(error => {
          alert('데이터를 불러올 수 없습니다.')
          console.log(error)
        })
    },
    onCreate(text) {
      const newTodoItem = { content: text }
      axios
        .post('/api/add_todo', newTodoItem)
        .then(() => {
          console.log('데이터 생성 완료', newTodoItem)
          this.onRead() // 데이터 생성 시 추가된 리스트 새롭게 불러오기
        })
        .catch(error => {
          alert('데이터 생성 실패')
          console.log(error)
        })
    },
    onUpdate(id, text) {
      const editedTodo = { content: text }
      axios
        .put(`/api/edit_todo/${id}`, editedTodo)
        .then(() => {
          console.log('데이터 수정 완료')
          this.onRead() // 데이터 수정 시 수정된 리스트 새롭게 불러오기
        })
        .catch(error => {
          alert('데이터 수정 실패')
          console.log(error)
        })
    },
    onDelete(id) {
      // this.todos = this.todos.filter(todo => todo.id !== id)
      axios
        .delete(`/api/delete_todo/${id}`)
        .then(() => {
          console.log('데이터 삭제 완료')
          this.onRead() // 데이터 삭제 시 리스트 새롭게 불러오기
        })
        .catch(error => {
          alert('데이터 삭제 실패')
          console.log(error)
        })
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
