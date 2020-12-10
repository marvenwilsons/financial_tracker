const express = require('express')
const app = express()
const router = express.Router()
const statement = require('./statement')
// postgres setup
const pg = require('pg')
const {Pool} = pg
const pool = new Pool({
    user: "postgres",
    password: "postgres",
    host: "localhost",
    port: 5432,
    database: 'money'
})
const query = (text,params) => pool.query(text,params)

// get all credit statements
router.get('/statement/credit' ,(req,res) => {
    

})
// get all debit staements
router.get('/statement/debit' ,(req,res) => {
    // const insertStatementQuery = statement.getInsertIntoStatementQuery(sampleStatement, 'debit')
    // const x = statement.addStatement(query,insertStatementQuery)
})
// get all 
// get a specific statement
router.get('/statement/:from_to', (req,res) => {
    // from_to is a point on time, ei: August 1 - October 1
    // so you have to use the BETWEEN statement
})
// add a new statement
router.post('/statement', async (req,res) => {
    try{
        console.log('adding statement')
        const { csv, statement_type } = req.body
        const cq = await query("SELECT TO_CHAR(statement.date :: DATE, 'MM-DD-YYYY') AS date FROM statement")
        
        // BETWEEN query: SELECT date FROM statement WHERE date BETWEEN '2020-12-30'::DATE AND '2020-12-30'::DATE
        // 1. Get the submit date start to finsih
        // 2. 

        // console.log(cq.rows)
        // console.log(dateRange.rows)
        const range = []
        const submitedDateRange = statement.parse(csv).map(({date,description,widthdrawn_amount}, index) => {
            if(index == 0) {
                range.push(date.replace('/','-').replace('/','-'))
            }else if(index == statement.parse(csv).length - 1) {
                range.push(date.replace('/','-').replace('/','-'))
            }
            const csvkeys = `${date.replace('/','-').replace('/','-')}${description}$${widthdrawn_amount}`
            return csvkeys
        })

        const dateRange = await query(`SELECT TO_CHAR(statement.date :: DATE, 'MM-DD-YYYY') AS date, description, widthdrawn_amount FROM statement WHERE date BETWEEN '${range[0]}'::DATE AND '${range[1]}'::DATE`)
        console.log(dateRange.rows.length === submitedDateRange.length)
        
        let repeatedItems = 0
        const nonRepeatedItems = []
        for(let i = 0; i < dateRange.rows.length; i++) {
            const {date,description,widthdrawn_amount} = dateRange.rows[i]
            const dbRange = `${date.replace('/','-').replace('/','-')}${description}${widthdrawn_amount == '$0.00' ? '$0' : widthdrawn_amount}`
            if(submitedDateRange.includes(dbRange)) {
                repeatedItems ++
            } else {
                nonRepeatedItems.push(submitedDateRange[i])
            }
        }

        if(repeatedItems == 0) {
            const insertStatementQuery = statement.getInsertIntoStatementQuery(csv,statement_type)
            const rows = await statement.addStatement(query,insertStatementQuery)
            console.log('Adding Statement', rows)
            res.status(200).json({
                status: 200,
                rows
            })
        } else {
            res.status(200).json({
                status: 'failed'
            })
        }
        

        //

    }catch(err) {
        console.log(err)
    }
})

// app.listen(5000,() => {
//     console.log('Node Sever running')
// })

module.exports = {
    handler: router,
    path: '/money'
}
