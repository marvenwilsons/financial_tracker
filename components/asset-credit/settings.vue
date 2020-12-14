<template>
    <div class="flex fullheight-percent" >
        <div class="flex1" >
            <div @click="selected = item" v-for="item in settings" :key="item"  :class="[selected == item ? 'active' : '', 'padleft025', 'pointer', 'item']" >
                <small>{{item}}</small>
            </div>
        </div>
        <div style="border:1px solid #afafaf" class="relative flex4" ></div>
    </div>
</template>

<script>
export default {
    data: () => ({
        settings: ['Coverage', 'Data Display', 'Bar'],
        selected: 'Coverage'
    })
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