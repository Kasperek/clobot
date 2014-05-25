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

jcrew
------
The `jcrew_spider` scrapes [J.Crew](https://www.jcrew.com). It is a SitemapSpider meaning that it crawls the pages matching the regex defined within the spider.

mrporter
------
The `mrporter_spider` scrapes [MR PORTER](http://www.mrporter.com). It is a CrawlSpider, it will crawl all of the pages matching the defined regex.

uniqlo
------
The `uniqlo_spider` scrapes [Uniqlo](http://www.uniqlo.com). It is a CrawlSpider like `mrporter_spider`.

Pipelines
======
InvalidPipeline
------
A pipeline for filtering out items that do not contain the minimum required data.

SanitizationPipeline
------
A pipeline for sanitizing items by removing html and converting encoding to ascii as well as other various other vanity changes.

Usage
======
In order to run a spider, run scrapy crawl spidername with a feed export defined. More information on feed export configuration can be found at [Scrapy Feed exports](http://doc.scrapy.org/en/latest/topics/feed-exports.html).

Sample command running the `jcrew_spider`and exporting output to jcrewitems.json in json format: 
```
scrapy crawl jcrew -o jcrewitems.json -t json
```

Sample output:
```
{"category": "MENS", "name": "484 selvedge jean in raw indigo", "url": "https://www.jcrew.com/mens_category/pants/Denim/PRDOVR~18975/18975.jsp", "image": ["https://s7.jcrew.com/is/image/jcrew/18975_WO6473_m?$pdp_fs418$"], "color": "", "brand": "J.CREW", "description": "Our slimmest fit yet, for guys who like their denim slim, not skinny. This is the 484 for the denim purist: It's made from genuine raw indigo selvedge cotton woven at one of Japan's oldest and most renowned mills. For those not in the know, raw denim (also called \"rigid\" or \"dry denim\") feels stiffer at first and then fades and distresses according to the individual wearer; in other words, these are as authentic as it gets. Sits below waist.Extra slim through hip and thigh, with our narrowest leg.14\" leg opening (based off size 32/32).Selvedge cotton.Button fly.Traditional 5-pocket styling.Machine wash.Import.Since these are indigo dyed, they're prone to crocking, or color transfer, so wear (and wash) them with dark colors till they're worn in."},
```

