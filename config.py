HEADERS_ACCEPT_TEXT = "text/plain"
HOST_URL = "https://httpbin.org/"
redirect_url = "https://httpbin.org/get"
file_name_for_logging = "tests.log"
dict_log_config = {
    "version": 1,
    "handlers": {
        "fileHandler": {
            "class": "logging.FileHandler",
            "formatter": "myFormatter",
            "filename": file_name_for_logging
        }
    },
    "loggers": {
        "test": {
            "handlers": ["fileHandler"],
            "level": "INFO",
        }
    },
    "formatters": {
        "myFormatter": {
            "format": "%(asctime)s - %(levelname)s - %(message)s"
        }
    }
}
