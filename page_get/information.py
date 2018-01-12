from config.conf import INFORMATION_LIST_URL, NEWS_CONTENT_URL, PROXIES, HEADER
import requests


def get_information_list(page, page_num):
    data = {"parentModuleID": 4, "moduleList": "10, 44, 45, 46, 47", "page": page, "pagenum": page_num}
    res = requests.post(INFORMATION_LIST_URL, data=data, headers=HEADER, proxies=PROXIES)
    if res.status_code == 200:
        return res.json()


def get_information_content(article_id):

    res = requests.post(NEWS_CONTENT_URL.format(article_id), headers=HEADER, proxies=PROXIES)
    if res.status_code == 200:
        return res.json()

if __name__ == "__main__":
    res = get_information_list(1,1)
    get_information_content(33401)