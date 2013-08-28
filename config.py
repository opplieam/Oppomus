"""A configuration file"""

#A list of bots to run in the system
#Ex. BOTS_TO_RUN = ['line','nested'] which run 2 bots
#Ex. BOTS_TO_RUN = ['line']
#Ex. BOTS_TO_RUN = [] which run all bots
#'line', 'nested' is the name of the file in bots package
BOTS_TO_RUN = []


#Default bot crawling method, If not specific the crawl method in bots file.
# The system will use this config.
#Ex. DEFAULT_CRAWL_METHOD = 'line'
#Ex. DEFAULT_CRAWL_METHOD = 'nested'
DEFAULT_CRAWL_METHOD = 'line'


#Logging level
#Ex. LOG_LEVEL = 'INFO'
#Ex. LOG_LEVEL = 'DEBUG'
#Ex. LOG_LEVEL = 'ERROR'
LOG_LEVEL = 'INFO'


# ----------------------
# Advanced configuration (For balancing)
# ----------------------

#A maximum number of bots to run at a time
#You can use the total cpu cores * 2
NUMBER_OF_WORKERS = 8

#A delay time (seconds) before the output process exit.
#Otherword, If the output pipe is empty for a specific delay time.
#The output process will exited
OUTPUT_PROCESS_TIMEOUT = 30

#A delay time (seconds) before the crawl process exit.
#Otherword, If the url pipe is empty for a specific delay time.
#The crawl process will exited
NESTED_CRAWL_TIMEOUT = 10