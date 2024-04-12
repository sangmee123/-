<template>
    <div>
        <q-btn push id="naver_id_login" @click="doNaverLogin">네이버에 로그인</q-btn>
    </div>
</template>
<script>
import * as NaverApi from '../api/first'

export default {
    data () {
        return {
            url: ""
        }
    },
    methods: {
        doNaverLogin(){
            window.location.href = this.url
        },
    },
    created(){
        NaverApi.RequestToken().then(response => {
            this.url = response.data;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}
</script>

<style lang="stylus" scoped>
$primary-color = #5378fb
$secondary-color = #8763fb

#naver_id_login
    width 250px
    margin 50px 0px
    padding 10px
    font-size 20px
    border-radius 10px
    background linear-gradient(to right, $primary-color, $secondary-color)
    color white
    margin-right 4px 
</style>