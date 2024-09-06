from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from datetime import datetime

class Post(Model):
    id = fields.IntField(pk=True)  # Primary key
    title = fields.CharField(max_length=255)  # Post title
    content = fields.TextField()  # Post content
    author = fields.CharField(max_length=100)  # Author name
    created_at = fields.DatetimeField(auto_now_add=True)  # Automatically set to current time on creation
    updated_at = fields.DatetimeField(auto_now=True)  # Automatically updates when the record is modified
    is_published = fields.BooleanField(default=True)  # Optional field to mark post as published or not



    def __str__(self):
        return self.title

    class PydanticMeta:
        table = "posts"  # Set the table name in the database





Post_Pydantic = pydantic_model_creator(Post, name="Book")
PostIn_Pydantic = pydantic_model_creator(Post, name="BookIn", exclude_readonly=True)

