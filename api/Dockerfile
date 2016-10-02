FROM ubuntu:14.04

# set argument
ARG PYTHON_VERSION=3.4.3

# install dependencies
RUN apt-get update && \
    apt-get install -yq --no-install-recommends \
    build-essential \
    git \
    make \
    curl \
    wget \
    python-dev \
    python-pip \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    supervisor \
    python-software-properties \
    software-properties-common && \
    add-apt-repository -y ppa:nginx/stable && \
    apt-get install -y --no-install-recommends nginx && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

# clone Pyenv
RUN git config --global http.sslVerify false && \
    git clone https://github.com/yyuu/pyenv.git /usr/local/.pyenv

# set environment variable
ENV PYENV_ROOT /usr/local/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# install Python 3.4.3
RUN export PYTHON_BUILD_MIRROR_URL="http://yyuu.github.io/pythons " && \
    pyenv install -v ${PYTHON_VERSION} && \
    pyenv global ${PYTHON_VERSION}

# set working directory
RUN mkdir /opt/app
WORKDIR /opt/app

COPY . /opt/app
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r /opt/app/requirements.txt

EXPOSE 8080 80
