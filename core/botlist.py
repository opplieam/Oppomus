# -*- coding: utf-8 -*-
from os import listdir, path
import config


def get_bot_list():
    if config.BOTS_TO_RUN:
        bots = config.BOTS_TO_RUN.__iter__()
    else:
        bots = [module[:-3] for module in listdir(path.abspath('bots/'))
                if module != '__init__.py' and module[-3:].startswith('.py')].__iter__()
    return bots

