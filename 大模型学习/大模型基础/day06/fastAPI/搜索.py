from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")  # 因为参数有默认值
async def read_item(skip: int = 0, limit: int = 10): # 查询0-10条数据
    return fake_items_db[skip : skip + limit]


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "这是多路径查询"}
        )
    return item


class Item(BaseModel):
    """
    创建数据模型,把数据模型声明为继承 BaseModel 的类。
    和查询参数一样，如果没有默认值就是必填属性
    """
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/itemx/")
async def create_item(item: Item):  # 使用与声明路径和查询参数相同的方式声明请求体，把请求体添加至路径操作
    item_dict = item.model_dump()  # 将对象字段转变成字典
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict