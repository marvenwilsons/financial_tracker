<template>
  <v-app>
    <v-main>
      <v-container>
        <nuxt />
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
