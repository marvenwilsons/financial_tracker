<template>
    <div>
        <section class="margintop050 pad125 borderRad4 relative" >
            <h4 class="colorwhite" >Add Statement</h4>
            <v-divider color="#677180" ></v-divider>
            <addStatement />
        </section>
    </div>
</template>

<script>
import addStatement from '@/components/add-statement/index'
export default {
    components: {
        addStatement
    }
}
</script>