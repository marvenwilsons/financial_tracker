<template>
     <v-expand-transition>
        <div v-if="isOpen" style="z-index:200; top:-10px;" class="absolute fullwidth fullheight-percent flex flexcenter">
            <v-expand-transition>
                <div 
                transition="scroll-y-reverse-transition" 
                style="background:whitesmoke; color:black;max-width:500px; height:300px;" 
                class="borderRad4 flex flexcol" 
                >
                    <div style="background: #afafaf" class="fullwidth flex spacebetween pad025 padleft050" >
                        <small>
                            <strong style="color:#26344a">
                            Settings
                            </strong>
                        </small>
                        <small @click="isOpen = false" class="pointer" >
                            <v-icon small >mdi-close</v-icon>
                        </small>
                    </div> 
                    <div class="pad050 fullheight-percent" >
                        <settings :menu="menu" @onSettingChange="onSettingChange" >
                            <!-- selected is a property of settings.vue passed as a prop and consumed here -->
                            <template v-slot:selected="{ selected }" >
                                 <slot :selected="selected" name="selected" ></slot>
                            </template>
                        </settings>
                    </div>
                    <div style="border-top: 1px solid lightgray;" class="flex flexend pad050 padright050 " >
                        <button class="borderRad4" style="background:#afafaf;" >
                            <small style="color:#26344a" class="padleft025 padright025 borderRad4" >
                                Apply
                            </small>
                        </button>
                    </div>
                </div>
            </v-expand-transition>
        </div>
    </v-expand-transition>
</template>

<script>
export default {
    props: ['openSetting'],
    data: () => ({
        isOpen: false,
        menu: []
    }),
    methods: {
        onSettingChange() {

        },
        toggle(menu) {
            this.menu = menu
            this.isOpen = !this.isOpen
        }
    }
}
</script>