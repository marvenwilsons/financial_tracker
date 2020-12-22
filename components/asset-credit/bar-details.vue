<template>
    <transition name="fade">
        <div v-if="barDetails" class="marginleft125 borderRad4 s widgetsection pad050" style="width:350px; overflow:hiden;" >
            <!--  -->
            <section transition="fade-transition" style="border:1px solid #3b495c;" >
                <div class="pad050" style="border:1px solid #3b495c; background:  #3b495c;" >
                    <strong style="color: yellow" >{{barDetails.report.date}}</strong>
                </div>
                <div class="pad050" >
                    {{barDetails.report.msg}}
                </div>
            </section>
            <!--  -->
            <section style="border:1px solid #3b495c;" >
                <div class="pad050" style="border:1px solid #3b495c; background:  #3b495c;" >
                    <span style="color:#afafaf"  >Debit activity</span>
                </div>
                <!-- highestAmountOfTheDay, lowestAmountOfTheDay, initialBalanceOfTheDay, finalBalanceOfTheDay -->
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
                    Credit activity
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
    }),
    methods: {
        moneyFormater(value) {
            var formatter = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',

            // These options are needed to round to whole numbers if that's what you want.
            //minimumFractionDigits: 0, // (this suffices for whole numbers, but will print 2500.10 as $2,500.1)
            //maximumFractionDigits: 0, // (causes 2500.99 to be printed as $2,501)
            });

            return formatter.format(value)
        },
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