<template lang="pug">
div    
    form(@submit.prevent)
        input(v-model="email" placeholder="이메일 ID" required)
        input(type="password" v-model="password" placeholder="Password" required)
        button(@click="onLogin" :class="{ buttonColor: isFormValid }") Login
</template>

<script>
import axios from 'axios'

export default {
  name: 'MohaetInternLoginForm',
  data() {
    return {
      email: '',
      password: '',
    }
  },
  computed: {
    isFormValid() {
      return this.email !== '' && this.password !== ''
    },
  },
  methods: {
    onLogin() {
      if (this.isFormValid) {
        const params = { email: this.email, password: this.password }
        axios
          .post('/api/login', params)
          .then(reponse => {
            const data = reponse.data
            const token = data.access_token
            localStorage.setItem('token', token)

            alert('로그인 성공')
            this.$router.push('/login')
          })
          .catch(error => {
            alert('로그인 실패')
            console.log('error', error)
          })
      }
    },
  },
}
</script>

<style lang="stylus" scoped>
div
    text-align: center;
    margin-top: 1rem;
input
    display: block;
    width: 75%;
    height: 2.8rem;
    background: transparent
    border: 1px solid #dadada;
    border-radius: 5px;
    padding-left: 15px;
    margin: 0 auto;
    margin-top: 0.5rem;
    margin-bottom: 10px;
    &:focus
        outline: none;
        border: 1px solid #F6D8CE;
        box-shadow: 0 0 4px #F6D8CE;
button
    margin: 0 auto;
    width: 75%;
    height: 2.5rem;
    border: none;
    border-radius: 5px;
    margin-top: 0.5rem;
    margin-bottom: 1rem;
    cursor: pointer;
.buttonColor
  background-color: #F6D8CE;
</style>
