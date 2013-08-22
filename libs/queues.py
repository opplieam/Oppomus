from multiprocessing import Queue
import config


class Queues():

    output_queue = None

    def __init__(self):
        Queues.output_queue = Queue()

    @staticmethod
    def send_to_output(data):
        Queues.output_queue.put(data)

    @staticmethod
    def get_output():
        return Queues.output_queue.get(timeout=config.OUTPUT_PROCESS_TIMEOUT)