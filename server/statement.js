async function addStatement(pgQuery, query) {
    const res = await pgQuery(query)
    return res.rows
}

function parse (statement) {
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

    const ar4 = ar3.map(e => {
        return {
            date: e.split(',')[0],
            description:  e.split(',')[1].replace("'",""),
            widthdrawn_amount:  e.split(',')[2],
            deposited_amount:  e.split(',')[3],
            balance_amount:  e.split(',')[4],
        }
    })
    return ar4
}

function convertToInsertToStatement (parsedStatement, statement_type) {
    let base =`INSERT INTO statement (date, description, withdrawn_amount, deposited_amount, statement_type, transaction_purpose, balance_amount) VALUES \n`
    parsedStatement.map((e,i) => {
        const d = `to_date('${e.date.replace("/","-").replace("/","-")}','MM-DD-YYYY')`
        const st = `${statement_type == 'credit' ? 'credit' : 'deposit'}`
        base = base.concat( `(${d}, '${e.description}', ${e.withdrawn_amount}, ${e.deposited_amount}, '${st}', '${e.transaction_purpose}', ${e.balance_amount})${i == parsedStatement.length - 1? ' returning *' : ','} \n` )
    })
    return base.trim()
}

function getInsertIntoStatementQuery (raw, type) {
    return convertToInsertToStatement(parse(raw), type)
}

module.exports = {
    addStatement,
    getInsertIntoStatementQuery,
    parse,
    convertToInsertToStatement
}