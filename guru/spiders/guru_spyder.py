from contextlib import nullcontext
from warnings import catch_warnings
import scrapy
from scrapy.loader import ItemLoader

from guru.items import GuruItem

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GuruSpider(scrapy.Spider):
    name = "guru"
    allowed_domains = ["guru.com"]
    start_urls = ['https://www.guru.com/d/freelancers/']

    def parse(self, response):
        self.logger.info('Parse function called on {}'.format(response.url))

        # getting all the freelancers on the page
        freelancers = response.css('p.freelancerAvatar_screenName > a')

        self.logger.info('CYCLING COMPANIES ON THE PAGE')

        for freelancer in freelancers:

            # get freelancer url
            freelancer_guru_url = freelancer.css('a::attr(href)').get()                        

            # go to the freelancer page
            yield response.follow(freelancer_guru_url, self.parse_freelancer)

        # go to Next page with companies
        for a in response.css('li.active + li > a'):                      ##errore qui se non trova l'ultima pagina/non termina
            yield response.follow(a, self.parse)

    def parse_freelancer(self, response):

        path = 'valuetoday\driver\chromedriver.exe'
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(executable_path=path, options=options)

        driver.get(response.request.url)

        # Implicit wait
        driver.implicitly_wait(10)
        # Explicit wait
        wait = WebDriverWait(driver, 10)


        
        # try:
        #     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.field.field--name-node-title.field--type-ds.field--label-hidden.field--item > h1 > a")))
        #     -- = driver.find_elements_by_css_selector("div.field.field--name-node-title.field--type-ds.field--label-hidden.field--item > h1 > a")
        #     -- = --[0].get_attribute('outerText')
        # except:
        #     -- = ''


    
        
        # try:
        #     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.clearfix.col-sm-12.field.field--name-field-freelancer-sub-category-.field--type-entity-reference.field--label-above > div.field--items > div")))
        #     __ = driver.find_elements_by_css_selector("div.clearfix.col-sm-12.field.field--name-field-freelancer-sub-category-.field--type-entity-reference.field--label-above > div.field--items > div")
        #     -- = ""
        #     for s in __:
        #         -- = -- + s.get_attribute('outerText') + ', '
        # except:
        #     -- = ''



        loader = ItemLoader(item=GuruItem(), response=response)
        # loader.add_value('freelancerName', freelancerName)
        # loader.add_value('worldRank', worldRank)
        # loader.add_value('marketValue', marketValue)
        # loader.add_value('annualRevenueUSD', annualRevenueUSD)
        # loader.add_value('headquartersCountry', headquartersCountry)
        # loader.add_value('freelancerBusiness', freelancerBusiness)
        # loader.add_value('businessSector', businessSector)
        # loader.add_value('CEO', CEO)
        # loader.add_value('founders', founders)
        # loader.add_value('foundedYear', foundedYear)
        # loader.add_value('nEmployees', nEmployees)
        # loader.add_value('webSite', webSite)

        yield loader.load_item()