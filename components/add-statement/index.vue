<template>
    <div style="min-height:300px;" class="relative" >
        <div v-if="isProcessDone.length == 2" style="z-index:200;" class="widgetsection flex flexcenter flexcol absolute fullwidth fullheight-percent">
            <h5 style="color:white" >REPORT</h5>
            <div class="pad125 marginbottom125 flex flexwrap flexcenter" style="border:1px solid white; width:400px;" >
                <small>
                    {{report}}
                </small>
            </div>
            <div class="flex flexcol" v-if="nonRepeatedData" >
                Below are non repeated data, please copy and try again
                <textarea style="background:white; height:50px; font-size:10px; font-family:monospace;" v-model="nonRepeatedData" id="" cols="40" rows="5"></textarea>
            </div>
            <v-btn class="marginbottom125 margintop125" @click="done" >
                DONE
            </v-btn>
        </div>
        <div class="flex spacebetween" >
            <div class="flex2" >
                <h5 style="color:white; margin:0;" class="flex1" > Add Statement </h5>
                <div v-if="dataSet.length == 0" >
                    Paste a CSV bank statement below, 
                    <a v-if="!addOneEntryMode" @click="addOneEntryMode = true" style="color:yellow;">Insert one entry</a>
                    <a v-if="addOneEntryMode" @click="addOneEntryMode = false" style="color:yellow;">back to bulk mode</a>
                </div>
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
        <div v-if="error" style="background:#c81c01;" class="smth margintop050" >
            <div class="pad050" > <span class="marginright025" >Error:</span> {{error}}</div>
        </div>
        <div v-if="info" class="margintop125 flex spacebetween pad050 borderRad4 flexcenter smth" style="background: #26344a;" >
            <div>
                <span class="marginleft050" >
                    ⚠️ 
                </span>
                <span  style="color:#c2a242" class="marginleft050" >
                    {{info}}
                </span>
            </div>
            <div>
                <v-btn class="marginright050"  @click="info = undefined" small >
                    Ok
                </v-btn>
            </div>
        </div>
        <!-- one entry mode -->
        <singleEntry @insertEntry="insertEntry" v-if="addOneEntryMode" />
        <!-- textarea -->
        <textarea v-if="dataSet.length == 0 && addOneEntryMode == false" v-model="csv" style="background:white; height:200px; font-size:13px; font-family:monospace;" class="fullwidth pad125" />
        <!-- review area -->
        <div v-if="dataSet.length && addOneEntryMode == false" :class="['relative', 'pad125', 'flex', 'flexcol', isReadyToSubmit ? 'isReady' : 'isNotReady','margintop050']" 
            style="height:550px; border:1px solid #40647b;background:#26344a; overflow-x:hidden;" >
            
            <div style="max-height:43px;" class="flex spacebetween">
                <div class="" style="width:30px;"  ># <br> ---- </div>
                <div  class="" style="width:75px;" >Date <br> ------ </div>
                <div class="" style="width:200px;"   >Description <br> <span style="color:#afafaf" >---------------</span> </div>
                <div class="" style="width:75px;" >Withdraw <br> --------------</div>
                <div class="" style="width:75px;"  >Deposit <br> ---------- </div>
                <div class="" style="width:75px;"  >Balance <br> ----------- </div>
                <div style="width:140px" >purpose <span v-if="transaction_purpose.tobeCompleted != 0" style="background:#c81c01;" class="padleft025 padright025" >
                    <small>{{transaction_purpose.tobeCompleted}} left</small></span> <br> ------------------------- 
                </div>
            </div>
            <div :style="{marginTop:'1px', background: problimaticDataIndex.includes(index) ? '#c81c01': ''}" 
                class="flex relative itemHover spacebetween" 
                style="font-size:14px; max-height:23px;" 
                v-for="(item,index) in dataSet" :key="index" 
            >
                <div v-if="isReadyToSubmit" id="luck" class="fullwidth fullheight-percent absolute" style="z-index:100" >
                    <loadingAnimation :dataSetLength="dataSet.length" @loadingComplete="loadingComplete" :index="index" />
                </div>
                <!-- index -->
                <div class="" style="width:30px;">
                    {{index}}
                </div>
                <!-- date -->
                <div class="" style="width:75px;" >
                    <input style="color:#c2a242; width:75px;" @change="inputChange"  :value="item.date" :id="`${index}-date`" type="text">
                </div>
                <!-- desc -->
                <div  style="width:200px;" class="" >
                    <input style="color:#c2a242; width:180px;" @change="inputChange"  :value="item.description" :id="`${index}-description`"  type="text">
                </div>
                <div style="width:75px;" class=" " >
                    <div class="flex flexcenter" >
                        <span style="margin-right:4px; color: #18cacc;" >$</span>
                        <input style="color:#afafaf; width:75px;" @change="inputChange" :id="`${index}-withdrawn_amount`" :value="item.withdrawn_amount" type="text">
                    </div>
                </div>
                <div style="width:75px;" class=" " >
                    <span class="flex" >
                        <span style="margin-right:4px; color: #18cacc;" >$</span>
                        <input :style="{color:item.deposited_amount > 0 ? '#0ff769' : '#afafaf', width:'75px',  textShadow: item.deposited_amount > 0 && `1px 1px #27364c`}"
                        @change="inputChange"  :value="item.deposited_amount" :id="`${index}-deposited_amount`" type="text">
                    </span>
                </div>
                <div style="width:75px;" class=" " >
                    <span class="flex" >
                        <span style="margin-right:4px; color: #18cacc;" >$</span>
                        <input :style="{color:item.balance_amount > 0 ? '#0ff769' : '#afafaf', width:'75px',  textShadow: item.balance_amount > 0 && `1px 1px #27364c`}"
                         @change="inputChange"  :value="item.balance_amount" :id="`${index}-balance_amount`" type="text">
                    </span>
                </div>
                <div :style="{width:'140px', background: dataSet[index].transaction_purpose == 'none' ? '#c81c01' : '' }" >
                    <select :id="`${index}-transaction_purpose`" @change="inputChange" :style="{color:dataSet[index].transaction_purpose == 'none' ? '#afafaf' : 'white' , width:'140px'}">
                        <option value="none" > &nbsp; none</option>
                        <option value="essential">Essential</option>
                        <option value="grocery">Grocery</option>
                        <option value="food-leisure">Food Leisure</option>
                        <option value="transportation">Transportation</option>
                        <option value="investment-self-improvement">Investment / Self Improvement</option>
                        <option value="clothing-personal_spending">Clothing / personal</option>
                        <option value="midical">Midical Speding</option>
                        <option value="dept-payment">Dept-payment</option>
                        <option value="entertainment">Entertainment</option>
                        <option value="online-subscription">Online Subscription</option>
                        <option value="occasional-spending">Occasional Spending</option>
                        <option value="bank-tax">Bank Tax</option>
                        <option value="bank-insurance">Bank insurance</option>
                        <option value="life-insurance">Life Insurerance</option>
                        <option value="phone-monthly-fee">Phone Monthly Fee</option>
                        <option value="interest-fee">Interest Fee</option>
                    </select>
                </div>
            </div>
        </div>
        <div class="flex flexend margintop125" >
            <v-btn small v-if="csv" @click="submit" >
                {{!isReadyToSubmit && transaction_purpose.isComplete == false ? 'Evaluate' : 'Submit'}}
            </v-btn>
        </div>
    </div>
</template>

<script>
import loadingAnimation from './loading-animation'
import singleEntry from './single-entry'
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
        },
        addOneEntryMode: false,
        isProcessDone: [],
        report: undefined,
        nonRepeatedData: undefined,
        info: undefined
    }),
    components: {
        loadingAnimation,
        singleEntry
    },
    methods: {
        done() {
            location.reload()
        },
        insertEntry(payload) {
            const { date, description, deposited_amount, withdrawn_amount, balance_amount } = payload
            const csv = `${date},'${description}',${withdrawn_amount},${deposited_amount},${balance_amount}`
            this.csv = csv
            this.addOneEntryMode = false
            this.submit()
        },
        parse(statement) {
            // const ar = statement.slice(statement.indexOf('\n')).split('\n')
            const ar = statement.slice('\n').split('\n')
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
                        description:  e.split(',')[1].replace(/[!@#$%^&*()_+\-=\[\]{};':"\\|<>\/?]/gim, ""),
                        withdrawn_amount:  e.split(',')[2],
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
                    const {withdrawn_amount, deposited_amount, balance_amount} = e
                    if(isNaN(withdrawn_amount) || isNaN(deposited_amount) || isNaN(balance_amount)) {
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
                console.log('Upload Response:')
                console.log(res)
                if(res.data.status == 'success') {
                    this.isProcessDone.push(true)
                    this.report = `Successfuly added ${res.data.results.length} ${res.data.results.length == 1 ? 'row' : 'rows'} in database`
                    this.csv = undefined
                } else {
                    this.isProcessDone.push(true)
                    this.csv = undefined
                    if(res.data.nonRepeatedData.length > 0) {
                        const to_csv = res.data.nonRepeatedData.map(e => {
                            const { date, description, deposited_amount, withdrawn_amount, balance_amount } = e
                            return `${date},'${description}',${withdrawn_amount},${deposited_amount},${balance_amount} \n`
                        })

                        this.nonRepeatedData = to_csv.join("")
                        this.report = res.data.msg
                    } else {
                        this.csv = undefined
                        this.report = res.data.msg
                    }
                }
            })
        },
        loadingComplete() {
            setTimeout(() => {
                // alert('Upload Complete')
                // location.reload()
                this.isProcessDone.push(true)
                this.dataSet = []
            }, 1000);
            console.log("Upload Completed")
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

                    const csv_to_array = this.csv.split('\n')

                    // remove dubplicates
                    const filtered_csv_array = csv_to_array.filter((item,index) => csv_to_array.indexOf(item) == index)
                    this.dataSet = this.parse(filtered_csv_array.join('\n'))

                    const duplicate_items = csv_to_array.filter((item,index) => csv_to_array.indexOf(item) !== index).length
                    if(duplicate_items > 0) {
                        this.info = `Found and removed ${duplicate_items} duplicate items`
                    }

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