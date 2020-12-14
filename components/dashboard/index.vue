<template>
    <div>
        <h5 class="colorwhite" >Dashboard</h5>
        <hr>
        <section class="s" >
            <AssetCreditComponent :StatementDataSet="rawData" />
        </section>
        <!-- sec1: total spending of all transaction from first statement to latest -->
        <!-- sec2: select statements to analyze -->
        <!-- sec3: dept vs asset chart -->
    </div>
</template>

<script>
import AssetCreditComponent from './asset-credit'
export default {
    components: {
        AssetCreditComponent
    },
    data: () => ({
        rawData: [
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
                date: '05/05/2020',
                withdrawn_amount: 300,
                deposited_amount: 0,
                balance_amount: 2000,
                description: 'Debit Test 1'
            },
            {
                statement_type: 'debit',
                date: '05/05/2020',
                withdrawn_amount: 300,
                deposited_amount: 0,
                balance_amount: 1900,
                description: 'Debit Test 2'
            },
            {
                statement_type: 'debit',
                date: '05/05/2020',
                withdrawn_amount: 300,
                deposited_amount: 0,
                balance_amount: 1800,
                description: 'Debit Test 3'
            }
        ]
    })
}
</script>