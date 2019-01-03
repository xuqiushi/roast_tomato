from back_end.controller.router_register import get, post
from back_end.exceptions import APIPermissionError, APIValueError, APIResourceNotFoundError
from back_end.models.models import Comments, Blog
from back_end.controller.common_controller import get_page_index, Page
from back_end.controller.user_controller import check_admin


@get("/api/comments")
async def api_comments(*, page="1"):
    page_index = get_page_index(page)
    num = await Comments.find_number("count(id)")
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, comments=())
    comments = await Comments.find_all(
        orderBy="created_at desc", limit=(p.offset, p.limit)
    )
    return dict(page=p, comments=comments)


@post("/api/blog_list/{comment_id}/comments")
async def api_create_comment(comment_id, request, *, content):
    user = request.__user__
    if user is None:
        raise APIPermissionError("Please signin first.")
    if not content or not content.strip():
        raise APIValueError("content")
    blog = await Blog.find(comment_id)
    if blog is None:
        raise APIResourceNotFoundError("Blog")
    comment = Comments(
        blog_id=blog.id,
        user_id=user.id,
        user_name=user.name,
        user_image=user.image,
        content=content.strip(),
    )
    await comment.save()
    return comment


@post("/api/comments/{comment_id}/delete")
async def api_delete_comments(comment_id, request):
    check_admin(request)
    c = await Comments.find(comment_id)
    if c is None:
        raise APIResourceNotFoundError("Comments")
    await c.remove()
    return dict(id=comment_id)