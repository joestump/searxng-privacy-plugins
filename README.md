# SearXNG Privacy Plugins

## Overview

This is a collection of plugins for [SearXNG](https://docs.searxng.org/) with a focus on further enhancing the privacy and readability of the results returned by the search engine.

## Plugins

* [`hello_world`](hello_world.py) – A simple example plugin. Logs what's passed to the plugin hooks.
* [`reader_news_proxy`](reader_news_proxy.py) – A plugin that enables proxying URLs from results through [Reader](https://github.com/Hydrophobefireman/reader), which is a [Postlight parser](https://github.com/postlight/parser) proxy for rendering readable versions of websites.

## Installation

### Create a Docker Container

Installing the plugin on Docker requires building a container:

```dockerfile
FROM docker.io/searxng/searxng:latest

RUN apk add --no-cache -t build-dependencies \
    git

RUN pip3 install --break-system-packages --no-cache git+https://github.com/joestump/searxng-privacy-plugins
```

### Enable Plugins in `settings.yml`

```yaml
plugins:
  - hello_world # For debug/testing only.
  - reader_news_proxy
```

## Configuration

### `reader_news_proxy`

* `proxy_url` – The URL to your Reader proxy.
* `article_patterns` – Regular expressions to match URLs against; if it matches, it will be replaced with `$proxy_url?url=$original_url`.

```yaml
reader_news_proxy:
  proxy_url: https://your-reader-instance.example.com
  article_patterns:
    - '^https:\/\/(.*\.)?cnn.com\/[0-9]{4}\/\d{2}\/\d{2}\/(.*)'
    - '^https:\/\/(.*\.)?newsweek.com/[0-9a-zA-Z\-]+$'
    - '^https:\/\/en.wikinews.org\/wiki\/[0-9a-zA-Z_,.]+$'
    - '^https:\/\/(.*\.)?npr.org/\d{4}\/\d{2}\/\d{2}\/(.*)'
    - '^https:\/\/(.*\.)?yahoo.com/news/(.*)'
```
