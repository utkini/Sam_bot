import requests
from bs4 import BeautifulSoup


class NewsVillageParser(object):
    """Данный класс предназначен для поиска нужных новостей

    """

    def __init__(self):
        url = 'http://www.the-village.ru/village/business'

    # get_html(self):
        r = requests.get(url)
        self.html = r.text

    def news_in_business(self):
        """Первая новость от Village

        :return:
        """
        soup = BeautifulSoup(self.html, 'lxml')
        news = soup.find_all('div', class_='post-item-news')
        i = 0
        d = {}
        for new in news:
            i += 1
            link_news ='http://www.the-village.ru' + new.find('a', class_='post-link').get('href')
            title = new.find('h3', class_='post-title').text
            d[link_news]=str(title)
            if i == 1:
                break
        return d


def main():
    n = NewsVillageParser()
    n.news_in_business()


if __name__ == '__main__':
    main()