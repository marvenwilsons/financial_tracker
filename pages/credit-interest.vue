<template>
    <div>
        <section class="margintop050 pad125 borderRad4 relative" >
            <h4 class="colorwhite" >Credit Interest Report </h4>
            <v-divider color="#677180" ></v-divider>
            <section>
                <Interest />
            </section>
        </section>

    </div>
</template>

<script>
import Interest from '@/components/break-down/interest.vue'
export default {
    components: {
        Interest
    }
}
</script>