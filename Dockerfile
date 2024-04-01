FROM nginx:latest

# Copy package.json and package-lock.json
COPY index.html /usr/share/nginx/html

