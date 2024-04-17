<template lang="pug">
.list
    input(:id="item.id" type="checkbox" v-model="isCheck" :class="{ hide: !isHide }")    
    label(:for="item.id"  :class="{ checked: isCheck, hide: !isHide }") {{ item.content }}

    div(class="editBox" :class="{ hide : isHide }")
        input(v-model="inputValue") 
        q-btn(type="button" flat style="color: #FF0080" label="save" @click="onSubmit(item.id, inputValue)")

    div.btnBox(:class="{ hide : isEdit }")
        button(@click="onEdit")
            img(src="../assets/images/free-icon-edit.png")     
        button(@click="onDelete(item.id)") 
            img(src="../assets/images/free-icon-delete.png")
</template>

<script>
export default {
  name: 'TodoListItem',
  components: {},
  props: {
    item: {
      type: Object,
    },
    onUpdate: Function,
    onDelete: Function,
  },
  data() {
    return {
      isCheck: false,
      isHide: true,
      isEdit: false,
      inputValue: this.item.content,
    }
  },
  methods: {
    onEdit() {
      this.isHide = !this.isHide
      this.isEdit = !this.isEdit
    },
    onSubmit(itemId, text) {
      this.onEdit()
      this.onUpdate(itemId, text)
    },
  },
}
</script>

<style lang="stylus">
.checked
    text-decoration: line-through;
.hide
    display: none;

.list
    display: flex;
    align-items: center;
    width: 100%;
    padding: 0.5rem;
    &:nth-child(even)
        background: #FBF2EF;
    input
        padding-left: 1rem;
        margin-left: 1rem;
        margin-right: 1rem;
        cursor: pointer;
        accent-color: #f5426c;
    .editBox
        width: 100%;
        input
            background: transparent;
            width: 80%;
            height: 2.2rem;
            border: 1px solid black;
        label
            cursor: pointer;

.btnBox
    margin-left auto;
    button
        background: none;
        border: none;
        cursor: pointer;
        img
            width: 1.5rem;
</style>
