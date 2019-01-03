from back_end.controller.router_register import get, post
from back_end.exceptions import APIValueError
from back_end.models.models import Blog
from back_end.controller.common_controller import get_page_index, Page
from back_end.controller.user_controller import check_admin


@get("/api/blog_list")
async def api_blog_list(*, page="1"):
    page_index = get_page_index(page)
    num = await Blog.find_number("count(id)")
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, blog_list=())
    blog_list = await Blog.find_all(
        orderBy="created_at desc", limit=(p.offset, p.limit)
    )
    return dict(page=p, blog_list=blog_list)


@get("/api/blog_list/{blog_id}")
async def api_get_blog(*, blog_id):
    blog = await Blog.find(blog_id)
    return blog


@post("/api/blog_list")
async def api_create_blog(request, *, name, summary, content):
    check_admin(request)
    if not name or not name.strip():
        raise APIValueError("name", "name cannot be empty.")
    if not summary or not summary.strip():
        raise APIValueError("summary", "summary cannot be empty.")
    if not content or not content.strip():
        raise APIValueError("content", "content cannot be empty.")
    blog = Blog(
        user_id=request.__user__.id,
        user_name=request.__user__.name,
        user_image=request.__user__.image,
        name=name.strip(),
        summary=summary.strip(),
        content=content.strip(),
    )
    await blog.save()
    return blog


@post("/api/blog_list/{blog_id}")
async def api_update_blog(blog_id, request, *, name, summary, content):
    check_admin(request)
    blog = await Blog.find(blog_id)
    if not name or not name.strip():
        raise APIValueError("name", "name cannot be empty.")
    if not summary or not summary.strip():
        raise APIValueError("summary", "summary cannot be empty.")
    if not content or not content.strip():
        raise APIValueError("content", "content cannot be empty.")
    blog.name = name.strip()
    blog.summary = summary.strip()
    blog.content = content.strip()
    await blog.update()
    return blog


@post("/api/manage_blog_list/{blog_id}/delete")
async def api_delete_blog(request, *, blog_id):
    check_admin(request)
    blog = await Blog.find(blog_id)
    await blog.remove()
    return dict(id=blog_id)


@get("/api/manage_blog_list")
async def api_manage_blog_list(*, request, page="1"):
    page_index = get_page_index(page)
    num = await Blog.find_number(
        select_field="count(id)", where="user_id = '%s'" % request.__user__.id
    )
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, blog_list=())
    blog_list = await Blog.find_all(
        where="user_id = '%s'" % request.__user__.id,
        orderBy="created_at desc",
        limit=(p.offset, p.limit),
    )
    return dict(page=p, blog_list=blog_list)