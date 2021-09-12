import scrapy


class SearchListItem(scrapy.Item):
    """
    github搜索页面列表项Item
    """
    namespace = scrapy.Field()
    tag_list = scrapy.Field()
    project_web_url = scrapy.Field()