<template lang="pug">
div
  div(class="title") ✅ 조회하실 주소를 입력해주세요
  div(class="dataInput")
    q-form(
      @submit="onSubmit"
      @reset="onReset"
      class="q-gutter-md"
    )
      q-input(
        filled
        v-model="addr.addrDo"
        label="시/도 *"
        hint="현재 거주하는 곳의 시 또는 도를 입력해주세요"
        lazy-rules
        :rules="[ val => val && val.length > 0 || '뭐라도 적어주세요']"
      )
      q-input(
        filled
        v-model="addr.addrSi"
        label="시"
        hint="현재 거주하는 곳의 시 또는 도를 입력해주세요"
        lazy-rules
      )
      q-input(
        filled
        type="text"
        v-model="addr.addrGu"
        label="구/군"
        lazy-rules
      )
      q-input(
        filled
        type="text"
        v-model="addr.addrLidong"
        label="동/면*"
        lazy-rules
        :rules="[ val => val && val.length > 0 || '뭐라도 적어주세요']"
      )
      q-input(
        filled
        type="text"
        v-model="addr.AddrLi"
        label="리"
        lazy-rules
      )
      q-input(
        filled
        type="text"
        v-model="addr.addrJibun"
        label="상세번지"
        lazy-rules
        
      )
      q-input(
        filled
        type="number"
        v-model="addr.substCd"
        label="변전소코드"
        lazy-rules  
      )
      
      div
        q-btn(label="Submit" type="submit" color="primary")
        q-btn(label="Reset" type="reset" color="primary" flat class="q-ml-sm")

  ul
    span(class="result_title") 주소지의 DL 결과 😄
    li
      span(class="dl_name") DL 용량
      span(class="dl_val") {{ this.res.volume }}
    li
      span(class="dl_name") DL 여유 용량
      span(class="dl_val") {{ this.res.extra_volume }}

</template>

<script>
import * as DataApi from '../api/apis'

export default {
  data(){
    return{
      res: {
        volume: '',
        extra_volume: '',
      },
      addr: {
        addrDo: '전라남도',
        addrSi: '',
        addrGu: '영암군',
        addrLidong: '도포면',
        AddrLi: '수산리',
        addrJibun: '447-2',
        substCd: '2583',
      },
    };  
  },
  methods: {
    onSubmit() {
      const resource_url = {}
      if (this.addr.addrDo != ""){
        resource_url['addrDo'] = this.addr.addrDo;
      }
      if (this.addr.addrSi != ""){
        resource_url['addrSi'] = this.addr.addrSi;
      }
      if (this.addr.addrGu != ""){
        resource_url['addrGu'] = this.addr.addrGu;
      }
      if (this.addr.addrLidong != ""){
        resource_url['addrLidong'] = this.addr.addrLidong;
      }
      if (this.addr.AddrLi != ""){
        resource_url['AddrLi'] = this.addr.AddrLi;
      }
      if (this.addr.addrJibun != ""){
        resource_url['addrJibun'] = this.addr.addrJibun;
      }
      if (this.addr.substCd != ""){
        resource_url['substCd'] = this.addr.substCd;
      }
      this.callAPI(resource_url)
    },
    onReset () {
      this.addr.addrDo = '',
      this.addr.addrSi = '',
      this.addr.addrGu = '',
      this.addr.addrLidong = '',
      this.addr.AddrLi = '',
      this.addr.addrJibun = '',
      this.addr.substCd = ''
    },
    callAPI(res){
      DataApi.DataHanJun(res).then(response => {
        this.res.volume = response.data.jsDlPwr;
        this.res.extra_volume = response.data.vol_3;
        console.log(response.data);
      })
      .catch(error => {
        console.error('Error', error);
      })
    }
  }
}
</script>

<style lang="stylus" scoped>
.title
  font-weight bold
  font-size 20px
.title
.dataInput
  width auto
  height auto
  display flex
  justify-content center
  padding-top 40px
  // backgroundß orange
  
  .q-form
    width 500px

ul
  list-style-type none
  padding-left 0px
  margin-top 20px
  text-align left
  display flex
  flex-direction column
  align-items center
  // background pink
  .result_title
    font-size 20px
    font-weight bold
    margin 15px
    padding-top 10px

  li
    width 500px
    height 50px
    min-height 50px
    line-height 50px
    margin 0.5rem 30px
    padding 0 0.9rem
    background  #e9e9e9
    border-radius 5px
    display flex
    .dl_name
      font-weight bold
      margin-right 13px
</style>
