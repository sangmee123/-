<template lang="pug">
header.nav
    div.color-box(v-for="(color, index) in colors" :key="index" :style="{ backgroundColor: '#' + color }" @click="changeTextColor(color)" :class="{ selected: value === color }")
</template>

<script>
export default {
  props: {
    value: String,
  },
  data() {
    return {
      colors: ['343a40', 'f03e3e', '12b886', '228ae6'],
    };
  },
  methods: {
    changeTextColor(color) {
      this.$emit('input', color);
    },
  },
};
</script>

<style scoped lang="stylus">
.nav
  display: flex
  justify-content: center
  gap: 1rem

.color-box
  opacity: .5
  width: 50px
  height: 50px
  transition: all .2s;

.color-box:hover
  opacity: 1
  cursor: pointer

.selected
  opacity: 1
</style>
