<template lang="pug">
div.wrapper
    p.label 테스트
    button.btn(type="button" @click="sendEmail()") 클릭

</template>
    
<script>
    import axios from 'axios';

    export default {
    data() {
        return {
        };
    },
    methods: {
        sendEmail() {
            axios
                .post(`/api/front_errors`)
                .then(response => {
                    console.log('성공', response.data);
                })
                .catch(error => {
                    console.error('Error fetching todos:', error);
                });
            },
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