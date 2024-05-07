<template lang="pug">
.loginBox
  .title SangMee's TodoApp
  NaverLogin
  //- KakaoLogin
  div(class="rowbar")
  LoginForm 
  span(class="text") 회원이 아니신가요?
  router-link(to='/register') 회원가입
</template>

<script>
import KakaoLogin from '../components/KakaoLogin.vue'
import NaverLogin from '../components/NaverLogin.vue'
import LoginForm from '../components/LoginForm.vue'

export default {
  name: 'Login',
  components: {
    LoginForm,
    KakaoLogin,
    NaverLogin,
  },
  data() {
    return {}
  },
}
</script>

<style lang="stylus" scoped>
.loginBox
  width: 25rem;
  height: 23rem;
  font-size: 15px;
  text-align: center;
  // border: 1px solid #c6c6c6;
  // border-radius: 0.5rem;
  margin: 0 auto;
  margin-top: 10rem;
  .title
      font-size: 1.5rem;
      text-align: center;
      padding: 1rem;
      margin-top: 1rem;
      margin-bottom: 1rem;
  .rowbar
    width: 75%;
    height: 1px;
    opacity: 0.1;
    background: #000;
    margin: 0 auto;
    margin-top: 0.5rem;
  .text
    margin-right: 1rem;
</style>
