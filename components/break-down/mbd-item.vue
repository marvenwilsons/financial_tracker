<template>
    <div
        v-if="ready"
        @click="$emit('itemClick', finalTally)"
        class="pointer margintop050 pad050 widgetsection marginleft050 tallyItem" 
        style="background: #222e42; border: 1px solid #3b485c; width:240px;" >
        <div>
            <span><small>{{item.text}}</small></span>
        </div>
        <div class="flex flexcenter" >
            <!-- <div class="relative borderRad4" style="width:80%; height:10px; background: #515c6e;" >
                <div class="fullheight-percent absolute borderRad4" :style="{background:'orange', width:'90%' }" ></div>
            </div> -->
            <div style="border" class="flex1 flex flexwrap spacebetween" >
                <div>
                    <small class="flex" >
                        <span style="color: #afafaf;" class="marginright025 flex1" >Credit:</span>  
                        <span class="flex1" style="color:orange;" >
                            <pre >{{ moneyFormater(totalArray(removeDuplicate(tally[item.value].total.credit))) }}</pre>
                        </span>
                    </small>
                </div>
                 <div>
                    <small class="flex" >
                        <span style="color: #afafaf;" class="marginright025 flex1" >Total:</span>  
                        <span class="flex1" style="color:yellow;" >
                            <pre >{{ 
                                moneyFormater(
                                    totalArray(removeDuplicate(tally[item.value].total.debit)) +
                                    totalArray(removeDuplicate(tally[item.value].total.credit))
                                )
                                }}</pre>
                        </span>
                    </small>
                </div>
                <div>
                    <small class="flex" >
                        <span style="color: #afafaf;" class="marginright025 flex1" >Debit:</span>  
                        <span class="flex1" style="color:orange;" >
                            <pre >{{ moneyFormater(totalArray(removeDuplicate(tally[item.value].total.debit))) }}</pre>
                        </span>
                    </small>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import MyMixin from '@/m'
export default {
    mixins: [MyMixin],
    props: ['item', 'tally'],
    data: () => ({
        highestAmount: 0,
        finalTally: undefined,
        ready: false
    }),
    methods: {
        removeDuplicate(s) {
            if(s){
                if(s.length) {
                    return s.filter((item,index) => s.indexOf(item) == index)
                }   
            } else {
                0
            }
        },
        totalArray(numSet) {
            if(numSet) {
                if(numSet.length) {
                    return numSet.reduce((total,num) => total + num)
                } else {
                    return 0
                }   
            } else {
                return 0
            }
        }
    },
    mounted() {
        const seen = new Set();
        const filteredArr = this.tally[this.item.value].items.filter(el => {
            const duplicate = seen.has(`${el.withdrawn_amount}-${el.date}-${el.description}`);
            seen.add(`${el.withdrawn_amount}-${el.date}-${el.description}`);
            return !duplicate;
        });

        this.finalTally = filteredArr

        if(this.finalTally) {
            this.ready = true
        }
    }
}
</script>

<style>
.tallyItem:hover {
    border: 1px solid orange !important;
}
</style>