# KgbScraper

This code contains a Class to define, acquire, and select a set dealer_reviews
from the website: https://www.dealerrater.com/
In particular we will be looking at:
https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685

The script will acquire x pages (5 by default) of dealer reviews and evaluate them based on the following criteria, in order of importance:
  1.  Star rating
  2.  Number of exclamation points used in the review set_text
  3.  Overall length of the review

Either of the .py scripts can be run at the command line or in an IDE.
For ease of execution, I have added the following lines at the end of the KgbScraper.py file:
  scraper = KgbScraper()
  scraper.run()

You may simply run the script in your IDE, or to enter `python KgbScraper.py` on the command line to acquire the desired output
NOTE: You may wish to comment out the lines at the end of KgbScraper.py when running ScrapeTest.py, to avoid executing twice, but is not strictly necessary


Depending on your existing python environment, you may need to do the following steps:
  `pip install html5lib`
  `pip install requests`
  `pip install bs4`


OUTPUT
-----------------------
{
stars:5
exclamations:13
text:Amazing service, knowledge & paid great attention to find me exactly what I needed for my family & situation!!!! Never felt pushed or forced & I knew exactly every detail of every step!! Most definitely worth the drive from Longview to Gladewater!!!! I HOPE Adrian still works for McKaig when the time comes for me to purchase another vehicle!!!
}
{
stars:5
exclamations:7
text:We had been looking for a 2021 Suburban for about 6 months and no one could find exactly what we wanted! We contacted Adrian at McKaig and he told us he could order one for us! Our Suburban was delivered in 4 weeks and had everything on it that we wanted! Adrian, Brandon, Dennis and Freddie all worked with us to get exactly what we wanted! They made phone calls and deals for us right on the spot and we drove out with a beautiful black Suburban! We will definitely use Adrian and McKaig Chevrolet again! Thank you for a fun car buying experience!
}
{
stars:5
exclamations:6
text:Adrian is the best… he helped get everything in order to buy our Jeep and had everything ready when we walked in to the dealership!!! Great experience!!!
}
[Finished in 6.69s]
