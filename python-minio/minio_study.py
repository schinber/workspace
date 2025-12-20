from minio import Minio
from minio.error import MinioException


class MinioOperate(object):
    def __init__(self):
        self.minio_client = Minio('192.168.43.128:9000',
                                  access_key='root',
                                  secret_key='admin123',
                                  secure=False)

    def create_bucket(self, bucket):
        """
        1、先检查minio bucket是否存在，存在则返回True
        2、再通过client调用make_bucket
        3、创建成功则返回True，否则返回False
        :param bucket: String
        :return: bool
        """
        try:
            if self.minio_client.bucket_exists(bucket):
                return True
            self.minio_client.make_bucket("a", location="us-east-1")
        except MinioException as err:
            print(err)
            return False
        except ValueError as val_err:
            print(val_err)
            return False

    def bucket_exist(self, bucket):
        """
        判断bucket是否存在,存在返回True， 不存在返回False
        """
        self.minio_client.bucket_exists(self, bucket)

    def delete_bucket(self, bucket):
        """
        删除minio中bucket
        :param bucket: bucket name
        :return: bool
        """
        try:
            if not self.minio_client.bucket_exists(bucket):
                print("桶子不存在")
                return False
            self.minio_client.remove_bucket(bucket)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    bucket = "abc"
    minio_client = MinioOperate()
    # minio_client.create_bucket(bucket)
    minio_client.delete_bucket(bucket)
