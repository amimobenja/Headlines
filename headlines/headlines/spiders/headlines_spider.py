from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import MapCompose, TakeFirst
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from headlines.items import HeadlinesItem

class HeadlineLoader(XPathItemLoader):
	default_item_class = HeadlinesItem
	default_input_processor = MapCompose(lambda x: x.strip())
	default_output_processor = TakeFirst()
	
class HeadlinesSpider(BaseSpider):
	name = "Headlines"
	allowed_domains = ["bloomberg.com"]
	
	start_urls = [
		"http://topics.bloomberg.com/kenya/"
	]
	
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		sites = hxs.select("//div[@id='stories']/ul/li")
		items = []		
		
		for site in sites:
			loader = HeadlineLoader(selector=site)
			loader.add_xpath('description', 'p/text()')
			loader.add_xpath('link', 'h3/a/@href')
			loader.add_xpath('title', 'h3/a/text()')
			items.append(loader.load_item())
		return items






















	
