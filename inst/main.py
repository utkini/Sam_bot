import requests
import configparser


conf = configparser.ConfigParser()
conf.read('config.conf')
url = conf['URL_PARAMETERS']['url']
r = requests.get(url)