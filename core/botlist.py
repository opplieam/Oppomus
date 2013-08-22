import config


def get_bot_list():
    return config.BOTS_TO_RUN.__iter__()

