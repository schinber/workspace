import os

import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from utils import func_cost

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
engine = create_engine(DB_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# 定义User模型（映射users表）
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    birthdate = Column(Date)
    is_active = Column(Boolean, default=True)


def insert_csv_to_db1(csv_path):
    df = pd.read_csv(csv_path)
    db = SessionLocal()
    try:
        for index, row in df.iterrows():
            user = User(
                id=row['id'] if 'id' in row else None,
                username=row['username'],
                email=row['email'],
                birthdate=pd.to_datetime(row['birthdate']).date() if 'birthdate' in row else None,
                is_active=row['is_active'] if 'is_active' in row else True
            )
            db.add(user)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"插入数据失败: {e}")
    finally:
        db.close()

@func_cost
def insert_csv_to_db2(csv_path):
    """
    批量插入
    使用 bulk_insert_mappings() 方法替代逐个添加对象
    这种方式会减少与数据库的交互次数，提高性能
    """
    df = pd.read_csv(csv_path)
    db = SessionLocal()
    try:
        # 准备数据列表
        users_data = []
        for index, row in df.iterrows():
            user_dict = {
                'username': row['username'],
                'email': row['email'],
                'birthdate': pd.to_datetime(row['birthdate']).date() if 'birthdate' in row else None,
                'is_active': row['is_active'] if 'is_active' in row else True
            }
            if 'id' in row and row['id'] is not None:
                user_dict['id'] = row['id']
            users_data.append(user_dict)

        # 批量插入
        db.bulk_insert_mappings(User, users_data)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"插入数据失败: {e}")
    finally:
        db.close()


@func_cost
def insert_csv_to_db_pandas(csv_path):
    """
    # DataFrame to SQL 方式示例
    """
    print("DataFrame to SQL方式开始写入数据库")
    df = pd.read_csv(csv_path)
    # 处理日期列
    if 'birthdate' in df.columns:
        df['birthdate'] = pd.to_datetime(df['birthdate'])
    # 使用 pandas 直接写入数据库
    df.to_sql('users', engine, if_exists='append', index=False, method='multi')
    print("写入完成!")


def insert_one():
    db = SessionLocal()
    try:
        user = User(
            id=1,
            username='赵四',
            email='zhaosi@163.com',
            birthdate='2020-05-05',
            is_active=True)
        db.add(user)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"插入数据失败: {e}")
    finally:
        db.close()
        print("ok")


if __name__ == "__main__":
    csv_file_path = 'users.csv'
    # insert_csv_to_db(csv_file_path)
    # insert_csv_to_db2(csv_file_path)
    insert_csv_to_db_pandas(csv_file_path)
