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

module.exports = query