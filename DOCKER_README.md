# 🏦 Financial Tracker - Docker Setup

## Quick Start

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### 🚀 One-Command Setup
```bash
./docker-setup.sh
```

### 📱 Access Your App
- **Application**: http://localhost:3000
- **Database**: localhost:5432 (user: postgres, db: money)

## 🐳 Docker Services

### Services Included:
1. **PostgreSQL Database** (port 5432)
   - Automatic schema initialization
   - Sample data setup
   - Health checks
   
2. **Nuxt.js Application** (port 3000)
   - Hot reload for development
   - Environment variables configured
   - Volume mapping for live code changes

## 📋 Manual Commands

### Start Services
```bash
docker-compose up -d
```

### View Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f app
docker-compose logs -f postgres
```

### Stop Services
```bash
docker-compose down
```

### Restart Services
```bash
docker-compose restart
```

### Fresh Start (removes all data)
```bash
docker-compose down -v
docker-compose up --build -d
```

## 🗄️ Database Access

### Connect to Database
```bash
# Using Docker
docker-compose exec postgres psql -U postgres -d money

# Using local psql client
psql -h localhost -U postgres -d money
```

### Useful SQL Commands
```sql
-- View all tables
\dt

-- View statements
SELECT * FROM statement LIMIT 10;

-- View users
SELECT * FROM users;

-- Check table structure
\d statement
```

## 📊 Data Import

### Import Your Converted Data
1. Use the converted CSV files in `converted_data/`
2. Go to http://localhost:3000/add-statement
3. Select "Credit Statement"
4. Paste the CSV content
5. Assign transaction purposes
6. Submit

### Sample Data Files:
- `converted_data/sample_test.csv` - Test data
- `converted_data/app_ready_2019.csv` - Your 2019 transactions
- `converted_data/app_ready_2020.csv` - Your 2020 transactions
- etc.

## 🔧 Development

### File Structure
```
financial_tracker/
├── docker-compose.yml      # Docker services configuration
├── Dockerfile             # App container definition
├── init-db.sql           # Database initialization
├── .env.example          # Environment variables template
├── converted_data/       # Your converted transaction data
├── server/              # Backend API
├── components/          # Vue.js components
├── pages/              # Nuxt.js pages
└── plugins/            # Vue.js plugins
```

### Environment Variables
Copy `.env.example` to `.env` and modify as needed:
```bash
cp .env.example .env
```

### Hot Reloading
Code changes are automatically reflected in the running container thanks to volume mapping.

## 🚨 Troubleshooting

### Port Already in Use
```bash
# Stop existing services
docker-compose down

# Or use different ports by editing docker-compose.yml
```

### Database Connection Issues
```bash
# Check if database is ready
docker-compose exec postgres pg_isready -U postgres

# Restart database service
docker-compose restart postgres
```

### App Not Loading
```bash
# Check app logs
docker-compose logs app

# Rebuild app container
docker-compose up --build app
```

### Reset Everything
```bash
# Nuclear option - removes all containers, volumes, and images
docker-compose down -v
docker system prune -a
./docker-setup.sh
```

## 📈 Production Deployment

For production, modify:
1. Change database passwords in `.env`
2. Set `NODE_ENV=production`
3. Use proper SSL certificates
4. Add reverse proxy (nginx)
5. Implement backup strategy

## 🎯 Next Steps

1. **Import Your Data**: Start with `sample_test.csv` to test
2. **Explore Dashboard**: View your financial visualizations
3. **Categorize Transactions**: Assign purposes to transactions
4. **Set Up Budgets**: Use the budgeting features
5. **Export Reports**: Generate financial reports

## 📞 Support

If you encounter issues:
1. Check the logs: `docker-compose logs -f`
2. Verify services are running: `docker-compose ps`
3. Try a fresh restart: `docker-compose down && docker-compose up -d`
