<template>
    <Widget style="min-height:744px;" class="flex1 " >
        <WidgetTitle>
            Monthly Spending Tally
        </WidgetTitle>
        <div class="padleft125 padright125 flex">
            <div  class="flex widgetsection" >
                <div 
                    v-for="item in cal" :key="item" @click="selectedMonth = item" 
                    :class="['borderRad4', 'pad025', 'padleft050', 'padright050', 'calItem', selectedMonth == item ? 'active' : '']" 
                    style="border: 1px solid #3b485c;" >{{item}}</div>
            </div>
            <div style="width:250px;" class="flex marginleft125 widgetsection" >
                <!-- available years scaned from statement -->
                <div 
                
                    v-for="year in availableYears" :key="year"
                    :class="['borderRad4', 'pad025', 'padleft050', 'padright050', 'calItem', selectedYear == year ? 'active' : '']" 
                    style="border: 1px solid #3b485c;" >{{year}}</div>
            </div>
        </div>
        <div style="min-height:400px;" class="relative pad125" >
            <div v-if="mbd_ready" style="min-height:400px; overflow: auto; border: 1px solid #3b485c" class="fullwidth pad050 padtop025 borderRad4 flex flexwrap" >
                <!--  -->
                <MBD_ITEM v-for="item in $store.state.categories" :key="item.value" :item="item" :tally="tally" ></MBD_ITEM>
                <!--  -->
            </div>
        </div>
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
       
    },
    watch: {
        selectedMonth(month) {
            this.mbd_ready = false
            this.statements.map(item => {
                if(item.report.monthOf == this.selectedMonth && item.report.yearOf == this.selectedYear) {
                    // debit
                    if(item.statements.debit.items.length != 0) {
                        const withdrawns = item.statements.debit.items.map(e => {
                            return e.withdrawn_amount
                        })

                        item.statements.debit.items.map((e,i) => {
                            this.tally[e.transaction_purpose].total = Math.round(withdrawns.reduce((total,num) => total + num))
                            this.tally[e.transaction_purpose].items.push(e)
                        })
                    }
                    // credit
                    if(item.statements.credit.items.length != 0) {
                        const withdrawns = item.statements.credit.items.map(e => {
                            return e.withdrawn_amount
                        })
                        item.statements.credit.items.map((e,i) => {
                            console.log(this.tally)
                            this.tally[e.transaction_purpose].total =  this.tally[e.transaction_purpose].total + Math.round(withdrawns.reduce((total,num) => total + num))
                            this.tally[e.transaction_purpose].items.push(e)
                        })
                    }
                }
            })
            console.log(this.tally)

            setTimeout(() => {
                this.mbd_ready = true
            },0)
        },
        statements() {
            if(this.selectedMonth == undefined) {
                this.$store.state.categories.map(e => {
                    this.tally[e.value] = {}
                    this.tally[e.value].total = 0
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