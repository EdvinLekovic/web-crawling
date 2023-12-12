from selenium import webdriver
from bs4 import BeautifulSoup
from .apartments_repository import ApartmentsRepository
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
class WebCrawler:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("headless")
        self.options.add_argument('--remote-debugging-port=9222')
        self.options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=self.options,service=ChromeService(ChromeDriverManager().install()))
        self.apartments_repository = ApartmentsRepository()

    def __fetch_page(self, url):
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        return soup

    def __find_n_apartments(self, url, num_apartments):
        soup = self.__fetch_page(url)
        all_apartments = soup.find_all(class_='property ng-scope')

        for page_number in range(2, 500):
            query_param = '?page=' + str(page_number)
            soup = self.__fetch_page(url + query_param)
            apartments = soup.find_all(class_='property ng-scope')
            all_apartments.extend(apartments)
            #print(len(all_apartments))
            if len(all_apartments) == num_apartments:
                break
        return all_apartments

    def __save_apartments(self, url, num_apartments):
        all_apartments = self.__find_n_apartments(url, num_apartments)
        if len(all_apartments) < num_apartments:
            num_apartments = len(all_apartments)
        for i in range(0, num_apartments):
            images = all_apartments[i].find_all('img')
            title = all_apartments[i].find('span',{'class':'name'})
            apartment_object = {'title': title.text}
            images_list = []
            for image in images:
                #select only images that starts with 'http'
                if image['src'][0:4] == 'http':
                    images_list.append(image['src'])

            apartment_object['images'] = images_list
            self.apartments_repository.add_new_apartment(apartment_object['title'], apartment_object['images'])

    def fetch_web_data(self, url, num_apartments):
        if self.apartments_repository.count_apartments() < num_apartments:
            self.apartments_repository.create_apartments_table()
            self.__save_apartments(url, num_apartments)

    def get_all_apartments(self):
        return self.apartments_repository.get_all_apartments()
