<template>
    <div class="relative flex fullheight-percent fullwidth" style="overflow-y:auto" >
        <div class="fullwidth absolute flexcol flex fullheight-percent pad125" >
            <small>
                <strong>Set Date Coverage</strong>
            </small>
            <v-divider class="margintop050 marginbottom050 fullwidth" ></v-divider>
            <div v-if="error" class="backgrounderr padleft050 flex spacebetween flex flexcenter " >
                <small>
                    {{error}}
                </small>
                <button @click="error = undefined" class="padleft050 padright050" >
                    <small>Ok</small>
                </button>
            </div>
            <!-- from -->
            <div class="margintop050">
                <small><strong>From:</strong></small> <br>
                <small>
                    Year: 
                    <select class="borderRad4 padleft050" style=" width:60px;" name="" id="">
                        <option class="flex flexcenter" v-for="year in availableYearCoverage" :key="year" value="">
                            <div class="pad050" >{{year}}</div>
                        </option>
                    </select>
                </small>
                <small>
                    Month:
                    <select style="border:1px solid gray; width:60px;" name="" id="">
                        <option v-for="month in months" :key="month" value="">
                            {{month}}
                        </option>
                    </select>
                </small>
                <small>
                    Day:
                    <select style="border:1px solid gray; width:60px;" name="" id="">
                        <option value="">Day</option>
                    </select>
                </small>
            </div>
            <!-- to -->
            <div class="marginbottom125 padbottom125 margintop050" >
                <small><strong>To:</strong></small> <br>
                <small>
                    Year: 
                    <select style="border:1px solid gray; width:60px;" name="" id="">
                        <option v-for="year in availableYearCoverage" :key="year" value="">
                            {{year}}
                        </option>
                    </select>
                </small>
                <small>
                    Month:
                    <select style="border:1px solid gray; width:60px;" name="" id="">
                        <option v-for="month in months" :key="month" value="">
                            {{month}}
                        </option>
                    </select>
                </small>
                <small>
                    Day:
                    <select style="border:1px solid gray; width:60px;" name="" id="">
                        <option value="">Day</option>
                    </select>
                </small>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data: () => ({
        error: undefined,
        availableYearCoverage: ['2020','2019','2018'],
        availableMonthCoverage: [],
        availableDayCoverage: [],
        months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    }),
    methods: {
        getData() {
            
        },
    }
}
</script>

<style>
select {
    border:1px solid #afafaf !important;
    border-radius: 4px !important;
    padding-left: 8px;
}
</style>