# SearXNG Privacy Plugins

## Overview

This is a collection of plugins for [SearXNG](https://docs.searxng.org/) with a focus on further enhancing the privacy and readability of the results returned by the search engine.

## Plugins

* [`hello_world`](hello_world.py) – A simple example plugin. Logs what's passed to the plugin hooks.
* [`url_rewrite`](url_rewrite.py) – A plugin that enables rewriting URLs from search results based on regular expressions. Can proxy URLs through privacy-preserving services, block unwanted domains, and adjust result priorities.

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
  - url_rewrite
```

## Configuration

### `url_rewrite`

The URL rewrite plugin allows you to modify search result URLs using regular expressions. Each rule can:
* Rewrite URLs to proxy them through privacy-preserving services
* Remove results from specific domains
* Adjust the priority of matching results
* Optionally preserve the original parsed URL

```yaml
url_rewrite:
  rules:
    - pattern: '^(?P<url>https://(.*\.)?cnn\.com/.*)$'
      repl: 'https://reader.example.com/?url=\g<url>'
    - pattern: '^https?://(?:www\.)?facebook\.com/.*'
      repl: false  # Removes matching results
    - pattern: '^(?P<url>https://news\.example\.com/.*)$'
      repl: 'https://proxy.example.com/?url=\g<url>'
      priority: high  # Increases result priority
    - pattern: '^(?P<url>https://tracking\.evil\.com/.*)$'
      repl: 'https://clean-proxy.example.com/?url=\g<url>'
      replace_url: false  # Preserves original parsed URL
```

Configuration options for each rule:
* `pattern`: Regular expression pattern to match against result URLs
* `repl`: Replacement string for matched URLs, or `false` to remove matching results
* `priority`: Optional priority adjustment ('high' or 'low') for matching results
* `replace_url`: Optional boolean to control whether the parsed URL is updated (defaults to true)
