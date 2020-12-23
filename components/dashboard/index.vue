<template>
    <div>
        <h4 class="colorwhite" >Dashboard</h4>
        <v-divider color="#677180" ></v-divider>
        <section role="asset value vs liability" v-if="rawData.length" class="s flex marginbottom125" >
            <AssetCreditComponent @barClick="barClick" :StatementDataSet="rawData" />
            <BarDetails :barDetails="barDetails" />
        </section>
        <section role="spending break down & Credit Interest Charge" class="flex flexcol" >
            <BreakDown />
            <div class="margin050" ></div>
            <Interest />
            <div class="margin050" ></div>
            <SpendingGrowth />
        </section>
        <!-- sec: total spending list of all transaction for this month, ei: PRESTO: $900 -->
        <!-- sec: get pre authorized transaction days, ei: LIFEINS: Every 30th of the month  -->
        <!-- sec: Consultant, input the desired withdraw to credit or debit, then it will give you the result of the effect into your accounts  -->
    </div>
</template>

<script>
import AssetCreditComponent from './asset-credit'
import BarDetails from '@/components/asset-credit/bar-details'
import BreakDown from '@/components/break-down/monthly-break-down.vue'
import Interest from '@/components/break-down/interest.vue'
import SpendingGrowth from '@/components/break-down/spending-growth-overtime.vue'

export default {
    components: {
        AssetCreditComponent,
        BarDetails,
        BreakDown,
        Interest,
        SpendingGrowth
    },
    data: () => ({
        rawData: [],
        barDetails: undefined
    }),
    async fetch() {
        const d = await this.$axios.get('/money/statement')
        const x = d.data.results.map(e => {
            return {
                ...e,
                balance_amount: parseFloat(e.balance_amount.split('$')[1].replace(',','')),
                date: e.date.split('T')[0].replace('-','/').replace('-','/'),
                withdrawn_amount: parseFloat(e.withdrawn_amount.split('$')[1].replace(',','')),
                deposited_amount: parseFloat(e.deposited_amount.split('$')[1].replace(',','')),
                transaction_purpose: e.transaction_purpose
            }
        })
        this.rawData = x
        // console.log(x[0])
    },
    methods: {
        barClick(bar) {
            this.barDetails = bar
        }
    },
    created() {
        // for(var i = 0; i < 230; i++) {
        //     this.rawData.push({
        //         statement_type: Math.round(Math.random(i) * 100) < 50 ? 'debit' : 'credit',
        //         date,
        //         withdrawn_amount: 100 * Math.round(Math.random(i) * Math.random(i) * 3),
        //         deposited_amount: 0,
        //         balance_amount: Math.random(i) * Math.round(Math.random(i) * Math.ceil(Math.random(i)) * 3),
        //         description: 'Credit Test 3'
        //     })
        // }
    }
}
</script>