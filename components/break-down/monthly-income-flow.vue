<template>
    <Widget style="height:400px;" class="flex1 " >
        <WidgetTitle>
            Monthly Income Flow
        </WidgetTitle>
        <div class="padleft125 padright125 flex">
            <div  class="flex widgetsection" >
                <div 
                    v-for="item in cal" :key="item" @click="selectedMonth = item" 
                    :class="['borderRad4', 'pad025', 'padleft050', 'padright050', 'calItem', selectedMonth == item ? 'active' : '']" 
                    style="border: 1px solid #3b485c;" >{{item}}</div>
            </div>
            <div style="width:250px;" class="flex marginleft125 widgetsection" >
                <!-- available years scaned from statement -->
                <div 
                
                    v-for="year in availableYears" :key="year"
                    :class="['borderRad4', 'pad025', 'padleft050', 'padright050', 'calItem', selectedYear == year ? 'active' : '']" 
                    style="border: 1px solid #3b485c;" >{{year}}</div>
            </div>
        </div>
        <WidgetContent >
            <!-- widget primary content -->
            <template #widgetContent="{showModal}">
                <div style="min-height:300px;" class="relative" >
                    <div v-if="mbd_ready" style="min-height:100px; overflow: auto; " class="flex padbottom050"  >
                        <MBD_ITEM 
                            @itemClick="showModal"
                            v-for="item in $store.state.incomeCategory" 
                            :key="item.value" :item="item" 
                            :tally="tally" ></MBD_ITEM>
                    </div>
                </div>
            </template>
            <!-- widget modal content -->
            <template  #modal="{modalContext}" >
                <!-- <DonqueTable :dataSet="modalContext.items" /> -->
                <div>
                    <div class="padleft125 padtop125">
                        {{selectedMonth}} - {{modalContext.length && modalContext[0].transaction_purpose}}
                    </div>
                    <!-- modal table -->
                    <ModalTable :modalContext="modalContext" />
                </div>
            </template>
        </WidgetContent>

    </Widget>
</template>

<script>
import MBD_ITEM from './mbd-item'
import ModalTable from './modal-table'
import MyMixin from '@/m'
export default {
    mixins:[MyMixin],
    components: {
        MBD_ITEM,
        ModalTable
    },
    data: () => ({
        cal: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        selectedMonth: undefined,
        selectedYear: undefined,
        availableYears: undefined,
        tally: {},
        mbd_ready: false,
    }),
    computed: {
        statements() {
            return this.$store.state.statements
        }
    },
    watch: {
        selectedMonth(month) {
            this.mbd_ready = false
            this.$store.state.categories.map(e => {
                this.tally[e.value] = {}
                this.tally[e.value].total = {
                    debit: 0,
                    credit: 0
                }
                this.tally[e.value].items = []
            })
            
            this.statements.map(item => {
                if(item.report.monthOf == this.selectedMonth && item.report.yearOf == this.selectedYear) {
                    // debit
                    if(item.statements.debit.items.length != 0) {
                        const deposited_amount = item.statements.debit.items.map(e => {
                            return e.deposited_amount
                        })

                        item.statements.debit.items.map((e,i) => {
                            this.tally[e.transaction_purpose].total.debit = Math.round(deposited_amount.reduce((total,num) => total + num))
                            this.tally[e.transaction_purpose].items.push(e)
                        })
                    }
                }
            })

            setTimeout(() => {
                this.mbd_ready = true
            },0)
        },
        statements() {
            if(this.selectedMonth == undefined) {
                this.$store.state.incomeCategory.map(e => {
                    this.tally[e.value] = {}
                    this.tally[e.value].total = {
                        debit: 0,
                        credit: 0
                    }
                    this.tally[e.value].items = []
                })

                setTimeout(() => {
                    this.mbd_ready = true
                    this.selectedMonth = 'Jan'
                    this.availableYears = this.$store.state.statementYears
                    this.selectedYear = this.availableYears[0]
                },0)
            }
        }
    }
}
</script>

<style>
.calItem:hover {
    background: orange;
    color: #333;
    cursor: pointer;
}
.calItem{
    min-width: 40px;
}
</style>