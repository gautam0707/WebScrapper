import scrapy


class EenaduSpider(scrapy.Spider):
    name = 'eenadu'
    download_delay = 3.0
    start_urls = [
        'http://www.eenadu.net/politics-news/andhra-pradesh-politics-news.aspx?item=ap-politics-news&no=5'
    ]
    allowed_domains = ['www.eenadu.net']

    @staticmethod
    def remove_blanks(string):
        return string.replace('\r\n', ' ').strip()

    def parse(self, response):
        news_body = response.css("body")
        news_block = news_body.css("span[id='PDSAIFullStory']")
        headings = news_block.css("font[size='+3']::text").extract()
        newsdata = news_block.css("font[size='+2']::text").extract()
        image_urls = list(map(lambda x: response.urljoin(x), news_block.css("img::attr(src)").extract()))
        if headings not in ([], None) and newsdata not in ([], None):
            headings = list(map(self.remove_blanks, headings))
            newsdata = list(map(self.remove_blanks, newsdata))

            news_object = {
                "Headings": headings,
                "News": newsdata,
                "image_urls": image_urls,
                "url": response.url
            }
            yield news_object

        new_links = response.css('a::attr(href)').extract()
        if new_links is not None:
            for link in new_links:
                newlink = response.urljoin(link)
                links_to_skip = ['calendar', 'sports', 'movies', 'special-pages',
                                 'social-media', 'magazines']
                if not any([True if i in newlink else False for i in links_to_skip]):
                    yield scrapy.Request(newlink, callback=self.parse)
