# -*- coding: utf-8 -*-


import requests
from cps.services.Metadata import Metadata

class Google(Metadata):
    __name__ = "豆瓣"
    __id__ = "douban"
    __url__ = "http://192.168.1.90:8085"

    def search(self, query, __):
        if self.active:
            val = list()
            result = requests.get(self.__url__ + "/v2/book/search?q="+query.replace(" ","+"))
            for r in result.json()['books']:
                v = dict()
                v['id'] = r['id']
                v['title'] = r['title']
                v['authors'] = r.get('author', [])
                v['description'] = r.get('summary', "")
                v['publisher'] = r.get('publisher', "")
                v['publishedDate'] = r.get('pubdate', "")
                v['tags'] = [i["name"] for i in r.get('tags')] if r.get('tags') else []
                if r.get('rating'):
                    rating = float(r.get('rating').get('average')) / 2.0
                else:
                    rating = 0
                v['rating'] = rating
                if r.get('image'):
                    v['cover'] = r['image']
                else:
                    v['cover'] = "/../../../static/generic_cover.jpg"
                v['source'] = {
                    "id": self.__id__,
                    "description": "豆瓣图书",
                    "link": "https://book.douban.com/"}
                v['url'] = self.__url__ + "/v2/book/" + r['id']
                val.append(v)
            return val


