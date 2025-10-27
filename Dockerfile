# Stage 1: Node.js backend
FROM node:18-slim AS node_builder

WORKDIR /app

COPY package.json ./
RUN npm install --production
COPY . .

# Final stage
FROM node:18-slim

WORKDIR /app

# Copy Node.js files from the node_builder stage
COPY --from=node_builder /app /app

# Set up a non-root user
RUN useradd --create-home appuser
USER appuser

# Expose the port the app runs on
EXPOSE 3000

# Start the Node.js server
CMD ["node", "strudel_server.js"]