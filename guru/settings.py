# Scrapy settings for guru project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'guru'

SPIDER_MODULES = ['guru.spiders']
NEWSPIDER_MODULE = 'guru.spiders'


#LOG_ENABLED = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 64

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   "Accept": "application/json, text/javascript, */*; q=0.01",
   "DNT": "1",
   "Accept-Encoding": "gzip, deflate, br",
   "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8",
   "x-requested-with": "XMLHttpRequest",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'trustpilot.middlewares.TrustpilotSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 100
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#     'tutorial.pipelines.DuplicatesPipeline': 100,
#     'tutorial.pipelines.SaveQuotesPipeline': 200,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 200
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


## USING COLORS ON LOG

# import copy
# from colorlog import ColoredFormatter
# import scrapy.utils.log
# color_formatter = ColoredFormatter(
#     (
#         '%(log_color)s%(levelname)-5s%(reset)s '
#         '%(yellow)s[%(asctime)s]%(reset)s'
#         '%(white)s %(name)s %(funcName)s %(bold_purple)s:%(lineno)d%(reset)s '
#         '%(log_color)s%(message)s%(reset)s'
#     ),
#     datefmt='%y-%m-%d %H:%M:%S',
#     log_colors={
#         'DEBUG': 'blue',
#         'INFO': 'bold_cyan',
#         'WARNING': 'red',
#         'ERROR': 'bg_bold_red',
#         'CRITICAL': 'red,bg_white',
#     }
# )
# _get_handler = copy.copy(scrapy.utils.log._get_handler)
# def _get_handler_custom(*args, **kwargs):
#     handler = _get_handler(*args, **kwargs)
#     handler.setFormatter(color_formatter)
#     return handler
# scrapy.utils.log._get_handler = _get_handler_custom