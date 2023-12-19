# Use an official Node.js runtime as the base image
FROM node:14 AS node_base
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the internship directory contents into the container at /app/internship
COPY . /app

# Copy the requirements.txt file from the current directory
COPY requirements.txt ./

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./


# Install app dependencies
RUN npm install


RUN python -m pip install
# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

FROM node_base AS final
# Copy app source code to the container
COPY . .

# Expose a port that your app will listen on
EXPOSE 3000

# Command to start your app
CMD ["node", "app.js"]
