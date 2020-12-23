<template>
    <div
        class="pointer margintop050 pad050 widgetsection marginleft050 tallyItem" 
        style="background: #222e42; border: 1px solid #3b485c; width:240px;" >
        <div>
            <span><small>{{item.text}}</small></span>
        </div>
        <div class="flex flexcenter" >
            <!-- <div class="relative borderRad4" style="width:80%; height:10px; background: #515c6e;" >
                <div class="fullheight-percent absolute borderRad4" :style="{background:'orange', width:'90%' }" ></div>
            </div> -->
            <div style="border" class="flex1 flex flexend" >
                <span style="color:yellow;" >
                   <pre>{{ moneyFormater(tally[item.value]) }}</pre>
                </span>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['item', 'tally'],
    data: () => ({
        highestAmount: 0
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
        }
    }
}
</script>

<style>
.tallyItem:hover {
    border: 1px solid orange !important;
}
</style>