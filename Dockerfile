FROM node:18-slim

WORKDIR /app

COPY package.json ./
RUN npm install --production
COPY . .

# Set up a non-root user
RUN useradd --create-home appuser
USER appuser

# Expose the port the app runs on
EXPOSE 3000
`
# Start the Node.js server
CMD ["node", "strudel_server.js"]
