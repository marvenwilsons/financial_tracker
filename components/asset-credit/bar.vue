<template>
    <div 
        class="flex  flexcol" 
        :style="{
            height:'50%', 
            alignSelf: item.statement_type == 'credit' ? 'flex-end' : 'flex-start'}" 
    >
        <div class="flex fullheight-percent" >
            <div 
                class="bar pointer" 
                :style="{
                    height: `${item.height}%`, 
                    width:`5px`,
                    borderBottom:'1px solid #be5a4b',
                    background: item.statement_type == 'credit' ? '#c81c01' : '#3fd140', 
                    alignSelf: item.statement_type == 'debit' && 'flex-end'
                }" 
            ></div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['item']
}
</script>

<style scoped>
.bar:hover {
    /* border: 1px solid yellow; */
    transition: 300ms;
}
.date{
    bottom: 0;
    transform: rotate(60deg);
}
</style>