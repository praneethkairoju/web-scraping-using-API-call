# needed libraries are requesta, csv
import requests
import csv

# web_scraper class
class web_scraper():


  #get_data method is used to get data from website using api
  def get_data(self):
    Base_url = 'https://www.ajio.com/api/category/830303008' # url of the website
    querystring = {"fields":"SITE","currentPage":"0","pageSize":"50","format":"json","query":":relevance","sortBy":"relevance","gridColumns":"3","advfilter":"true"}

    payload = ""
    headers = {"cookie": "V=201"}
    lis1 = []

    
  
    res = requests.request("GET", Base_url, data=payload, headers=headers, params=querystring) # request for get data from website through api

    data_json = res.json() # converting row data to json format fo better usage

    for i in data_json['products']:
      modified_dict = {}
      modified_dict['bname']= i['brandTypeName']
      modified_dict['pname'] = i['name']
      modified_dict['original_mrp'] = i['wasPriceData']['value']
      modified_dict['sale_mrp'] = i['price']['value']
     
      lis1.append(modified_dict)
      k = 0
      for p in data_json['products'][k]['images']:
        lisdist = {}
        lisdist['imgs'] = p['url']
        lis1.append(lisdist)
        k +=1
    
    return lis1 

# discount method is proccess the price as given in the probleam statement

  def discount(self, x):
   
    
    if x<500:
        p = 28/100 * x
        result = x-p
    
    elif 500<x>1000:
        p = 42/100 * x
        result = x-p
        
    elif 2000<x>3000:
        p = 55/100 * x
        result = x-p
        
    elif 3000<x>5000:
        p = 60/100 * x
        result = x-p
        
    elif 5000<x>10000:
        p = 72/100 * x
        result = x-p
        
    else:
        p = 78/100 * x
        result = x-p
    return result  

  def disc_mk(self):
    r = self.get_data()
    for i in r[:0]:
      i['original_mrp'] = i['sale_mrp']
      p = i['sale_mrp']
      i['sale_mrp'] = self.discount(p)
      
    return r
# for creating csv file based on data
  def create_csv(self, data): 
  
    fields = ['bname', 'pname', 'original_mrp', 'sale_mrp', 'imgs']
    filename = 'scrap.csv'

    with open(filename,'w' ) as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=fields)
      writer.writeheader()
      writer.writerows(data)

        
# objects of web_scraper class
data = web_scraper().disc_mk()
final = web_scraper().create_csv(data)

