<template lang="pug">
.todo-wrapper
  .flex
    DatePicker(@update:date="updateDate")
    form.logout_form(@submit.prevent="logoutForm")
      q-btn.logout(type="submit" ) 로그아웃
  .todoapp
    ColorPicker(v-model="textColor")

    input.new-todo(autofocus, :style="{color: '#' + textColor}", @keyup.enter="addTodo")

    section.main 
      input.toggle-all#toggle-all(type="checkbox", :checked="remaining === 0", @change="toggleAll")
      label(for="toggle-all") 모두 완료표시하기
      ul.todo-list
        Items(v-for="todo in filteredTodos" 
        :key="todo.id" 
        :todo="todo" 
        :editedTodo="editedTodo" 
        @complete="handleComplete" 
        @remove="removeTodo"
        @edit="editTodo" 
        @doneEdit="doneEdit" 
        @cancelEdit="cancelEdit"
        )

    footer.footer
      span.todo-count
        strong {{ remaining }}
        span 개 남음
      ul.filters
        li
          q-btn.btn(label="전체", :class="{ selected: visibility === 'all' }")(@click="handleFilter('all')")
        li 
          q-btn.btn(label="진행중", :class="{ selected: visibility === 'active' }")(@click="handleFilter('active')")
        li
          q-btn.btn(label="완료", :class="{ selected: visibility === 'completed' }")(@click="handleFilter('completed')")
      q-btn.clear-completed(style="background: #307fe2, color: white", label="완료 모두삭제")( @click="removeCompleted")

</template>

<script>
import axios from 'axios';
import ColorPicker from 'src/components/TodoList/ColorPicker.vue';
import Items from 'src/components/TodoList/Items.vue';
import DatePicker from 'src/components/TodoList/DatePicker.vue';

const STORAGE_KEY = 'vue-todomvc';

export default {
  components: {
    ColorPicker,
    Items,
    DatePicker
  },

  data: () => ({
    todos: [],
    editedTodo: null,
    visibility: 'all',
    textColor: '343a40',
    date: new Date().toISOString().substr(0, 10),
    isSubmitting: false
  }),

  computed: {
    active() {
      return this.todos.filter(todo => !todo.done);
    },
    completed() {
      return this.todos.filter(todo => todo.done);
    },
    filteredTodos() {
      if (this.visibility === 'all') return this.todos;
      else if (this.visibility === 'active') return this.active;
      return this.completed;
    },
    remaining() {
      return this.todos.filter(todo => !todo.done).length;
    },
  },

  mounted() {
    this.fetchTodos();
    // this.naverAuth();
  },

  methods: {
    async logoutForm() {
        if (this.isSubmitting) return;
        this.isSubmitting = true; 
        try {
            await axios.get('/api/logout');
            this.$router.push('/'); // 페이지 리로드 x
        } catch (error) {
            console.error(error)
        } finally {
            this.isSubmitting = false
        }
    },
    updateDate(date) {
      this.date = date.replace(/\//g, '-');
      this.fetchTodos();

    },
    // naverAuth(){
    //   axios.get('/api/naver_auth')
    //   .then(response => {
    //       console.log('naverAuth 데이터 가져오기 성공', response.data);
    //     })
    //   .catch(error => {
    //     console.error('naverAuth 에러:', error);
    //   });
    // },
    // READ
    fetchTodos() {
      axios
        .get(`/api/read_todo/${this.date}`)
        .then(response => {
          console.log('데이터 가져오기 성공', response.data);
          this.todos = response.data;
        })
        .catch(error => {
          console.error('Error fetching todos:', error);
        });
    },
    // CREATE
    addTodo(e) {
      const value = e.target.value.trim();
      if (!value) {
        return;
      }
      const newTodo = {
        text: value,
        date: this.date,
        done: false,
        color: this.textColor,
      };
      axios
        .post('/api/add_todo', newTodo)
        .then(response => {
          this.todos = [...this.todos, response.data]; // 추가된 데이터가 화면에 바로 업데이트 할 수 있도록 해줌
          console.log('데이터 추가 성공', response.data);
        })
        .catch(error => {
          console.error('데이터 추가 실패!:', error);
        });
      e.target.value = '';
    },
    // UPDATE
    doneEdit(todo) {
      if (!this.editedTodo) {
        return;
      }
      this.editedTodo = null;
      todo.text = todo.text.trim();
      if (!todo.text) {
        this.removeTodo(todo);
      }
      axios.put(`/api/edit_todo/${todo.id}`, todo).catch(error => {
        console.error('Error updating todo:', error);
      });
    },

    editTodo(todo) {
      this.beforeEditCache = todo.text;
      this.editedTodo = todo;
    },
    cancelEdit(todo) {
      this.editedTodo = null;
      todo.text = this.beforeEditCache;
    },
    handleComplete(todo) {
      todo.done = !todo.done
      axios
      .put(`/api/edit_todo/${todo.id}`, todo)
      .catch(error => {
        console.error('Error updating todo:', error);
      });
    },
    // DELETE
    removeTodo(todo) {
      axios
        .delete(`/api/delete_todo/${todo.id}`)
        .then(() => {
          this.todos = this.todos.filter(t => t !== todo);
        })
        .catch(error => {
          console.error('Error removing todo:', error);
        });
    },
    
    removeCompleted(){
      const completedTodos = this.todos.filter(todo => todo.done);

      completedTodos.forEach(todo => {
        axios
          .delete(`/api/delete_todo/${todo.id}`)
          .then(() => {
            this.todos = this.todos.filter(t => t !== todo);
          })
          .catch(error => {
            console.error('Error removing completed todo:', error);
          });
      });
    },
    handleFilter(filter) {
      this.visibility = filter;
    },
    toggleAll(e) {
      const isChecked = e.target.checked;
      this.todos.forEach(todo => {
        todo.done = isChecked;
      });
    },
  },
};
</script>

<style lang="stylus">
@import '../css/todo.styl'
</style>
