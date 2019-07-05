from controller.router_register import get, post
from controller.common_controller import get_page_index, Page
from models.models import Blog


@get("/api/blog_list")
async def api_blog_list(*, page="1"):
    page_index = get_page_index(page)
    num = await Blog.find_number("count(id)")
    p = Page(num, page_index)
    if num == 0:
        return {"previewBlogList": []}
    blog_list = await Blog.find_all(
        orderBy="created_at desc", limit=(p.offset, p.limit)
    )
    return dict(page=p, blog_list=blog_list)


@get("/api/get_blog_pagination_count")
async def api_blog_pagination_count(*, page_count=1):
    page_count = int(page_count)
    num = await Blog.find_number("count(id)")
    return {"countAll": (num + (page_count - num % page_count)) / page_count}