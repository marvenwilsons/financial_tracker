<template>
    <div class="fullwidth widgetsection pad125 borderRad4 relative" >
        <!-- settings -->
        <DonqueSettingComponent ref="setting" >
            <template v-slot:selected="{ selected }">
                <AssetCreditCoverageSetting  v-if="selected == 'Coverage'" />
                <AssetCreditBarSetting       v-if="selected == 'Bar'" />
                <AssetCreditDataDisplay      v-if="selected == 'Data Display'"/>
            </template>
        </DonqueSettingComponent>

        <div style="color: #afafaf" class="flex flexcenter marginbottom125" >
            Asset VS Credit
        </div>
        <div class="flex spacebetween">
            <div>
                <small style="color:#afafaf" >
                    MUP: <span style="color:yellow;" >{{moneyFormater(assetMaximumPeak.balance_amount)}}</span> on 
                    <span style="color:yellow;" > {{dateFormater(assetMaximumPeak.date,'YYYY/MM/DD')}} </span> - asset
                </small>
            </div>
            <div 
                @click="() =>  $refs.setting.toggle(['Coverage', 'Data Display', 'Bar'])" 
                class="pointer" >
                ⚙️ 
            </div>
        </div>

        <!--  -->
        <div style="height:250px; align-items:center; overflow:hidden;" class="relative flex" >
            <div style="height:95%; z-index:1" class="absolute flex flexcenter" >
               <small style="color:#afafaf" >
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
                            <bar :index="index" :item="item" />
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
                    MDP: 
                    <span style="color:yellow;" >{{moneyFormater(creditMaximumPeak.balance_amount)}}</span> on
                    <span style="color:yellow;" >{{dateFormater(creditMaximumPeak.date,'YYYY/MM/DD')}}</span>
                     - credit
                </small>
            </div>
            <!-- bottom-option-bar -->
            <bottomOptionBar
                @scrollToLeft="scroll('left')"
                @scrollToRight="scroll('right')"
                :StatementDataSet="statements"
             />
        </div>

    </div>
</template>

<script>
import bar from '@/components/asset-credit/bar'
import bottomOptionBar from '@/components/asset-credit/bottom-action-bar'
import barInfo from '@/components/asset-credit/bar-info'
import DonqueSettingComponent from '@/components/settings-pane/window'

import AssetCreditCoverageSetting from '@/components/asset-credit/settings/coverage'
import AssetCreditBarSetting from '@/components/asset-credit/settings/bar'
import AssetCreditDataDisplay from '@/components/asset-credit/settings/data-display'

export default {
    props: ['StatementDataSet'],
    components: {
        bar,
        bottomOptionBar,
        barInfo,
        DonqueSettingComponent,
        AssetCreditCoverageSetting,
        AssetCreditBarSetting,
        AssetCreditDataDisplay
    },
    data: () => ({
        statements: [],
        barMove: 0,
        creditMaximumPeak: 0,
        assetMaximumPeak: 0,
        openSetting: false,
        months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
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
        },
        openSettings() {
            this.openSetting = true
        },
        onSettingChange(obj) {

        },
        moneyFormater(value) {
            var formatter = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',

            // These options are needed to round to whole numbers if that's what you want.
            //minimumFractionDigits: 0, // (this suffices for whole numbers, but will print 2500.10 as $2,500.1)
            //maximumFractionDigits: 0, // (causes 2500.99 to be printed as $2,501)
            });

            return formatter.format(value)
        },
        dateFormater(value,formatOrigin) {
            if(value) {
                const formatOriginYear = formatOrigin.split('/').indexOf('YYYY')
                const formatOriginMonth = formatOrigin.split('/').indexOf('MM')
                const formatOriginDay = formatOrigin.split('/').indexOf('DD')
                const sliceValue = value.split('/')
                
                const months = this.months
                const final = `${ months[parseInt(sliceValue[formatOriginMonth]) - 1] } ${sliceValue[formatOriginDay]}, ${sliceValue[formatOriginYear]}`
                return final
            } else {
                return value
            }
            
        }
    },
    mounted() {
        this.statements = []
        const rawData= this.StatementDataSet

        const findPercenOfTotal = (totalValue, numberVsTotal) => {
            const a = numberVsTotal / totalValue
            const b = a * 100
            return b
        }
        const parsedDataSet = []

        // for credit
        const creditMaximumPeak = rawData.map(e => e.statement_type == 'credit' && e.balance_amount).sort((a,b) => b - a)[0]
        const creditMaximumPeakObject = rawData.filter(e => e.balance_amount == creditMaximumPeak)[0]
        this.creditMaximumPeak = creditMaximumPeakObject


        let assetMaximumPeak = rawData.map(e => e.statement_type == 'debit' && e.balance_amount).sort((a,b) => b - a)[0]
        const assetMaximumPeakObject = rawData.filter(e => e.balance_amount == assetMaximumPeak)[0]
        this.assetMaximumPeak = assetMaximumPeakObject

        // credit
        rawData.map(item => {
            if(item.statement_type == 'credit') {
                parsedDataSet.push({
                    height: Math.round(findPercenOfTotal(creditMaximumPeak,item.balance_amount)) < 0 ? 0 : Math.round(findPercenOfTotal(creditMaximumPeak,item.balance_amount)),
                    statement_type: item.statement_type,
                    date: this.dateFormater(item.date,'YYYY/MM/DD'),
                    balance_amount: Math.round(item.balance_amount),
                })
            } else {
                parsedDataSet.push({
                    height: Math.round(findPercenOfTotal(assetMaximumPeak,item.balance_amount)) < 0 ? 0 : Math.round(findPercenOfTotal(assetMaximumPeak,item.balance_amount)),
                    statement_type: item.statement_type,
                    date: this.dateFormater(item.date,'YYYY/MM/DD'),
                    balance_amount: Math.round(item.balance_amount),
                })
            }
            
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