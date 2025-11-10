import os
from datetime import timedelta  # 新增：导入时间间隔类

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 新增：会话超时配置（1分钟）
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=120)
    # 启用持久化会话
    SESSION_PERMANENT = True
    SESSION_REFRESH_EACH_REQUEST = True

    # 日志配置
    LOG_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'logs')
    LOG_LEVEL = 'INFO'  # DEBUG, INFO, WARNING, ERROR, CRITICAL

    # 确保日志目录存在
    @staticmethod
    def init_app(app):
        if not os.path.exists(app.config['LOG_DIR']):
            os.makedirs(app.config['LOG_DIR'])


class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LEVEL = 'DEBUG'


class ProductionConfig(Config):
    DEBUG = False
    LOG_LEVEL = 'WARNING'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
