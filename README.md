# wayback_scraper
Scraping urls from archive.org (Wayback Machine Snapshots)

#Command-Line Interface
The usage information can be printed by running wayback-scraper -h.

    
    usage: wayback-scraper [-h] -u URL [-l LIMIT] [-f Start TIMESTAMP]
                       [-t End TIMESTAMP] [-p DIRECTORY] [-n FILENAME] -o
                       Output type

    optional arguments:
      -h, --help            show this help message and exit
      -u URL, --url URL     url for the wayback scraper to scrape. [eg:
                            http://www.example.com
      -l LIMIT, --limit LIMIT
                            limit the number of results to scrape
      -f Start TIMESTAMP, --from Start TIMESTAMP
                            start date, format - YYYYmmddHHMMSS. Example : -f 2011
      -t End TIMESTAMP, --to End TIMESTAMP
                            end date, format - YYYYmmddHHMMSS. Example : -t 201205
      -p DIRECTORY, --path DIRECTORY
                            Output file path
      -n FILENAME, --name FILENAME
                            filename for the output data
      -o Output type, --output Output type
                            output type


Examples

The usage can be perhaps be made more clear with a couple of concrete examples.
    
        wayback-scraper -u https://www.archive.org -l 2 -f 2011 -t 2012 -n output-o json
which produces:
          
        {
            'archived_urls':
                [
                    'url':'http://www.archive.org:80/',
                    'date':'1997-01-26',
                    'timestamp':'19970126045828'
                ],
                [
                    'url':'http://www.archive.org:80/',
                    'date':'1997-10-01',
                    'timestamp':'19971011050034'
                ]
        }
            
            