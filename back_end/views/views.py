import markdown2

from controller.router_register import get
from models.models import (
    Blog,
    User,
    NovelTree,
    Novels,
    NovelComments,
    UserPic,
    Comments,
)
from controller.novel_controller import find_total_tree
from controller.common_controller import get_page_index, text2html, Page


# from controller.user_controller import check_admin


@get("/")
async def index(request, *, page="1"):
    # check_admin(request)
    page_index = get_page_index(page)
    num = await Blog.find_number("count(id)")
    page = Page(num, page_index)
    if num == 0:
        blog_list = []
    else:
        blog_list = await Blog.find_all(
            orderBy="created_at desc", limit=(page.offset, page.limit)
        )
    return {
        "__template__": "blog_list.html",
        "page": page,
        "page_index": page_index,
        "blog_list": blog_list,
        "__user__": request.__user__,
    }


@get("/register")
def register():
    return {"__template__": "index.html"}


@get("/signin")
def signin():
    return {"__template__": "index.html"}


@get("/manage/")
def manage():
    return "redirect:/manage/blog_list"


@get("/manage/comments")
def manage_comments(*, request, page="1"):
    return {
        "__template__": "manage_comments.html",
        "page_index": get_page_index(page),
        "__user__": request.__user__,
    }


@get("/manage/blog_list")
def manage_blog_list(*, request, page="1"):
    return {
        "__template__": "manage_blog_list.html",
        "page_index": get_page_index(page),
        "__user__": request.__user__,
    }


@get("/manage/blog_list/create")
def manage_create_blog(request):
    return {
        "__template__": "manage_blog_edit.html",
        "id": "",
        "action": "/api/blog_list",
        "__user__": request.__user__,
    }


@get("/manage/blog_list/edit")
def manage_edit_blog(*, blog_id):
    return {
        "__template__": "manage_blog_edit.html",
        "id": blog_id,
        "action": "/api/blog_list/%s" % blog_id,
    }


@get("/manage/users")
def manage_users(*, request, page="1"):
    return {
        "__template__": "manage_users.html",
        "page_index": get_page_index(page),
        "__user__": request.__user__,
    }


@get("/manage/users/{user_id}/update")
async def manage_users_update(*, user_id):
    user_ls = await User.find_all(where="id = '%s'" % user_id)
    user = user_ls[0]
    return {"__template__": "manage_user.html", "user": user}


@get("/novels")
async def novels_index(request, *, page="1"):
    page_index = get_page_index(page)
    num = await NovelTree.find_number(
        "count(novels_tree.id)",
        where="novel_level = 1",
        inner_join="novels on novels.id = novels_tree.novel_id",
    )
    page = Page(num, page_index)
    if num == 0:
        novels = []
    else:
        novels = await Novels.find_all(
            orderBy="created_at desc",
            where="novel_level = 1",
            inner_join="novels_tree on novels.id = novels_tree.novel_id",
            limit=(page.offset, page.limit),
        )
    return {
        "__template__": "novels.html",
        "page": page,
        "page_index": page_index,
        "novels": novels,
        "__user__": request.__user__,
    }


@get("/novel/{novel_id}")
async def get_novel(*, request, novel_id):
    novel = await Novels.find(novel_id)
    novel_comments = await NovelComments.find_all(
        "novel_id=?", args=[novel_id], orderBy="created_at desc"
    )
    for c in novel_comments:
        c.html_content = text2html(c.content)
    novel.html_content = markdown2.markdown(novel.content)
    return {
        "__template__": "novel.html",
        "novel": novel[0],
        # 'tree_id':novel_tree_id,
        # 'tree_name':novel_tree_name,
        "novel_comments": novel_comments,
        "__user__": request.__user__,
    }


@get("/novel/tree/{novel_id}")
async def get_novel_tree(*, request, novel_id):
    novel = await Novels.find(novel_id)
    novel_comments = await NovelComments.find_all(
        "novel_id=?", args=[novel_id], orderBy="created_at desc"
    )
    for c in novel_comments:
        c.html_content = text2html(c.content)
    novel.html_content = markdown2.markdown(novel.content)
    node_club = []
    novel_primary_node = await NovelTree.find_all(
        where="novel_id = '%s'" % novel_id, orderby="tree_order", limit=1
    )
    await find_total_tree(novel_primary_node, node_club)
    return {
        "__template__": "novel_tree.html",
        "novel": novel,
        "node_club": node_club,
        "novel_comments": novel_comments,
        "__user__": request.__user__,
    }


@get("/manage/novels")
def manage_novels(*, request, page="1"):
    return {
        "__template__": "manage_novels.html",
        "page_index": get_page_index(page),
        "__user__": request.__user__,
    }


@get("/manage/novels/edit")
async def manage_edit_novel(*, novel_id):
    novel = await Novels.find(novel_id)
    novel_comments = await NovelComments.find_all(
        "novel_id=?", args=[novel_id], orderBy="created_at desc"
    )
    for c in novel_comments:
        c.html_content = text2html(c.content)
    novel.html_content = markdown2.markdown(novel.content)
    node_club = []
    novel_primary_node = await NovelTree.find_all(
        where="novel_id = '%s'" % novel_id, orderby="tree_order", limit=1
    )
    await find_total_tree(novel_primary_node, node_club)
    return {
        "__template__": "manage_novel_edit.html",
        "novel": novel,
        "node_club": node_club,
        "id": novel_id,
        "action": "/api/novels/",
    }


@get("/manage/novels/create")
def manage_create_novel(request):
    return {
        "__template__": "manage_novel_edit.html",
        "id": "",
        "action": "/api/novels",
        "__user__": request.__user__,
    }


@get("/manage/novel_comments")
def manage_novel_comments(*, request, page="1"):
    return {
        "__template__": "manage_novel_comments.html",
        "page_index": get_page_index(page),
        "__user__": request.__user__,
    }


@get("/manage/user_pic")
async def manage_user_pic(request, *, page="1"):
    user_id = request.__user__.id
    page_index = get_page_index(page)
    num = await UserPic.find_number(
        select_field="count(id)", where="user_id = '%s'" % user_id
    )
    page = Page(num, page_index)
    if num == 0:
        pics = []
    else:
        pics = await UserPic.find_all(
            where="user_id = '%s'" % user_id,
            orderBy="created_at desc",
            limit=(page.offset, page.limit),
        )
    return {
        "__template__": "manage_user_pic.html",
        "pics": pics,
        "__user__": request.__user__,
        "page": page,
        "page_index": page_index,
    }


@get("/blog/{blog_id}")
async def get_blog(*, request, blog_id):
    blog = await Blog.find(blog_id)
    comments = await Comments.find_all(
        "blog_id=?", args=[blog_id], orderBy="created_at desc"
    )
    for c in comments:
        c.html_content = text2html(c.content)
    blog.html_content = markdown2.markdown(blog.content)
    return {
        "__template__": "blog.html",
        "blog": blog,
        "comments": comments,
        "__user__": request.__user__,
    }
