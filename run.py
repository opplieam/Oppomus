#!/usr/bin/env python
import os
from os.path import abspath, isdir
from controllers.main import main

logs_dir = abspath('logs/')


def run():
    if not isdir(logs_dir):
        os.makedirs(logs_dir)

    main()

run()