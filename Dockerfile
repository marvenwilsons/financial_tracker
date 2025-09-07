# Financial Tracker App
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache \
    postgresql-client \
    python3 \
    make \
    g++ \
    py3-pip

# Copy package files
COPY package*.json ./

# Install all dependencies (including dev dependencies for Nuxt development mode)
RUN npm ci

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p /app/converted_data

# Expose port
EXPOSE 3000

# Start command (development mode)
CMD ["npm", "run", "dev"]
