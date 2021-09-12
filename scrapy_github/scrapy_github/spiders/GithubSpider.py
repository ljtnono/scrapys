import json
import uuid
import os
import scrapy
from scrapy import Spider


class GithubSpider(Spider):
    """ 
    Github爬虫类
    """
    name = "GithubSpider"
    allowed_domains = ["api.github.com", "github.com"]
    start_urls = ["https://github.com/search"]

    def __init__(self, search_condition=None, page_num=1, page_size=10, *args, **kwargs):
        super(GithubSpider, self).__init__(*args, **kwargs)
        # 配置控制台查询参数
        self.search_condition = search_condition
        self.page_num = page_num
        self.page_size = page_size
        self.start_urls = ["https://github.com/search?q=" + search_condition]

    def parse(self, response, **kwargs):
        li_list = response.css("ul.repo-list li.repo-list-item")
        for li in li_list:
            a = li.css("a.v-align-middle::attr(data-hydro-click)")
            data_hydro_click = json.loads(a.get())
            repository_url = data_hydro_click['payload']['result']['url']
            download_url = repository_url + "/archive/refs/heads/master.zip"
            yield scrapy.Request(url=download_url, callback=self.download_repository)


    def download_repository(self, response, **kwargs):
        """
        下载仓库文件
        :param: reponse 响应
        :return: None
        """
        # 下载文件
        file_name = str(response.headers['Content-Disposition']).split(";")[1][len(" filename="):-1]
        folder = str(uuid.uuid1())
        save_folder = "/Users/lingjiatong/Desktop/github_spider/" + folder
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        with open(save_folder + "/" + file_name, mode='wb+') as f:
            f.write(response.body)
