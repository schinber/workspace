# coding:utf-8
from cassandra.cqlengine.models import Model

b = [1, 2, 3, 4, "a"]
# print [1, 2]
# exit()
q = list()
from cassandra.cluster import Cluster

# class QuerySetDescriptor(object):
#     """
#     returns a fresh queryset for the given model
#     it's declared on everytime it's accessed
#     """
#
#     def __get__(self, obj, model):
#         """ :rtype: ModelQuerySet """
#         if model.__abstract__:
#             print "cannot execute queries against abstract models"
#             # raise CQLEngineException('cannot execute queries against abstract models')
#         queryset = model.__queryset__(model)

# class A():
#     def __init__(self, name):
#         self.name = name
#     def g(self):


# x = A()
x = Model.objects.filter(pk__in=[x.pk for x in b])
print(b)
print(b.pop())
print(b)
