from contextlib import nullcontext
from warnings import catch_warnings
import scrapy
from itemloaders import ItemLoader

from guru.items import GuruItem

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GuruSpider(scrapy.Spider):
    name = "guru"
    allowed_domains = ["guru.com"]
    start_urls = ['https://www.guru.com/d/freelancers/c/programming-development/sc/web-development-design/']

    def parse(self, response):
        self.logger.info('Parse function called on {}'.format(response.url))

        # getting all the freelancers on the page
        freelancers = response.css("div.avatarinfo > h3 > a")

        self.logger.info('CYCLING COMPANIES ON THE PAGE')
        self.logger.info(len(freelancers))

        for freelancer in freelancers:

            # get freelancer url
            freelancer_guru_url = freelancer.css('a::attr(href)').get()
            # go to the freelancer page
            yield response.follow(freelancer_guru_url, self.parse_freelancer)

        # go to Next page with companies
        for a in response.css('li.active + li > a'):                      ##errore qui se non trova l'ultima pagina/non termina
            yield response.follow(a, self.parse)

    def parse_freelancer(self, response):

        path = 'guru/driver/chromedriver'
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-extensions")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')
        #driver = webdriver.Chrome(executable_path=path, options=options)

        driver.get(response.request.url)

        # Explicit wait
        wait = WebDriverWait(driver, 0.3)


        
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1 > strong")))
            name = driver.find_elements_by_css_selector("h1 > strong")
            name = name[0].get_attribute('outerText')
        except:
            name = ''
        
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.profile-avatar__info__location > span:nth-child(2)")))
            country = driver.find_elements_by_css_selector("p.profile-avatar__info__location > span:nth-child(2)")
            country = country[0].get_attribute('outerText')
        except:
            country = ''

        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#feedback-percent > strong ")))
            rating = driver.find_elements_by_css_selector("#feedback-percent > strong ")
            rating = rating[0].get_attribute('outerText')
        except:
            rating = ''

        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#freelancer-details > div.p-box.p-identity > div:nth-child(2) > dl > dd:nth-child(2)")))
            all_time_earnings = driver.find_elements_by_css_selector("#freelancer-details > div.p-box.p-identity > div:nth-child(2) > dl > dd:nth-child(2)")
            all_time_earnings = all_time_earnings[0].get_attribute('outerText')
        except:
            all_time_earnings = ''

        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#freelancer-details > div.p-box.p-identity > div:nth-child(2) > dl > dd:nth-child(6)")))
            number_of_employers = driver.find_elements_by_css_selector("#freelancer-details > div.p-box.p-identity > div:nth-child(2) > dl > dd:nth-child(6)")
            number_of_employers = number_of_employers[0].get_attribute('outerText')
        except:
            number_of_employers = ''

        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#freelancer-details > div.p-box.p-identity > div:nth-child(2) > dl > dd:nth-child(10)")))
            member_since = driver.find_elements_by_css_selector("#freelancer-details > div.p-box.p-identity > div:nth-child(2) > dl > dd:nth-child(10)")
            member_since = member_since[0].get_attribute('outerText')
        except:
            all_time_earnings = ''

        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#visit-website")))
            website = driver.find_elements_by_css_selector("#visit-website")
            website = website[0].get_attribute('href')
        except:
            website = ''

        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#aboutUs > div > p:nth-child(2)")))
            description = driver.find_elements_by_css_selector("#aboutUs > div > p:nth-child(2)")
            description = description[0].get_attribute('outerText')
        except:
            description = ''
        
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#topSkills > li")))
            skills = driver.find_elements_by_css_selector("#topSkills > li")
            guru_skills = ""
            for s in skills:
                guru_skills = guru_skills + s.get_attribute('outerText') + ', '
        except:
            guru_skills = ''

        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ctl00_guB_ucProfileOverview_divServicesList > div > div > ul > li > div > div.serviceListing__details > h2 > a > span")))
            services = driver.find_elements_by_css_selector("#ctl00_guB_ucProfileOverview_divServicesList > div > div > ul > li > div > div.serviceListing__details > h2 > a > span")
            guru_services = ''
            for s in services:
                guru_services = guru_services + s.get_attribute('outerText') + ', '
        except:
            guru_services = ''

        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.serviceListing__rates")))
            prices_per_hour = driver.find_elements_by_css_selector("p.serviceListing__rates")
            guru_avg_price_per_hour = 0
            for p in prices_per_hour:
                price = p.get_attribute('outerText').split()[0]
                price = int(price[1:-3])
                self.logger.info(price)
                guru_avg_price_per_hour = guru_avg_price_per_hour + price
            guru_avg_price_per_hour = guru_avg_price_per_hour / len(prices_per_hour)
        except:
            guru_avg_price_per_hour = 0
            

        loader = ItemLoader(item=GuruItem(), response=response)
        loader.add_value('name', name)
        loader.add_value('country', country)
        loader.add_value('rating', rating)
        loader.add_value('number_of_employers', number_of_employers)
        loader.add_value('member_since', member_since)
        loader.add_value('website', website)
        loader.add_value('description', description)
        loader.add_value('guru_skills', guru_skills)
        loader.add_value('guru_services', guru_services)
        loader.add_value('guru_avg_price_per_hour', str(guru_avg_price_per_hour))

        yield loader.load_item()