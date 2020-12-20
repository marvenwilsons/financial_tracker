<template>
    <div 
        class="flex  flexcol" 
        :style="{
            height:'50%', 
            alignSelf: item.statement_type == 'credit' ? 'flex-end' : 'flex-start'}" 
    >
        <div class="flex fullheight-percent" >
            <div 
                class="bar pointer smthw" 
                :style="{
                    height: `${height}%`, 
                    width:`10px`,
                    borderBottom:'1px solid #be5a4b',
                    background: item.statement_type == 'credit' ? 'red' : '#3fd140', 
                    alignSelf: item.statement_type == 'debit' && 'flex-end'
                }" 
            ></div>
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
        const incrementHeight = setInterval(() => {
            if(this.height != this.item.height) {
                const addAmount = this.item.height / 8
                // this.height = this.height + addAmount
                this.height = this.item.height
                this.$emit('chunkAdded', this.index + 1)
            } else {
                clearInterval(incrementHeight)
            }
        },this.index)
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