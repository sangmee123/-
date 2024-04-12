<template lang="pug">
li(:class="{ completed: todo.completed, editing: todo === editedTodo }")
    .view
      input.toggle(type="checkbox" :checked="todo.done" @change="$emit('complete', todo)")
      label(:style="{ color: '#' + todo.color }" @click="$emit('edit', todo)") {{ todo.text }}
      .q-pa-md.q-gutter-sm.destroy
        q-btn.btn(style="background: #12124f; color: white", label="수정" @click="$emit('edit', todo)")
        q-btn.btn(style="background: #ff6b6b; color: white", label="삭제" @click="$emit('remove', todo)")
    input.edit(v-if="todo === editedTodo", type="text", v-model="todo.text", @blur="$emit('doneEdit', todo)", @keyup.enter="$emit('doneEdit', todo)", @keyup.escape="$emit('cancelEdit', todo)")
</template>

<script>
export default {
  props: {
    todo: Object,
    editedTodo: Object,
  },

  methods: {
    handleComplete(todo) {
      this.$emit('complete', todo);
    },
    editTodo() {
      this.$emit('edit', this.todo);
    },
    removeTodo() {
      this.$emit('remove', this.todo);
    },
    doneEdit(todo) {
      this.$emit('done-edit', todo);
    },
    cancelEdit(todo) {
      this.$emit('cancel-edit', todo);
    },
  },
};
</script>

<style scoped lang="stylus">
.todo-list
  margin: 0
  padding: 0
  list-style: none

.todo-list li
  position: relative
  font-size: 20px
  border-bottom: 1px solid #ededed

.todo-list li:last-child
  border-bottom: none

.todo-list li:hover
  background-color: #d6f1d5

.todo-list li.editing
  border-bottom: none
  padding: 0

.todo-list li.editing .edit
  display: block
  width: calc(100% - 43px)
  padding: 12px 16px
  margin: 0 0 0 43px

.todo-list li.editing .view
  display: none

.todo-list li .toggle
  text-align: center
  width: 40px
  height: auto
  position: absolute
  top: 0
  bottom: 0
  margin: auto 0
  border: none
  -webkit-appearance: none
  appearance: none

.todo-list li .toggle
  opacity: 0

.todo-list li .toggle + label
  background-image: url('data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2240%22%20height%3D%2240%22%20viewBox%3D%22-10%20-18%20100%20135%22%3E%3Ccircle%20cx%3D%2250%22%20cy%3D%2250%22%20r%3D%2250%22%20fill%3D%22none%22%20stroke%3D%22%23949494%22%20stroke-width%3D%223%22/%3E%3C/svg%3E')
  background-repeat: no-repeat
  background-position: center left

.todo-list li .toggle:checked + label
  background-image: url('data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2240%22%20height%3D%2240%22%20viewBox%3D%22-10%20-18%20100%20135%22%3E%3Ccircle%20cx%3D%2250%22%20cy%3D%2250%22%20r%3D%2250%22%20fill%3D%22none%22%20stroke%3D%22%2359A193%22%20stroke-width%3D%223%22%2F%3E%3Cpath%20fill%3D%22%233EA390%22%20d%3D%22M72%2025L42%2071%2027%2056l-4%204%2020%2020%2034-52z%22%2F%3E%3C%2Fsvg%3E')

.todo-list li label
  word-break: break-all
  padding: 15px 15px 15px 60px
  display: block
  line-height: 1.2
  transition: color 0.4s
  font-weight: 400
  color: #484848
  cursor: pointer

.todo-list li.completed label
  color: #adb5bd
  text-decoration: line-through

.todo-list li .destroy
  display: none
  position: absolute
  top: 0
  right: 0
  bottom: 0
  width: 160px
  height: 70px
  margin: auto 0
  font-size: 30px
  transition: color 0.2s ease-out

.todo-list li .destroy:hover,
.todo-list li .destroy:focus
  color: #C18585

.todo-list li .destroy:after
  display: block
  height: 100%
  line-height: 1.1

.todo-list li:hover .destroy
  display: flex

.todo-list li .btn
  margin: 0 auto
  display: block

.todo-list li .edit
  display: none

.todo-list li.editing:last-child
  margin-bottom: -1px
</style>
