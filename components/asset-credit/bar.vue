<template>
    <div 
        class="flex  flexcol" 
        :style="{
            height:'100%',
            width:'10px',
            alignSelf: item.statement_type == 'credit' ? 'flex-end' : 'flex-start'}" 
    >
        <div style="align-self:flex-end" class="fullwidth flex1 relative">
            <!-- asset amount -->
            <div :style="{bottom:0, background: '#7c8592', height: `${item.bar.debitAmountHeight}%`}" class="smth absolute fullwidth" ></div>
            <!-- asset value -->
            <div :style="{bottom:0, background: '#3fd140', height: `${item.bar.debitValueHeight}%`}" class="absolute fullwidth" ></div>
        </div>
         <div class="flex1 relative">
            <!-- creidt amount -->
            <div :style="{height: `${item.bar.creditAmountHeight}%`, background: '#7c8592'}" class="absolute fullwidth" > </div>
            <!-- credit value -->
            <div :style="{height: `${item.bar.creditValueHeight}%`, background: 'red'}" class="absolute fullwidth" > </div>
        </div>
    </div>
</template>

<script>
// background: item.statement_type == 'credit' ? 'red' : '#3fd140'

export default {
    props: ['item', 'index'],
    data: () => ({
        height: 0
    }),
    mounted() {
        // const incrementHeight = setInterval(() => {
        //     if(this.height != this.item.height) {
        //         const addAmount = this.item.height / 8
        //         // this.height = this.height + addAmount
        //         // this.height = this.item.height
        //         this.$emit('chunkAdded', this.index + 1)
        //     } else {
        //         clearInterval(incrementHeight)
        //     }
        // },this.index)

        setTimeout(() => {
            this.$emit('chunkAdded', this.index + 1)
        }, this.index)
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