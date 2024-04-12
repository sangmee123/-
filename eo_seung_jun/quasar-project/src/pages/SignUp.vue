<template lang="pug">
div.signup_wrapper
    .login_label
        p 이미 회원이신가요? 
        router-link.link(to="/") 로그인
    form.signup_form(@submit.prevent="submitForm")
        InputField(type="email", id="email", v-model="formData.email", :required="true", placeholder="아이디로 사용할 이메일")
        InputField(type="password", id="password", v-model="formData.password", :required="true", placeholder="비밀번호")
        InputField(type="text", id="name", v-model="formData.name", :required="true", placeholder="이름")
        InputField(type="text", id="phone", v-model="formData.phone", :required="true", placeholder="휴대폰 번호")
        
        div
            button.signup_btn(type="submit") 회원가입
</template>

<script>
import axios from 'axios';
import InputField from 'src/components/InputField';

export default {
components: {
    InputField 
  },
data() {
    return {
    formData: {
        email: '',
        name: '',
        phone: '',
        password: ''
    }
    };
},

methods: {
    async submitForm() {
      if (this.isPasswordInvalid) {
        return;
      }
      try {
        const response = await axios.post('/api/signup', this.formData, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        console.log(response)

        alert('Signup successful');
        this.$router.push('/');
      } catch (error) {
        alert('Signup failed: ' + error.response.data.detail);
      }
    }
  }
};
</script>

<style lang="stylus">
.signup_wrapper
    position: absolute
    top: 45%
    left: 50%
    transform: translate(-50%, -50%)
    width: 400px

.login_label
    display: flex
    gap: .5rem
    justify-content: center
    color: #656565

.login_label .link
    color: #3f416b
    font-weight: bold

.signup_btn
    background-color: #fc2b4f
    border: none
    color: white
    border-radius: .6rem
    opacity: .9

.signup_form
    display: flex
    flex-direction: column
    gap: 1rem

.signup_form div input
    width: 100%
    border: 1px solid #ddd
    border-radius: .6rem
    padding: 15px 20px

.signup_form div button
    width: 100%
    padding: 15px 0
    cursor: pointer
    font-size: 18px
    font-weight: bold    

.error-message
    color: red
    padding-left: 5px

</style>
