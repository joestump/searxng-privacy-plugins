"""
Searx privacy plugins

searx-privacy-plugins
  Plugins to handle redirecting URLs to private alternatives

"""

from setuptools import setup

GIT_URL='https://gitea.stump.wtf/joestump/searxng-privacy-plugins'

setup(
    name                = 'searxng-privacy-plugins'
    , version           = '0.1'
    , description       = 'Privacy redirecting/proxying plugins'
    , long_description  = __doc__
    , url               =  GIT_URL
    , author            = 'Joe Stump'
    , author_email      = 'joe@stu.mp'
    , project_urls      = {
        "Code"              : GIT_URL
        , "Issue tracker"   : GIT_URL + "/issues"
    }
    , license           = 'GNU Affero General Public License'
    , zip_safe          = False
    , py_modules        = [
        'hello_world',
        'url_rewrite',
    ]
    , entry_points      = {
        'searxng.plugins' : [
            'searxng-privacy.hello_world = hello_world',
            'searxng-privacy.url_rewrite = url_rewrite',
        ]
    }
)
