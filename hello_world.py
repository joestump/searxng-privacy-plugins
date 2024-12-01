from flask_babel import gettext
from searx.plugins import logger


name = "Hello World"
description = gettext("Test plugin that prints debug log messages")
default_on = False
preference_section = 'general'
plugin_id = 'hello-world'


logger = logger.getChild(plugin_id)


def pre_search(request, search):
    logger.info(f"Search: {search}")
    logger.info(f"Request: {request}")
    return True


def post_search(request, search):
    logger.info(f"Search: {search}")
    logger.info(f"Request: {request}")
    return None


def on_result(request, search, result):
    logger.info(f"Search: {search}")
    logger.info(f"Result: {result}")
    return True
