<template>
  <v-app style="background:#515d6e;" >
    <v-main  >
      <v-container class="bg relative margintop125" style="min-width:1080px;max-width:1080px;" >
        <section class="pad125 widgetsection absolute fullwidth relative" style="z-index:1; top:25px; left:-0px;" >
          <div style="left:0px; top:-40px;" class="absolute fullwidth flex flexend pad050 nav" >
            Logout
          </div>
          <section class="borderRad4 flex flexcenter spacebetween" >
            <div>
              <img style="height:40px; width:40px;" src="/favicon.ico" alt="">
            </div>
            <div>
              <div class="flex" >
                <div class="colorwhite pointer marginright125" >
                  <NuxtLink to="/account-details">Account Details</NuxtLink>
                </div>
                <div class="colorwhite pointer marginright125" >
                  <NuxtLink to="/settings">Settings</NuxtLink>
                </div>
                <div class="colorwhite pointer marginright125" >
                  <NuxtLink to="/login-security">Login & Security</NuxtLink>
                </div>
                <div class="colorwhite pointer " >
                  <NuxtLink to="/privacy-statement">Privacy Statement</NuxtLink>
                </div>
              </div>
            </div>
          </section>
        </section>
        <div class="margintop125" style="height:30px;" ></div>
        <section style="border-radius:4px;" class="flex relative s margintop125 padbottom125" >
          <div style="min-width:200px; left:-42px; z-index:1; top:70px;" class="pad125 absolute widgetsection borderRad4"  >
            <div to="dashboard" class="pad025 padbottom050 padtop050 nav" >
              <NuxtLink @click="active = 'Monthly Report' " to="/">
                <span @click="active = 'Monthly Report' " :class="[active == 'Monthly Report' ? 'active-link' : '']" >
                  Monthly Report
                </span>
              </NuxtLink>
            </div>
            <div class="pad025 padbottom050 padtop050 nav" >
              <NuxtLink  to="/add-statement">
                <span @click="active = 'Add Statements' " :class="[active == 'Add Statements' ? 'active-link' : '']" >
                  Add Statements
                </span>
              </NuxtLink>
            </div>
            <div  class="pad025 padbottom050 padtop050 nav" >
              <NuxtLink to="/manage-statements">
                <span @click="active = 'Manage Statements' " :class="[active == 'Manage Statements' ? 'active-link' : '']" >
                  Manage Statements
                </span>
              </NuxtLink>
            </div>
            <div  class="pad025 padbottom050 padtop050 nav" >
              <NuxtLink to="/consult-spend">
                <span @click="active = 'Consult & Spend' " :class="[active == 'Consult & Spend' ? 'active-link' : '']" >
                  Consult & Spend
                </span>
              </NuxtLink>
            </div>
            <div  class="pad025 padbottom050 padtop050 nav" >
              <NuxtLink to="/credit-interest">
                <span @click="active = 'Credit Interest Report' " :class="[active == 'Credit Interest Report' ? 'active-link' : '']" >
                  Credit Interest Report
                </span>
              </NuxtLink>
            </div>
            <div  class="pad025 padbottom050 padtop050 nav" >
              <NuxtLink to="/spending-growth">
                <span @click="active = 'Spending Growth' " :class="[active == 'Spending Growth' ? 'active-link' : '']" >
                  Spending Growth
                </span>
              </NuxtLink>
            </div>
            <div  class="pad025 padbottom050 padtop050" >
              <NuxtLink to="/my-notes">
                <span @click="active = 'My Notes' " :class="[active == 'My Notes' ? 'active-link' : '']" >
                  My Notes
                </span>
              </NuxtLink>
            </div>
          </div>
          <div class="fullwidth flex flexend borderRad4" >
            <nuxt style="width:900px;" />
          </div>

        </section>
          <div class="pad125 flex flexcenter" style="background: #26344a; color: #afafaf; border-top:1px solid #677080" >
            <span>
              Donque Financial Tracking Limited | Copyright 2020
            </span>
          </div>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    active: undefined
  }),
  methods: {
    onLinkClick() {
      
    }
  },
  created() {
    this.active = 'Monthly Report'
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
.widgetTitle {
  color: #afafaf
}
.active-link {
  color: #ffff00;
}
</style>
