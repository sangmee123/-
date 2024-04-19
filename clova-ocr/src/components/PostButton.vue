<template lang="pug">
form(@submit.prevent="onSubmit")
  button(class="w-btn w-btn-gra1 w-btn-gra-anim") Send
</template>

<script>
// import axios from "axios";

export default {
  name: "PostButton",

  data() {
    return {
      imgUrl: "https://storage.googleapis.com/cdn-asia/ocr/lee_sang_mee.png",
    };
  },

  mounted() {},
  methods: {
    onSubmit() {
      this.$emit("url", this.imgUrl);
    },
  },
};
</script>

<style lang="stylus">
.w-btn
    display: inline-block;
    text-decoration: none;
    font-family: "paybooc-Light", sans-serif;
    font-weight: 600;
    font-size: 15px;
    border: none;
    border-radius: 0.5rem;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
    padding: 0.6rem 2rem;
    margin-top: 2rem;
    position: relative;
    transition: 0.25s;
    cursor: pointer;
    &:hover
      letter-spacing: 2px;
      transform: scale(1.0);
      cursor: pointer;

.w-btn-gra1
    background: linear-gradient(-45deg, #F6D8CE 0%, #519d9e 100%);
    color: white;

.w-btn-gra-anim
    background-size: 400% 400%;
    animation: gradient1 5s ease infinite;

@keyframes gradient1
    0%
        background-position: 0% 50%;

    50%
        background-position: 100% 50%;

    100%
        background-position: 0% 50%;
</style>
