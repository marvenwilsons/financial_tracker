<template>
  <div class="" >
    <!--  -->
    <section class="borderRad4 pad125 flex flexcenter spacebetween s" >
      <img style="height:40px; width:40px;" src="/favicon.ico" alt="">
      <div>
        <v-btn outlined color="white" @click="view = 'dashboard'" class="marginright125" >
          Dashboard
        </v-btn>
        <v-btn outlined color="white" @click="view = 'add-statement'" >
          Add Statement
        </v-btn>
      </div>
    </section>
    <!--  -->
    <section class="s margintop050 pad125 borderRad4">
      <addStatement v-if="view === 'add-statement'" />
      <dashboard v-if="view === 'dashboard'" />
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
  background: #567a91;
  color: white;
}
.colorwhite{
  color: white !important;
}
</style>