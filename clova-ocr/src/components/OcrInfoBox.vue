<template lang="pug">
.infoBox
    table
        tr(v-for="(item, id) in info" :key="item.id")
            td {{ item.label }}
            td {{ item.value }}

    PostButton(@url="getData")
</template>

<script>
import axios from "axios";
import PostButton from "src/components/PostButton.vue";

export default {
  name: "ClovaOcrOcrInfoBox",
  components: { PostButton },
  data() {
    return {
      info: [
        { label: "면허 종류", value: "" },
        { label: "자동차 일련번호", value: "" },
        { label: "이름", value: "" },
        { label: "주민등록증 반호", value: "" },
        { label: "주소", value: "" },
      ],
      imgUrl: null,
      loading: false, // 로딩 상태
    };
  },
  methods: {
    getData(url) {
      console.log("click Event data: ", url);
      const params = { imgUrl: url };
      this.loading = true; // 데이터 요청 시 로딩 표시
      this.$emit("loading", this.loading);

      axios
        .get("/api/get_data", { params })
        .then((response) => {
          const data = response.data;
          const imgInfo = data.images[0].fields;
          console.log(imgInfo);

          imgInfo.map((item, id) => {
            this.info[id].label = item.name;
            this.info[id].value = item.inferText;
          });
          this.loading = false; // 데이터 받은 후 로딩 숨기기
          this.$emit("loading", this.loading);
        })
        .catch((error) => {
          console.log(error);
          alert("데이터를 불러올 수 없습니다.");
          this.loading = false; // 오류 발생 시도 로딩 숨기기
          this.$emit("loading", this.loading);
        });
    },
  },
};
</script>

<style lang="stylus">
.infoBox
    width: 95%;
    height: auto;
    padding: 0.5rem;
    margin: auto;
    table
        width: 100%;
        border: 1px solid gray;
        border-radius: 0.5rem;
        padding: 0.5rem;
        tr
          border: 1px solid black;
          td:nth-child(2)
            background-color: #F5F5F5;
            width: 70%;
</style>
