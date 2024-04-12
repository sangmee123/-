<template lang="pug">
q-page

  TodoInput(v-model ="todoItems")
  TodoList(v-model= "todoItems")
  TodoFooter(@clearAll="clearAllItems")
</template>

<script>
import TodoInput from '../components/TodoInputItems.vue';
import TodoList from '../components/TodoList.vue';
import TodoFooter from '../components/TodoFooter.vue';


export default {
  data(){
    return {
      todoItems: []
    }
  },
  methods:{
    clearAllItems(){
      localStorage.clear();
      this.todoItems = [];
    }
  },
  created(){

    /** For To Do List **/
    if (localStorage.length >0){
      for (var i=0; i <localStorage.length; i++){
        if (localStorage.key(i) !== 'loglevel:webpack-dev-server'){
          this.todoItems.push(JSON.parse(localStorage.getItem(localStorage.key(i))));
        }
      }
    }
  },
  components:{
    TodoInput,
    TodoFooter,
    TodoList
  },
  
}
</script>

<style lang="stylus" scoped>
</style>
    