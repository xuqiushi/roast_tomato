from models.models import NovelTree


async def find_total_tree(nodes, pre_club: []):
    for node in nodes:
        node["sons"] = []
        pre_club.append(node)
        temp = await NovelTree.find_all(
            where="(parent_id = '%s')" % node.id, orderBy="tree_order ASC"
        )
        if temp:
            await find_total_tree(temp, pre_club[nodes.index(node)]["sons"])