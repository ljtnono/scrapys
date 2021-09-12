

class GithubSearchPageDTO:
    """
    github分页查询DTO对象
    """

    def __init__(self, page_num=1, page_size=10, search_condition=None):
        self.page_num = page_num
        self.page_size = page_size
        self.search_condition = search_condition
