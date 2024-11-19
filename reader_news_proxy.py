from flask_babel import gettext
import re
from urllib.parse import urlparse
from searx import settings
from searx.settings_loader import get_yaml_cfg
from searx.plugins import logger


name = "Reader News Proxy"
description = gettext("Proxy news articles through a Postlight parser for viewing")
default_on = True
preference_section = 'general'
plugin_id = 'reader_news_proxy'


logger = logger.getChild(plugin_id)
config = settings.get(plugin_id, {})
article_patterns = config.get("article_patterns", [])
reader_proxy_url = config.get("proxy_url", None)

def on_result(request, search, result):
    if 'url' not in result:
        logger.debug("No url found in result")
        return True  # Nothing to do here.

    if reader_proxy_url is None:
        logger.warn("No proxy_url found in settings.yml")
        return True  # Improperly configured.

    if len(article_patterns) == 0:
       logger.warn("No article_patterns found in settings.yml")
       return True  # Nothing to do here.

    for pattern in article_patterns:
        if re.match(pattern, result["url"]):
            new_url = f"{reader_proxy_url}?url={result['url']}"
            result["url"] = new_url
            result["parsed_url"] = urlparse(new_url)
            logger.info(f'{result["url"]} matched {pattern} - updated URL is {new_url}')
        else:
            logger.debug(f'{result["url"]} did not match any patterns')

    return True  # Always keep the result.
