from urllib import request

goog_url = "https://www.sample-videos.com/csv/Sample-Spreadsheet-1000-rows.csv"


def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'WebScrape.csv'
    fw = open(dest_url, "w")
    for line in lines:
        fw.write(line + '\n')
    fw.close()
    print("Web Scraping completed!")


download_stock_data(goog_url)
