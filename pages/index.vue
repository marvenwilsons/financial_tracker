<template>
  <div class="" >
    <!--  -->
    <section class="pad125 flex flexend s" >
      <v-btn class="marginright125" >
        Get All Statement
      </v-btn>
      <v-btn @click="view = 'add-statement'" >
        Add New Statement
      </v-btn>
    </section>
    <!--  -->
    <section class="s margintop125 pad125">
      <addStatement v-if="view === 'add-statement'" />
    </section>
  </div>
</template>

<script>
import addStatement from '@/components/add-statement/index'

export default {
  components: {
    addStatement
  },
  data:() => ({
    view: 'home'
  })
}
</script>

<style>
.s {
  background: #567a91;
  color: white;
}
</style>