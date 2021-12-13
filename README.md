# web-scraping-using-API-call

It is a Web Scraping project using API call
the Project goal is to basically make a script to scrape some data from the website and process it.

WEBSITE  : 'https://www.ajio.com/api/category/830303008'

Data :  a)      Brand name
        b)      Product name
        c)      Product MRP Price
        d)      Product Sale price*
        e)      Product images links


it just get the data from the website Ajio and perform some logic with the Product Price.

Logic : Changing Discount for the Product according to this given conditions.
            If the Sale price is
                -> Below 500 we will make off 28%
                -> 500-1000 we will make off 42%
                -> 2000-3000 we will make off 55%
                -> 3000-5000 we will make off 60%
                -> 5000-10000 we will make off 72%
                -> 10000 or above we will make off 78%


And save into CSV file