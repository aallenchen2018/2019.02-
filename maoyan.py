import requests
from lxml import etree

def getOnePage(n):

    url=f'https://maoyan.com/board/4?offset={n}'

    #告诉服务器,我们是浏览器
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    r=requests.get(url,headers=header)
    return r.text


def parse(text):
    #标准化HTML
    html=etree.HTML(text)
    #提取想要的信息 需要些html语法
    names=html.xpath('//div[@class="movie-item-info"]/p[@class="name"]/a/@title')
    print(names)

text=getOnePage(10)
parse(text)