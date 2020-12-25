<template>
    <v-expand-transition>
        <section class="pad125 relative" >
        <section style="border: 1px solid #3b485c" class="fullwidth borderRad4 flex flexwrap relative" >
            <!-- modal -->
            <transition name="fade2" >
                <section v-if="modal" class="absolute fullwidth fullheight-percent" style="z-index:1" >
                    <div @click="modal = false" class="flex flexcenter flexcol fullheight-percent pad125 relative" >
                        <div @click.stop="" class="widgetsection borderRad4 pad125" 
                            style="max-height:80%; min-width:80%; max-width:80%; overflow:auto; border: 1px solid #3b485c;" >
                            <slot :modalContext="modalContext" name="modal" ></slot>
                        </div>
                    </div>
                </section>
            </transition>

            <!-- main content -->
            <section >
                <slot :showModal="showModal" name="widgetContent" ></slot>
            </section>
        </section>
    </section>
    </v-expand-transition>
    
</template>

<script>
export default {
    name: 'WidgetContent',
    data: () => ({
        modal: false,
        modalContext: undefined
    }),
    methods: {
        showModal(itemContent) {
            this.modal = !this.modal
            this.modalContext = itemContent
        }
    }
}
</script>

<style >
.fade2-enter-active, .fade2-leave-active {
  transition: opacity 500ms;
}
.fade2-enter, .fade2-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>