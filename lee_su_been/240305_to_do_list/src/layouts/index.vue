<template lang="pug">
q-layout(view="1Hh Lor lFf")
    TodoHeader
    q-page-container
        router-view
    

</template>

<script>
import TodoHeader from '../components/TodoHeader.vue';
export default {
components: {
    TodoHeader
}
}
</script>

<style lang="stylus">

</style>