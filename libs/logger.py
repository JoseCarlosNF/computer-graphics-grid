import logging
from sys import stdout


def log(module_name: str):
    handler_stdout = logging.StreamHandler(stdout)
    handler_stdout.setLevel(logging.DEBUG)

    logging.basicConfig(
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S',
        format='%(asctime)s %(levelname)8s - %(name)s - %(message)s',
        handlers=[handler_stdout],
    )
    return logging.getLogger(module_name)
