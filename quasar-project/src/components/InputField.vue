<template lang="pug">
div
  input(:type="type", :id="id", :value="value", @input="handleInput", :required="required", :placeholder="placeholder")
  div.error-message(v-if="shouldDisplayErrorMessage") {{ errorMessage }}
</template>

<script>
export default {
  props: {
    type: String,
    id: String,
    value: [String, Number],
    required: Boolean,
    placeholder: String
  },
  data() {
    return {
      errorMessage: ''
    };
  },
  methods: {
    handleInput(event) {
      this.$emit('input', event.target.value);
      if (this.type === 'password' && event.target.value.length > 0) {
        this.validatePassword(event.target.value);
      } else {
        this.errorMessage = '';
      }
    },
    validatePassword(password) {
      const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
      if (!passwordRegex.test(password)) {
        this.errorMessage = '비밀번호는 8자리 이상이어야 하며, 영문과 숫자를 모두 포함해야 합니다.';
      } else {
        this.errorMessage = '';
      }
    }
  },
  computed: {
    shouldDisplayErrorMessage() {
      return this.errorMessage !== '' && this.type === 'password';
    }
  }
};
</script>

<style scoped>
.error-message {
  color: red;
  padding-left: 5px;
  margin-top: 5px;
}
</style>
