<template>
    <div class="flex spacebetween pad125" >
        <div>Date 
            <div style="color: #afafaf" v-for="(item,index) in modalContext" :key="`${item.date}-${index}`" ><small>{{item.date}}</small></div>
        </div>
        <div>Account 
            <div style="color: #afafaf" v-for="(item,index) in modalContext" :key="`${item.statement_type}-${index}`" ><small>{{item.statement_type}}</small></div>
        </div>
        <div>Description
            <div style="color: #afafaf" v-for="(item,index) in modalContext" :key="`${item.description}-${index + 3}`" ><small>{{item.description}}</small></div>
        </div>
        <div>Withdrawn Amount
            <div style="color: orange" v-for="(item,index) in modalContext" :key="`${item.description}-${index + 9}`" ><small>{{moneyFormater(item.withdrawn_amount)}}</small></div>
        </div>
    </div>
</template>

<script>
import MyMixin from '@/m'
export default {
    mixins: [MyMixin],
    props: ['modalContext']
}
</script>