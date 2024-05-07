<template>
  <div class="container">
    <h2>Naver Login Callback</h2>
    <span><img :src="profileImg" /></span>
    <p>email: {{ email }}</p>
    <p>name: {{ name }}</p>
    <p>mobile: {{ mobile }}</p>

    <button @click="naverLogin">이 계정으로 TodoList 로그인하기</button>
  </div>
</template>

<script>
import { CLIENT_ID } from 'src/naverAuth'
import axios from 'axios'

export default {
  data() {
    return {
      accessToken: '',
      profileImg: '',
      email: '',
      name: '',
      mobile: '',
    }
  },
  mounted() {
    const naverIdLogin = new window.naver_id_login(CLIENT_ID)
    this.accessToken = naverIdLogin.oauthParams.access_token

    // 사용자 프로필 조회 및 회원가입
    this.userInfo()
  },
  methods: {
    async userInfo() {
      const headers = { Authorization: 'Bearer ' + this.accessToken }
      const { data } = await axios.get('/v1/nid/me', { headers })

      console.log('*****naverUserInfo data***** => ', data)

      this.profileImg = data.response.profile_image
      this.email = data.response.email
      this.name = data.response.name
      this.mobile = data.response.mobile

      const params = {
        email: this.email,
        name: this.name,
        mobile: this.mobile,
      }
      axios
        .post('/api/add_naver', params)
        .then(response => {
          if (response.data.message) {
            // 기존에 네이버로 가입돼 있는 경우
            alert(response.data.message)
          } else {
            alert('네이버 회원가입 완료')
          }
        })
        .catch(error => {
          alert(error)
        })
    },
    naverLogin() {
      axios
        .post('/api/naver_login', { email: this.email })
        .then(reponse => {
          const token = reponse.data.token
          localStorage.setItem('token', token)

          this.$router.push('/login')
        })
        .catch(error => {
          alert('로그인 실패')
          console.log('error', error)
        })
    },
  },
}
</script>

<style lang="stylus" scoped>
.container
  text-align: center;
  span
    display: block;
    width: 5rem;
    height: 5rem;
    border-radius: 50%;
    margin: 0 auto;
    overflow: hidden;
    img
      width: 5rem;
</style>
