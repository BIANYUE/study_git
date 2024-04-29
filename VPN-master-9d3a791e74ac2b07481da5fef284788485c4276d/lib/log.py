import os
import datetime
import logging.config

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 当前文件的路径
LOG_DIR = os.path.join(os.path.dirname(BASE_DIR), "logs")  # 在当前路径下拼接log xx/logs
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)  # 创建路径
LOG_FILE = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"  # 文件名 如 2019-03-25.log

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            'format': '%(asctime)s [%(filename)s:%(lineno)d] - %(message)s',
            'datefmt': '%Y-%m-%d  %H:%M:%S'
        },
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },

        "default": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": os.path.join(LOG_DIR, LOG_FILE),
            'mode': 'w+',
            "maxBytes": 1024 * 1024 * 5000,
            "backupCount": 20,
            "encoding": "utf8"
        },
    },

    "root": {
        'handlers': ['default'],
        'level': "INFO",
        'propagate': False
    }
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("test日子")
    logger.exception("123")
