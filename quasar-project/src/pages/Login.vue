<template lang="pug">
div.login_wrapper
    .signup_label
        p 회원이 아니신가요? 
        router-link.link(to="/signup") 회원가입

    button.google_login_btn(type="button" @click="oauthLoginForm('google')") 구글 로그인
    button.naver_login_btn(type="button" @click="oauthLoginForm('naver')") 네이버 로그인

    .flex 
        .line 
        p 또는
        .line

    form.login_form(@submit.prevent="loginForm")
        //- div
        //-     input(type="text" id="username" v-model="formData.username" required placeholder="이메일 ID")
        //- div
        //-     input(type="password" id="password" v-model="formData.password" required placeholder="비밀번호")
        InputField(type="email" id="username" :value="formData.username" :required="true" placeholder="이메일 ID" @input="formData.username = $event")
        InputField(type="password" id="password" :value="formData.password" :required="true" placeholder="비밀번호" @input="formData.password = $event")
       
        div
            button.login_btn(type="submit" ) 로그인
        p(v-if="errorMessage", style="color: red;") {{ errorMessage }}
    
    .signup_label
        router-link.link(to="/dataqueryingkepco") 한전 분산전원 검색
        router-link.link(to="/backgroundtask") BackgroundTask
        router-link.link(to="/scrolltest1") 스크롤 연습1
        // router-link.link(to="/scrolltest2") 스크롤 연습2
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
        username: '',
        password: '',
    },
    errorMessage: '',
    isSubmitting: false 
    };
},
methods: {
    async loginForm() {
        if (this.isSubmitting) return;
        this.isSubmitting = true; 
        try {
            const formData = new FormData();
            formData.append('username', this.formData.username);
            formData.append('password', this.formData.password);

            await axios.post('/api/login', formData, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            this.errorMessage = '';
            this.$router.push('/todolist');
        } catch (error) {
            this.errorMessage = error.response.data.detail;
            console.error(error)
        } finally {
            this.isSubmitting = false
        }
    },
    oauthLoginForm(portal) {
        window.location.href = `/api/oauth_login/${portal}`
    },
}
};
</script>

<style lang="stylus">
.login_wrapper
    position: absolute
    top: 45%
    left: 50%
    transform: translate(-50%, -50%)
    width: 400px


.signup_label
    display: flex
    gap: .5rem
    justify-content: center
    color: #656565

.signup_label .link
    color: #3f416b
    font-weight: bold

.naver_login_btn
    border: none
    cursor: pointer
    background-color: rgb(3, 199, 90)
    color: white
    width 100%
    padding: 15px 0
    font-size: 18px
    margin-bottom: 20px
    border-radius: .6rem
    font-weight: bold
    position: relative // 부모 요소의 위치를 상대적으로 설정

    &::before {
        content: '';
        position: absolute;
        left: 0; // 왼쪽에 위치
        top: 50%; // 상단 정렬
        transform: translateY(-50%); // 수직 정렬
        width: 50px; // 이미지의 너비
        height: 50px; // 이미지의 높이
        background: url('~assets/btnG_아이콘사각.png') no-repeat; // 이미지 경로
        background-size: contain; // 이미지를 가득 채울 수 있도록 설정
        margin-left: 10px
    }

.google_login_btn
    border: none
    cursor: pointer
    background-color: rgb(66, 133, 244)
    color: white
    width 100%
    padding: 15px 0
    font-size: 18px
    margin-bottom: 20px
    border-radius: .6rem
    font-weight: bold
    position: relative // 부모 요소의 위치를 상대적으로 설정

    &::before {
        content: '';
        position: absolute;
        left: 0; // 왼쪽에 위치
        top: 50%; // 상단 정렬
        transform: translateY(-50%); // 수직 정렬
        width: 47.5px; // 이미지의 너비
        height: 47.5px; // 이미지의 높이
        background: url('~assets/web_light_sq_na@4x.png') no-repeat; // 이미지 경로
        background-size: contain; // 이미지를 가득 채울 수 있도록 설정
        margin-left: 10px
    }

.login_btn
    background-color: #fc2b4f
    border: none
    color: white
    border-radius: .6rem
    opacity: .9

.login_form
    display: flex
    flex-direction: column
    gap: 1rem

.login_form div input
    width: 100%
    border: 1px solid #ddd
    border-radius: .6rem
    padding: 15px 20px

.login_form div button
    width: 100%
    padding: 15px 0
    cursor: pointer
    font-size: 18px
    font-weight: bold

.flex
    display: flex
    justify-content: center
    align-items: center
    margin-bottom: 20px

.flex p
    color: #656565
    margin: 0 10px
    
.line
    border: 1px solid black
    opacity: .1
    width: 44%
</style>