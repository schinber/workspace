"""
python 连接hdfs 练习
"""
import pyhdfs
import pydash

client = pyhdfs.HdfsClient(hosts="192.168.216.130", user_name="tianxinbo")
print(client)

# -*- coding:utf-8 -*-


'''pip install pyhdfs'''


class FileManager(object):

    # upload file to hdfs from local file system
    def file_upload(self, host, user_name, local_path, hdfs_path):
        print("file upload start")
        fs = pyhdfs.HdfsClient(hosts=host, user_name=user_name)
        print(fs.listdir('/'))
        fs.copy_from_local(local_path, hdfs_path)
        print("file upload finish")

    # download file from hdfs file system
    def file_down(self, host, user_name, local_path, hdfs_path):
        print("file download start")
        fs = pyhdfs.HdfsClient(hosts=host, user_name=user_name)
        fs.copy_to_local(hdfs_path, local_path)
        print("file download finish")


if __name__ == '__main__':
    file_manager = FileManager()
    # client = pyhdfs.HdfsClient(hosts="192.168.216.130", user_name="tianxinbo")
    file_manager.file_upload("192.168.216.130", "tianxinbo", r"D:\apache-maven-3.6.1\README.txt",
                             "/home/tianxinbo/README.txt")
    # file_manager.file_down("ip:50070", "admin", u"local_file.xlsx", u"hdfs_file.xlsx")
