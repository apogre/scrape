# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class VacaturesItem(Item):
    url = Field()
    job_title = Field()
    org_desc = Field()
    job_desc = Field()
    our_offer = Field()
    we_ask = Field()
    full_part_time = Field()
    branch = Field()
    domain = Field()
    employment = Field()
    workhour = Field()
    work = Field()
    salary = Field()
    vacature_nr = Field()
    place = Field()
    JobId = Field()
    SelectedOffice = Field()
    SelectedOfficeName = Field()
    TopEmployerName = Field()
    TopEmployerCode = Field()
    navpath = Field()
    contact_name = Field()
    contact_name1 = Field()
    contact_number =Field()



    pass
