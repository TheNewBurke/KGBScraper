import unittest
import KgbScraper

class ScrapeTest(unittest.TestCase, KgbScraper.KgbScraper):
    scraper = KgbScraper.KgbScraper()
    scraper.run()

    """
    This was my first use of unittest.  I hope these make rational test cases
    """

    def test1_Params(self):
        # Test that default parameters are being set
        self.assertTrue(self.scraper.pages == 5)
        self.assertTrue(self.scraper.number_of_reviews == 3)

    def test2_ReviewAcquisition(self):
        # Test that soup methods acquired 10 reviews per page
        self.assertTrue(len(self.scraper.dealer_reviews) == self.scraper.pages*10)

    def test3_ReviewContentExists(self):
        # Test that each of the dealer review text fields is not empty
        for i in range(0, len(self.scraper.dealer_reviews)):
            self.assertTrue(len(self.scraper.dealer_reviews[i].text) > 0)

    def test4_StarRatingSorting(self):
        # Test that sort methods correctly sorted the reviews relative to each other's stars
        for i in range(0, len(self.scraper.dealer_reviews)-1):
            self.assertTrue(self.scraper.dealer_reviews[i].stars >= self.scraper.dealer_reviews[i+1].stars)

    def test5_ExclamationSorting(self):
        # Test that sort methods correctly sorted the reviews with the same stars, relative to each other's exclamations
        for i in range(0, len(self.scraper.dealer_reviews)-1):
            if (self.scraper.dealer_reviews[i].stars == self.scraper.dealer_reviews[i+1].stars):
                self.assertTrue(self.scraper.dealer_reviews[i].exclamations >= self.scraper.dealer_reviews[i+1].exclamations)

    def test6_TextLengthSorting(self):
        # Test that sort methods correctly sorted the reviews with same ratings and exclamations, next by greater text length
        for i in range(0, len(self.scraper.dealer_reviews)-1):
            if ((self.scraper.dealer_reviews[i].stars == self.scraper.dealer_reviews[i+1].stars) and
            (self.scraper.dealer_reviews[i].exclamations == self.scraper.dealer_reviews[i+1].exclamations)):
                self.assertTrue(len(self.scraper.dealer_reviews[i].text) >= len(self.scraper.dealer_reviews[i+1].text))



if __name__ == '__main__':
    unittest.main()
