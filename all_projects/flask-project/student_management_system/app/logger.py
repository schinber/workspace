import logging
import os
from logging.handlers import TimedRotatingFileHandler
from flask import request


class RequestFormatter(logging.Formatter):
    """自定义日志格式器，包含请求信息"""

    def format(self, record):
        record.url = request.url if request else 'N/A'
        record.remote_addr = request.remote_addr if request else 'N/A'
        return super().format(record)


def setup_logger(app):
    """配置应用日志"""
    log_dir = app.config['LOG_DIR']
    log_level = getattr(logging, app.config['LOG_LEVEL'])

    # 创建格式器
    formatter = RequestFormatter(
        '%(asctime)s - %(name)s - %(levelname)s - '
        '[%(remote_addr)s] - %(url)s - %(message)s'
    )

    # 清除默认处理器
    app.logger.handlers.clear()
    app.logger.setLevel(log_level)

    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(log_level)
    app.logger.addHandler(console_handler)

    # 文件处理器 - 主日志
    main_log = os.path.join(log_dir, 'app.log')
    file_handler = TimedRotatingFileHandler(
        main_log,
        when='midnight',
        interval=1,
        backupCount=30,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(log_level)
    app.logger.addHandler(file_handler)

    # 错误日志处理器
    error_log = os.path.join(log_dir, 'error.log')
    error_handler = TimedRotatingFileHandler(
        error_log,
        when='midnight',
        interval=1,
        backupCount=30,
        encoding='utf-8'
    )
    error_handler.setFormatter(formatter)
    error_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_handler)

    # 记录启动日志
    app.logger.info(f'应用启动 - 日志级别: {app.config["LOG_LEVEL"]}')
    app.logger.info(f'日志目录: {log_dir}')
