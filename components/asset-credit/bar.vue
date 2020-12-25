<template>
    <div 
        class="flex flexcol relative" 
        :style="{
            height:'100%',
            width:'10px',
            borderLeft: item.report.dayOf == '01' && `1px solid white`,
            }" 
    >
        <div v-if="selectedBar == index " class="absolute fullwidth fullheight-percent" style="background:rgba(255, 255, 0, 0.800); z-index: 100" >

        </div>
        <div class="absolute padleft050"  style="z-index:100;" v-if="item.report.dayOf == '01'">
            <small>{{item.report.monthOf}} {{item.report.yearOf}}</small>
        </div>
        <div style="align-self:flex-end" class="fullwidth flex1 relative">
            <!-- asset amount -->
            <div :style="{
                bottom:0, 
                background: '#7c8592', 
                height: `${item.bar.debitAmountHeight}%`}" class="smth absolute fullwidth" ></div>
            <!-- asset value -->
            <div :style="{
                bottom:0,
                background: item.statements.debit.inheritFrom ? '#7fbf7f' : '#3fd140', 
                height: `${item.bar.debitValueHeight}%`}" class="absolute fullwidth" ></div>
        </div>
         <div class="flex1 relative">
            <!-- no activity -->
            <div 
            v-if="item.report.msg == 'No Available Credit Data Reference To Inherit From'"
            :style="{height: `${item.bar.creditAmountHeight}%`, background: '#4a4f57', zIndex:100}" class="absolute fullwidth" > </div>
            <!-- creidt amount -->
            <div :style="{height: `${item.bar.creditAmountHeight}%`, background: '#7c8592'}" class="absolute fullwidth" > </div>
            <!-- credit value -->
            <div :style="{
                height: `${item.bar.creditValueHeight}%`, 
                background: item.statements.credit.inheritFrom ? '#ff9999' : 'red',
            }" class="absolute fullwidth" ></div>
        </div>
    </div>
</template>

<script>
// background: item.statement_type == 'credit' ? 'red' : '#3fd140'

export default {
    props: ['item', 'index', 'selectedBar'],
    data: () => ({
        height: 0
    }),
    mounted() {
        // setTimeout(() => {
            
        // }, this.index)
        this.$emit('chunkAdded', this.index + 1)
    }
}
</script>

<style scoped>
.bar:hover {
    /* border: 1px solid yellow; */
    transition: 100ms;
}
.date{
    bottom: 0;
    transform: rotate(60deg);
}
.smthw {
    transition: 1s;
}
</style>