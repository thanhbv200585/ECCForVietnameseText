# Use an official Node.js LTS (Long Term Support) image as the base
FROM node:lts-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the working directory
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the entire project to the working directory
COPY . .

# Build the React app for production
RUN npm run build

# Expose the desired port (e.g., 80) for the container
EXPOSE 5173

# Start the web server when the container is run
CMD ["npm", "run", "dev"]