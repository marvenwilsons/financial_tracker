<template>
    <div class="flex fullheight-percent" >
        <div class="flex1" >
            <div
             @click="selected = item" v-for="item in menu" :key="item"  
            :class="[selected == item ? 'active' : '', 'padleft025', 'pointer', 'item']" >
                <small>{{item}}</small>
            </div>
        </div>
        <div style="border:1px solid #afafaf" class="relative flex4" >
            <slot name="selected" :selected="selected" ></slot>
        </div>
    </div>
</template>

<script>
export default {
    props: ['menu'],
    data: () => ({
        selected: undefined
    }),
    mounted() {
        this.selected = this.menu[0]
    }
}
</script>

<style scoped>
.item:hover {
    font-weight: 600;
    transition: 300ms;
}
.active {
    font-weight: 600;
}
</style>