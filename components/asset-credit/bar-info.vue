<template>
    <div class="absolute bar-info" >
        <!-- <div class="flex flexcol" >
            <div class="fullwidth flex" >
                {{item}}  
            </div>
            <div class="fullwidth flex" >
                <strong class="marginright025" >
                    Debit:
                </strong>{{item.statement_type == 'debit' ? moneyFormater(item.balance_amount) : 'N/A'}}
            </div>
            <div class="fullwidth flex" >
                <strong class="marginright025" >
                    Credit:
                </strong>{{item.statement_type == 'credit' ? moneyFormater(item.balance_amount) : 'N/A'}}
            </div>
        </div> -->
    </div>
</template>

<script>
export default {
    props: ['item', 'moneyFormater']
}
</script>