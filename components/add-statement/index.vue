<template>
    <div >
        <div class="flex spacebetween" >
            <h5 style="color:white;" class="flex1" >Add Statement</h5>
            <div class=" flex flexcenter" >
                <span class="marginright125" >
                    Statement Type: 
                </span>
                <select v-model="statement_type" style="background:white;" class="padleft125 padright125" >
                    <option selected disabled value="select_statement"> Select Statement</option>
                    <option value="credit"> Credit Statement</option>
                    <option value="debit">Debit Stateement</option>
                </select>
            </div>
        </div>
        <div v-if="error" style="background:white;" >
            <div class="pad050 backgrounderr err" > <span class="marginright025" >Error:</span> {{error}}</div>
        </div>
        <textarea v-if="dataSet.length == 0" v-model="csv" style="background:white; height:200px; font-size:11px;" class="fullwidth pad125" />
        <div v-if="dataSet.length" :class="['relative', 'pad125', 'flex', 'flexcol', isReadyToSubmit ? 'isReady' : 'isNotReady']" style="height:500px; border:1px solid #40647b;background:#40647b" >
            
            <div class="flex">
                <div  style="width:30px;"  ># <br> -- </div>
                <div style="width:95px;" >date <br> ------ </div>
                <div class="flex1" >description <br> --------------- </div>
                <div class="flex1" >widthdrawn_amount <br> --------------------------- </div>
                <div class="flex1" >deposited_amount <br> ------------------------- </div>
            </div>
            <div :style="{background: problimaticDataIndex.includes(index) ? 'red': ''}" class="flex relative" style="font-size:14px;" v-for="(item,index) in dataSet" :key="index" >
                <div v-if="isReadyToSubmit" id="luck" class="fullwidth fullheight-percent absolute" style="z-index:100" ></div>
                <div style="width:30px;">
                    {{index}}
                </div>
                <div style="width:95px;" >
                    <input style="color:white; width:90px;" @change="inputChange"  :value="item.date" :id="`${index}-date`" type="text">
                </div>
                <div  class="flex1" >
                    <input style="color:white;" @change="inputChange"  :value="item.description" :id="`${index}-description`"  type="text">
                </div>
                <div class="flex1" >
                    <span class="flex flexcenter" >
                        <input style="color:white;" @change="inputChange" :id="`${index}-widthdrawn_amount`" :value="item.widthdrawn_amount" type="text">
                    </span>
                </div>
                <div class="flex1" >
                    <span class="flex flexcenter" >
                        <input style="color:white;" @change="inputChange"  :value="item.deposited_amount" :id="`${index}-deposited_amount`" type="text">
                    </span>
                </div>
            </div>
        </div>
        <div class="flex flexend margintop125" >
            <v-btn v-if="csv" @click="submit" >
                {{!isReadyToSubmit ? 'Evaluate' : 'Submit'}}
            </v-btn>
        </div>
    </div>
</template>

<script>
export default {
    data: () => ({
        csv: undefined,
        error: undefined,
        statement_type: 'select_statement',
        dataSet: [],
        problimaticDataIndex: [],
        isReadyToSubmit: false
    }),
    methods: {
        parse(statement) {
            const ar = statement.slice(statement.indexOf('\n') + 1).split('\n')
            const ar2 = ar.map(e => {
                
                if(e){
                    let r = undefined
                    if(e.includes(',,')) {
                        r = e.replace(',,',',0,')
                    } else {
                        r = e
                    }
                    return r
                }

            })
            const ar3 = ar2.filter(e => e && e)

            const ar4 = ar3.map(e => {
                return {
                    date: e.split(',')[0],
                    description:  e.split(',')[1].replace(/[^a-zA-Z ]/g, ""),
                    widthdrawn_amount:  e.split(',')[2],
                    deposited_amount:  e.split(',')[3],
                    balance_amount:  e.split(',')[4],
                }
            })
            return ar4
        },
        inputChange(e) {
            const value = e.target.value
            const index = e.target.id.split('-')[0]
            const prop = e.target.id.split('-')[1]
            this.$set(this.dataSet[index], prop, value)
        },
        scanProblems(dSet,allowParse) {
            const sc = (a) => {
                return a.map((e,i) => {
                    const {widthdrawn_amount, deposited_amount, balance_amount} = e
                    if(isNaN(widthdrawn_amount) || isNaN(deposited_amount) || isNaN(balance_amount)) {
                        return {
                            problem: true,
                            data: e,
                            index: i
                        }
                    }
                }).filter(e => e)
            }

            if(!allowParse) {
                return sc(this.parse(dSet))
            } else {
                return sc(dSet)
            }
             
        },
        pushToServer() {
            this.$axios.post('/money/statement', {
                dataSet: this.dataSet,
                statement_type: this.statement_type
            }).then(res => {
                console.log(res)
            })
        },
        submit() {
            if(!this.csv) {
                this.error = 'Invalid CSV'
            } if(this.statement_type == 'select_statement') {
                this.error = 'Statement type cannot be undefined'
            } else {
                console.log('submitting')
                this.error = undefined
                
                if(this.dataSet.length != 0) {
                    const problimaticData = this.scanProblems(this.dataSet, true)

                    if(problimaticData.length != 0) {
                        this.error = `Found ${problimaticData.length} Problematic Data`
                        this.problimaticData = problimaticData

                        const remainingProblem = problimaticData.map(e => {
                            console.log(e.index)
                            if(!this.problimaticDataIndex.includes(e.index)) {
                                this.problimaticDataIndex.push(e.index)
                            }

                            return e.index
                        })

                        
                        this.problimaticDataIndex = remainingProblem
                        console.log('remainingProblem', remainingProblem)
                    } else {
                        this.isReadyToSubmit = true
                        this.problimaticDataIndex = []
                        this.pushToServer()
                    }
                } else {
                    this.dataSet = this.parse(this.csv)
                    const problimaticData = this.scanProblems(this.csv, false)

                    if(problimaticData.length != 0) {
                        this.error = `Found ${problimaticData.length} Problematic Data`
                        this.problimaticData = problimaticData
                        problimaticData.map(e => {
                            this.problimaticDataIndex.push(e.index)
                        }) 
                    } else {
                        this.isReadyToSubmit = true
                        this.problimaticDataIndex = []
                        this.pushToServer()
                    }
                }
            }
        }
    }
}
</script>

<style>
.isReady {
    overflow: hidden;
}
#luck {
    background-color: rgba(128, 128, 128, 0.219);
}
.isNotReady {
    overflow-y:scroll
}
</style>