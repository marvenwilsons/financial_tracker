<template>
    <div>
        <h5 class="colorwhite" >Dashboard</h5>
        <hr>
        <section v-if="rawData.length" class="s" >
            <AssetCreditComponent :StatementDataSet="rawData" />
        </section>
        <!-- sec: dept vs asset chart -->
        <!-- sec: total spending of all transaction for this month -->
        <!-- sec: get pre authorized transaction days  -->
    </div>
</template>

<script>
import AssetCreditComponent from './asset-credit'
export default {
    components: {
        AssetCreditComponent
    },
    data: () => ({
        rawData: []
    }),
    async fetch() {
        const d = await this.$axios.get('/money/statement')
        const x = d.data.results.map(e => {
            return {
                ...e,
                balance_amount: parseFloat(e.balance_amount.split('$')[1].replace(',','')),
                date: e.date.split('T')[0].replace('-','/').replace('-','/'),
                withdrawn_amount: parseFloat(e.withdrawn_amount.split('$')[1].replace(',','')),
                deposited_amount: parseFloat(e.deposited_amount.split('$')[1].replace(',',''))
            }
        })
        this.rawData = x
        // console.log(x[0])
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