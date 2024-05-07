<template lang="pug">
.membershipBox 
    .title 회원가입
    div
        label(for="email") 이메일 주소
        span(class="red") {{ emailCheckMessage }}
        input(id="email" v-model="email" required)
        
        label(for="password") 비밀번호
        input(type="password" id="password" v-model="password" required)
        
        label(for="pwCheck") 비밀번호 확인
        span(:class="{ green: isCorrect, red: !isCorrect }") {{ pwCheckMessage }}
        input(type="password" id="pwCheck" v-model="rePassword" required)
        
        .userInfo
          div
            label(for="name" class="nameLabel") 이름
            label(for="mobile" class="mobileLabel") 휴대폰 번호

          input(id="name" class="name" v-model="name" required)          
          input(
              type="text" 
              id="mobile"
              :maxLength="13"
              class="mobile"
              v-model="mobile"
              @change="mobileCheck(mobile)"
              required
          )
        button(@click="onSubmit" :class="{ buttonColor: isFormValid }") 가입하기
</template>

<script>
import axios from 'axios'
export default {
  name: 'Membership',
  computed: {
    isFormValid() {
      return this.email !== '' && this.password !== '' && this.rePassword !== '' && this.name !== '' && this.mobile !== '' && this.isCorrect // 비밀번호와 비밀번호 확인이 일치해야 함
    },
  },
  data() {
    return {
      email: '',
      emailCheckMessage: '',
      password: '',
      rePassword: '',
      pwCheckMessage: '',
      isCorrect: '',
      name: '',
      mobile: '',
    }
  },
  watch: {
    email(value) {
      this.emailCheckMessage = this.emailCheck(value)
    },
    password(value) {
      this.pwCheckMessage = this.passwordCheck(value)
    },
    rePassword(value) {
      this.pwCheckMessage = this.passwordCheck(value)
    },
    mobile(value) {
      this.mobileCheck(value)
    },
  },
  methods: {
    emailCheck(address) {
      const emailRregex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i
      if (!emailRregex.test(address)) {
        return '이메일 주소를 정확히 입력해주세요.'
      } else {
        return ''
      }
    },
    passwordCheck() {
      if (this.password === this.rePassword) {
        this.isCorrect = true
        return '비밀번호가 일치합니다.'
      } else {
        this.isCorrect = false
        return '비밀번호가 일치하지 않습니다.'
      }
    },
    mobileCheck(mobile) {
      this.mobile = mobile
        .replace(/[^0-9]/g, '')
        .replace(/^(\d{0,3})(\d{0,4})(\d{0,4})$/g, '$1-$2-$3')
        .replace(/(\-{1,2})$/g, '')
    },
    onSubmit() {
      if (this.isFormValid) {
        const params = {
          email: this.email,
          password: this.password,
          name: this.name,
          mobile: this.mobile,
        }
        axios
          .post('/api/add_member', params)
          .then(() => {
            alert('회원가입 성공')
            this.$router.push('/')
          })
          .catch(error => {
            alert(error)
          })
      }
    },
  },
}
</script>

<style lang="stylus" scoped>
.green
  color: green
.red
  color: red
.buttonColor
  background-color: #F6D8CE;
.membershipBox
  width: 27rem;
  border: 1px solid #c6c6c6;
  border-radius: 5px;
  margin: 0 auto;
  margin-top: 7rem;
  .title
      font-size: 1.5rem;
      text-align: center;
      padding: 1rem;
      margin-top: 1rem;
      margin-bottom: 1rem;
  label
    margin-left: 3.8rem;
  span
    font-size: 11px;
    margin-left: 0.5rem;
  input
      display: block;
      width: 75%;
      height: 35px;
      background: transparent
      border: 1px solid #dadada;
      border-radius: 5px;
      padding-left: 15px;
      margin: 0 auto;
      margin-top: 5px;
      margin-bottom: 10px;
      &:focus
          outline: none;
          border: 1px solid #F6D8CE;
          box-shadow: 0 0 4px #F6D8CE;
.userInfo
  width: 75%;
  margin: 0 auto;
  .nameLabel
    margin-left: 0.5rem;
  .mobileLabel
    margin-left: 5.5rem;
  input
    display: inline-block;
  .name
    width: 35%;
    margin-right: 0.5rem;
  .mobile
    width: 62.5%;
button
  display: flex;
  justify-content: center;
  align-items: center;
  width: 75%;
  height: 2.5rem;
  border: none;
  border-radius: 5px;
  margin: 0 auto;
  margin-top: 1.5rem;
  margin-bottom: 2rem;
  cursor: pointer;
</style>
