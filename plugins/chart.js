import Chart from 'chart.js/auto'

export default (context, inject) => {
  // Make Chart.js available globally
  if (process.client) {
    window.Chart = Chart
  }
}
