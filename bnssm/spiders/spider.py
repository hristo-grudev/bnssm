import scrapy

from scrapy.loader import ItemLoader
from ..items import BnssmItem
from itemloaders.processors import TakeFirst


class BnssmSpider(scrapy.Spider):
	name = 'bnssm'
	start_urls = ['https://bns.sm/index.php/category/comunicati/']

	def parse(self, response):
		post_links = response.xpath('//a[@class="continue-reading-link"]/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="entry-content"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=BnssmItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)

		return item.load_item()
