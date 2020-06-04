# encoding:utf-8

from html.parser import HTMLParser

class BeikeParser(HTMLParser):
    def __init__(self):
        super().__init__()
        # 存储中间数据（链家为总房价与单价）
        self.span = ""
        # 小区名称
        self.houseName = []
        # 小区地址
        self.villageName = []
        # 小区介绍
        self.houseNote = []
        # 总价
        self.houseTotlePrice = []
        # 单价
        self.houseUnitPrice = []
        # 房屋链接
        self.houseLink = []
        # 第一张图片
        self.houseImg = []
        # 用于标记数据类型
        self.flag = []
        self.sign = 0

    def feed(self, data):
        super().feed(data)
        # 校验数据个数是否统一
        size = len(self.houseName)
        if len(self.houseName) != size or len(self.villageName) != size or len(self.houseNote) != size \
                or len(self.houseTotlePrice) != size or len(self.houseUnitPrice) != size or len(self.houseLink) != size \
                or len(self.houseImg) != size:
            raise ValueError("数据个数不一致：houseName-" + str(len(self.houseName)) + ",villageName-" + str(len(self.villageName)) +
                             ",houseNote-" + str(len(self.houseNote)) + ",houseTotlePrice-" + str(len(self.houseTotlePrice)) +
                             ",houseUnitPrice-" + str(len(self.houseUnitPrice)) + ",houseLink-" + str(len(self.houseLink)) +
                             ",houseImg-" + str(len(self.houseImg)))
        return self.houseName, self.villageName, self.houseNote, self.houseTotlePrice, self.houseUnitPrice, self.houseLink, self.houseImg

    def handle_starttag(self, tag, attrs):
        if tag == "a" and ("class", "name ") in attrs:
            for attr in attrs:
                if attr[0] == "title":
                    self.houseName.append(attr[1])
                    break
            for attr in attrs:
                if attr[0] == "href":
                    self.houseLink.append("https://bj.fang.ke.com" + attr[1])
                    break
        elif tag == "img" and ("class", "lj-lazy") in attrs:
            for attr in attrs:
                if attr[0] == "data-original":
                    self.houseImg.append(attr[1])
                    break
        elif tag == "a" and ("class", "resblock-location") in attrs:
            for attr in attrs:
                if attr[0] == "title":
                    self.villageName.append(attr[1])
                    break
        elif tag == "a" and ("class", "resblock-room") in attrs:
            self.flag.append("houseNote")
            self.houseNote.append('')
        elif tag == "span" and len(self.flag) > 0 and self.flag[-1] == "houseNote":
            self.flag.append("span")
        elif tag == "i" and ("class", "split") in attrs and len(self.flag) > 0 and self.flag[-1] == "houseNote":
            self.flag.append("span")
        elif tag == "div" and ("class", "main-price") in attrs:
            self.flag.append("housePrice")
            self.houseTotlePrice.append('')
            self.houseUnitPrice.append('')
        elif tag == "span" and len(self.flag) > 0 and self.flag[-1] == "housePrice":
            self.flag.append("span")
        elif tag == "div" and ("class", "second") in attrs:
            self.flag.append("div")
        elif tag == "div" and ("class", "resblock-follow") in attrs and len(self.flag) > 0 and self.flag[-1] == "housePrice":
            self.flag.pop()

    def handle_data(self, data):
        if len(self.flag) != 0:
            if self.flag[-1] == "span" and self.flag[-2] == "houseNote":
                self.houseNote[-1] = self.houseNote[-1] + data.replace(' ','')
                self.flag.pop()
            elif self.flag[-1] == "span" and self.flag[-2] == "housePrice":
                self.houseUnitPrice[-1] = self.houseUnitPrice[-1] + data.replace(' ','')
                self.flag.pop()
            elif self.flag[-1] == "div" and self.flag[-2] == "housePrice":
                self.houseTotlePrice[-1] = self.houseTotlePrice[-1] + data.replace(' ','')
                self.flag.pop()

    def handle_endtag(self, tag):
        if tag == "a" and len(self.flag) > 0 and self.flag[-1] == "houseNote":
            self.flag.pop()
