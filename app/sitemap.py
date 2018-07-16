from app.db_manager.content_manager import filter_article_order_by_id, get_all_category

article_dict = {
    'queryset': filter_article_order_by_id(),
    'date_field': 'modified_time',
}
