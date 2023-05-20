# Get the latest version of Playwright
FROM mcr.microsoft.com/playwright:v1.34.0-jammy

# mkdir for the application tests 
RUN mkdir /opt/my_app
WORKDIR /opt/my_app
# Copy npm package.json
COPY package.json ./
# Install axe plugin
RUN npm install @axe-core/playwright
# Run npm install to install any dependencies in the package json
RUN  npm install
# Copy tests from the current dir to the container
COPY ./tests /opt/my_app/tests

