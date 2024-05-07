<!-- <template lang="pug">
button(class="naverLogo" @click="naverLogin") 
  span(class="n") N 
  span 네이버 로그인  
</template> -->

<template>
  <div id="naver_id_login"></div>
</template>

<script>
import { CLIENT_ID, REDIRECT_URI } from 'src/naverAuth'

export default {
  data() {
    return {}
  },
  mounted() {
    const naver_id_login = new window.naver_id_login(CLIENT_ID, REDIRECT_URI)
    const state = naver_id_login.getUniqState()
    naver_id_login.setButton('green', 1, 35)
    naver_id_login.setDomain('http://localhost:8080')
    naver_id_login.setState(state)
    naver_id_login.init_naver_id_login()
  },
  methods: {
    // naverLogin() {
    //   window.location.href = REDIRECT_URI
    // },
  },
}
</script>

<style lang="stylus" scoped>
.naverLogo
  background-color: #03C75A;
  width: 75%;
  height: 3rem;
  color: white;
  border: none;
  border-radius: 5px;
  margin-bottom: 2rem;
  cursor: pointer;
  .n
    font-size: 20px;
    font-weight: bolder;
    margin-right: 0.5rem;
</style>
