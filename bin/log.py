
import logging

#Initialize logging 
def init_logging(log):
    log.setLevel(logging.DEBUG)
    stdoutHandler = logging.StreamHandler()
    stdoutHandler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s")
    stdoutHandler.setFormatter(formatter)
    log.addHandler(stdoutHandler)

