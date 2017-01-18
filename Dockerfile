FROM quay.io/mozmar/base

# Set Python-related environment variables to reduce annoying-ness
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV LANG=C.UTF-8

CMD ["./run.sh"]
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential python3-dev python3-pip python3-setuptools gettext && \
    rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10
RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 10

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
