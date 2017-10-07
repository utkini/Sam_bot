import requests
from bs4 import BeautifulSoup

"""Сделать генератор новостей от виладж
1. Взять все новости по бизнесу
2. Взять все новости по людям
3. По городу
4. Еда
5. Стиль
6. Развлечения
"""


class NewsVillageParser(object):
    """Данный класс предназначен для поиска нужных новостей

    """

    def news_in_business(self):
        """Первая новость от Village

        :return: dict : Словарь d[ссылка на новость]= имя новости
        """
        url = 'http://www.the-village.ru/news'

        r = requests.get(url)
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        news = soup.find_all('div', class_='just-bl')
        i = 0
        d = {}
        for new in news:
            i += 1
            link_news = 'http://www.the-village.ru' + new.find('a', class_='post-link').get('href')
            try:
                title = new.find('h2', class_='post-title').text
            except Exception:
                title = new.find('h3', class_='post-title').text
            d[link_news] = str(title)
            if i == 3:
                break
        return d

    def news_in_city(self):
        """Первая новость по городу от Village

        :return: dict : Словарь d[ссылка на новость]= имя новости
        """
        url = 'http://www.the-village.ru/village/city'

        r = requests.get(url)
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        news = soup.find_all('div',class_='post-block-featured-h201')
        i = 0
        d = {}
        for new in news:
            i += 1
            link = 'http://www.the-village.ru' + new.find('a',class_='post-link').get('href')
            text = new.find('h2', class_='post-title').text
            print(link,text, sep=' -> ')
            d[link] = str(text)
        return d


def main():
    n = NewsVillageParser()
    # Тест новости виладж
    # di = n.news_in_business()
    # for d in di:
    #     print(d, di[d])
    city = n.news_in_city()
    print(city)


if __name__ == '__main__':
    main()
