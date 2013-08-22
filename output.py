# -*- coding: utf-8 -*-
from libs.logger import Logger
from libs.queues import Queues


def execute_output():
    Logger()
    Logger.debug('Start Output Process')
    while True:
        try:
            result = Queues.get_output()
            Logger.info(result)
            #Your output logic go there


        except:
            break
    Logger.debug('End Output Process')