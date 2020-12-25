<template>
    <Widget style="min-height:744px;" class="flex1 " >
        <WidgetTitle>
            Monthly Spending Tally
        </WidgetTitle>
        <div class="padleft125 padright125 flex">
            <div  class="flex widgetsection" >
                <div 
                    v-for="item in cal" :key="item" @click="selectedMonth = item" 
                    :class="['borderRad4', 'pad025', 'padleft050', 'padright050', 'calItem', 
                    selectedMonth == item ? 'active' : '']" 
                    style="border: 1px solid #3b485c;" >{{item}}</div>
            </div>
            <div style="width:250px;" class="flex marginleft125 widgetsection" >
                <!-- available years scaned from statement -->
                <div 
                    v-for="year in availableYears" :key="year"
                    :class="['borderRad4', 'pad025', 'padleft050', 'padright050', 'calItem',
                    selectedYear == year ? 'active' : '']" 
                    style="border: 1px solid #3b485c;" >{{year}}</div>
            </div>
        </div>
        <WidgetContent style="min-height:400px;" class="relative pad125" >
            <template #widgetContent="{showModal}" >
                <div v-if="mbd_ready" 
                    style="min-height:400px; overflow: auto; border: 1px solid #3b485c" 
                    class="fullwidth pad050 padtop025 borderRad4 flex flexwrap" >
                    <!--  -->
                    <MBD_ITEM 
                        @itemClick="showModal"
                        v-for="item in $store.state.categories" 
                        :key="item.value" 
                        :item="item" 
                        :tally="tally" ></MBD_ITEM>
                    <!--  -->
                </div>
            </template>
            <template  #modal="{modalContext}" >
                <!-- <DonqueTable :dataSet="modalContext.items" /> -->
                <div >
                    <div class="padleft125 padtop125">
                        {{selectedMonth}} - {{modalContext.length && modalContext[0].transaction_purpose}}
                    </div>
                    <div class="flex spacebetween pad125" >
                        <div>Date 
                            <div style="color: #afafaf" v-for="(item,index) in modalContext" :key="`${item.date}-${index}`" ><small>{{item.date}}</small></div>
                        </div>
                        <div>Account 
                            <div style="color: #afafaf" v-for="(item,index) in modalContext" :key="`${item.statement_type}-${index}`" ><small>{{item.statement_type}}</small></div>
                        </div>
                        <div>Description
                            <div style="color: #afafaf" v-for="(item,index) in modalContext" :key="`${item.description}-${index + 3}`" ><small>{{item.description}}</small></div>
                        </div>
                        <div>Withdrawn Amount
                            <div style="color: orange" v-for="(item,index) in modalContext" :key="`${item.description}-${index + 9}`" ><small>{{moneyFormater(item.withdrawn_amount)}}</small></div>
                        </div>
                    </div>
                </div>
            </template>
        </WidgetContent>
    </Widget>
</template>

<script>
import MBD_ITEM from './mbd-item'
export default {
    components: {
        MBD_ITEM,
    },
    data: () => ({
        cal: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        selectedMonth: undefined,
        selectedYear: undefined,
        availableYears: undefined,
        tally: {},
        mbd_ready: false
    }),
    computed: {
        statements() {
            return this.$store.state.statements
        }
    },
    methods: {
       moneyFormater(value) {
            if(isNaN(value)) return '$0.00'

            var formatter = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',

            // These options are needed to round to whole numbers if that's what you want.
            //minimumFractionDigits: 0, // (this suffices for whole numbers, but will print 2500.10 as $2,500.1)
            //maximumFractionDigits: 0, // (causes 2500.99 to be printed as $2,501)
            });

            return formatter.format(value)
        },
    },
    watch: {
        selectedMonth(month) {
            this.mbd_ready = false
            this.$store.state.categories.map(e => {
                this.tally[e.value] = {}
                this.tally[e.value].total = {
                    debit: [],
                    credit: []
                }
                this.tally[e.value].items = []
            })
            
            this.statements.map(item => {
                if(item.report.monthOf == this.selectedMonth && item.report.yearOf == this.selectedYear) {
                    // debit
                    if(item.statements.debit.items.length != 0) {

                        // set total
                        item.statements.debit.items
                        .map(e => this.tally[e.transaction_purpose].total.debit.push(e.withdrawn_amount) )

                        // set
                        item.statements.debit.items.map(e => this.tally[e.transaction_purpose].items.push(e))
                    }
                    // credit
                    if(item.statements.credit.items.length != 0) {
                        // get withdrawns
                        item.statements.credit.items
                        .map(e => this.tally[e.transaction_purpose].total.credit.push(e.withdrawn_amount)) 

                        // set
                        item.statements.credit.items.map(e => this.tally[e.transaction_purpose].items.push(e))
                    }
                }
            })
            setTimeout(() => {
                this.mbd_ready = true
            },200)
        },
        statements() {
            if(this.selectedMonth == undefined) {
                this.$store.state.categories.map(e => {
                    this.tally[e.value] = {}
                    this.tally[e.value].total = {
                        debit: [],
                        credit: []
                    }
                    this.tally[e.value].items = []
                })

                setTimeout(() => {
                    this.mbd_ready = true
                    this.selectedMonth = 'Jan'
                    this.availableYears = this.$store.state.statementYears
                    this.selectedYear = this.availableYears[0]
                },0)
            }
        }
    }
}
</script>

<style>
.calItem:hover {
    background: orange;
    color: #333;
    cursor: pointer;
}
.calItem{
    min-width: 40px;
}
</style>