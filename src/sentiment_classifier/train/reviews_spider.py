# std
import re

# scrapy
import scrapy

# get review mark
def get_mark(raw_str):
    result = re.findall(r'(\d{3})px', raw_str)
    if len(result) != 0:
        mark = int(result[0])//26
    else:
        result = re.findall(r'(\d{2})px', raw_str)
        mark = int(result[0])//26
        
    if mark <= 3:
        return 0
    else:
        return 1

# get review text
def get_review(review_response):
    review = review_response.xpath('div')
    if len(review) != 0:
        mark = get_mark(review[0].xpath('div/div').extract_first())
        raw_text = ' '.join(review[1].xpath('text()').extract())
        
        review_text = raw_text.replace('\r', '')
        review_text = review_text.replace('Достоинства:', '')
        review_text = review_text.replace('Недостатки:', '')
        review_text = review_text.replace('Комментарий:', '')
        
        return (review_text, mark)
    else:
        return None
        
class ReviewsSpider(scrapy.Spider):
    name = "Mobile reviews parser"

    # request to start
    def start_requests(self):
        try:
            # you can provide filename with "-a urls_to_parse=<filename>"
            urls_to_parse_filename = getattr(
                self, 
                'urls_to_parse', 
                'urls_to_parse.txt'
            )

            with open(urls_to_parse_filename, 'r') as urls_to_parse_file:
                urls = urls_to_parse_file.readlines()

        except Exception as e:
            print(e)
            print('Unable open file with urls to parse')
            raise RuntimeError

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # parse response to get review
    def parse(self, response):
        for element in response.xpath('/html/body/div[1]/div[2]/div[1]/div/div/div[5]/div'):
            review = get_review(element)
            
            yield {
                'review' : review[0],
                'target' : review[1]
            }