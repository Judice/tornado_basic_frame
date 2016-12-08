# -*- coding: utf-8 -*-

import tornado.web
from config import APP_SETTINGS

from handlers import ROUTES

from utils.log import LOG

class Application(tornado.web.Application):

    def __init__(self):
        LOG.info("Server application initializing.")
        LOG.info("App debug switch : %s" % APP_SETTINGS['debug'])
        super(Application, self).__init__(ROUTES, **APP_SETTINGS)
        LOG.info("Server application initialization done.")