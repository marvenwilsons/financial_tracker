<template>
    <v-expand-transition>
        <section class="pad125 relative" >
        <section style="border: 1px solid #3b485c" class="fullwidth borderRad4 flex flexwrap relative" >
            <!-- modal -->
            <section v-if="modal" class="absolute fullwidth fullheight-percent" style="z-index:1" >
                <div @click="modal = false" class="flex flexcenter flexcol fullheight-percent pad125 relative" >
                    <div @click.stop="" class="widgetsection borderRad4" style="min-height:80%; max-height:80%; min-width:80%; max-width:80%; overflow:auto" >
                        <slot :modalContext="modalContext" name="modal" ></slot>
                    </div>
                </div>
            </section>
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