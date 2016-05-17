import requests
import random
from lxml import etree


URL_LOGIN = 'http://apply.csc.edu.cn/csc/main/person/login/index.jsf'
URL_MAIN = ''


def main():
    s = requests.session()
    headers_for_get = {
        'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
        'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'apply.csc.edu.cn',
        'Connection': 'Keep-Alive',
    }
    get_content = s.get(URL_LOGIN, headers=headers_for_get)
    code = get_headers_and_code(get_content)

    headers = {
        'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
        'Referer': 'http://apply.csc.edu.cn/csc/main/person/login/index.jsf',
        'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Length': 268,
        'Host': 'apply.csc.edu.cn',
        'Connection': 'Keep-Alive',
        'Pragma': 'no-cache',
    }
    data = {
        'mainForm:userName': 'ddmax2',
        'mainForm:registerFlag': '',
        'mainForm:pwd': 'qqq123',
        'mainForm:inputVrfCode': code,
        'mainForm:timeZone': '-8',
        'mainForm:identity': '12103',
        'mainForm:state': '2',
        'mainForm_SUBMIT': '1',
        'mainForm:_idcl': '',
        'jsf_sequence': '2',
        'mainForm:_idJsp1.x': '13',
        'mainForm:_idJsp1.y': '7',
    }

    html = s.post(URL_LOGIN, data=data, headers=headers)
    content = html.content

    status_content = parse(content)
    print(status_content)


def get_headers_and_code(content):
    if content is not None:
        selector = etree.HTML(content.content)
        result = str(selector.xpath(r'//*[@id="mainForm:vrfImg"]/text()')[0])
        print('code is: ' + result)
        return result
    return None


def parse(content):
    if content is not None:
        selector = etree.HTML(content)
        result = str(selector.xpath(r'//*[@id="mainForm:pit6"]/text()'))
        return result
    return None


if __name__ == '__main__':
    main()