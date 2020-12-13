<template>
    <div class="absolute bar-info pad025" >
        <div class="flex flexcol" >
            <div class="fullwidth flex" >
                {{item.date}}  
            </div>
            <div class="fullwidth flex" >
                <strong class="marginright025" >
                    Debit:
                </strong>${{item.balance_amount}} 
            </div>
            <div class="fullwidth flex" >
                <strong class="marginright025" >
                    Credit:
                </strong>${{item.balance_amount}}  
            </div>

        </div>
    </div>
</template>

<script>
export default {
    props: ['item']
}
</script>