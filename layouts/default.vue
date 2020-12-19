<template>
  <v-app style="background:#515d6e;" >
    <v-main  >
      <v-container class="bg relative margintop125" style="width:1080px;" >
        <section class="pad125 widgetsection absolute fullwidth relative" style="z-index:1; top:25px; left:-0px;" >
          <div style="left:0px; top:-40px;" class="absolute fullwidth flex flexend pad050 nav" >
            Logout
          </div>
          <section class="borderRad4 flex flexcenter spacebetween" >
            <img style="height:40px; width:40px;" src="/favicon.ico" alt="">
          </section>
        </section>
        <div class="margintop125" style="height:30px;" ></div>
        <section style="border-radius:4px;" class="flex relative s margintop125 padbottom125" >
          <div style="min-width:200px; left:-42px; z-index:1; top:70px;" class="pad125 absolute widgetsection borderRad4"  >
            <div to="dashboard" class="pad025 padbottom050 padtop050 nav" >
              <NuxtLink to="/">Dashboard</NuxtLink>
            </div>
            <div class="pad025 padbottom050 padtop050 nav" >
              <NuxtLink to="/add-statement">Add Statements</NuxtLink>
            </div>
            <div  class="pad025 padbottom050 padtop050 nav" >
              <NuxtLink to="/manage-statements">Manage Statements</NuxtLink>
            </div>
            <div  class="pad025 padbottom050 padtop050 nav" >
              <NuxtLink to="/consult-spend">Consult & Spend</NuxtLink>
            </div>
          </div>
          <div class="fullwidth flex flexend borderRad4" >
            <nuxt style="width:900px;" />
          </div>
        </section>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data () {
    return {
    }
  },
  created() {
    setTimeout(() => {
            this.$vuetify.theme.themes.light.primary = '#409eff'
        }, 0);
  }
}
</script>

<style>
.nav {
  color:#ebe8e8;
  border-bottom:1px solid #677180;
  cursor: pointer;
}
.nav:hover {
  color: white;
  transition: 500ms;
}
</style>
