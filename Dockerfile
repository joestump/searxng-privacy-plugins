FROM docker.io/searxng/searxng:latest

ARG PLUGIN_PATH=/tmp/searxng-privacy-plugins

RUN apk add --no-cache -t build-dependencies \
    git

COPY . $PLUGIN_PATH

RUN pip3 install --break-system-packages --no-cache $PLUGIN_PATH
