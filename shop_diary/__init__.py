import os
import logging

LOG_FORMAT = '[%(levelname)s] %(asctime)s %(name)s %(message)s'
LOG_LEVEL = int(os.environ.get("LOG_LEVEL", logging.INFO))


# configure the root logger so that it works the same locally
# as it does in the lambda runtime
def configure_logger():
    # use the root logger so that child loggers inherit configuration
    logger = logging.getLogger()
    logger.handlers = []
    logger.setLevel(LOG_LEVEL)
    logger.addHandler(logging.StreamHandler())
    formatter = logging.Formatter(LOG_FORMAT)
    for handler in logger.handlers:
        handler.setFormatter(formatter)


configure_logger()


intents = {
    "What's in my garage": [
        "what do I have",
        "what bicycles or motorcycles do I have"
    ],
    "log entry": ["log an entry", "create a log entry"],
    "torque specs": ["how tight should I make this bolt"]
}
