const express = require('express')
const app = express()
// const router = express.Router()
const statement = require('./statement')
const db = require('./db')
const { isReapeated } = require('./statement')

app.use(express.json())
// get all credit statements
app.get('/statement/credit' ,(req,res) => {
    

})
// get all debit staements
app.get('/statement/debit' ,(req,res) => {
    // const insertStatementQuery = statement.getInsertIntoStatementQuery(sampleStatement, 'debit')
    // const x = statement.addStatement(query,insertStatementQuery)
})
// get all 
// get a specific statement
app.get('/statement/:from_to', (req,res) => {
    // from_to is a point on time, ei: August 1 - October 1
    // so you have to use the BETWEEN statement
})
// add a new statement
app.post('/statement', async (req,res) => {
    // const cq = await db("SELECT TO_CHAR(statement.date :: DATE, 'MM-DD-YYYY') AS date FROM statement")
    // BETWEEN query: SELECT date FROM statement WHERE date BETWEEN '2020-12-30'::DATE AND '2020-12-30'::DATE
    const ERRORS = {
        REPEATED_ITEMS: (repeatedItems) => `Cannot insert ${repeatedItems} statement because similar statement found already exist in database`
    }
    try{
        console.log('==> Adding statement')
        const { dataSet, statement_type } = req.body
        const duplicateCheckResult = await statement.isRepeated(dataSet,db)
        
        if(duplicateCheckResult.repeatedItems == 0) {
            console.log('==> Adding Entry')
            console.log('==> Data OK! Adding Statement')
            const insertStatementQuery = statement.convertToInsertToStatement(dataSet,statement_type)
            const rows = await statement.addStatement(db,insertStatementQuery)
            res.status(200).json({
                status: 'success',
                results: rows
            })
        } else {
            console.log('==> Data Not OK!')
            console.log('==> duplicateCheckResult',duplicateCheckResult)

            const nonRepeatedData = dataSet.filter((e,i) => {
                return duplicateCheckResult.repeatedItemsIndex[i] != i && e
            })

            res.status(200).json({
                status: 'failed',
                msg: ERRORS.REPEATED_ITEMS(duplicateCheckResult.repeatedItems),
                nonRepeatedData
            })
        }
    }catch(err) {
        res.status(200).json({
            status: 'failed',
            msg: err
        })
        console.log(err)
    }
})

// app.listen(5000,() => {
//     console.log('Node Sever running')
// })

module.exports = {
    handler: app,
    path: '/money'
}
