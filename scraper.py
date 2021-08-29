import requests, csv
from bs4 import BeautifulSoup

#create csv file to save date
csv_file = open('cms_scrape.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'date', 'summary', 'vid_link'])

#scrape part
source_html = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source_html, 'lxml')

main_html = soup.find('main', class_='content')
articles = main_html.find_all('article')


for article in articles:
    title = article.header.h2.a.text
    date = article.header.p.time.text
    summary = article.find('div', class_='entry-content').p.text
    
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('?')[0].split('/')[-1]
        vid_link = f'https://youtube.com/watch?v={vid_id}'
    
    except TypeError:
        #can't find a video for the article
        vid_link = None
        
    csv_writer.writerow([title, date, summary, vid_link])

csv_file.close()
        

