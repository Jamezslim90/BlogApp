
# Importing  HTTPException to handle errors.
# Importing the ORM model `Post` and two Pydantic models:
# `PostIn_Pydantic` for input data, and `Post_Pydantic` for output data.
# Importing BaseModel from Pydantic, which will be used to define models for request and response validation.
# Importing List from typing to define the type of response as a list of objects.


from app.models import Post, PostIn_Pydantic, Post_Pydantic
from tortoise.contrib.fastapi import HTTPNotFoundError
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List


router = APIRouter()


class Message(BaseModel):
    message: str
# Defining a simple Pydantic model for response messages (used in the delete operation), with a single field `message`.

@router.get('/posts', response_model=List[Post_Pydantic])
async def get_all_posts():
    # This endpoint returns all blog posts. The `response_model` is a list of `Book_Pydantic` objects.
    return await Post_Pydantic.from_queryset(Post.all())
    # Fetches all posts from the database and converts them into Pydantic models for the response.

@router.post('/post', response_model=Post_Pydantic)
async def create_a_post(post: PostIn_Pydantic):
    # This POST endpoint is for creating a new blog post. The input is a `PostIn_Pydantic` object.
    postobj = await Post.create(**post.dict(exclude_unset=True))
    # Creates a new post entry in the database by converting the Pydantic object to a dictionary.
    return await Post_Pydantic.from_tortoise_orm(postobj)
    # Converts the newly created database post object into a Pydantic model for the response.

@router.get('/post/{id}', response_model=Post_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def get_one_post(id: int):
    # This GET endpoint retrieves a post by its ID. If the book is not found, it returns a 404 error.
    return await Post_Pydantic.from_queryset_single(Post.get(id=id))
    # Retrieves a single post from the database and converts it into a Pydantic model.

@router.put("/post/{id}", response_model=Post_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def update_a_post(id: int, post: PostIn_Pydantic):
    # This PUT endpoint updates a post by its ID. It takes the post data as `PostIn_Pydantic` and updates the database entry.
    await Post.filter(id=id).update(**post.dict(exclude_unset=True))
    # Updates the post entry in the database with the provided fields, skipping unset values.
    return await Post_Pydantic.from_queryset_single(Post.get(id=id))
    # After updating, it fetches the updated post and returns it as a Pydantic model.

@router.delete("/post/{id}", response_model=Message, responses={404: {"model": HTTPNotFoundError}})
async def delete(id: int):
    # This DELETE endpoint deletes a post by its ID. It returns a success message or a 404 error if the book is not found.
    delete_obj = await Post.filter(id=id).delete()
    # Attempts to delete the post by its ID. If the post is not found, `delete_obj` will be 0.
    if not delete_obj:
        raise HTTPException(status_code=404, detail="This post is not found.")
    # If no post is deleted, raise a 404 error with a message.
    return Message(message="Successfully Deleted")
    # If the post is deleted successfully, return a success message.
















































