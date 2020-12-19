<template>
  <div class="" >
    <!--  -->

    <!--  -->
    <section class="margintop050 pad125 borderRad4 relative">
      <div class="" >
        <addStatement v-if="view === 'add-statement'" />
        <dashboard v-if="view === 'dashboard'" />
      </div>
    </section>
  </div>
</template>

<script>
import addStatement from '@/components/add-statement/index'
import dashboard from '@/components/dashboard/index'

export default {
  components: {
    addStatement,
    dashboard
  },
  data:() => ({
    view: 'home'
  }),
  mounted() {
    this.view = 'dashboard'
  }
}
</script>

<style>
.s {
  background: #3b495c;
  color: white;
}
.colorwhite{
  color: white !important;
}
.active {
  background: #ffa33c;
  color: black !important;
  border: 1px solid #ffa33c;
}
.non_active {
  border: 1px solid white;
  color: white !important;
}
.widgetsection {
  background: #26344a;
    -webkit-box-shadow: 0px 0px 22px -6px rgba(0,0,0,0.71);
  -moz-box-shadow: 0px 0px 22px -6px rgba(0,0,0,0.71);
  box-shadow: 0px 0px 22px -6px rgba(0,0,0,0.71);
  border-radius: 4px !important;
}
</style>