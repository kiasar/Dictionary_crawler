import re

import scrapy

# by Peyman (mohsenikiasari@ce.sharif.edu) in 2019.

words = ['I', 'hope', 'you', 'like', 'this', 'dictionary', 'web', 'crawler']

#  scrapy crawl oxford -o oxford.jl
class OxfordCrawler(scrapy.Spider):
    name = "oxford"
    allowed_domains = ["www.lexico.com"]
    start_urls = ["https://www.lexico.com/en/definition/" + word for word in words]

    def parse(self, response):
        word = response.request.url.split("/")[-1]
        definition_dict = {}

        for sections in response.xpath("//section[@class='gramb']"):
            try:
                part_of_speech = sections.xpath(".//span[@class='pos']/text()").extract()[0]
            except:
                part_of_speech = False
            def_list = sections.xpath("./ul/li/div[@class='trg']//span[@class='ind']").extract()
            if not def_list:
                def_list = sections.xpath(".//div[@class='empty_sense']//div[@class='crossReference']").extract()

            def_list = [re.sub(r'<.*?>', "", i).strip() for i in def_list]
            def_list = [i for i in def_list if i]

            if def_list and part_of_speech:
                if part_of_speech in definition_dict:
                    definition_dict[part_of_speech] += def_list
                else:
                    definition_dict[part_of_speech] = def_list

        if definition_dict:
            yield {word: definition_dict}


#  scrapy crawl longman -o longman.jl
class LongmanCrawler(scrapy.Spider):
    name = "longman"
    allowed_domains = ["https://www.ldoceonline.com"]
    start_urls = ["https://www.ldoceonline.com/dictionary/" + word for word in words]

    def parse(self, response):
        word = response.request.url.split("/")[-1]
        definition_dict = {}

        for sections in response.xpath("//span[@class='dictentry']"):
            try:
                part_of_speech = (sections.xpath(".//span[@class='POS']/text()").extract()[0]).strip()
            except:
                part_of_speech = False
            def_list = sections.xpath(".//span[@class='Sense']/span[@class='DEF']").extract()
            def_list = [re.sub(r'<.*?>', "", i[18:-7]).strip() for i in def_list]
            def_list = [i for i in def_list if i]

            if def_list and part_of_speech:
                if part_of_speech in definition_dict:
                    definition_dict[part_of_speech] += def_list
                else:
                    definition_dict[part_of_speech] = def_list

        if definition_dict:
            yield {word: definition_dict}


#  scrapy crawl cambridge -o cambridge.jl
class CambridgeCrawler(scrapy.Spider):
    name = "cambridge"
    allowed_domains = ["https://dictionary.cambridge.org"]
    start_urls = ["https://dictionary.cambridge.org/dictionary/english/" + word for word in words]

    def parse(self, response):
        word = response.request.url.split("/")[-1]
        definition_dict = {}

        for enrty in response.xpath("//div[@class='entry-body__el clrd js-share-holder']"):
            part_of_speeches = enrty.xpath("./div[@class='pos-header']//span[@class='pos']/text()").extract()
            def_list = enrty.xpath(
                ".//div[@class='sense-body']/div[@class='def-block pad-indent']//b[@class='def']").extract()
            def_list = [re.sub(r'<.*?>|:', "", i[15:-4]).strip() for i in def_list]
            def_list = [i for i in def_list if i]

            if def_list and part_of_speech:
                for part_of_speech in part_of_speeches:
                    if part_of_speech in definition_dict:
                        definition_dict[part_of_speech] += def_list
                    else:
                        definition_dict[part_of_speech] = def_list

        if definition_dict:
            yield {word: definition_dict}


#  scrapy crawl webster -o webster.jl
class WebsterCrawler(scrapy.Spider):
    name = "webster"
    allowed_domains = ["https://www.merriam-webster.com"]
    start_urls = ["https://www.merriam-webster.com/dictionary/" + word for word in words]

    def parse(self, response):
        word = response.request.url.split("/")[-1]
        definition_dict = {}

        part_of_speeches = [re.sub(r'\(.*\)', "", i).strip() for i in
                            response.xpath("//span[@class='fl']/a/text()|//span[@class='fl']/text()").extract()]

        for sections in response.xpath("//div[contains(@id, 'dictionary-entry')]/div[@class='vg']"):
            part_of_speech = part_of_speeches.pop(0)
            def_list = sections.xpath(
                ".//span[@class='dtText' or @class='unText'][not(ancestor::span[@class='dtText'])]").extract()
            def_list = [re.sub(r'<span.*>.+</span>', "", i[21:-7]) for i in def_list]
            def_list = [re.sub(r'<.*?>|:', "", i).strip() for i in def_list]
            def_list = [i for i in def_list if i]

            if def_list and part_of_speech:
                if part_of_speech in definition_dict:
                    definition_dict[part_of_speech] += def_list
                else:
                    definition_dict[part_of_speech] = def_list

        if definition_dict:
            yield {word: definition_dict}


#  scrapy crawl collins -o collins.jl
class CollinsCrawler(scrapy.Spider):
    name = "collins"
    allowed_domains = ["https://www.collinsdictionary.com"]
    start_urls = ["https://www.collinsdictionary.com/dictionary/english/" + word for word in words]

    def parse(self, response):
        word = response.request.url.split("/")[-1]
        definition_dict = {}

        for sections in response.xpath("//div[@class='dictionary Cob_Adv_Brit']"
                                       "//div[@class='content definitions cobuild br']/div[@class='hom']"):
            try:
                part_of_speech = (sections.xpath(".//span[@class='pos']/text()").extract()[0]).strip()
            except:
                part_of_speech = False
            def_list = sections.xpath("./div[@class='sense']/div[@class='def']").extract()
            def_list = [re.sub(r'<.*?>', "", i[17:-6]).strip() for i in def_list]
            def_list = [i for i in def_list if i]

            if def_list and part_of_speech:
                if part_of_speech in definition_dict:
                    definition_dict[part_of_speech] += def_list
                else:
                    definition_dict[part_of_speech] = def_list

        if definition_dict:
            yield {word: definition_dict}
