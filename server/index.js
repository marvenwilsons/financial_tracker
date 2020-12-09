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
router.post('/statement', (req,res) => {
    const { raw, statement_type } = req.body
    const insertStatementQuery = statement.getInsertIntoStatementQuery(raw,statement_type)
    const rows = statement.addStatement(query,insertStatementQuery)
    res.status(200).json({
        status: 200,
        rows
    })
})

// app.listen(5000,() => {
//     console.log('Node Sever running')
// })

module.exports = {
    handler: router,
    path: '/money'
}
