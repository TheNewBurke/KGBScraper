import requests
from bs4 import BeautifulSoup

class KgbScraper(object):
    """
    KGB Scraper
    @Author: Matthew Newburke

    This code contains a class to define, acquire, and select a set dealer_reviews
    from the website: https://www.dealerrater.com/
    In particular we will be looking at pages of reviews for:
    https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685
    """

    def __init__(self, pages = 5, number_of_reviews = 3):
        # By default the scraper will pull 5 pages of reviews and produce a list of the 3 most extreme comments
        super(KgbScraper, self).__init__()
        self.dealer_reviews = []
        self.pages = pages
        self.number_of_reviews = number_of_reviews

    def __repr__(self):
        return "pages:% s \nnumber_of_reviews:% s \ndealer_reviews:% s" % (self.pages, self.number_of_reviews, self.dealer_reviews)

    def run(self):
        self.dealer_reviews = []
        for page in range(1,self.pages+1):
           for review in self._scrape_page_for_reviews("https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page"+str(page)):
               self.dealer_reviews.append(review)

        for top in self._pull_top_x_reviews():
            #If you want to output only the review text, switch comments to print(top.text) only
            print(top)
            #print(top.text + "\n")

    def _scrape_page_for_reviews(self, URL):
       """
       This function will parse and acquire a star rating, and review text from reviews on www.dealerrater.com
       Parameters:
            ----------
            URL : The address/page# on which to perform a get URL request
       Returns:
            --------
            reviews: list of Review objects
       """
       reviews = []
       r = requests.get(URL)
       soup = BeautifulSoup(r.content, 'html5lib')

       # This div contains the list of reviews for a requested, paginated set of reviews
       table = soup.find('div', attrs = {'id':'reviews'})
       for review_entry in table.findAll('div', attrs = {'class':'review-entry'}):
           review = Review()

           # This div contains a clever class/css handling for 5-star ratings we can use
           for rev5_rating in review_entry.findAll('div', attrs = {'class':'rating-50'}):
               review.set_stars(5)
           for rev4_rating in review_entry.findAll('div', attrs = {'class':'rating-40'}):
               review.set_stars(4)
           for rev3_rating in review_entry.findAll('div', attrs = {'class':'rating-30'}):
               review.set_stars(3)
           for rev2_rating in review_entry.findAll('div', attrs = {'class':'rating-20'}):
               review.set_stars(2)
           for rev1_rating in review_entry.findAll('div', attrs = {'class':'rating-10'}):
               review.set_stars(1)

           # This span contains the actual review text of the dealership
           for rev_content in review_entry.findAll('p', attrs = {'class':'review-content'}):
               review.set_text(rev_content.text)

           reviews.append(review)

       return reviews

    def _pull_top_x_reviews(self):
       """
       This function will sort based on these stars,exclamations, and text length, in that order, and return a list with the x most extreme reviews first

       Returns:
            --------
            the_few_the_extreme: list of top 3 Review objects
       """

       the_few_the_extreme = []
       self.dealer_reviews.sort(key=lambda x: [int(x.stars), int(x.exclamations), len(x.text)], reverse=True)

       for i in range(self.number_of_reviews):
           the_few_the_extreme.append(self.dealer_reviews[i])

       if (len(the_few_the_extreme) == self.number_of_reviews):
           return the_few_the_extreme
       else: return False

class Review(object):
   """
   Review object to hold the number of stars for a review,
   as well as the text, and a method to add up number of !s in the text
   as a measure of the extreme nature of the comment
   """
   def __init__(self, stars=0, exclamations=0, text=''):
       super(Review, self).__init__()
       self.stars = stars
       self.exclamations = exclamations
       self.text = text

   def __repr__(self):
       # Allows print(review) to present an object-style representation of this class
       return "{\nstars:% s \nexclamations:% s \ntext:% s\n}" % (self.stars, self.exclamations, self.text)

   def set_stars(self, x):
       self.stars = x

   def set_text(self, x):
       self.text = x
       self.count_exclamations()

   def count_exclamations(self):
       self.exclamations = self.text.count("!")


scraper = KgbScraper()
scraper.run()
