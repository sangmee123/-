//
<template lang="pug">
//     span(@click="kakaoLogin" class="kakao")
//         img(
//             src="../assets/images/kakao_login.png" 
//             alt="카카오 로그인 버튼"
//         )
// </template>

//
<script>
// import { KAKAO_AUTH_URL } from '../KakaoAuth'

// export default {
//   name: 'KakaoLogin',

//   data() {
//     return {}
//   },
//   methods: {
//     async kakaoLogin() {
//       window.Kakao.Auth.login({
//         scope: 'profile, account_email, gender, age_range, birthday', //동의항목 페이지에 있는 개인정보 보호 테이블의 활성화된 ID값을 넣습니다.
//         success: function (response) {
//           console.log(response) // 로그인 성공하면 받아오는 데이터
//           window.Kakao.API.request({
//             // 사용자 정보 가져오기
//             url: '/v2/user/me',
//             success: res => {
//               const kakao_account = res.kakao_account
//               console.log(kakao_account)
//             },
//           })
//           window.location.href = KAKAO_AUTH_URL //리다이렉트 되는 코드
//         },
//         fail: function (error) {
//           console.log(error)
//         },
//       })
//       // window.location.href = KAKAO_AUTH_URL

//       //   // 현재 URL에서 쿼리 문자열 파싱하여 인가 코드 추출
//       //   const urlParams = new URLSearchParams(window.location.search)
//       //   const code = urlParams.get('code')

//       //   if (code) {
//       //     try {
//       //       // Kakao로부터 액세스 토큰 요청
//       //       const response = await axios.post('/api/kakao/token', { code })
//       //       const accessToken = response.data.access_token
//       //       localStorage.setItem('accessToken', accessToken)
//       //       // 사용자를 다음 경로로 리다이렉트 또는 다른 작업 수행
//       //       this.$router.push('/login')
//       //     } catch (error) {
//       //       console.error('액세스 토큰 요청 실패:', error)
//       //     }
//       //   }
//     },
//   },
// }
//
</script>
//
<style lang="stylus" scoped>
// .kakao
//     cursor: pointer;
//     img
//         width: 75%;
//
</style>
