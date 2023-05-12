FROM python:3.11
# install pytest using pip
RUN pip install pytest-playwright
# install playwright
RUN playwright install
# install playwright dependencies
RUN playwright install-deps
# copy tests from the current dir to the container
COPY ./tests /opt/

WORKDIR /opt/tests

