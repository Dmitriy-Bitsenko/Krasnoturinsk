import scrapy


class KrasnoturinskSpider(scrapy.Spider):
    name = "krasnoturinsk"
    allowed_domains = ["krasnoturinsk-ppi.ru"]
    start_urls = ["https://krasnoturinsk-ppi.ru/documents"]

    def parse(self, response):
        n = 0
        while n < 10000:
            n += 1
            document = f'http://krasnoturinsk-ppi.ru/documents/item/{n}'
            print(document)
            yield scrapy.Request(url=document, callback=self.parse_all_documents)

    def parse_all_documents(self, response):
        name = response.css('div.doc-item h2::text').get().replace('\n', '').replace('\r', '').lstrip().rstrip()
        document_number = response.css('tr.info-item td.right::text').getall()[0]
        accepted = response.css('tr.info-item td.right::text').getall()[1]
        published = response.css('tr.info-item td.right::text').getall()[2]
        source = response.css('tr.info-item td.right::text').getall()[3]
        adopting_agency = response.css('tr.info-item td.right::text').getall()[4]
        publication_number = response.css('tr.info-item td.right::text').getall()[5]
        file_name = response.css('div.file span.caption::text').get()
        yield {'Наименование': name, 'Номер документа': document_number, 'Принят': accepted, 'Опубликован': published,
            'Источник': source, 'Принявший орган': adopting_agency, 'Номер опубликования': publication_number, 'Имя файла': file_name}

#
# next_page = f'http://krasnoturinsk-ppi.ru/documents/item/{n}'
# if next_page is not None:
#     page = next_page
#     yield response.follow(page, callback=self.parse_all_documents)