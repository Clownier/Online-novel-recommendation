import requests  # 导入requests包
from bs4 import BeautifulSoup


def getSoupByID(id=None):
    url = 'https://book.qidian.com/info/' + id
    strhtml = requests.get(url)
    soup = BeautifulSoup(strhtml.text, 'lxml')
    return soup


def getFansSoupByID(id=None):
    url = 'https://book.qidian.com/fansrank/' + id
    strhtml = requests.get(url)
    fanssoup = BeautifulSoup(strhtml.text, 'lxml')
    return fanssoup


def getKindBySoup(soup=None):
    data = soup.select(
        'body > div > div.crumbs-nav.center990 > span > a')
    # print(data)
    result = []
    for item in data:
        result += [item.get_text()]
    # print(result[1:3])
    return result[1:3]


def getNameBySoup(soup=None):
    data = soup.select(
        'body > div > div.crumbs-nav.center990 > span > a:nth-child(8)')
    # print(data)
    result = data[0].get_text()
    # print(result)
    return result


def getTagBySoup(soup=None):
    data = soup.select(
        'body > div > div.book-detail-wrap.center990 > div.book-information.cf > div.book-info > p.tag > span')
    # print(data)
    result = []
    for item in data:
        result += [item.get_text()]
    # print(result)
    return result


def getIntroBySoup(soup=None):
    data = soup.select(
        'body > div > div.book-detail-wrap.center990 > div.book-information.cf > div.book-info > p.intro')
    print(data)
    result = data[0].get_text();
    print(result)
    return result


def getNumBySoup(soup=None, cmap=None):
    '''
    unfinish TODO decrypt
    :param soup:
    :param cmap:
    :return:
    '''
    data = soup.select(
        'body > div > div.book-detail-wrap.center990 > div.book-information.cf > div.book-info > p:nth-child(4) > '
        'em:nth-child(1) > span')
    print(data)
    result = data[0].get_text()
    return result


def getFansBySoup(soup=None):
    '''
    TODO unable to get fans
    :param soup:
    :return:
    '''
    # data = soup.select(
    #     'body > div > div.book-detail-wrap.center990 > div.book-content-wrap.cf > div.right-wrap.fr > '
    #     'div.fansRankWrap.mb10  > div > div > div > ul > li:nth-child(1) > div.top-name-box > p > span '
    # )
    data=soup.select('body > div > div.book-detail-wrap.center990 > div.book-content-wrap.cf > div.right-wrap.fr')

    print(data)
    return data


if __name__ == '__main__':
    soup = getSoupByID('2643379')
    # fanssoup = getFansSoupByID('2643379')
    # kind = getKindBySoup(soup)
    # name = getNameBySoup(soup)
    # tag = getTagBySoup(soup)
    # intro = getIntroBySoup(soup)
    # Num = getNumBySoup(soup,cmap)
    fans = getFansBySoup(soup)

# body > div > div.book-detail-wrap.center990 > div.book-information.cf > div.book-info > h1 > em
# url = 'https://book.qidian.com/info/2643379'
# strhtml = requests.get(url)
# soup = BeautifulSoup(strhtml.text, 'lxml')
# data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li > a')
# print(data)
# for item in data:
#     result={
#         'title':item.get_text(),
#         'link':item.get('href'),
#         'content':item.get('title'),
#         'ID':re.findall('\d+',item.get('href'))
#     }
#     print(result)
