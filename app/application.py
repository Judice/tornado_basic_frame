# -*- coding: utf-8 -*-

import os
import tornado.web
from tornado.options import options, define
from config import STATIC_PATH

from handlers import ROUTES

from utils.log import LOG

define("env", default="debug", help="service run environment")
define("port", default=8080, type=int, help="bind port")

class Application(tornado.web.Application):
    def __init__(self):
        LOG.info("Server application initializing.")
        debug = options.env == "debug"
        LOG.info("App debug switch : %s" % debug)
        app_settings = {
                'gzip': 'on',
                'static_path': STATIC_PATH,
                'debug': debug,
                }
        super(Application, self).__init__(ROUTES, **app_settings)
        LOG.info("Server application initialization done.")