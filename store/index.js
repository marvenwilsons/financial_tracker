export const state = () => ({
    statements: undefined,
    statementYears: undefined,
    categories: [
        {text: 'Essential', value: 'essential'},
        {value: 'grocery', text: 'Grocery'},
        {value: 'food-leisure', text: 'Food Leisure'},
        {value: 'transportation', text: 'Transportation'},
        {value: 'investment-self-improvement', text: 'Investment / Self Improvementtation'},
        {value: 'clothing-personal_spending', text: 'Clothing / personal'},
        {value: 'midical', text: 'Midical Speding'},
        {value: 'dept-payment', text: 'Dept-payment'},
        {value: 'entertainment', text: 'Entertainment'},
        {value: 'online-subscription', text: 'Online Subscription'},
        {value: 'occasional-spending', text: 'Occasional Spending'},
        {value: 'bank-tax', text: 'Bank Tax'},
        {value: 'bank-insurance', text: 'Bank insurance'},
        {value: 'life-insurance', text: 'Life Insurerance'},
        {value: 'phone-monthly-fee', text: 'Phone Monthly Fee'},
        {value: 'interest-fee', text: 'Interest Fee'},
        {value: 'monthly-rent', text: 'Monthly Rent'},
        {value: 'monthly-account-fee', text: 'Monthly Account Fee'},
        {value: 'gov-benefits', text: 'Gov Benefits'},
        {value: 'savings', text: 'Savings'},
        {value: 'remitance', text: 'Remitance'},
        {value: 'other', text: 'Other'},
        {value: 'income / deposit / workpay', text: 'Income / deposit / workpay'},
    ],
    incomeCategory: [
        {value: 'gov-benefits', text: 'Gov Benefits'},
        {value: 'income / deposit / workpay', text: 'Income / deposit / workpay'},
    ],
    spendCategory: [
        {text: 'Essential', value: 'essential'},
        {value: 'grocery', text: 'Grocery'},
        {value: 'food-leisure', text: 'Food Leisure'},
        {value: 'transportation', text: 'Transportation'},
        {value: 'investment-self-improvement', text: 'Investment / Self Improvementtation'},
        {value: 'clothing-personal_spending', text: 'Clothing / personal'},
        {value: 'midical', text: 'Midical Speding'},
        {value: 'dept-payment', text: 'Dept-payment'},
        {value: 'entertainment', text: 'Entertainment'},
        {value: 'online-subscription', text: 'Online Subscription'},
        {value: 'occasional-spending', text: 'Occasional Spending'},
        {value: 'bank-tax', text: 'Bank Tax'},
        {value: 'bank-insurance', text: 'Bank insurance'},
        {value: 'life-insurance', text: 'Life Insurerance'},
        {value: 'phone-monthly-fee', text: 'Phone Monthly Fee'},
        {value: 'monthly-rent', text: 'Monthly Rent'},
        {value: 'remitance', text: 'Remitance'},
        {value: 'other', text: 'Other'}
    ]
})

export const mutations = {
    setStatements(state,payload) {
        state.statements = payload
    },
    setStatementYears(state,payload) {
        state.statementYears = payload
    }
}