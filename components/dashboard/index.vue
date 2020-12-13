<template>
    <div>
        <h5 class="colorwhite" >Dashboard</h5>
        <hr>
        <section class="s" >
            <assetCredit />
        </section>
        <!-- sec1: total spending of all transaction from first statement to latest -->
        <!-- sec2: select statements to analyze -->
        <!-- sec3: dept vs asset chart -->
    </div>
</template>

<script>
import assetCredit from './asset-credit'
export default {
    components: {
        assetCredit
    }
}
</script>