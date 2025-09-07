const pg = require('pg')
const {Pool} = pg

const pool = new Pool({
    user: process.env.DB_USER || "postgres",
    password: process.env.DB_PASSWORD || "postgres",
    host: process.env.DB_HOST || "localhost",
    port: process.env.DB_PORT || 5432,
    database: process.env.DB_NAME || 'money'
})

const query = (text,params) => pool.query(text,params)

module.exports = query
