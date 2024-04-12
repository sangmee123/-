<template lang="pug">
.clearAllContainer
    span.clearAllBtn(@click="clearTodo") Clear All
</div>
</template>

<script>
    export default {
        methods:{
            clearTodo(){
                this.$emit('clearAll');
            }
        }
    }
</script>

<style lang="stylus" scoped>
.clearAllContainer
    width 8.5rem
    height 50px
    line-height 50px
    background-color white
    border-radius 5px
    margin 0 auto
    margin-top 20px

.clearAllBtn
    color #e20303
    display block
    font-size 16px

</style>