<template>
    <div class="fullheight-percent"  :style="{width:`${width}%`, background:'rgba(55, 201, 55, 0.600)'}"></div>
</template>
<script>
export default {
    props: ['index', 'dataSetLength'],
    data: () => ({
        width: 0
    }),
    mounted() {
        setTimeout(() => {
            const incrementWidth = setInterval(() => {
                if(this.width == 100) {
                    clearInterval(incrementWidth)
                    if(this.dataSetLength - 1 == this.index) {
                        this.$emit('loadingComplete')
                    }
                } else {
                    this.width  = this.width + 5
                }

            },0.1)
        }, this.index * 100);

        
    }
}
</script>