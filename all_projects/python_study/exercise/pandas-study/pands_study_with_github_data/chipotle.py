"""
探索快餐数据
    – 将数据集存入一个名为chipo的数据框内
    – 查看前10行内容
    – 数据集中有多少个列(columns)？
    – 打印出全部的列名称
    – 数据集的索引是怎样的？
    – 被下单数最多商品(item)是什么?
    – 在item_name这一列中，一共有多少种商品被下单？
    – 在choice_description中，下单次数最多的商品是什么？
    – 一共有多少商品被下单？
    – 将item_price转换为浮点数
    – 在该数据集对应的时期内，收入(revenue)是多少？
    – 在该数据集对应的时期内，一共有多少订单？
    – 每一单(order)对应的平均总价是多少？
    ————————————————
    版权声明：本文为CSDN博主「王大阳_」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
    原文链接：https://blog.csdn.net/weixin_43746433/article/details/90454463
"""
import pandas as pd
csv_path = "./Pandas_exercises-master/chipotle.tsv"
# 默认是以逗号“，”作为分割符，若是以其它分隔符，比如制表符“/t”，则需要显示的指定分隔符
chipo = pd.read_csv(csv_path, sep='\t')
print(chipo.head(10))
print(chipo.shape)
print('columns:', chipo.columns)
print('info\n', chipo.info())
print('index\n', chipo.index)
print(chipo['item_name'].value_counts().head(1))
# 查看商品数
print(chipo['item_name'].unique())
print(chipo['choice_description'].value_counts().head())
# 商品下单数量
print('商品下单数量', chipo['quantity'].sum)