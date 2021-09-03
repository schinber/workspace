# coding:utf-8

import redis

if __name__ == "__main__":
    try:
        r = redis.StrictRedis(host='192.168.216.130', port=9527, db=0)
        # StrictRedis 严格模式下连接redis服务器。
        # 1、不实现slect
        # 2、redis 的del 命令改用delete命令(原因是python 中del也是关键字)
        print(r.get('slogan').decode('utf-8'))  # 接收到的对象是byte类型的
    except Exception as err:
        print(err)
