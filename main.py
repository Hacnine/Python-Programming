from bs4 import BeautifulSoup
import requests
import csv


def link_builder(link):
    parts = link.split('/')[4]
    parts = parts.split('?')[0]
    # final_link = 'https://www.youtube.com/watch?v=' + parts
    final_link = f"https://www.youtube.com/watch?v={parts}"
    return final_link


# csv_file = open('amazon_islamic_book', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['headline', 'summary', 'video_link'])


source = requests.get('http://amazon.com/s?k=islamic+books&i=stripbooks-intl-ship&crid=AY83UTWZIRZ4&sprefix=Islamic+book%2Caps%2C512&ref=nb_sb_ss_ts-a-p_3_12').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

headline = soup.find('span', class_="a-size-base")
# headline = article.h2.a.text
print(headline)

# for article in soup.find_all('div', class_='class="sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28"'):
#     headline = soup.find('div', class_='a-section a-spacing-none').h2
#     # headline = article.h2.a.text
#     print(headline)
#
#     summary = article.find('div', class_='entry-content').p.text
#     print(summary)
#
#     try:
#         primary_vid_src = article.find('iframe', class_='youtube-player')['src']
#         final_vid_src = link_builder(primary_vid_src)
#
#     except Exception:
#         print(Exception)
#
#     csv_writer.writerow([headline, summary, final_vid_src])
# csv_file.close()
#
# # to grab title
# # article = soup.find('article')
# # article = soup.find('header', class_='entry-header')
# # paragraph = article.h2.a.text
#
# # to grab paragraph
# # article = soup.find('div', class_='entry-content')
# # paragraph = article.p.text
#
# # to grab the youtube link
# # article = soup.find('article')
# # vid_src = article.find('iframe', class_='youtube-player')['src']
# #
# # print(link_builder(vid_src))
#
#
# # to get any sites html and text
# # source = requests.get('https://www.somewhereinblog.net/').text
# #
# # soup = BeautifulSoup(source, 'lxml')
# #
# # print(soup)
#
# # to get any sites text only
# # source = requests.get('https://www.somewhereinblog.net/').text
# #
# # soup = BeautifulSoup(source, 'lxml').text
# #
# # print(soup)
#
