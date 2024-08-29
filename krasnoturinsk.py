import scrapy


class KrasnoturinskSpider(scrapy.Spider):
    name = "krasnoturinsk"
    allowed_domains = ["krasnoturinsk-ppi.ru"]
    start_urls = ["https://krasnoturinsk-ppi.ru/documents"]

    def parse(self, response):
        documents = response.css("div.list-item a.caption")
        for document in documents:
            document_link = document.css("div.list-item a.caption").attrib['href']
            yield scrapy.Request(url=document_link, callback=self.parse_all_brands)

    def parse_all_documents(self, response):
        name = response.css('div.doc-item h2::text').get().replace('\n', '').replace('\r', '').lstrip().rstrip()
        brand = response.css('td.right::text').get()
        title = response.css('a.product--title::text').get()
        badge = response.css('div.product--badge.badge--newcomer::text').get()
        colors = response.css('div.raw-color-container a::attr(title)').get()
        price = response.css('span.price--content.content--default ::attr(content)').get()
        description = response.css('div.content--short-description font::text').get()
        file_name = ...
        yield {'Наименование': name, 'Номер документа': brand, 'Принят': title, 'Опубликован': badge,
            'Источник': colors, 'Принявший орган': price, 'Номер опубликования': description, 'Имя файла': file_name}

