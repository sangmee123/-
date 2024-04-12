<template>
    <div>
        <ul>
            <li v-for="(todoItem, index) in value" :key="todoItem.item" class="shadow">
                <!-- {{ todoItem }} -->
                <!-- 1. 체크여부 기능 -->
                <span class="checkBtn"
                v-on:click="toggleComplete(todoItem, index)"
                v-bind:class="{checkBtnCompleted: todoItem.completed}">
                    <q-icon name="check" size="22px"></q-icon>
                </span>

                <!-- 할일 -->
                <span id="here" v-if="!todoItem.edit" :class="{textCompleted: todoItem.completed }" :contenteditable="todoItem.edit"> 
                    {{ todoItem.item }}
                </span>
                <input type="text" v-else v-model="todoItem.new_val">
                <!-- 2. 삭제 기능 -->
                <!-- (1) 아이콘 없는 버전 -->
                <!-- <button v-on:click="removeTodo(todoItem, index)">delete</button> -->

                <!-- (2) 아이콘 있는 버전 -->
                <span class="removeBtn" v-on:click="removeTodo(todoItem, index)">
                    <q-icon name="delete" size="22px"></q-icon>
                </span>

                <!-- 3. 수정 기능 -->
                <span >
                    <div v-if="todoItem.edit===false">
                        <q-btn class="editBtn" label="수정" v-on:click="editTodo(todoItem, index)"></q-btn>
                    </div>
                    <div v-else>
                        <q-btn class="editBtn" push label="완료" v-on:click="editOk(todoItem, index)"/>
                        <q-btn class="editBtn" push label="취소" v-on:click="editNo(todoItem, index)" />
                    </div>
                </span>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    props: ['value'],
    methods: {
        toggleComplete(todoItem, index){
            // this.$emit('toggleItem', todoItem, index)
            // 원래 기존거 삭제
            localStorage.removeItem(todoItem.item);

            // ** 1) 이벤트 버스를 통해 컴포넌트 간의 경계를 명확히 해야함
            // this.todoItems[index].completed = !this.todoItems[index].completed;
            
            const arr = [...this.value.slice(0, index), {...todoItem, completed: !todoItem.completed}, ...this.value.slice(index+1, this.value.length)];
            this.$emit("input", arr);

            // ** 2) 별로 안 좋은 거
            // todoItem.completed = !todoItem.completed;

            // 새로운 변경사항 반영해서 다시 저장
            localStorage.setItem(todoItem.item, JSON.stringify(todoItem))
        },
        removeTodo(todoItem, index){
            // this.$emit('removeItem', todoItem, index)
            localStorage.removeItem(todoItem.item);
            
            const newarr = [...this.value];
            newarr.splice(index, 1);

            this.$emit('input', newarr);
        },
        //수정 버튼
        editTodo(todoItem, index){
            if (todoItem.edit) return
            todoItem.edit = true;

            const arr = [...this.value.slice(0, index), {...todoItem, edit:todoItem.edit}, ...this.value.slice(index+1, this.value.length)];
            this.$emit('input', arr);
            
            localStorage.setItem(todoItem.item, JSON.stringify(todoItem));
        },
        // 완료 버튼
        editOk(todoItem, index){
            if (!todoItem.edit) return
            todoItem.edit = false;

            // 돔으로 직접 접근하면 Vue가 추적하기 힘들어서 지양해야한다.
            // 새로운 값 받기
            // let val = document.getElementById("here");
            // val = val.innerText.trim();
            
            
            // item들로 이루어진 배열
            const itemList = this.value.map(item=> item.item);
            
            // 중복키는 못 들어옴
            if (!itemList.includes(todoItem.new_val)){
                console.log(todoItem.item);
                // 원본 삭제 작업
                localStorage.removeItem(todoItem.item);
                
                // 값 변경(edit)
                let arr = [...this.value.slice(0, index), {...todoItem, edit: !todoItem.edit}, ...this.value.slice(index+1, this.value.length)];

                // 값 변경(item)
                arr = [...arr.slice(0, index), {...todoItem, item: todoItem.new_val}, ...arr.slice(index+1, arr.length)];

                // 값 갱신
                this.$emit('input', arr);

                localStorage.setItem(arr[index].item, JSON.stringify(arr[index]));

            }else{
                this.editNo(todoItem, index);
            }
        },
        // 취소 버튼
        editNo(todoItem,index){
            if (!todoItem.edit) return
            todoItem.edit = false;

            localStorage.removeItem(todoItem.item);

            // 텍스트 원상 복구
            // const mode = document.getElementById("here");
            // mode.innerText = todoItem.item;
            todoItem.new_val = todoItem.item;
            
            // 버튼 전환
            const arr = [...this.value.slice(0, index), {...todoItem, edit:todoItem.edit}, ...this.value.slice(index+1, this.value.length)];
            this.$emit('input', arr);
            localStorage.setItem(todoItem.item, JSON.stringify(todoItem));
        }
    }
   
}
</script>

<style lang="stylus" scoped>
$primary-color = #5378fb
$secondary-color = #8763fb

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

.checkBtn
  line-height 45px
  color #62acde
  margin-right 10px

.checkBtnCompleted
  color #b3adad

.textCompleted
  text-decoration line-through
  color #b3adad

.removeBtn
  margin-left auto
  margin-right 10px
  color #de4343

#here:not([contenteditable="true"])
  font-size 16px

input[type="text"]
  font-size 16px
  border none
  outline none

.editBtn
  font-size 14px
  border-radius 10px
  background linear-gradient(to right, $primary-color, $secondary-color)
  color white
  margin-right 4px

  &:last-child
    margin-right 0px
</style>