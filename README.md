
clobot
======

Scrapy project used to scrape men's and women's product items from clothing retailer websites.

Items
======

The items scraped by this project each represent one article of clothing, defined in the class: 
```
clobot.items.ProductItem
```
Spiders
======
This project contains several spiders, each of the spiders are responsible for scraping the product items from their accompanying retailer website.
 
Spider: jcrew
------

The `jcrew_spider` scrapes [J.Crew](https://www.jcrew.com). It is a SitemapSpider meaning that it crawls the pages matching the regex defined within the spider.

Spider: uniqlo
------

The `uniqlo_spider` scrapes [Uniqlo](http://www.uniqlo.com). It is a CrawlSpider, it will crawl all of the pages matching the defined regex.

Spider: mrporter
------
The `mrporter_spider` scrapes [MR PORTER](http://www.mrporter.com). It is a CrawlSpider like `uniqlo_spider`


Usage:
In order to run a spider, run scrapy crawl spidername with a feed export defined. More information on feed export configuration can be found at [Scrapy Feed exports](http://doc.scrapy.org/en/latest/topics/feed-exports.html).

Sample command: 
```
scrapy crawl jcrew -o jcrewitems.json -t json
```

Pipelines
======

ProductItemPipeline
------
Performs basic transformations to get item data from different sources to match such as capitalizing brand names and clothing categories.
