const express = require('express')
const router = express.Router()

// get all financials
router.get('/statement' ,(req,res) => {

})
// get a specific statement
router.get('/statement/:id', (req,res) => {

})
// add a new statement
router.post('/statement', (req,res) => {

})

app.listen(5000,() => {
    console.log('Node Sever running')
})

module.exports = {
    path: '/money'
}
