<template>
    <div class="flex spacebetween flexcenter" >
        <div class="fullwidth marginright050" >
            <small>
                <span style="color:#afafaf;" >Coverage:</span> 
                <span style="color:yellow" >({{StatementDataSet.length}} Days) <span style="color:#afafaf;" >
                    From:</span> {{StatementDataSet[0].date}}
                </span> 
                <span style="color:yellow" >  <span style="color:#afafaf;" >
                    To:</span> {{StatementDataSet[StatementDataSet.length - 1].date}}
                </span>
            </small>
        </div>
        <div class="" >
            <div class="flex" >
                <div  @mousedown="mousedown('left')" @mouseup="mouseup('left')" class="pointer marginright025" >
                    ⬅️
                </div>
                <div  @mousedown="mousedown('right')" @mouseup="mouseup('right')"  class="pointer" >
                ➡️
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['StatementDataSet'],
    data: () => ({
        stopScrolling: false
    }),
    methods: {

        scrollToLeft() {
            this.$emit('scrollToLeft')
        },
        scrollToRight() {
            this.$emit('scrollToRight')
        },
        keepScrolling(direction, stop) {
            if(this.stopScrolling == false) {
                const scrollInterval = setInterval(() => {
                    if(direction == 'left') {
                        this.scrollToLeft()
                    } else {
                        this.scrollToRight()
                    }

                    if(this.stopScrolling == true) {
                        clearInterval(scrollInterval)
                    }
                },40)
            }
        },
        mousedown(mode) {
            // console.log('mouse down', mode)
            this.stopScrolling = false
            this.keepScrolling(mode)
        },
        mouseup(mode) {
            // console.log('stop')
            this.stopScrolling = true
        }
    }
}
</script>

<style >

</style>