FROM python:3.11
# install pytest using pip
RUN pip install pytest-playwright
# install playwright
RUN playwright install
# install playwright dependencies. 
# This also installs the browsers when running in headed mode
RUN playwright install-deps
# copy tests from the current dir to the container
COPY ./tests /opt/
# set the working directory
WORKDIR /opt/tests

