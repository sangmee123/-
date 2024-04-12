<template lang="pug">
div.wrapper
    p.label 주소를 입력해주세요
    input.search(type="button", @click="execDaumPostcode", :value="searchButtonText")
    button.btn(type="button" @click="searchDL(jibunAddress)") 검색

    table
        tr
            td dlNm (DL명)
            td :
            td {{ DLItems.dlNm }} 
        tr
            td jsDlPwr (DL용량)
            td :
            td {{ DLItems.jsDlPwr }}
        tr
            td vol_3 (DL여유용량)
            td :
            td {{ DLItems.vol_3 }} 
    //- div.flex
        //- input(type="text", v-model="roadAddress", placeholder="도로명주소")
        //- input(type="text", v-model="jibunAddress", placeholder="지번주소")
        //- span(v-if="guide", style="color:#999") {{ guide }}
        //- input(type="text", v-model="extraAddress", placeholder="참고항목")
        //- input(type="text", v-model="postcode", placeholder="우편번호")
</template>
  
<script>
  import axios from 'axios';

  export default {
    data() {
      return {
        // postcode: '',
        // roadAddress: '',
        jibunAddress: '',
        // extraAddress: '',
        guide: '',
        DLItems: []
      };
    },
    mounted() {
    this.loadDaumPostcodeScript();
    },
    computed: {
      searchButtonText() {
        return this.jibunAddress ? this.jibunAddress : '우편번호 검색하기';
      }
    },
    methods: {
        searchDL(jibunAddress) {
            axios.get('/api/DL', {
                params: {
                    jibunAddress: jibunAddress,
                }
                })
                .then(response => {
                    console.log(response.data[0]);
                    this.DLItems = response.data[0];
                })
                .catch(error => {
                    console.error(error);
                });
        },
    loadDaumPostcodeScript() {
      const script = document.createElement('script');
      script.src = '//t1.daumcdn.net/mapjsapi/bundle/postcode/prod/postcode.v2.js';
      script.onload = () => {
        // 스크립트 로드 후 호출되는 함수
        console.log('Daum Postcode script loaded');
      };
      document.body.appendChild(script);
    },
      execDaumPostcode() {
        new daum.Postcode({
          oncomplete: (data) => {
            let roadAddr = data.roadAddress;
            let extraRoadAddr = '';
  
            if (data.bname !== '' && /[동|로|가]$/g.test(data.bname)) {
              extraRoadAddr += data.bname;
            }
  
            if (data.buildingName !== '' && data.apartment === 'Y') {
              extraRoadAddr += (extraRoadAddr !== '' ? ', ' + data.buildingName : data.buildingName);
            }
  
            if (extraRoadAddr !== '') {
              extraRoadAddr = ' (' + extraRoadAddr + ')';
            }
  
            this.postcode = data.zonecode;
            this.roadAddress = roadAddr;
            this.jibunAddress = data.jibunAddress;
  
            if (roadAddr !== '') {
              this.extraAddress = extraRoadAddr;
            } else {
              this.extraAddress = '';
            }
  
            if (data.autoRoadAddress) {
              this.guide = '(예상 도로명 주소 : ' + data.autoRoadAddress + extraRoadAddr + ')';
            } else if (data.autoJibunAddress) {
              this.guide = '(예상 지번 주소 : ' + data.autoJibunAddress + ')';
            } else {
              this.guide = '';
            }
          }
        }).open();
      }
    }
  };
</script>
  
<style lang="stylus">
.wrapper
    position: absolute
    top: 25%
    left: 50%
    transform: translate(-50%, -50%)
    width: 500px
    border-radius: 20px
    display: flex
    flex-direction: column
    justify-content: center
    align-items: center
    padding: 20px 0
    gap: 1rem
    box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.2);  

.label
    font-size: 20px

.search
    border: 1px solid rgb(221,221,221)
    border-radius: 10px
    background-color: white
    color: #656565
    font-size: 16px
    padding: 15px 20px
    cursor: pointer
    width: 80%
    text-align: left

.btn
    border: none
    cursor: pointer
    background-color: #fc2b4f
    color: white
    width 80%
    padding: 12.5px 0
    font-size: 16px
    border-radius: .6rem
    font-weight: bold
</style>