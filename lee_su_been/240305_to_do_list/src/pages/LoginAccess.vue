<template>
    <div>
        <div class="success"> 네이버 로그인에 성공했습니다 😄 </div>
        <ul>
            <li><span>이름:</span>{{ this.name }}</li>
            <li><span>닉네임:</span>{{ this.nickname }}</li>
            <li><span>성별:</span>{{ this.gender }}</li>
            <li><span>전화번호:</span>{{ this.mobile }}</li>
        </ul>

        <q-btn outline @click="pageLink" style="color: #5378fb; margin: 20px; padding: 5px; font-weight: bold;"> 
            {{ this.name }}의 TO DO LIST 보러 가기 
        </q-btn>
    </div>
</template>

<script>
import * as NaverApi from '../api/first'
    export default {
        data(){
            return {
                name: '',
                mobile:'',
                gender: '',
                nickname: ''
            }
        },
        methods:{
            pageLink(){
                this.$router.push({path:'/login'})
            }
        },  
        created(){
            /** For Naver Login **/
            const query = this.$route.query;
            
            NaverApi.GetToken(query.code, query.state).then(response => {
                // console.log("ddddddddd",response.data.response);
                const res = response.data.response;
                this.name = res.name;
                this.mobile = res.mobile;
                if (res.gender=='F'){
                    this.gender = '여성';
                }else{
                    this.gender = res.gender;
                }
                this.nickname = res.nickname;
            })
            .catch(error => {
                console.error('Error', error);
            })

        }
    }
</script>

<style lang="stylus" scoped>
.success
    // background red
    font-size 30px
    padding 20px 0px
    padding-top 40px
    font-weight bold
    
ul
    list-style-type none
    padding-left 0px
    margin-top 20px
    text-align left

    li
        display flex
        min-height 50px
        height 50px
        line-height 50px
        margin 0.5rem 30px
        padding 0 0.9rem
        background white
        border-radius 5px
    span
        font-weight bold    
        margin-right 10px

</style>