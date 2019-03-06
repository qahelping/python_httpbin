ACCEPT = "text/plain"
CONFIG = "https://httpbin.org/"

redirect_url = "https://httpbin.org/get"

file_name = "tests.log"
dictLogConfig = {
    "version": 1,
    "handlers": {
        "fileHandler": {
            "class": "logging.FileHandler",
            "formatter": "myFormatter",
            "filename": file_name
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

