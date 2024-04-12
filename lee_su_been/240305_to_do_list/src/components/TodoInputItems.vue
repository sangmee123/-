<template lang="pug">
div.inputBox.shadow
    input(type="text" v-model="newTodoItem" @keyup.enter="addTodo")
    span.addContainer
        i.fas.fa-plus.addBtn(@click="addTodo")
    

</template>

<script>
// import { registerUser } from 'src/api';

export default {
    props: {value: Array},

    data(){
        return {
            newTodoItem: "",
            todoItems: [],
        }
    },
    watch:{
        todoItems(oldval,newval){
            if (oldval !== newval){
                this.$emit('input', this.todoItems);
            }
        }
    },
    methods:{
        addTodo(){
            // registerUser();

            const itemList = this.value.map(item => item.item);

            if (this.newTodoItem !== '' && !itemList.includes(this.newTodoItem)) {
                const obj = {completed: false, item: this.newTodoItem, edit: false, new_val: this.newTodoItem}
                localStorage.setItem(this.newTodoItem, JSON.stringify(obj));
                this.todoItems = [...this.value, obj];

                // 직접 접근은 위험합니다.
                // this.todoItems.push(this.todoItems);

                this.clearInput();

                // console.log(this.newTodoItem);
            } else{
                console.log(this.newTodoItem);
                alert("type smt");
            }
        },
        clearInput(){
            this.newTodoItem = '';
        }
    },

}
</script>

<style lang="stylus" scoped>
$primary-color = #5378fb
$secondary-color = #8763fb

input:focus
    outline none
    text-size 16px

.inputBox
    margin 10px 30px
    margin-top 15px
    background white
    height 50
    line-height 50px
    border-radius 5px

    input 
        // background tomato
        border-style none
        font-size 16px

.addContainer 
    float right
    background linear-gradient(to right, $primary-color, $secondary-color)
    display block
    width 4rem
    height 53px
    border-radius 0 5px 5px 0

    .addBtn
        color white
        vertical-align middle
        font-size 20px

</style>