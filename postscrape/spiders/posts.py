import scrapy


class PostsSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ['www.blog.scrapinghub.com']
    start_urls = ['https://www.x23qb.com/book/199102/78262004.html']

    def parse(self, response):
        for post in response.css('div.post-item'):
            yield {
                'title': post.css('.post-header a::text')[0].get(),
                'date': post.css('.post-header a::text')[1].get(),
                'author': post.css('.post-header a::text')[2].get(),
                'comments': post.css('.post-header a::text')[3].get(),
            }
        next_page = response.css('a.next-posts-link::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
