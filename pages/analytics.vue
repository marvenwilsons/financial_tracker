<template>
  <div class="charts-container">
    <v-container fluid>
      <v-row>
        <v-col cols="12">
          <h1 class="display-1 mb-4">📊 Financial Analytics Dashboard</h1>

          <!-- Year Filter -->
          <v-card class="mb-4">
            <v-card-text>
              <v-row>
                <v-col cols="12" md="4">
                  <v-select
                    v-model="selectedYear"
                    :items="availableYears"
                    label="Filter by Year"
                    prepend-icon="mdi-calendar"
                    @change="createCharts"
                  ></v-select>
                </v-col>
                <v-col cols="12" md="4">
                  <v-select
                    v-model="selectedDataSource"
                    :items="[
                      { text: 'Credit Card', value: 'credit' },
                      { text: 'Chequing Account', value: 'chequing' },
                      { text: 'Combined View', value: 'combined' }
                    ]"
                    label="Data Source"
                    prepend-icon="mdi-credit-card"
                    @change="createCharts"
                  ></v-select>
                </v-col>
                <v-col cols="12" md="4">
                  <v-card outlined class="pa-3">
                    <div class="text-caption">Showing: <strong>{{ getDataSourceLabel() }}</strong></div>
                    <div class="text-caption">Year: <strong>{{ selectedYear === 'all' ? 'All Years' : selectedYear }}</strong></div>
                    <div class="text-caption">Records: <strong>{{ filteredStatements.length }}</strong></div>
                  </v-card>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <!-- Summary Cards Row -->
      <v-row class="mb-6">
        <v-col cols="12" md="3">
          <v-card class="pa-4 text-center" color="success" dark>
            <v-card-title class="justify-center">
              <v-icon large class="mr-2">mdi-cash-plus</v-icon>
              Total Deposits
            </v-card-title>
            <v-card-text>
              <div class="display-1">${{ totalDeposits.toLocaleString() }}</div>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="3">
          <v-card class="pa-4 text-center" color="error" dark>
            <v-card-title class="justify-center">
              <v-icon large class="mr-2">mdi-cash-minus</v-icon>
              Total Withdrawals
            </v-card-title>
            <v-card-text>
              <div class="display-1">${{ totalWithdrawals.toLocaleString() }}</div>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="3">
          <v-card class="pa-4 text-center" color="info" dark>
            <v-card-title class="justify-center">
              <v-icon large class="mr-2">mdi-calculator</v-icon>
              Net Balance
            </v-card-title>
            <v-card-text>
              <div class="display-1">${{ netBalance.toLocaleString() }}</div>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="3">
          <v-card class="pa-4 text-center" color="primary" dark>
            <v-card-title class="justify-center">
              <v-icon large class="mr-2">mdi-receipt</v-icon>
              Total Transactions
            </v-card-title>
            <v-card-text>
              <div class="display-1">{{ totalTransactions }}</div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <!-- Charts Row 1 -->
      <v-row class="mb-6">
        <v-col cols="12" md="6">
          <v-card class="pa-4">
            <v-card-title>
              <v-icon class="mr-2">mdi-chart-line</v-icon>
              Balance Over Time
            </v-card-title>
            <v-card-text>
              <canvas ref="balanceChart" width="400" height="200" style="max-width: 100%;"></canvas>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="6">
          <v-card class="pa-4">
            <v-card-title>
              <v-icon class="mr-2">mdi-scale-balance</v-icon>
              Net Cash Flow (Deposits vs Spending)
            </v-card-title>
            <v-card-subtitle>
              Negative = Credit spending exceeds chequing deposits
            </v-card-subtitle>
            <v-card-text>
              <canvas ref="netFlowChart" width="400" height="200" style="max-width: 100%;"></canvas>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <!-- Charts Row 2 -->
      <v-row class="mb-6">
        <v-col cols="12" md="6">
          <v-card class="pa-4">
            <v-card-title>
              <v-icon class="mr-2">mdi-chart-pie</v-icon>
              Transaction Types
            </v-card-title>
            <v-card-text>
              <canvas ref="typeChart" width="400" height="200" style="max-width: 100%;"></canvas>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="6">
          <v-card class="pa-4">
            <v-card-title>
              <v-icon class="mr-2">mdi-chart-bar</v-icon>
              Monthly Spending Trends
            </v-card-title>
            <v-card-text>
              <canvas ref="monthlyChart" width="400" height="200" style="max-width: 100%;"></canvas>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <!-- Charts Row 3 -->
      <v-row class="mb-6">
        <v-col cols="12" md="6">
          <v-card class="pa-4">
            <v-card-title>
              <v-icon class="mr-2">mdi-format-list-bulleted</v-icon>
              Top Spending Categories
            </v-card-title>
            <v-card-text>
              <div v-for="(category, index) in topCategories" :key="index" class="mb-3">
                <div class="d-flex justify-space-between align-center mb-1">
                  <span class="font-weight-medium">{{ category.name }}</span>
                  <span class="font-weight-bold">${{ category.amount.toLocaleString() }}</span>
                </div>
                <v-progress-linear
                  :value="(category.amount / (topCategories[0]?.amount || 1)) * 100"
                  :color="categoryColors[index % categoryColors.length]"
                  height="10"
                  rounded
                ></v-progress-linear>
              </div>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="6">
          <v-card class="pa-4">
            <v-card-title>
              <v-icon class="mr-2">mdi-chart-timeline-variant</v-icon>
              Yearly Summary
            </v-card-title>
            <v-card-text>
              <div v-for="year in yearlySummary" :key="year.year" class="mb-3">
                <div class="d-flex justify-space-between align-center mb-1">
                  <span class="font-weight-medium">{{ year.year }}</span>
                  <span :class="year.netFlow >= 0 ? 'green--text' : 'red--text'" class="font-weight-bold">
                    {{ year.netFlow >= 0 ? '+' : '' }}${{ year.netFlow.toLocaleString() }}
                  </span>
                </div>
                <div class="caption text--secondary">
                  Deposits: ${{ year.deposits.toLocaleString() }} |
                  Spending: ${{ year.spending.toLocaleString() }}
                </div>
              </div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <!-- Recent Transactions Table -->
      <v-row>
        <v-col cols="12">
          <v-card>
            <v-card-title>
              <v-icon class="mr-2">mdi-format-list-bulleted</v-icon>
              Recent Transactions
              <v-spacer></v-spacer>
              <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Search transactions"
                single-line
                hide-details
              ></v-text-field>
            </v-card-title>
            <v-data-table
              :headers="headers"
              :items="recentTransactions"
              :search="search"
              :items-per-page="10"
              class="elevation-1"
            >
              <template v-slot:[`item.date`]="{ item }">
                {{ formatDate(item.date) }}
              </template>
              <template v-slot:[`item.statement_type`]="{ item }">
                <v-chip
                  :color="item.statement_type === 'deposit' ? 'success' : 'error'"
                  text-color="white"
                  small
                >
                  {{ item.statement_type }}
                </v-chip>
              </template>
              <template v-slot:[`item.withdrawn_amount`]="{ item }">
                <span :class="item.withdrawn_amount > 0 ? 'red--text' : ''">
                  {{ item.withdrawn_amount }}
                </span>
              </template>
              <template v-slot:[`item.deposited_amount`]="{ item }">
                <span :class="item.deposited_amount > 0 ? 'green--text' : ''">
                  {{ item.deposited_amount }}
                </span>
              </template>
            </v-data-table>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'AnalyticsPage',
  data() {
    return {
      statements: [],
      chequingStatements: [],
      selectedYear: 'all',
      selectedDataSource: 'credit',
      search: '',
      categoryColors: ['error', 'success', 'primary', 'warning', 'info', 'purple'],
      headers: [
        { text: 'Date', value: 'date', sortable: true },
        { text: 'Description', value: 'description', sortable: false },
        { text: 'Type', value: 'statement_type', sortable: true },
        { text: 'Withdrawn', value: 'withdrawn_amount', sortable: true },
        { text: 'Deposited', value: 'deposited_amount', sortable: true },
        { text: 'Balance', value: 'balance_amount', sortable: true }
      ]
    }
  },
  computed: {
    availableYears() {
      const allStatements = [...this.statements, ...this.chequingStatements]
      const years = [...new Set(allStatements.map(s => new Date(s.date).getFullYear()))]
        .sort((a, b) => b - a) // Sort descending (newest first)
      return [
        { text: 'All Years', value: 'all' },
        ...years.map(year => ({ text: year.toString(), value: year.toString() }))
      ]
    },
    currentStatements() {
      if (this.selectedDataSource === 'credit') return this.statements
      if (this.selectedDataSource === 'chequing') return this.chequingStatements
      return [...this.statements, ...this.chequingStatements] // combined
    },
    filteredStatements() {
      if (this.selectedYear === 'all') {
        return this.currentStatements
      }
      return this.currentStatements.filter(s => {
        const year = new Date(s.date).getFullYear().toString()
        return year === this.selectedYear
      })
    },
    totalDeposits() {
      return this.filteredStatements
        .filter(s => s.statement_type === 'deposit')
        .reduce((sum, s) => sum + this.parseAmount(s.deposited_amount), 0)
    },
    totalWithdrawals() {
      return this.filteredStatements
        .filter(s => s.statement_type === 'withdrawal')
        .reduce((sum, s) => sum + this.parseAmount(s.withdrawn_amount), 0)
    },
    netBalance() {
      return this.totalDeposits - this.totalWithdrawals
    },
    totalTransactions() {
      return this.filteredStatements.length
    },
    recentTransactions() {
      return this.filteredStatements
        .sort((a, b) => new Date(b.date) - new Date(a.date))
        .slice(0, 100) // Show more recent transactions
    },
    monthlyData() {
      const monthly = {}
      this.filteredStatements.forEach(statement => {
        const date = new Date(statement.date)
        const monthKey = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}`

        if (!monthly[monthKey]) {
          monthly[monthKey] = { deposits: 0, withdrawals: 0 }
        }

        if (statement.statement_type === 'deposit') {
          monthly[monthKey].deposits += this.parseAmount(statement.deposited_amount)
        } else {
          monthly[monthKey].withdrawals += this.parseAmount(statement.withdrawn_amount)
        }
      })

      return Object.keys(monthly)
        .sort()
        .map(month => ({
          month,
          ...monthly[month]
        }))
    },
    categoryData() {
      const categories = {}
      this.filteredStatements
        .filter(s => s.statement_type === 'withdrawal')
        .forEach(statement => {
          const description = statement.description.toLowerCase()
          let category = 'Other'

          if (description.includes('mcdonalds') || description.includes('tim hortons') ||
              description.includes('subway') || description.includes('restaurant') ||
              description.includes('jollibee') || description.includes('kfc')) {
            category = 'Food & Dining'
          } else if (description.includes('presto') || description.includes('uber')) {
            category = 'Transportation'
          } else if (description.includes('amazon') || description.includes('walmart') ||
                     description.includes('shoppers') || description.includes('mall')) {
            category = 'Shopping'
          } else if (description.includes('heroku') || description.includes('netflix') ||
                     description.includes('spotify') || description.includes('microsoft')) {
            category = 'Subscriptions'
          } else if (description.includes('insurance') || description.includes('phone') ||
                     description.includes('telus')) {
            category = 'Bills & Utilities'
          }

          if (!categories[category]) {
            categories[category] = 0
          }
          categories[category] += this.parseAmount(statement.withdrawn_amount)
        })

      return Object.entries(categories)
        .map(([name, amount]) => ({ name, amount }))
        .sort((a, b) => b.amount - a.amount)
    },
    topCategories() {
      return this.categoryData.slice(0, 6)
    },
    netFlowData() {
      // Calculate monthly net flow: chequing deposits - credit spending
      const monthlyFlow = {}

      // Get chequing deposits by month
      this.chequingStatements.forEach(statement => {
        const date = new Date(statement.date)
        const monthKey = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}`

        if (!monthlyFlow[monthKey]) {
          monthlyFlow[monthKey] = { deposits: 0, spending: 0, netFlow: 0 }
        }

        if (statement.statement_type === 'deposit') {
          monthlyFlow[monthKey].deposits += this.parseAmount(statement.deposited_amount)
        }
      })

      // Subtract credit spending by month
      this.statements.forEach(statement => {
        const date = new Date(statement.date)
        const monthKey = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}`

        if (!monthlyFlow[monthKey]) {
          monthlyFlow[monthKey] = { deposits: 0, spending: 0, netFlow: 0 }
        }

        if (statement.statement_type === 'withdrawal') {
          monthlyFlow[monthKey].spending += this.parseAmount(statement.withdrawn_amount)
        }
      })

      // Calculate net flow for each month
      Object.keys(monthlyFlow).forEach(month => {
        monthlyFlow[month].netFlow = monthlyFlow[month].deposits - monthlyFlow[month].spending
      })

      return Object.keys(monthlyFlow)
        .sort()
        .map(month => ({
          month,
          ...monthlyFlow[month]
        }))
    },
    yearlySummary() {
      const yearlyData = {}

      // Process chequing deposits
      this.chequingStatements.forEach(statement => {
        const year = new Date(statement.date).getFullYear()
        if (!yearlyData[year]) {
          yearlyData[year] = { deposits: 0, spending: 0, netFlow: 0 }
        }

        if (statement.statement_type === 'deposit') {
          yearlyData[year].deposits += this.parseAmount(statement.deposited_amount)
        }
      })

      // Process credit spending
      this.statements.forEach(statement => {
        const year = new Date(statement.date).getFullYear()
        if (!yearlyData[year]) {
          yearlyData[year] = { deposits: 0, spending: 0, netFlow: 0 }
        }

        if (statement.statement_type === 'withdrawal') {
          yearlyData[year].spending += this.parseAmount(statement.withdrawn_amount)
        }
      })

      // Calculate net flow and format
      return Object.keys(yearlyData)
        .sort((a, b) => b - a) // Sort descending
        .map(year => ({
          year: parseInt(year),
          ...yearlyData[year],
          netFlow: yearlyData[year].deposits - yearlyData[year].spending
        }))
        .slice(0, 8) // Show last 8 years
    }
  },
  async mounted() {
    await this.fetchStatements()
    await this.fetchChequingStatements()
    this.$nextTick(() => {
      this.createCharts()
    })
  },
  methods: {
    async fetchStatements() {
      try {
        const response = await this.$axios.get('/money/statement')
        if (response.data.status === 'success') {
          this.statements = response.data.results
        }
      } catch (error) {
        console.error('Error fetching statements:', error)
        alert('Failed to load credit card data')
      }
    },
    async fetchChequingStatements() {
      try {
        const response = await this.$axios.get('/money/chequing-statements')
        if (response.data.status === 'success') {
          this.chequingStatements = response.data.results
        }
      } catch (error) {
        console.error('Error fetching chequing statements:', error)
        // Don't show alert for chequing data as it might not be available
        console.log('Chequing data not available')
      }
    },
    getDataSourceLabel() {
      const labels = {
        'credit': 'Credit Card Data',
        'chequing': 'Chequing Account Data',
        'combined': 'Credit + Chequing Combined'
      }
      return labels[this.selectedDataSource] || 'Unknown'
    },
    parseAmount(amount) {
      if (typeof amount === 'string') {
        return parseFloat(amount.replace(/[$,]/g, '')) || 0
      }
      return parseFloat(amount) || 0
    },
    formatDate(date) {
      return new Date(date).toLocaleDateString()
    },
    createCharts() {
      this.createBalanceChart()
      this.createNetFlowChart()
      this.createTypeChart()
      this.createMonthlyChart()
    },
    createBalanceChart() {
      const canvas = this.$refs.balanceChart
      if (!canvas) return

      const ctx = canvas.getContext('2d')
      const sortedStatements = [...this.filteredStatements].sort((a, b) => new Date(a.date) - new Date(b.date))

      // Show all data but sample it if there are too many points for chart readability
      const maxPoints = 100
      const step = Math.max(1, Math.floor(sortedStatements.length / maxPoints))
      const sampledData = []
      const sampledLabels = []

      for (let i = 0; i < sortedStatements.length; i += step) {
        sampledData.push(this.parseAmount(sortedStatements[i].balance_amount))
        sampledLabels.push(this.formatDate(sortedStatements[i].date))
      }

      this.drawLineChart(ctx, canvas, sampledData, sampledLabels, 'Balance Over Time')
    },
    createNetFlowChart() {
      const canvas = this.$refs.netFlowChart
      if (!canvas) return

      const ctx = canvas.getContext('2d')
      const data = this.netFlowData

      // Filter data if year is selected
      let filteredData = data
      if (this.selectedYear !== 'all') {
        filteredData = data.filter(d => d.month.startsWith(this.selectedYear))
      }

      this.drawNetFlowChart(ctx, canvas, filteredData)
    },
    createTypeChart() {
      const canvas = this.$refs.typeChart
      if (!canvas) return

      const ctx = canvas.getContext('2d')
      const deposits = this.filteredStatements.filter(s => s.statement_type === 'deposit').length
      const withdrawals = this.filteredStatements.filter(s => s.statement_type === 'withdrawal').length

      this.drawPieChart(ctx, canvas, [
        { label: 'Deposits', value: deposits, color: '#4CAF50' },
        { label: 'Withdrawals', value: withdrawals, color: '#FF5722' }
      ])
    },
    createMonthlyChart() {
      const canvas = this.$refs.monthlyChart
      if (!canvas) return

      const ctx = canvas.getContext('2d')
      // Show all monthly data instead of limiting to last 12 months
      const data = this.monthlyData

      this.drawBarChart(ctx, canvas, data.map(d => [d.deposits, d.withdrawals]), data.map(d => d.month))
    },
    drawLineChart(ctx, canvas, data, labels, title) {
      const padding = 40
      const width = canvas.width - 2 * padding
      const height = canvas.height - 2 * padding

      ctx.clearRect(0, 0, canvas.width, canvas.height)

      if (data.length === 0) return

      // Find min/max for scaling
      const min = Math.min(...data)
      const max = Math.max(...data)
      const range = max - min || 1

      // Draw axes
      ctx.strokeStyle = '#666'
      ctx.lineWidth = 1
      ctx.beginPath()
      ctx.moveTo(padding, padding)
      ctx.lineTo(padding, canvas.height - padding)
      ctx.lineTo(canvas.width - padding, canvas.height - padding)
      ctx.stroke()

      // Draw line
      ctx.strokeStyle = '#2196F3'
      ctx.lineWidth = 3
      ctx.beginPath()

      data.forEach((value, index) => {
        const x = padding + (index / (data.length - 1)) * width
        const y = canvas.height - padding - ((value - min) / range) * height

        if (index === 0) {
          ctx.moveTo(x, y)
        } else {
          ctx.lineTo(x, y)
        }
      })

      ctx.stroke()

      // Draw points
      ctx.fillStyle = '#2196F3'
      data.forEach((value, index) => {
        const x = padding + (index / (data.length - 1)) * width
        const y = canvas.height - padding - ((value - min) / range) * height

        ctx.beginPath()
        ctx.arc(x, y, 4, 0, 2 * Math.PI)
        ctx.fill()
      })
    },
    drawPieChart(ctx, canvas, data) {
      ctx.clearRect(0, 0, canvas.width, canvas.height)

      const centerX = canvas.width / 2
      const centerY = canvas.height / 2
      const radius = Math.min(centerX, centerY) - 30

      const total = data.reduce((sum, item) => sum + item.value, 0)

      let currentAngle = -Math.PI / 2

      data.forEach(item => {
        const sliceAngle = (item.value / total) * 2 * Math.PI

        ctx.fillStyle = item.color
        ctx.beginPath()
        ctx.moveTo(centerX, centerY)
        ctx.arc(centerX, centerY, radius, currentAngle, currentAngle + sliceAngle)
        ctx.closePath()
        ctx.fill()

        // Draw label
        const labelAngle = currentAngle + sliceAngle / 2
        const labelX = centerX + Math.cos(labelAngle) * (radius + 25)
        const labelY = centerY + Math.sin(labelAngle) * (radius + 25)

        ctx.fillStyle = '#000'
        ctx.font = '12px Arial'
        ctx.textAlign = 'center'
        ctx.fillText(item.label, labelX, labelY)
        ctx.fillText(item.value, labelX, labelY + 15)

        currentAngle += sliceAngle
      })
    },
    drawBarChart(ctx, canvas, data, labels) {
      ctx.clearRect(0, 0, canvas.width, canvas.height)

      const padding = 40
      const width = canvas.width - 2 * padding
      const height = canvas.height - 2 * padding

      if (data.length === 0) return

      const maxValue = Math.max(...data.flat())
      const barWidth = Math.max(2, (width / data.length) * 0.8) // Minimum width of 2px
      const barSpacing = (width / data.length) * 0.2

      // Draw axes
      ctx.strokeStyle = '#666'
      ctx.lineWidth = 1
      ctx.beginPath()
      ctx.moveTo(padding, padding)
      ctx.lineTo(padding, canvas.height - padding)
      ctx.lineTo(canvas.width - padding, canvas.height - padding)
      ctx.stroke()

      data.forEach((values, index) => {
        const x = padding + index * (width / data.length) + barSpacing / 2

        // Draw deposits bar
        const depositHeight = (values[0] / maxValue) * height
        ctx.fillStyle = '#4CAF50'
        ctx.fillRect(x, canvas.height - padding - depositHeight, barWidth / 2, depositHeight)

        // Draw withdrawals bar
        const withdrawalHeight = (values[1] / maxValue) * height
        ctx.fillStyle = '#FF5722'
        ctx.fillRect(x + barWidth / 2, canvas.height - padding - withdrawalHeight, barWidth / 2, withdrawalHeight)
      })

      // Add year labels for better readability when showing all data
      ctx.fillStyle = '#666'
      ctx.font = '10px Arial'
      ctx.textAlign = 'center'

      // Show year labels at reasonable intervals
      const yearInterval = Math.max(1, Math.floor(data.length / 8))
      labels.forEach((label, index) => {
        if (index % yearInterval === 0) {
          const x = padding + index * (width / data.length) + (width / data.length) / 2
          const year = label.split('-')[0]
          ctx.fillText(year, x, canvas.height - padding + 15)
        }
      })
    },
    drawNetFlowChart(ctx, canvas, data) {
      ctx.clearRect(0, 0, canvas.width, canvas.height)

      const padding = 50
      const width = canvas.width - 2 * padding
      const height = canvas.height - 2 * padding

      if (data.length === 0) {
        ctx.fillStyle = '#666'
        ctx.font = '14px Arial'
        ctx.textAlign = 'center'
        ctx.fillText('No data available', canvas.width / 2, canvas.height / 2)
        return
      }

      // Find min/max values for scaling
      const values = data.map(d => d.netFlow)
      const maxValue = Math.max(...values)
      const minValue = Math.min(...values)
      const absMax = Math.max(Math.abs(maxValue), Math.abs(minValue))

      // Draw axes
      ctx.strokeStyle = '#666'
      ctx.lineWidth = 1
      ctx.beginPath()
      // Y-axis
      ctx.moveTo(padding, padding)
      ctx.lineTo(padding, canvas.height - padding)
      // X-axis
      ctx.moveTo(padding, canvas.height - padding)
      ctx.lineTo(canvas.width - padding, canvas.height - padding)
      // Zero line
      const zeroY = canvas.height - padding - (height / 2)
      ctx.moveTo(padding, zeroY)
      ctx.lineTo(canvas.width - padding, zeroY)
      ctx.stroke()

      // Draw zero line label
      ctx.fillStyle = '#666'
      ctx.font = '10px Arial'
      ctx.textAlign = 'right'
      ctx.fillText('$0', padding - 5, zeroY + 3)

      const barWidth = Math.max(2, (width / data.length) * 0.8)
      const barSpacing = (width / data.length) * 0.2

      data.forEach((item, index) => {
        const x = padding + index * (width / data.length) + barSpacing / 2
        const value = item.netFlow
        const barHeight = Math.abs(value / absMax) * (height / 2)

        // Color based on positive/negative
        ctx.fillStyle = value >= 0 ? '#4CAF50' : '#FF5722'

        if (value >= 0) {
          // Positive bar (above zero line)
          ctx.fillRect(x, zeroY - barHeight, barWidth, barHeight)
        } else {
          // Negative bar (below zero line)
          ctx.fillRect(x, zeroY, barWidth, barHeight)
        }

        // Add month labels (show every few months for readability)
        if (index % Math.max(1, Math.floor(data.length / 12)) === 0) {
          ctx.fillStyle = '#666'
          ctx.font = '9px Arial'
          ctx.textAlign = 'center'
          const monthLabel = item.month.split('-').slice(0, 2).join('/')
          ctx.fillText(monthLabel, x + barWidth / 2, canvas.height - padding + 15)
        }
      })

      // Add value labels on axes
      ctx.fillStyle = '#666'
      ctx.font = '10px Arial'
      ctx.textAlign = 'right'

      // Positive max
      ctx.fillText(`+$${(absMax / 1000).toFixed(0)}k`, padding - 5, padding + 10)
      // Negative max
      ctx.fillText(`-$${(absMax / 1000).toFixed(0)}k`, padding - 5, canvas.height - padding - 5)

      // Title
      ctx.fillStyle = '#333'
      ctx.font = 'bold 12px Arial'
      ctx.textAlign = 'center'
      ctx.fillText('Net Cash Flow (Chequing Deposits - Credit Spending)', canvas.width / 2, 20)
    }
  }
}
</script>

<style scoped>
.charts-container {
  padding: 20px;
}

.display-1 {
  font-weight: bold;
}

.v-card {
  transition: transform 0.2s;
}

.v-card:hover {
  transform: translateY(-2px);
}

canvas {
  border-radius: 4px;
}
</style>
