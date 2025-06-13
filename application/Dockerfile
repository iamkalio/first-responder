# Use a recommended Node.js Long Term Support (LTS) version
FROM node:18-slim

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to leverage Docker cache
COPY package*.json ./

# Install application dependencies
RUN npm install

# Copy the rest of your application code
COPY . .

# Expose the port your Express app listens on
EXPOSE 8080

CMD [ "npm", "start" ]