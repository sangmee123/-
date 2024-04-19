<template lang="pug">
.ocrBox 
  div(class="loading-wrap" v-if="loading")
    div(class="loading-spinner")
  
  OcrHeader
  ImgBox
  OcrInfoBox(@loading="isLoading")
</template>

<script>
import OcrHeader from "src/components/OcrHeader.vue";
import ImgBox from "src/components/ImgBox.vue";
import OcrInfoBox from "src/components/OcrInfoBox.vue";

export default {
  name: "ClovaOcrApp",
  components: {
    OcrHeader,
    ImgBox,
    OcrInfoBox,
  },
  data() {
    return {
      loading: false, // 초기 로딩 상태는 false로 설정
    };
  },
  methods: {
    isLoading(loading) {
      this.loading = loading; // 자식 컴포넌트로부터 로딩 상태를 받아옴
    },
  },
};
</script>

<style lang="stylus">
.ocrBox
    background-color: #fcfcfb;
    width: 100%;
    max-width: 26rem;
    height: 100vh;
    margin: auto;
    text-align: center;

.loading-wrap
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 26rem;
  height: 100%;
  background-color: #0002;
  position: fixed;

.loading-spinner
  width: 40px;
  height: 40px;
  border: 5px solid #3498db;
  border-top: 5px solid transparent;
  border-radius: 50%;
  animation: rotate 1s linear infinite;


@keyframes rotate
  from
    transform: rotate(0deg);

  to
    transform: rotate(360deg);
</style>
