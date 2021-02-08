from urllib.request import urlopen
from bs4 import BeautifulSoup
import wget


def get_images_from_yahoo(search: str, img_count: int = 5):
    url = (
        f"https://images.search.yahoo.com/search/images;_ylt=AwrExl85jiFgsm8A7KSLuLkF;_ylc=X1MDOTYwNTc0ODMEX3IDMgRmcgMEZ3ByaWQDa1hhdW9oRExTSy4xU0pKVkwuVzNiQQRuX3N1Z2cDMTAEb3JpZ2luA2ltYWdlcy5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDBHFzdHJsAzQEcXVlcnkDY2F0cwR0X3N0bXADMTYxMjgxMTgzNw--?fr2=sb-top-images.search&p={search}&ei=UTF-8&iscqry=&fr=sfp")
    link = urlopen(url)
    soup = BeautifulSoup(link, 'html.parser')
    images = soup.find_all('img')
    print(images)
    count = 0
    img_links = []
    for item in images:
        try:
            print(item['src'])
            count = count + 1
            print(count)
            img_links.append(item['src'])
            if count > img_count:
                break
        except KeyError:
            print('could not find src')

    return img_links


def download_links(links: [], img_disc: str):
    print('Beginning to download images!')
    print(links)
    img_num = 0
    while img_num < len(links):
        for link in links:
            print(link)
            url = str(link)
            print(url)
            wget.download(url, f'C:\\Users\Ferni\\OneDrive\\Desktop\\Tests\\{img_disc}_{img_num}.jpg')
            img_num = img_num + 1
            print(img_num)
    else:
        print('all done from downloading')
