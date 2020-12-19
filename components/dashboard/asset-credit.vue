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
                    MUP: <span style="color:yellow;" >{{assetMaximumPeak ? moneyFormater(assetMaximumPeak.balance_amount) : 'N/A'}}</span> on 
                    <span style="color:yellow;" > {{assetMaximumPeak ? dateFormater(assetMaximumPeak.date,'YYYY/MM/DD') : 'N/A'}} </span> - asset
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
                             :item="item"
                             :moneyFormater="moneyFormater" />
                            <bar :index="index" :item="item" />
                        </div>
                        <!-- end -->
                    </div>
                </div>
            </div>
        </div>
        <!--  -->
        <div class="flex spacebetween">
            <div class="flex2" >
                <small style="color:#afafaf" >
                    MDP: 
                    <span style="color:yellow;" > {{creditMaximumPeak ? moneyFormater(creditMaximumPeak.balance_amount) : 'N/A'}}</span> on
                    <span style="color:yellow;" >{{creditMaximumPeak ? dateFormater(creditMaximumPeak.date,'YYYY/MM/DD') : 'N/A'}}</span>
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
                    const stopCondition = (Math.abs(this.barMove) + 550) > barParent.offsetWidth
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
            
        },
        getTotalDaysOfMonth(month,yearEndVal) {
            function isEven(value) {
                if(value == 0 || value == '00') {
                    return true
                } else {
                    if (value%2 == 0)
                        return true;
                    else
                        return false;
                }
                
            }                                                                                                                       
            switch(month) {
                case 'Jan':
                    return 31
                case 'Feb':
                    return  isEven(yearEndVal) ? 29 : 28
                case 'Mar':
                    return 31
                case 'Apr':
                    return 30
                case 'May':
                    return 31
                case 'Jun':
                    return 30
                case 'Jul':
                    return 31
                case 'Aug':
                    return 31
                case 'Sep':
                    return 30
                case 'Oct':
                    return 31
                case 'Nov':
                    return 30
                case 'Dec':
                    return 31
            }
        },
        getCalendar(year) {
            // fill the gaps
            const monthsWithExpectedDays = {Jan:[],Feb:[],Mar:[],Apr:[],May:[],Jun:[],Jul:[],Aug:[],Sep:[],Oct:[],Nov:[],Dec:[]}

            for(const key in monthsWithExpectedDays) {
                for(var i = 0; i < this.getTotalDaysOfMonth(key); i++) {
                    monthsWithExpectedDays[key].push(`${key} ${(i + 1) < 10 ? `0${i + 1}` : `${i + 1}`}, ${year}`)
                }
            }
            return monthsWithExpectedDays
        },
        getMonthIndex(month) {
            switch(month) {
                case 'Jan':
                    return 0
                case 'Feb':
                    return 1
                case 'Mar':
                    return 2
                case 'Apr':
                    return 3
                case 'May':
                    return 4
                case 'Jun':
                    return 5
                case 'Jul':
                    return 6
                case 'Aug':
                    return 7
                case 'Sep':
                    return 8
                case 'Oct':
                    return 9
                case 'Nov':
                    return 10
                case 'Dec':
                    return 11
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
        const scannedYears = []
        rawData.map(item => {
            const year = item.date.split('/')[0]
            if(scannedYears.includes(year) == false) {
                scannedYears.push(year)
            }

            parsedDataSet.push({
                // height: Math.round(findPercenOfTotal(assetMaximumPeak,item.balance_amount)) < 0 ? 0 : Math.round(findPercenOfTotal(assetMaximumPeak,item.balance_amount)),
                statement_type: item.statement_type,
                date: this.dateFormater(item.date,'YYYY/MM/DD'),
                balance_amount: Math.round(item.balance_amount),
                withdrawn_amount: item.withdrawn_amount,
                deposited_amount: item.deposited_amount,
                description: item.description
            })
        })

        this.statements = parsedDataSet

        const template = {}
        
        // create tenplate using the year(s) used in dataSet
        scannedYears.map(year => {
            const calendar = this.getCalendar(year)
            for(const month in calendar) {
                calendar[month].map(day => {
                    template[day] = {
                        statements: {
                            credit: {
                                initialDeptBalanceOfTheDay: 0,
                                finalDeptBalanceOfTheDay: 0,
                                totalAmountPaidOfTheDay: 0,
                                totalBorrowedAmountOfTheDay: 0,
                                items: []
                            },
                            debit: {
                                highestAmountOfTheDay:0,
                                lowestAmountOfTheDay: 0,
                                initialBalanceOfTheDay: 0,
                                finalBalanceOfTheDay: 0,
                                totalAmountSubtracted: 0,
                                items: []
                            },
                        },
                        report: {
                            date: `${month} ${day.split(' ')[1].replace(',','')}, ${year}`,
                            monthOf: month,
                            yearOf: parseInt(year),
                            dayOf: parseInt(day.split(' ')[1].replace(',','')),
                            monthIndex: this.getMonthIndex(month),
                            finalAssetValue: 0,
                            finalDeptValue: 0,
                            initialAssetValue: 0,
                            initialDeptValue: 0,
                            hasActivity: false,
                            statementInheritDate: null,
                            totalWithdrawnAmount: 0,
                            msg: null,
                            progress_type: null
                        },
                        bar: {
                            creditAmountHeight: 0,
                            creditValueHeight: 0,
                            debitAmountHeight: 0,
                            debitValueHeight: 0
                        }
                    }
                })
            }
        })

        // populate template with statement using date
        parsedDataSet.map(e => {
            if(e.statement_type == 'credit') {
                template[e.date].statements.credit.items.push(e)
            } else {
                template[e.date].statements.debit.items.push(e)
            }
        })

        // mark days without activity
        for(const item in template) {
            if(template[item].statements.length != 0) {
                template[item].report.hasActivity = true
            }
        }
        

        const finalDataSet = []

        // sort data
        scannedYears.map(year => {
            for(var i = 0; i < 12; i++) {
                for(const item in template) {
                    if(template[item].report.yearOf == year) {
                        if(template[item].report.monthIndex == i) {
                            finalDataSet.push(template[item])
                        }
                    }
                }
            }
        })

        // populate days without activity
        let lastDebitDayStatement= undefined
        let lastCreditDayStatement = undefined
        
        for(var i = 0; i < finalDataSet.length; i++) {
            if(finalDataSet[i].statements.credit.items.length != 0) {
                lastCreditDayStatement = finalDataSet[i].statements.credit
                // console.log(`Credit: Found non empty data assigning now ${finalDataSet[i].report.date}`)
            }
            if(finalDataSet[i].statements.debit.items.length != 0) {
                lastDebitDayStatement = finalDataSet[i].statements.debit
                // console.log(`Debit: Found non empty data assigning now ${finalDataSet[i].report.date}`)

            }

            if(finalDataSet[i].statements.credit.items.length == 0 && lastCreditDayStatement != undefined) {
                finalDataSet[i].statements.credit = lastCreditDayStatement
            }
            if(finalDataSet[i].statements.debit.items.length == 0 && lastDebitDayStatement != undefined) {
                finalDataSet[i].statements.debit = lastDebitDayStatement
            }
        }

        // set statementInheritDate property
        for(var i = 0; i < finalDataSet.length; i ++) {
            if(i != 0) {
                finalDataSet[i].report.statementInheritDate = finalDataSet[i - 1].report.date
            }

            // set initialAssetAmount, initialDeptAmount, totalWithdrawnAmount
            if(finalDataSet[i].statements.length != 0) {
                if(finalDataSet[i].statements.debit.items.length != 0) {
                    const finalBalanceOfTheDay = finalDataSet[i].statements.debit.items[0].balance_amount
                    finalDataSet[i].statements.debit.finalBalanceOfTheDay = finalBalanceOfTheDay

                    const initialBalanceOfTheDay = finalDataSet[i].statements.debit.items[finalDataSet[i].statements.debit.items.length - 1].balance_amount
                    finalDataSet[i].statements.debit.initialBalanceOfTheDay = initialBalanceOfTheDay

                    const withdrawnAmountOftheDay = finalDataSet[i].statements.debit.items.map(e => e.withdrawn_amount).reduce((total,num) => total + num)
                    finalDataSet[i].statements.debit.totalAmountSubtracted = withdrawnAmountOftheDay

                    const highesLowestAmountOfTheDay = finalDataSet[i].statements.debit.items.map(e => e.balance_amount).sort((a,b) => b - a)
                    finalDataSet[i].statements.debit.highestAmountOfTheDay = highesLowestAmountOfTheDay[0]
                    finalDataSet[i].statements.debit.lowestAmountOfTheDay = highesLowestAmountOfTheDay[highesLowestAmountOfTheDay.length - 1]
                } else {
                    // debit without activity should inherit the day before prop
                    // a debit without items is invalid
                    console.log('DEBIT:: \t cant find reference ==> ', finalDataSet[i].report.date)
                }

                if(finalDataSet[i].statements.credit.items.length != 0) {
                    const withdrawnsOfTheDay = Math.round(finalDataSet[i].statements.credit.items.map(e => e.withdrawn_amount).reduce((total,num) => total + num))
                    finalDataSet[i].statements.credit.totalBorrowedAmountOfTheDay = withdrawnsOfTheDay

                    const initialDeptBalanceOfTheDay = finalDataSet[i].statements.credit.items[finalDataSet[i].statements.credit.items.length - 1].balance_amount
                    finalDataSet[i].statements.credit.initialDeptBalanceOfTheDay = initialDeptBalanceOfTheDay

                    const totalAmountPaidOfTheDay = Math.round(finalDataSet[i].statements.credit.items.map(e => e.deposited_amount).reduce((total,num) => total + num))
                    finalDataSet[i].statements.credit.totalAmountPaidOfTheDay = totalAmountPaidOfTheDay

                    const finalDeptBalanceOfTheDay = finalDataSet[i].statements.credit.items[0].balance_amount
                    finalDataSet[i].statements.credit.finalDeptBalanceOfTheDay = finalDeptBalanceOfTheDay
                } else {
                    // credit without activity should inherit the day before prop
                    // a credit without items is invalid
                    console.log('CREDIT:: \t cant find reference ==> ', finalDataSet[i].report.date)
                }

                const { credit, debit } = finalDataSet[i].statements

                const finalAssetValue = (debit.finalBalanceOfTheDay - credit.finalDeptBalanceOfTheDay) < 0 ? 0 :  debit.finalBalanceOfTheDay - credit.finalDeptBalanceOfTheDay
                finalDataSet[i].report.finalAssetValue = finalAssetValue

                const finalDeptValue = (credit.finalDeptBalanceOfTheDay - debit.finalBalanceOfTheDay) < 0 ? 0 :  credit.finalDeptBalanceOfTheDay - debit.finalBalanceOfTheDay
                finalDataSet[i].report.finalDeptValue = finalDeptValue

                const initialAssetValue = finalDataSet[i].statements.debit.initialBalanceOfTheDay - finalDataSet[i].statements.credit.initialDeptBalanceOfTheDay
                finalDataSet[i].report.initialAssetValue =  initialAssetValue

                const initialDeptValue = finalDataSet[i].statements.credit.initialDeptBalanceOfTheDay - finalDataSet[i].statements.debit.initialBalanceOfTheDay
                finalDataSet[i].report.initialDeptValue = initialDeptValue

                if(finalAssetValue == 0 || finalAssetValue < 0) {
                    finalDataSet[i].report.msg = `Asset value went down to zero, and liablilty value went up to ${finalDeptValue}`
                    finalDataSet[i].report.progress_type = 'negative'
                } else if(finalAssetValue > 0 && finalDeptValue <= 0 ) {
                    finalDataSet[i].report.msg = `Asset value went up to ${finalAssetValue}`
                    finalDataSet[i].report.progress_type = 'positive'
                }


            }

        }

        
        console.log(finalDataSet)


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
    top: 20px;
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