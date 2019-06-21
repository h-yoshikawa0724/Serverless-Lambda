FROM python:3.6
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

# update apt-get
RUN apt-get update -y && apt-get upgrade -y

# Install Nodejs 8
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs

COPY ./requirements.txt /src

# install library
RUN pip install --no-cache-dir -r requirements.txt

# install serverless framework
RUN npm install -g serverless

# install serverless-python-requirements
WORKDIR /
RUN npm install --save serverless-python-requirements

# set aws key
RUN sls config credentials --provider aws --key $AWS_ACCESS_KEY_ID --secret $AWS_SECRET_ACCESS_KEY
