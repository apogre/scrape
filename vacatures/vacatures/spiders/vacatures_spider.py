from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from vacatures.items import VacaturesItem

class vacaturesSpider(CrawlSpider):
	"""docstring for vacaturesSpider"""
	name = "vacatures"
	start_urls = ['http://www.olympia.nl/Vacatures']
	rules = (Rule(SgmlLinkExtractor(allow=[r'\/V-\d{7}\/[\w\S]+']), callback='parse_item'),
             Rule(SgmlLinkExtractor(allow=[r'\?page\=\d+\&sortCriteria\=1']), follow=True))

	def parse_item(self, response):
		hxs = HtmlXPathSelector(response)
		item = VacaturesItem()
		item['url'] = response.url
		item['job_title'] = hxs.select('//html/body/div[2]/div/div/div[2]/div/article/h1/text()').extract()[0]
		org_desc = hxs.select('//html/body/div[2]/div/div/div[3]/div/section/section/article/div[1]/text()').extract()
		org_desc_list = ''
		for i in range(0,len(org_desc)):
		 org_desc_list += org_desc[i].encode('utf-8')
		item['org_desc'] = org_desc_list
		job_desc = hxs.select('//html/body/div[2]/div/div/div[3]/div/section/section/article/div[2]/text()').extract()
		job_desc_list = ''
		for i in range(0,len(job_desc)):
		 job_desc_list += job_desc[i].encode('utf-8')
		item['job_desc'] = job_desc_list		
		our_offer = hxs.select('//html/body/div[2]/div/div/div[3]/div/section/section/article/div[3]/text()').extract()
		our_offer_list = ''
		for i in range(0,len(our_offer)):
		 our_offer_list += our_offer[i].encode('utf-8')
		item['our_offer'] = our_offer_list		
		we_ask = hxs.select('//html/body/div[2]/div/div/div[3]/div/section/section/article/div[4]/text()').extract()
		we_ask_list = ''
		for i in range(0,len(we_ask)):
		 we_ask_list +=  we_ask[i].encode('utf-8')
		item['we_ask'] = we_ask_list		

		item['full_part_time'] = hxs.select('//html/body/div[2]/div/div/div[3]/div/section/section[2]/div[2]/div/div/div/div/div/strong/text()').extract()[0]
		item['branch'] = hxs.select('//html/body/div[2]/div/div/div[3]/div/section/section[2]/div[2]/div/div/div/div/div/strong/text()').extract()[1]
		item['domain'] = hxs.select('//html/body/div[2]/div/div/div[3]/div/section/section[2]/div[2]/div/div/div/div/div/strong/text()').extract()[2]
		item['employment'] = hxs.select('//html/body/div[2]/div/div/div[3]/div/section/section[2]/div[2]/div/div/div/div/div/strong/text()').extract()[3]
		item['workhour'] = hxs.select('//html/body/div[2]/div/div/div[3]/div/section/section[2]/div[2]/div/div/div/div/div/strong/text()').extract()[4]
		item['work'] = hxs.select('//html/body/div[2]/div/div/div[3]/div/section/section[2]/div[2]/div/div/div/div/div/strong/text()').extract()[5]
		item['salary'] = hxs.select('//html/body/div[2]/div/div/div[3]/div/section/section[2]/div[2]/div/div/div/div/div/strong/text()').extract()[6]
		item['vacature_nr'] = hxs.select('//html/body/div[2]/div/div/div[3]/div/section/section[2]/div[2]/div/div/div/div/div/strong/text()').extract()[7]
		item['place'] = hxs.select('//html/body/div[2]/div/div/div[3]/div/section/section[2]/div[2]/div/div/div/div/div/strong/text()').extract()[8] 

		item['contact_name'] = hxs.select('//html/body/div[2]/div/div/div[3]/div/section/section[2]/div/div/h3/text()').extract()[0]
		item['contact_name1'] = hxs.select('//html/body/div[2]/div/div/div[3]/div/section/section[2]/div/div/span/text()').extract()[0]
		item['contact_number'] = hxs.select('//html/body/div[2]/div/div/div[3]/div/section/section[2]/div/div/div/div/div[2]/strong/text()').extract()[0]

		navpath = hxs.select('//html/body/div[2]/div/div/div/article/div/a/text()').extract()
		navpath_list = ''
		for i in range(0,len(navpath)):
		 navpath_list += navpath[i].encode('utf-8')
		item['navpath'] = navpath_list		

		item['JobId'] = hxs.select('//html/body/div[2]/div/div/div[3]/div/input[1]/@value').extract()[0]
		item['SelectedOffice'] = hxs.select('//html/body/div[2]/div/div/div[3]/div/input[2]/@value').extract()[0]
		item['SelectedOfficeName'] = hxs.select('//html/body/div[2]/div/div/div[3]/div/input[3]/@value').extract()[0]
		item['TopEmployerName'] = hxs.select('//html/body/div[2]/div/div/div[3]/div/input[4]/@value').extract()[0]
		item['TopEmployerCode'] = hxs.select('//html/body/div[2]/div/div/div[3]/div/input[5]/@value').extract()[0]
		
		return item