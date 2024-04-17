<template lang="pug">
    form(@submit.prevent="handleSubmit")
        input(v-model="inputValue" placeholder="할 일을 입력하세요.")
        button(@click="onCreate(inputValue)") +
</template>

<script>
export default {
  props: {
    onCreate: Function,
  },
  data() {
    return {
      inputValue: '',
    }
  },
  methods: {
    handleSubmit() {
      this.inputValue = ''
    },
  },
}
</script>

<style lang="stylus">
form
    display: flex;
    background: #495057;
    padding-left: 0.5rem;
    input
        background: none;
        outline: none;
        border: none;
        padding: 0.5rem 0 0.5rem 1rem;
        font-size: 1.125rem;
        line-height: 1.5;
        color: white;
        &::placeholder
            color: #dee2e6;
        flex: 1;
    button
        background: none;
        outline: none;
        border: none;
        background: #868e96;
        color: white;
        padding-left: 1rem;
        padding-right: 1rem;
        font-size: 1.5rem;
        display: flex;
        align-items: center;
        cursor: pointer;
        transition: 0.1s background ease-in;
        &:hover
            background: #adb5bd;
</style>
