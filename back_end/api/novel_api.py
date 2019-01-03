import markdown2

from back_end.controller.router_register import get, post
from back_end.exceptions import APIValueError
from back_end.models.models import Novels, NovelComments, NovelTree
from back_end.controller.novel_controller import find_total_tree
from back_end.controller.common_controller import get_page_index, text2html, Page
from back_end.controller.user_controller import check_admin


@get("/api/novels")
async def api_novels(*, page="1"):
    page_index = get_page_index(page)
    num = await Novels.find_number(
        "count(novels_tree.id)",
        where="novel_level = 1",
        inner_join="novels_tree on novels.id = novels_tree.novel_id",
    )
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, novels=())
    novels = await Novels.find_all(
        where="novel_level = 1",
        inner_join="novels_tree on novels.id = novels_tree.novel_id",
        orderBy="created_at desc",
        limit=(p.offset, p.limit),
    )
    return dict(page=p, novels=novels)


@get("/api/novels/{id}")
async def api_get_novel(*, novel_id):
    novel = await Novels.find(novel_id)
    novel_comment = await NovelComments.find_all(where="novel_id = '%s'" % novel_id)
    for c in novel_comment:
        c.html_content = text2html(c.content)
    novel.html_content = markdown2.markdown(novel.content)
    novel.novel_comment = novel_comment
    return novel


@post("/api/novels/{novel_id}")
async def api_update_novel(novel_id, request, *, name, summary, content):
    check_admin(request)
    novel = await Novels.find(novel_id)
    if not name or not name.strip():
        raise APIValueError("name", "name cannot be empty.")
    if not summary or not summary.strip():
        raise APIValueError("summary", "summary cannot be empty.")
    if not content or not content.strip():
        raise APIValueError("content", "content cannot be empty.")
    novel.name = name.strip()
    novel.summary = summary.strip()
    novel.content = content.strip()
    await novel.update()
    return novel


@post("/api/novel_tree/{novel_tree_node_id}")
async def api_update_novel_tree(novel_tree_node_id, request, **kw):
    check_admin(request)
    temp = await NovelTree.find_all(where="novel_id = '%s'" % novel_tree_node_id)
    novel_tree = temp[0]
    if "name" in kw:
        if kw["name"].strip():
            novel_tree.novel_name = kw["name"].strip()
    if "tree_order" in kw:
        novel_tree.tree_order = kw["tree_order"]
    await novel_tree.update()
    return novel_tree


@post("/api/novel")
async def api_create_novel(request, *, name, summary, content):
    check_admin(request)
    if not name or not name.strip():
        raise APIValueError("name", "name cannot be empty.")
    if not summary or not summary.strip():
        raise APIValueError("summary", "summary cannot be empty.")
    if not content or not content.strip():
        raise APIValueError("content", "content cannot be empty.")
    novel = Novels(
        user_id=request.__user__.id,
        user_name=request.__user__.name,
        user_image=request.__user__.image,
        name=name.strip(),
        summary=summary.strip(),
        content=content.strip(),
    )
    await novel.save()
    return novel


@post("/api/novel/tree_point")
async def api_create_novel_tree_point(
    request, *, novel_level, novel_name, parent_id, son_id, tree_order
):
    check_admin(request)
    if not novel_name or not novel_name.strip():
        raise APIValueError("name", "name cannot be empty.")
    novel = Novels(
        user_id=request.__user__.id,
        user_name=request.__user__.name,
        user_image=request.__user__.image,
        name=novel_name,
        summary="",
        content="",
    )
    await novel.save()
    novel_tree = NovelTree(
        novel_id=novel.id,
        novel_level=novel_level,
        novel_name=novel_name,
        parent_id=parent_id,
        son_id=son_id,
        tree_order=tree_order,
    )
    await novel_tree.save()
    return novel_tree


async def find_total_tree_to_delete(nodes, pre_club):
    for node in nodes:
        node["sons"] = []
        pre_club.append(node)
        temp = await NovelTree.find_all(
            where="(parent_id = '%s')" % node.id, orderBy="tree_order ASC"
        )
        if temp:
            await find_total_tree(temp, pre_club)


@post("/api/novels/{novel_id}/delete")
async def api_delete_novel(request, *, novel_id):
    check_admin(request)
    novel_tree_point = await NovelTree.find_all(where="novel_id = '%s'" % novel_id)
    node_to_delete = []
    await find_total_tree_to_delete(novel_tree_point, node_to_delete)
    for temp_point in node_to_delete:
        novel = await Novels.find(temp_point.novel_id)
        novel_tree_point = await NovelTree.find(temp_point.id)
        await novel_tree_point.remove()
        await novel.remove()
    return dict(id=novel_id)


@get("/api/novels_tree/{novel_tree_node_id}")
async def api_get_novels_tree(*, novel_tree_node_id):
    novel_primary_node = await NovelTree.find_all(
        where="novel_id = '%s'" % novel_tree_node_id, orderby="tree_order", limit=1
    )
    novel_second_level_node = await NovelTree.find_all(
        where="(novel_level = 2) and (parent_id = '%s')" % novel_primary_node[0].id,
        orderby="tree_order",
    )
    novel_tree_id = {
        novel_primary_node[0].id: {r.id: None for r in novel_second_level_node}
    }
    novel_tree_name = {
        novel_second_level_node[0].novel_name: {
            r.novel_name: None for r in novel_second_level_node
        }
    }
    for node2 in novel_second_level_node:
        novel_third_level_node = await NovelTree.find_all(
            where="(novel_level = 3) and (parent_id = '%s')" % node2.id,
            orderby="tree_order",
        )
        novel_tree_id[novel_primary_node[0].id][node2.id] = {
            r.id: None for r in novel_third_level_node
        }
        novel_tree_name[novel_primary_node[0].novel_name][node2.novel_name] = {
            r.novel_name: None for r in novel_third_level_node
        }
    return dict(tree_id=novel_tree_id, tree_name=novel_tree_name)


@get("/api/manage_novels")
async def api_manage_novels(*, request, page="1"):
    page_index = get_page_index(page)
    num = await Novels.find_number(
        "count(novels_tree.id)",
        where="novel_level = 1 and user_id = '%s'" % request.__user__.id,
        inner_join="novels_tree on novels.id = novels_tree.novel_id",
    )
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, novels=())
    novels = await Novels.find_all(
        where="novel_level = 1 and user_id = '%s'" % request.__user__.id,
        inner_join="novels_tree on novels.id = novels_tree.novel_id",
        orderBy="created_at desc",
        limit=(p.offset, p.limit),
    )
    return dict(page=p, novels=novels)