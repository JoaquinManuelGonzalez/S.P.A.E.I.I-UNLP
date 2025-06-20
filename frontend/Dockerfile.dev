# Use Node.js for Vue app
FROM node:lts-alpine

WORKDIR /vue

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the app source and build it
COPY . .
RUN npm run build

# Expose the port for the dev server
EXPOSE 5173

# Command for development
CMD ["npm", "run", "dev"]