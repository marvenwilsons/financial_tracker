<template>
    <div class="relative flex fullheight-percent fullwidth" style="overflow-y:auto" >
        <div class="fullwidth absolute flexcol flex fullheight-percent pad125" >
            <small>
                Set Date Coverage
            </small>
            <hr>
            <!-- from -->
            <div style="background: whitesmoke" class="">
                <small><strong>From:</strong></small> <br>
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
                        <option value="">2020</option>
                    </select>
                </small>
                <small>
                    Day:
                    <select style="border:1px solid gray; width:60px;" name="" id="">
                        <option value="">2020</option>
                    </select>
                </small>
            </div>
            <!-- to -->
            <div>
                <small><strong>To:</strong></small> <br>
                <small>
                    Year: 
                    <select style="border:1px solid gray; width:60px;" name="" id="">
                        <option value="">2020</option>
                    </select>
                </small>
                <small>
                    Month:
                    <select style="border:1px solid gray; width:60px;" name="" id="">
                        <option value="">2020</option>
                    </select>
                </small>
                <small>
                    Day:
                    <select style="border:1px solid gray; width:60px;" name="" id="">
                        <option value="">2020</option>
                    </select>
                </small>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data: () => ({
        availableYearCoverage: ['2020','2019'],
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