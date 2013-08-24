#!/usr/bin/env python
from controllers.main import main
import os

logs_dir = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'logs')


def run():
    print logs_dir
    if not os.path.isdir(logs_dir):
        print ("Creating %s" % logs_dir)
        os.makedirs(logs_dir)

    main()

run()