<template>
    <div style="background:white; color:black;" class="pad125 flex flexcol flexcenter" >
        <div v-if="error" class="backgrounderr fullwidth pad050 marginbottom125 borderRad4" >
            ERROR: {{error}}
        </div>
        <div>
            <div>
                <div class="label" >Date:</div>
                <input v-model="date" class="padleft025" type="text"> <br>
                <span style="color:gray;" >
                    <small>
                        Format MM/DD/YYYY
                    </small>
                </span>
            </div>
            <div class="margintop025 label" >
                <div class="label" > Deposited Amount:</div>
                <input v-model="deposited_amount" type="number" class="padleft025">
            </div>
            <div class="margintop025" >
                <div class="label" >Withdraw Amount:</div>
                <input v-model="withdrawn_amount" type="number" class="padleft025">
            </div>
            <div class="margintop025" >
                <div class="label">Balance Amount:</div>
                <input v-model="balance_amount" type="number" class="padleft025">
            </div>
            <div class="margintop025" >
                <div class="label">Description:</div>
                <input v-model="description" type="text" class="padleft025">
            </div>
            <div class="flex flexend" >
                <button @click="addEntry" class="padleft025 padright025 margintop125" >
                    Add Entry
                </button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['error'],
    data: () => ({
        date: 'MM/DD/YYYY',
        deposited_amount: 0,
        withdrawn_amount: 0,
        balance_amount: 0,
        description: undefined
    }),
    methods: {
        addEntry() {
            this.$emit('insertEntry', {
                deposited_amount: this.deposited_amount,
                date: this.date,
                withdrawn_amount: this.withdrawn_amount,
                balance_amount: this.balance_amount,
                description: this.description
            })
        }
    }
}
</script>

<style scoped>
input {
    border: 1px solid gray;
}
button {
    border: 1px solid gray;
    background: lightgray;
}
</style>