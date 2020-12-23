<template>
    <div>
        <section class="margintop050 pad125 borderRad4 relative" >
            <h4 class="colorwhite" >Spending Growth Report</h4>
            <v-divider color="#677180" ></v-divider>
            <section>
                <SpendingGrowth />
            </section>
        </section>
    </div>
</template>

<script>
import SpendingGrowth from '@/components/break-down/spending-growth-overtime.vue'

export default {
    components: {
        SpendingGrowth
    }
}
</script>