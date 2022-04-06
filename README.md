### Create Scrapy project

1. After creating a python project, install Scrapy plugin.
2. When Scrapy gets installed, run the following commands
   1. ``scrapy startproject vrbodata``
   2. ``cd vrbodata``
   3. ``scrapy genspider vrbo_spider vrbo.com``
3. Inside spiders folder, a spider file created that will do the crwaling tasks.
4. start_urls variable name should remain same but change the url "https://www.vrbo.com/vacation-rentals/beach/usa/florida"
5. As per requirement we need below `items` for each property.
   1. Property name, 
   2. Property Details (Bedroom,Bathroom) 
   3. Property Price, 
   4. Property Image, 
 
6. Here The property data is loaded dynamically through different request. Also, the data is inside Javascript <script> tag as JSON response.
   1. ``Splash``
   2. ``Playwright``
   3. ``BeautifulSoup4`` are the different ways to parse the JSON response from <script> Javascript

### Run scrapy project 
run this command in terminal ``scrapy crawl vrbos``

### Run through shell to render Javascript data
1. scrapy shell "https://www.vrbo.com/vacation-rentals/beach/usa/florida"
2. view(response)  #View Response in a browser
3. If the desired data is hardcoded in JavaScript, you first need to get the JavaScript code: ``response.text``

### Store data to pipeline 
1. Make sure the ``ITEM_PIPELINE`` is uncommented in ``settings.py``
2. Also make sure Mysql workbench is login and mysql server is open