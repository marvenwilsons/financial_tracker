<template>
    <div>
        <h5 class="colorwhite" >Dashboard</h5>
        <hr>
        <section class="s" >
            <AssetCreditComponent :StatementDataSet="rawData" />
        </section>
        <!-- sec: dept vs asset chart -->
        <!-- sec: total spending of all transaction for this month -->
        <!-- sec: get pre authorized transaction days  -->
    </div>
</template>

<script>
import AssetCreditComponent from './asset-credit'
const date =  '2020/05/05'
export default {
    components: {
        AssetCreditComponent
    },
    data: () => ({
        rawData: [
        ]
    }),
    created() {
        for(var i = 0; i < 230; i++) {
            this.rawData.push({
                statement_type: Math.round(Math.random(i) * 100) < 50 ? 'debit' : 'credit',
                date,
                withdrawn_amount: 100 * Math.round(Math.random(i) * Math.random(i) * 3),
                deposited_amount: 0,
                balance_amount: Math.random(i) * Math.round(Math.random(i) * Math.ceil(Math.random(i)) * 3),
                description: 'Credit Test 3'
            })
        }
    }
}
</script>