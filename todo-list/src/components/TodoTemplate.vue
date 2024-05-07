<template lang="pug">
div
  UserBox(:username='username')
  Calendar(class="calendar" @selectedDateTodos="onDate" :memberId="memberId") 
  .boxSize 
    .title To do List  
    TodoInsert(:onCreate="onCreate")

    q-scroll-area(style="height: 24rem;")
        TodoList(
          :memberId="memberId"
          :isPastDate="isPastDate"
          :todos="todos", 
          :onUpdate="onUpdate" 
          :onDelete="onDelete" 
        )
</template>

<script>
import Calendar from './Calendar.vue'
import TodoInsert from './TodoInsert.vue'
import TodoList from './TodoList.vue'
import axios from 'axios'
import { getCurrentDate } from '../utils/date'
import { mapState } from 'vuex'
import UserBox from '../components/UserBox.vue'

export default {
  name: 'TodoApp',
  components: {
    UserBox,
    Calendar,
    TodoInsert,
    TodoList,
  },
  props: {
    pastTodos: Array,
  },
  data() {
    return {
      username: '',
      memberId: null,
      todos: [],
      isPastDate: false,
    }
  },
  mounted() {
    // 컴포넌트가 마운트될 때 getTodo 메서드 호출
    this.onRead()
  },
  computed: {
    ...mapState(['userInfo']),
  },
  methods: {
    onDate(selectedTodos, selectedDate) {
      this.todos = selectedTodos
      console.log(selectedDate, ' todos', selectedTodos)

      const today = new Date()
      if (selectedDate !== getCurrentDate(today)) {
        this.isPastDate = true
      } else {
        this.isPastDate = false
      }
    },
    onRead() {
      const token = localStorage.getItem('token')
      axios
        .get('/api/lists', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then(response => {
          this.todos = response.data.lists
          console.log('현재 todos', this.todos)

          const user = response.data.user
          this.username = user.user_name
          this.memberId = user.user_id
        })
        .catch(error => {
          alert('데이터를 불러올 수 없습니다.')
          console.log(error)
        })
    },
    onCreate(text) {
      const newTodoItem = {
        member: this.memberId,
        content: text,
      }
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
      const editedTodo = {
        member: this.memberId,
        content: text,
      }
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

<style lang="stylus" scoped>
.calendar
  background-color: #F6D8CE;
  width: 13rem;
  height: 2.2rem;
  text-align: center;
  border-radius: 0.7rem;

.boxSize
  width: 35rem;
  border-radius: 0.3rem 0.3rem 0 0;
  box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
  margin: auto;
  margin-top: 1rem;
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
