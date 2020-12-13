<template>
    <div class="fullwidth widgetsection pad125 borderRad4" >
        <div style="color: #afafaf" class="flex flexcenter marginbottom125" >
            Asset VS Credit
        </div>
        <div class="flex spacebetween">
            <div>
                <small style="color:#afafaf" >
                    MP: <span style="color:yellow;" >$4,250</span> on August 5, 2020 - asset
                </small>
            </div>
            <div class="pointer" >
                ⚙️ 
            </div>
        </div>

        <!--  -->
        <div style="height:250px; align-items:center; overflow:hidden;" class="relative flex" >
            <div style="height:95%; z-index:1" class="absolute flex flexcenter" >
               <small>
                    0
               </small>
            </div>
            <div style="border-top:1px solid gray;" class="absolute fullwidth marginleft050" >
            </div>
            <!-- charts bar here -->
            <div style="width:1900px; overflow-x:hidden; border-top:1px solid gray; border-bottom:1px solid gray;" 
            class="fullheight-percent fullwidth flex relative pad050 marginleft025" >
                <div  class="fullheight-percent" >
                    <div id="barParent" :style="{alignItems:'center', transform: `translateX(${barMove}px)`}" 
                    class="flex fullheight-percent flexcenter p"  >
                        <!-- bar item -->
                        <div v-for="(item,index) in statements" :key="index" class="relative bar-parent fullheight-percent flex" >
                            <barInfo
                             :item="item" />
                            <bar :item="item" />
                        </div>
                        <!-- end -->
                    </div>
                </div>
            </div>
        </div>
        <!--  -->
        <div class="flex spacebetween">
            <div class="flex1" >
                <small style="color:#afafaf" >
                    MP: <span style="color:yellow;" >$4,250</span> on August 5, 2020 - credit
                </small>
            </div>
            <!-- bottom-option-bar -->
            <bottomOptionBar
                @scrollToLeft="scroll('left')"
                @scrollToRight="scroll('right')"
             />
        </div>

    </div>
</template>

<script>
import bar from '@/components/asset-credit/bar'
import bottomOptionBar from '@/components/asset-credit/bottom-action-bar'
import barInfo from '@/components/asset-credit/bar-info'
export default {
    components: {
        bar,
        bottomOptionBar,
        barInfo
    },
    data: () => ({
        statements: [],
        barMove: 0,
    }),
    methods: {
        scroll(mode) {
            // console.log('test', mode)
            const barParent = document.getElementById('barParent')

            if(barParent.offsetWidth > 882) {
                if(mode == 'right') {
                    const stopCondition = (Math.abs(this.barMove) + 750) > barParent.offsetWidth
                    if(stopCondition == false) {
                        this.barMove = this.barMove - 40
                    }
                } else if( mode == 'left') {
                    if(this.barMove != 0) {
                        this.barMove = this.barMove + 40
                    }
                }
            }
        }
    },
    mounted() {
        this.statements = []
        const rawData = [
            {
                statement_type: 'credit',
                date: '05/05/2020',
                withdrawn_amount: 14.99,
                deposited_amount: 0,
                balance_amount: 4243.61,
                description: 'Credit Test 1'
            },
            {
                statement_type: 'credit',
                date: '05/05/2020',
                withdrawn_amount: 34.75,
                deposited_amount: 0,
                balance_amount: 4278.36,
                description: 'Credit Test 2'
            },
            {
                statement_type: 'credit',
                date: '05/05/2020',
                withdrawn_amount: 15.60,
                deposited_amount: 0,
                balance_amount: 4293.96,
                description: 'Credit Test 3'
            },
            {
                statement_type: 'credit',
                date: '05/05/2020',
                withdrawn_amount: 15.60,
                deposited_amount: 0,
                balance_amount: 5293.96,
                description: 'Credit Test 3'
            },
            {
                statement_type: 'credit',
                date: '05/05/2020',
                withdrawn_amount: 15.60,
                deposited_amount: 0,
                balance_amount: 3100,
                description: 'Credit Test 3'
            },
            {
                statement_type: 'credit',
                date: '05/05/2020',
                withdrawn_amount: 15.60,
                deposited_amount: 0,
                balance_amount: 2100,
                description: 'Credit Test 3'
            },
            {
                statement_type: 'credit',
                date: '05/05/2020',
                withdrawn_amount: 15.60,
                deposited_amount: 0,
                balance_amount: 1100,
                description: 'Credit Test 3'
            },
            {
                statement_type: 'credit',
                date: '05/05/2020',
                withdrawn_amount: 15.60,
                deposited_amount: 0,
                balance_amount: 900,
                description: 'Credit Test 3'
            },
            {
                statement_type: 'credit',
                date: '05/05/2020',
                withdrawn_amount: 15.60,
                deposited_amount: 0,
                balance_amount: 100,
                description: 'Credit Test 3'
            },
            //
            {
                statement_type: 'debit',
                date: '',
                withdrawn_amount: 300,
                deposited_amount: 0,
                balance_amount: 2000,
                description: 'Debit Test 1'
            },
            {
                statement_type: 'debit',
                date: '',
                withdrawn_amount: 300,
                deposited_amount: 0,
                balance_amount: 1900,
                description: 'Debit Test 2'
            },
            {
                statement_type: 'debit',
                date: '',
                withdrawn_amount: 300,
                deposited_amount: 0,
                balance_amount: 1800,
                description: 'Debit Test 3'
            }
        ]

        // fetch statements


        const findPercenOfTotal = (totalValue, numberVsTotal) => {
            const a = numberVsTotal / totalValue
            const b = a * 100
            return b
        }
        const parsedDataSet = []

        // for credit
        let assetMaximumPeak = 0
        for(let i = 0; i < 191; i++) {
            rawData.push( {
                statement_type: 'credit',
                date: '05/05/2020',
                withdrawn_amount: 14.99,
                deposited_amount: 0,
                balance_amount: 4243.61 + (i * 100),
                description: 'Credit Test 1'
            },)
        }
        let creditMaximumPeak = rawData.map(e => e.statement_type == 'credit' && e.balance_amount).sort((a,b) => b - a)[0]

        rawData.map(item => {
            parsedDataSet.push({
                height: Math.round(findPercenOfTotal(creditMaximumPeak,item.balance_amount)) < 0 ? 0 : Math.round(findPercenOfTotal(creditMaximumPeak,item.balance_amount)),
                statement_type: item.statement_type,
                date: item.date,
                balance_amount: Math.round(item.balance_amount),
            })
        })

        this.statements = parsedDataSet
    }
}
</script>

<style >
.bar-parent:hover{
    border:1px solid yellow;
}
.bar-info {
    display: none;
    background: yellow;
    left: 10px;
    top: -1px;
    color: black;
    font-size: 11px;
    z-index: 100;
}
.bar-parent:hover > .bar-info {
    display: block;
}
.p {
    transition: 500ms;
}
</style>