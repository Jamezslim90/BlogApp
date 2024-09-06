from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from tortoise.contrib.fastapi import register_tortoise
from app.routers import blog_routes
from fastapi.responses import HTMLResponse


app = FastAPI()


# Mount static files
# app.mount("/static", StaticFiles(directory="/static"), name="static")

# Jinja2 templates
# templates = Jinja2Templates(directory="/templates")

# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return templates.TemplateResponse("home.html", {"request": request})

# Include routers
app.include_router(blog_routes.router)

# Register Tortoise ORM
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
