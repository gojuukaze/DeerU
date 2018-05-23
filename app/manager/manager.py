from django.utils.html import format_html

from app.db_manager.content_manager import get_all_category, get_all_tag, get_category_by_id


def get_category_tree():
    """
    返回分级关系的category list
    {1:{name:xx},2:{ name:xx, children:{3:{name:xx},...} } ,... }
    :return:
    """
    category = get_all_category()
    result = {}
    child_category = {}
    for c in category:
        if c.father_id == -1:
            result[c.id] = {'name': c.name}
        else:
            child_category[c.id] = c
    # 更深的层次
    deep_category = {}
    # 找2级分类
    for k, c in child_category.items():
        if c.father_id in result:
            children = result[c.father_id].get('children', {})
            children[c.id] = {'name': c.name}
            result[c.father_id]['children'] = children
            child_category[c.id] = result[c.father_id]['children'][c.id]
        else:
            # 如果在child_category没有father_id，说明数据库被黑了！！
            if c.father_id in child_category:
                deep_category[c.id] = c

    # 防止死循环，一般应该不会出现的，这里以防万一
    max = 5
    while deep_category and max > 0:
        max -= 1
        for k, c in list(deep_category.items()):
            if isinstance(child_category[c.father_id], dict):
                children = child_category[c.father_id].get('children', {})
                children[c.id] = {'name': c.name}
                child_category[c.father_id]['children'] = children
                child_category[c.id] = child_category[c.father_id]['children'][c.id]

                deep_category.pop(k)

    return result


def get_category_for_choice(category=get_category_tree, deep=0):
    if deep == 0:
        category = get_category_tree()
    choice = []
    for k, v in category.items():
        name = v['name'] if deep == 0 else format_html(
            '%s|%s&nbsp;&nbsp;%s' % ('&nbsp;&nbsp;' * deep, '_' * deep, v['name']))
        choice.append((k, name))
        if 'children' in v:
            choice += get_category_for_choice(v['children'], deep + 1)

    return choice


def get_father_category(category, include_self=False):
    # category = get_category_by_id(category_id)
    if category.father_id == -1:
        return []
    if include_self:
        result = [category]
    else:
        result = []
    father_category = get_category_by_id(category.father_id)

    if father_category:
        result.append(father_category)
    result += get_father_category(father_category)

    return result


def get_tag_for_choice():
    return [t.name for t in get_all_tag()]


def update_one_to_many_relation_model(relation_model, one_id_name, one_id,
                                      many_id_name, new_many_data, get_many_ids_by_data, old_many_ids=[]):
    """
    更新一对多关系的模型

    :param relation_model:
    :param one_id_name:
    :param one_id:
    :param many_id_name:
    :param new_many_data:
    :param get_many_ids_by_data:
    :param old_many_ids:
    :return:
    """
    if not isinstance(old_many_ids, list):
        old_many_ids = list(
            relation_model.objects.filter(**{one_id_name: one_id}).values_list(many_id_name, flat=True))

    new_many_ids = set(get_many_ids_by_data(new_many_data))
    old_many_ids = set(old_many_ids)

    delete_many_ids = list(old_many_ids.difference(new_many_ids))
    add_many_ids = list(new_many_ids.difference(old_many_ids))

    for m_id in add_many_ids:
        relation_model.objects.create(**{one_id_name: one_id, many_id_name: m_id})
    for m_id in delete_many_ids:
        relation_model.objects.get(**{one_id_name: one_id, many_id_name: m_id}).delete()

    return delete_many_ids
