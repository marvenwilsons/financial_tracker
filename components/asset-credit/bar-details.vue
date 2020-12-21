<template>
    <div v-if="barDetails" class="marginleft125 borderRad4 s widgetsection pad050" style="width:350px;" >
        <!--  -->
        <section  style="border:1px solid #3b495c;" >
            <div class="pad050" style="border:1px solid #3b495c; background:  #3b495c;" >
                <strong>{{barDetails.report.date}}</strong>
            </div>
            <div class="pad050" >
                {{barDetails.report.msg}}
            </div>
        </section>
        <!--  -->
        <section  style="border:1px solid #3b495c;" >
            <div class="pad050" style="border:1px solid #3b495c; background:  #3b495c;" >
                <strong>Debit activity</strong>
            </div>
            <div class="pad050" >
                {{barDetails.report.msg}}
            </div>
        </section>
    </div>
</template>

<script>
export default {
    props: ['barDetails']
}
</script>