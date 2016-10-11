import scrapy

#    start_urls=['http://www.emagister.it/corsi_formazione/web/search/?searchAction=search&segment=corsi_formazione%2F&idsegment=6&p=1&rangoPrecioMax=13&rangoPrecioMin=17&idFiltroDuracionMax=20&idFiltroDuracionMin=10&idCategSeg=2']



class Emagister(scrapy.Spider):
    name = 'emagister'
    #start_urls = ['http://stackoverflow.com/questions?sort=votes']
    start_urls=[]
    for i in xrange(1,123):
        #start_urls.append('http://www.emagister.it/corsi_formazione/web/search/?searchAction=search&segment=corsi_formazione%2F&idsegment=6&p='+str(i)+'&rangoPrecioMax=13&rangoPrecioMin=17&idFiltroDuracionMax=20&idFiltroDuracionMin=10&idCategSeg=2')
        start_urls.append('http://www.emagister.it/web/search/?searchAction=search&segment=&idsegment=1&p='+str(i)+'&rangoPrecioMax=13&rangoPrecioMin=23&idFiltroDuracionMax=20&idFiltroDuracionMin=10&idCategSeg=2')

    def parse(self, response):
        for href in response.css('.course-title-link::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'title':  response.css('h1::text').extract_first(),
            'price': response.css('.price span::text').extract_first(),
            'school':response.css('.course-tarjeton a::text').extract_first(),
            'link_school':response.css('.course-tarjeton a::attr(href)').extract_first(),
            'hours':response.css('.icons-clock-grey-before::text').extract_first(),
            #'votes': response.css('.question .vote-count-post::text').extract_first(),
            #'#body': response.css('.question .post-text').extract_first(),
            #'tags': response.css('.question .post-tag::text').extract(),
            #'link': response.url,
        }
