<template>
    <transition name="fade">
        <div v-if="barDetails" class="marginleft125 borderRad4 s widgetsection pad050" style="width:350px; overflow:hiden;" >
            <!--  -->
            <section transition="fade-transition" style="border:1px solid #3b495c;" >
                <div class="pad050" style="border:1px solid #3b495c; background:  #3b495c;" >
                    <strong style="color: yellow" >{{barDetails.report.date}}</strong>
                </div>
                <div class="pad050" >
                    {{msg}} 
                    <span style="color:yellow;" >
                        {{moneyFormater(msgValue)}}
                    </span>
                </div>
            </section>
            <!--  -->
            <section style="border:1px solid #3b495c;" >
                <div class="pad050" style="border:1px solid #3b495c; background:  #3b495c;" >
                    <span style="color:#afafaf"  >Debit total of the day</span>
                </div>
                <div v-if="barDetails.statements.debit.inheritFrom && barDetails.report.date != barDetails.statements.debit.inheritFrom" class="flex flexcenter" >
                    <small style="color:yellow;" >
                        Data copied from: {{barDetails.statements.debit.inheritFrom}}
                    </small>
                </div>
                <div class="pad050 flex flexcenter" >
                    <small class="flex1" >Initial Balance</small>
                    <span style="color:yellow ">
                        <pre>{{moneyFormater(barDetails.statements.debit.initialBalanceOfTheDay)}}</pre>
                    </span>
                </div>
                <div class="pad050 flex flexcenter" >
                    <small class="flex1" >Final Balance</small>
                    <span style="color:yellow " >
                         <pre>{{moneyFormater(barDetails.statements.debit.finalBalanceOfTheDay)}}</pre>
                    </span>
                </div>
                <div class="pad050 flex flexcenter" >
                    <small class="flex1" >Amount Subtracted</small> <br>
                    <span style="color:yellow " >
                        <pre>{{moneyFormater(barDetails.statements.debit.totalAmountSubtracted)}}</pre>
                    </span>
                </div>
            </section>
            <section style="border:1px solid #3b495c;" >
                <div class="pad050" style="border:1px solid #3b495c; background:  #3b495c; color: #afafaf" >
                    Credit total of the day
                </div>
                <div v-if="barDetails.statements.credit.inheritFrom && barDetails.report.date != barDetails.statements.credit.inheritFrom" class="flex flexcenter" >
                    <small style="color:yellow;" >
                        Data copied from: {{barDetails.statements.credit.inheritFrom}}
                    </small>
                </div>
                <!-- highestAmountOfTheDay, lowestAmountOfTheDay, initialBalanceOfTheDay, finalBalanceOfTheDay -->
                <div class="pad050 flex" >
                    <small class="flex1" >Initial Dept</small>
                    <span style="color:yellow ">
                        <pre>{{moneyFormater(barDetails.statements.credit.initialDeptBalanceOfTheDay)}}</pre>
                    </span>
                </div>
                <div class="pad050 flex" >
                    <small class="flex1" >Final Dept</small>
                    <span style="color:yellow " >
                         <pre>{{moneyFormater(barDetails.statements.credit.finalDeptBalanceOfTheDay)}}</pre>
                    </span>
                </div>
                <div class="pad050 flex" >
                    <small class="flex1" >Borrowed Amount</small>
                    <span style="color:yellow " >
                        <pre>{{moneyFormater(barDetails.statements.credit.totalBorrowedAmountOfTheDay)}}</pre>
                    </span>
                </div>
            </section>
        </div>
  </transition>
</template>

<script>
export default {
    props: ['barDetails'],
    data: () => ({
        msg: undefined,
        msgValue: undefined
    }),
    methods: {
        moneyFormater(value) {
            if(!isNaN(value)) {
                var formatter = new Intl.NumberFormat('en-US', {
                    style: 'currency',
                    currency: 'USD',
                });
                return formatter.format(value)
            }   
        },
    },
    watch: {
        barDetails() {
            if(this.barDetails) {
                const msg = this.barDetails.report.msg
                this.msg = msg.split('up to')[0]
                this.msgValue = msg.split('up to')[1]
            }
        }
    }
}
</script>

<style >
.fade-enter-active, .fade-leave-active {
  transition: opacity 1s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>