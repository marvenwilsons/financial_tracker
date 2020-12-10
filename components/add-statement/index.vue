<template>
    <div >
        <div class="flex spacebetween" >
            <div class="flex1" >
                <h5 style="color:white; margin:0;" class="flex1" >Add Statement</h5>
                <div>Paste a CSV bank statement below.</div>
            </div>
            <div class="flex1 flex flexend"  >
                <span class="marginright125" >
                    Statement Type: 
                </span>
                <div>
                    <select v-model="statement_type" style="background:white;" class="padleft125 padright125" >
                        <option selected disabled value="select_statement"> Select Statement</option>
                        <option value="credit"> Credit Statement</option>
                        <option value="debit">Debit Stateement</option>
                    </select>
                </div>
            </div>
        </div>
        <div v-if="error" style="background:white;" class="smth" >
            <div class="pad050 backgrounderr err" > <span class="marginright025" >Error:</span> {{error}}</div>
        </div>
        <textarea v-if="dataSet.length == 0" v-model="csv" style="background:white; height:200px; font-size:11px;" class="fullwidth pad125" />
        <div v-if="dataSet.length" :class="['relative', 'pad125', 'flex', 'flexcol', isReadyToSubmit ? 'isReady' : 'isNotReady']" 
        style="height:550px; border:1px solid #40647b;background:#40647b" >
            
            <div style="max-height:43px;" class="flex">
                <div  style="width:30px;"  ># <br> -- </div>
                <div style="width:95px;" >date <br> ------ </div>
                <div style="width:200px;"   >description <br> --------------- </div>
                <div class="marginright125" >widthdrawn_amount <br> --------------------------- </div>
                <div class="" style="width:160px;"  >deposited_amount <br> ------------------------- </div>
                <div class="flex1" >transaction_purpose <span v-if="transaction_purpose.tobeCompleted != 0" style="background:red;" class="padleft025 padright025" >
                    {{transaction_purpose.tobeCompleted}} left</span> <br> ------------------------- 
                </div>
            </div>
            <div :style="{marginTop:'1px', background: problimaticDataIndex.includes(index) ? 'red': ''}" 
                class="flex relative itemHover" 
                style="font-size:14px; max-height:23px;" 
                v-for="(item,index) in dataSet" :key="index" 
            >
                <div v-if="isReadyToSubmit" id="luck" class="fullwidth fullheight-percent absolute" style="z-index:100" >
                    <loadingAnimation :dataSetLength="dataSet.length" @loadingComplete="loadingComplete" :index="index" />
                </div>
                <div style="width:30px;">
                    {{index}}
                </div>
                <div style="width:100px;" >
                    <input style="color:white; width:90px;" @change="inputChange"  :value="item.date" :id="`${index}-date`" type="text">
                </div>
                <div  style="width:200px;" >
                    <input style="color:white; width:180px;" @change="inputChange"  :value="item.description" :id="`${index}-description`"  type="text">
                </div>
                <div class="marginright125" >
                    <span class="flex flexcenter" >
                        <input style="color:white;" @change="inputChange" :id="`${index}-widthdrawn_amount`" :value="item.widthdrawn_amount" type="text">
                    </span>
                </div>
                <div class="" style="width:160px;" >
                    <span class="flex" >
                        <input style="color:white;" @change="inputChange"  :value="item.deposited_amount" :id="`${index}-deposited_amount`" type="text">
                    </span>
                </div>
                <div :style="{width:'150px', background: dataSet[index].transaction_purpose == 'none' ? 'red' : '' }" >
                    <select :id="`${index}-transaction_purpose`" @change="inputChange" style="color:white;">
                        <option value="none" >none</option>
                        <option value="essential">essential</option>
                        <option value="food-essential">food-essential</option>
                        <option value="food-leisure">food-leisure</option>
                        <option value="Investment">Investment</option>
                        <option value="clothes-personal">clothes-personal</option>
                        <option value="medicine-doctor">medicine-doctor</option>
                        <option value="monthly-responsibility">monthly-responsibility</option>
                        <option value="monthly-deductions">monthly-deductions</option>
                        <option value="dept-payment">dept-payment</option>
                        <option value="entertainment">entertainment</option>
                        <option value="online-subscription">online-subscription</option>
                        <option value="occasional-spending">occasional-spending</option>
                    </select>
                </div>
            </div>
        </div>
        <div class="flex flexend margintop125" >
            <v-btn v-if="csv" @click="submit" >
                {{!isReadyToSubmit && transaction_purpose.isComplete == false ? 'Evaluate' : 'Submit'}}
            </v-btn>
        </div>
    </div>
</template>

<script>
import loadingAnimation from './loading-animation'
export default {
    data: () => ({
        csv: undefined,
        error: undefined,
        statement_type: 'select_statement',
        dataSet: [],
        problimaticDataIndex: [],
        problimaticDataSet: [],
        isReadyToSubmit: false,
        transactionPurposeTobeCompleted: 0,
        transaction_purpose: {
            tobeCompleted: 0,
            isComplete: false,
            error: undefined
        }
    }),
    components: {
        loadingAnimation
    },
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

            try{
                const ar4 = ar3.map(e => {
                    return {
                        date: e.split(',')[0],
                        description:  e.split(',')[1].replace(/[^a-zA-Z ]/g, "") == undefined ?  e.split(',')[1] : e.split(',')[1].replace(/[^a-zA-Z ]/g, ""),
                        widthdrawn_amount:  e.split(',')[2],
                        deposited_amount:  e.split(',')[3],
                        balance_amount:  e.split(',')[4],
                        transaction_purpose: 'none'
                    }
                })
                return ar4
            }catch(err) {
                console.log('err', err)
                alert('INVALID CSV DATA DETECTED, APP IS RELOADING')
                location.reload()
            }
        },
        inputChange(e) {
            const value = e.target.value
            const index = e.target.id.split('-')[0]
            const prop = e.target.id.split('-')[1]
            this.$set(this.dataSet[index], prop, value)

            // remove error from corrected data
            const problimaticData = this.scanProblems(this.dataSet, true)
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
            if(remainingProblem.length == 0) {
                this.error = undefined
            }


            // transaction_purpose to be completed
            if(e.srcElement.localName == 'select') {
                this.transaction_purpose.tobeCompleted = 0
                this.dataSet.map(({transaction_purpose}) => {
                    if(transaction_purpose == 'none') {
                        this.transaction_purpose.tobeCompleted ++
                    }
                })
            }
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
        loadingComplete() {
            alert("Upload Completed")
            location.reload()
        },
        submit() {
            if(!this.csv) {
                this.error = 'Invalid CSV'
            } if(this.statement_type == 'select_statement') {
                this.error = 'Statement type cannot be undefined'
            } else {
                console.log('submitting')
                this.error = undefined
                this.transactionPurposeTobeCompleted = 0
                
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
                    } else {
                        
                        if(this.transaction_purpose.tobeCompleted == 0) {
                            this.isReadyToSubmit = true
                            this.problimaticDataIndex = []
                            this.pushToServer()
                        }
                    }
                } else {
                    this.dataSet = this.parse(this.csv)
                    this.transaction_purpose.tobeCompleted = this.dataSet.length
                    const problimaticData = this.scanProblems(this.csv, false)

                    if(problimaticData.length != 0) {
                        this.error = `Found ${problimaticData.length} Problematic Data`
                        this.problimaticData = problimaticData

                        problimaticData.map(e => {
                            this.problimaticDataIndex.push(e.index)
                        }) 
                    } else {
                        if(this.transaction_purpose.tobeCompleted == 0) {
                            this.isReadyToSubmit = true
                            this.problimaticDataIndex = []
                            this.pushToServer()
                        }
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
.itemHover:hover{
    background: #1f303b;
}
.smth{
    transition: 300ms;
}
</style>