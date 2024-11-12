from flask_babel import gettext
from searx.plugins import logger


name = "Hello World"
description = gettext("Test plugin that prints debug log messages")
default_on = True
preference_section = 'general'
plugin_id = 'hello-world'


logger = logger.getChild(plugin_id)


def pre_search(request, search):
    logger.info('Search: ', search)
    logger.info('Request: ', request)
    return True


def post_search(request, search):
    logger.info('Search: ', search)
    logger.info('Request: ', request)
    return None


def on_result(request, search, result):
    logger.info('Search: ', search)
    logger.info('Result: ', result)
    return True
