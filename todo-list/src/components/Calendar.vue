<template lang="pug">
input(type="date" :value="currentDate" :max="currentDate" @change="onSelectedDate")
</template>

<script>
import axios from 'axios'
import { getCurrentDate } from '../utils/date'

export default {
  name: 'Calendar',

  data() {
    return { currentDate: null }
  },

  mounted() {
    this.todayDate()
  },

  methods: {
    todayDate() {
      const today = new Date()
      this.currentDate = getCurrentDate(today)
    },
    onSelectedDate(e) {
      const params = { selectedDate: e.target.value }
      axios
        .get('/api/selected_date', { params })
        .then(response => {
          const todos = response.data
          this.$emit('selectedDateTodos', todos, e.target.value)
        })
        .catch(error => {
          console.log(error)
        })
    },
  },
}
</script>

<style lang="stylus">
input
    background: none;
    font-size: 15px;
    border: none;
    outline: none;
    padding: 1rem;

input::-webkit-calendar-picker-indicator
  cursor: pointer;
</style>
