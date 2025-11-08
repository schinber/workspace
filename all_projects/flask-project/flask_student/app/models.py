import os

from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

# 数据库连接配置（替换为你的实际信息）
DB_CONFIG = {
    "user": "root",
    "password": os.environ.get("mysql_pwd"),
    "host": "localhost",
    "port": 3306,
    "db_name": "runoob"
}
DB_URL = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['db_name']}?charset=utf8mb4"

# 初始化引擎和会话
engine = create_engine(DB_URL, echo=False)  # echo=True 可打印SQL语句（调试用）
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 定义User模型（映射users表）
class User(Base):
    __tablename__ = "users"  # 对应表名

    # 字段映射（与建表语句一致）
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)  # NOT NULL
    email = Column(String(100), nullable=False)     # NOT NULL
    birthdate = Column(Date)                       # 可为空（DATE类型）
    is_active = Column(Boolean, default=True)      # 默认值TRUE

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"


# 模型映射到数据库中
Base.metadata.create_all(bind=engine)

# 保存到数据库中
# 类的实例化   __call__  将类变成方法去调用
SESSION = SessionLocal()  # 创建会话实例
