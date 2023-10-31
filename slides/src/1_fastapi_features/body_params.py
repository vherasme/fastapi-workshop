"""
This example shows how to use body parameters.

To run this example, use the following command:

    uvicorn body_params:app --reload

And then open your browser at http://localhost:8000/docs.
"""
from typing import Annotated


from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

NameType = Annotated[str, Field(examples=["Potato"])]
DescriptionType = Annotated[str, Field(examples=["Tomato"])]


class Item(BaseModel):
    name: NameType
    description: DescriptionType


@app.post("/items/")
async def create_item(item: Item):
    return item
