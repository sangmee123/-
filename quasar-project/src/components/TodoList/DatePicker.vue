<template lang="pug">
div.q-pa-md(style="max-width: 180px")
    q-input(filled, v-model="date", mask="date", :rules="['date']" )
        template(slot="append")
            q-icon(name="event", class="cursor-pointer")
                q-popup-proxy(cover, transition-show="scale", transition-hide="scale")
                    q-date(v-model="date" @input="emitDate")
                        div.row.items-center.justify-end
                            q-btn(v-close-popup, label="Close", color="primary", flat)
</template>

<script>
export default {
    data() {
        return {
            date: new Date().toISOString().substr(0, 10).replace(/-/g, '/')
        };
    },
    methods: {
        emitDate() {
            this.$emit('update:date', this.date);
        }
    }
}
</script>

<style lang="stylus">

</style>
