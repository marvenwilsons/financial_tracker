#!/bin/bash

# Financial Tracker Docker Setup Script
echo "🏦 Setting up Financial Tracker with Docker"
echo "==========================================="

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"

# Stop any existing containers
echo "🛑 Stopping existing containers..."
docker-compose down

# Remove old containers and volumes (optional - uncomment if you want a fresh start)
# echo "🧹 Cleaning up old containers and volumes..."
# docker-compose down -v
# docker system prune -f

# Build and start the services
echo "🔨 Building and starting services..."
docker-compose up --build -d

# Wait for database to be ready
echo "⏳ Waiting for database to be ready..."
sleep 10

# Check if services are running
echo "🔍 Checking service status..."
docker-compose ps

# Show logs
echo "📋 Service logs:"
docker-compose logs --tail=20

echo ""
echo "🎉 Setup complete!"
echo "📱 Application: http://localhost:3000"
echo "🗄️  Database: localhost:5432 (user: postgres, db: money)"
echo ""
echo "📝 Useful commands:"
echo "   View logs: docker-compose logs -f"
echo "   Stop services: docker-compose down"
echo "   Restart: docker-compose restart"
echo "   Database shell: docker-compose exec postgres psql -U postgres -d money"
