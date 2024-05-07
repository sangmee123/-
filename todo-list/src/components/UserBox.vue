<template lang="pug">
div 
  span 안녕하세요. {{ username }}님
  span 오늘 하루도 힘차게 나아갑시다.
  button(@click="Logout") Logout

</template>

<script>
export default {
  name: 'UserBox',
  props: {
    username: String,
  },
  data() {
    return {}
  },
  methods: {
    Logout() {
      localStorage.removeItem('token') // 토큰 삭제
      this.$router.push({ path: '/', replace: true }) // 로그인 페이지 이동, 히스토리를 제거
    },
  },
}
</script>

<style lang="stylus" scoped>
span
  display: block;
</style>
