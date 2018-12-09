import json
import requests
import csv
import argparse

base_url = "https://web.archive.org/web/"
scraped_data = {}
scraped_data['archived_urls'] = []

def main():
    args = parse_args()
    filepath = args['path']
    limit = args['limit']
    output_type = args['output']
    if not args['from'] and not args['to'] :
        cdx_url = f"http://web.archive.org/cdx/search/cdx?url={args['url']}&fl=timestamp,original&output=json&limit={limit}"
    elif not args['to']:
        cdx_url = f"http://web.archive.org/cdx/search/cdx?url={args['url']}&fl=timestamp,original&output=json&from={args['from']}&limit={limit}"
    elif not args['from']:
        cdx_url = f"http://web.archive.org/cdx/search/cdx?url={args['url']}&fl=timestamp,original&output=json&to={args['to']}&limit={limit}"
    url_response = requests.get(cdx_url)
    archive_json = json.loads(url_response.content)
    for item in range(1, len(archive_json)):
        timestamp = archive_json[item][0]
        original_url = archive_json[item][1]
        url = base_url + timestamp + '/' + original_url
        year = timestamp[:4]
        month = timestamp[4:6]
        day = timestamp[6:8]
        date = year + '-' + month + '-' + day
        scraped_data['archived_urls'].append(
            {
                "url": url,
                "date": date,
                "timestamp": timestamp
            })
    output_file(filepath, output_type)


def output_file(filepath, output_type):
    if output_type == 'json':
        with open(f'{filepath}.json', 'w') as file:
            json.dump(scraped_data, file)
    elif output_type == 'csv':
        with open(f"{filepath}.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['url', 'date', 'timestamp'])
            for item in scraped_data['archived_urls']:
                writer.writerow(item)
    elif output_type == 'html':
        for data in scraped_data['archived_urls']:
            html_data = requests.get(data['url'])
            with open(f"{filepath}_{data['timestamp']}.html", 'wb') as f:
                f.write(html_data.content)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True, help="url for the wayback scraper to scrape. [eg: http://www.example.com")
    parser.add_argument("-l", "--limit",default=0, help=" url limit")
    parser.add_argument("-f", "--from", metavar='Start TIMESTAMP',
                        help="start date, format - YYYYmmddHHMMSS. Example : -f 2011")
    parser.add_argument("-t", "--to", metavar='End TIMESTAMP',
                        help="end date, format - YYYYmmddHHMMSS. Example : -t 201205")
    parser.add_argument("-p", "--path", metavar='DIRECTORY', default='wayback_scraper', help="Output file path")
    parser.add_argument("-n", "--name", metavar='FILENAME', help="filename for the output data")
    parser.add_argument("-o", "--output", metavar='Output type',required=True, choices=['json', 'csv', 'html'], help="output type")

    args = vars(parser.parse_args())
    return args


if __name__ == '__main__':
    main()
