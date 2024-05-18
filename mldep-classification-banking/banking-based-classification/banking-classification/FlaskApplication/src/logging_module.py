
import os
import logging
from logging.handlers import RotatingFileHandler
from flask.logging import default_handler
from flask import has_request_context, request
# from newrelic.agent import NewRelicContextFormatter

# log_format = logging.Formatter(
#     '[%(asctime)s] {%(levelname)s %(name)s %(threadName)s} : %(message)s')

# Define log directory path
log_dir = os.path.join(os.path.dirname(__file__), 'logs')

# Create log directory if it doesn't exist
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Define log file paths
debug_info_log_file_name = os.path.join(log_dir, 'debug.log')
warn_error_critical_log_file_name = os.path.join(log_dir, 'error.log')

# Other logging configurations remain the same
logger_name = os.environ.get("logger_name", "flask_app_logger")
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)

# Define a custom log formatter with request information
class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)

formatter = RequestFormatter(
    '[%(asctime)s] %(remote_addr)s requested %(url)s %(levelname)s '
    '{%(name)s %(threadName)s} : %(message)s'
)

# Set up stream handler
def set_stream_handler(log_level):
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(log_level)
    logger.addHandler(stream_handler)

set_stream_handler(logging.DEBUG)

# Set up file handlers
MAX_BYTES = 1000000
BACKUP_COUNT = 10

def set_file_handler(log_file_name, log_level, filter_=None):
    file_handler = RotatingFileHandler(
        log_file_name, maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(log_level)
    if filter_:
        file_handler.addFilter(filter_)
    logger.addHandler(file_handler)

set_file_handler(warn_error_critical_log_file_name, logging.WARN)
set_file_handler(debug_info_log_file_name, logging.DEBUG)



