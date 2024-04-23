dict_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s",
            }
        },
        "handlers": {
            "util_handler": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "when": "h",
                "interval": 10,
                "backupCount": 5,
                "level": "DEBUG",
                "formatter": "simple",
                "filename": "util.log",
                "encoding": "utf-8",
            }
        },
        "loggers": {
            "utils_logger": {
                "level": "INFO",
                "handlers": ["util_handler"]
            },
            "app_loger": {
                "level": "INFO",
                "handlers": ["util_handler"]
            }
        },
    }
