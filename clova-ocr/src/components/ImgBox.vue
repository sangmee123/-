<template lang="pug">
.ImgBox
    img(:src='imgUrl' alt="ID Card")
</template>

<script>
export default {
  name: "ClovaOcrImgBox",

  data() {
    return {
      imgUrl: "https://storage.googleapis.com/cdn-asia/ocr/lee_sang_mee.png",
    };
  },

  mounted() {},

  methods: {},
};
</script>

<style lang="stylus">
.ImgBox
    width: 80%;
    height: 11rem;
    // border: 1px solid gray;
    margin: auto;
    margin-top: 2rem;
    img
        width: 25rem;
        right: 3rem;
        bottom: 4.5rem;
        position: relative;
</style>
