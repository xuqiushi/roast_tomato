from controller.router_register import get, post
from exceptions import APIPermissionError, APIValueError, APIResourceNotFoundError
from models.models import NovelComments, Novels
from controller.common_controller import get_page_index, Page
from controller.user_controller import check_admin


@get("/api/novel_comments")
async def api_novel_comments(*, page="1"):
    page_index = get_page_index(page)
    num = await NovelComments.find_number("count(id)")
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, novel_comments=())
    novel_comments = await NovelComments.find_all(
        orderBy="created_at desc", limit=(p.offset, p.limit)
    )
    return dict(page=p, novel_comments=novel_comments)


@post("/api/novels/{novel_id}/novel_comments")
async def api_create_novel_comment(novel_id, request, *, content):
    user = request.__user__
    if user is None:
        raise APIPermissionError("Please signin first.")
    if not content or not content.strip():
        raise APIValueError("content")
    novel = await Novels.find(novel_id)
    if novel is None:
        raise APIResourceNotFoundError("Novels")
    novel_comment = NovelComments(
        novel_id=novel.id,
        user_id=user.id,
        user_name=user.name,
        user_image=user.image,
        content=content.strip(),
    )
    await novel_comment.save()
    return novel_comment


@post("/api/novel_comments/{novel_comment_id}/delete")
async def api_delete_novel_comments(novel_comment_id, request):
    check_admin(request)
    c = await NovelComments.find(novel_comment_id)
    if c is None:
        raise APIResourceNotFoundError("NovelComments")
    await c.remove()
    return dict(id=novel_comment_id)