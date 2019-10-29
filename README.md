<p align="center">

<img src="https://vignette.wikia.nocookie.net/gravityfalls/images/8/83/Soos_appearance.png/revision/latest?cb=20150915080601" data-canonical-src="soos" width="200" height="380" />
<br>
Are flight tickets really the cheapest on Tuesday mornings?<br>
<a href="https://github.com/aayush4vedi/Aeroplot"><img src="https://img.shields.io/badge/version-0.1-f39f37" alt="Downloads"></a>
<a href="https://github.com/aayush4vedi/Aeroplot"><img src="https://img.shields.io/badge/Made With-python-1abc9c" alt="Downloads"></a>
<a href="https://github.com/aayush4vedi/Aeroplot"><img src="https://img.shields.io/badge/Made With-D3.js-yellow" alt="Downloads"></a>
<a href="https://github.com/aayush4vedi/Aeroplot"><img src="https://img.shields.io/badge/Made With-crontab-orange" alt="Downloads"></a>
<a href="https://github.com/aayush4vedi/Aeroplot"><img src="https://img.shields.io/badge/Made With-<3-red" alt="Downloads"></a>
</p>

# Running Instructions:
* Update flight list in `flights.txt`
* Update flight-data & clense the db : `python autopilot.py`
* Adjust time-period & frequency in `aeroplot.cron`
* Start cron: `crontab aeroplot.cron` :x: | edit crontask with `crontab -e` :white_check_mark:
* Stop cron: `crontab -r`


## Idea
The project started as a bet among my friends when I told my observation about booking flights that they are the cheapest on Tuesday (office-time) mornings. So here I'll try to hypothesize my postulate by collecting data from multiple flight booking services for multiple future flights(holiday & non-holiday both) and analysing it graphically.


## Plan
* Scrape data from multiple booking sites.
* Plot using D3 the following:
    * for day D<sub>i(i:0,N)</sub> :  plot price p<sub>jk(j:1,b; k:1,f)</sub> v/s time t<sub>h(h:0-24)</sub>
        <br>where: 
        * N = number of days I want to make observations
        * b = number of booking sites to take data from
        * f = number of flights I want to observe prices for
        * h = hours of day
    * P<sub>i</sub> = avg(p<sub>ji(j:0,b)</sub>) v/s t<sub>h(h:0-24)</sub> for all days D<sub>i(i:0,N)</sub>
    * Insert other plots here

# Data Selection:
* Cities: Home(Departure time>= 1800):Delhi <-> Work(Departure Time <=0800):Bangalore
* Website: [google flights](www.google.com/flights)
* Day Types: around holiday(holiday just after weekend), normal
* Multiple airlines for one day: select the cheapest flight in set Departure Time

## Flights
* list of flights to be tracked: [text-file](https://github.com/aayush4vedi/Aeroplot/blob/master/flights.txt)
* Airlines: (in decreading order of: Dep. Time > price)
    * Indigo:     6E
    * SpiceJet:   SG
    * AirIndia:   AI
    * GoAir:      G8
* Days Types:
    * Around Holidays:(To be deleted when project gets completed)
        * 2019-10-24 blr->del
        * 2019-10-25 blr->del
        * 2019-11-01 blr->del
        * 2019-11-02 blr->del
        * ----
        * 2019-10-28 del->blr
        * 2019-10-29 del->blr
        * 2019-10-30 del->blr
        * 2019-11-04 del->blr
    * Normal:
        * 2019-10-23 blr->del
        * 2019-10-24 blr->del
        * 2019-11-06 blr->del
        * 2019-11-07 blr->del
        * ----
        * 2019-10-24 del->blr
        * 2019-10-23 del->blr
        * 2019-11-06 del->blr
        * 2019-11-07 del->blr

# Progress & Blockers:
* **Blocker>>** Google Flight: getting empty content on parsing. Maybe some unknown issue
    * **Resolved:** Use Dynamic Web Scraping
* **Automation:** of to-be-tracked-flights data.Python is <3
    * Point of change: `flights.txt` (also copied in README.md)
    * txt -> excel: `autopilot.py`
    * excel file(just for display): `flights.xlsx`
* **Blocker>>** Not enough time for JS to load on page, causes null price value
    * **Resolved:** give it enough (sleep)time to load, also catch the error & assume price hasn't changed from the last hour.
* **Recurring script running :** use `crontab` (a real boon) 
* **Blocker>>** Browser opening every hour on screen is very-very disturbing.
    * **Workarounds:**
        * Minimise the browser window: `driver.set_window_size(0, 0)`
        * :no_entry_sign: Selenium Support DEPRECATED: Use PhantomJS browser: `driver = webdriver.PhantomJS()`
            * It's a discontinued **headless** browser used for automating web page interaction
        * **Solution:** use headless version of Chrome/Firefox
            * **Headless browser ==** normal browser minus any UI component
                ```py
                options = Options()
                options.set_headless(headless=True)
                driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',options=options)
                ```
* Planning to run for a month(23Sep to 23Oct '19) to collect data.Lets see how the project grows with time :) 
* UPDATE on 23Oct'19(a month after):
    - Flight Data successfully fetched.
    - Have difficult time racing with clock to keep laptop open, could have deployd on Heroku etc, next time
    - Some flights got removed from google flight, some threw NULL because of other reasons
* Plan for Plotting:
    - Clean Data:
        - remove f34 & f61 (~50% errors rate)
        - In column: if NULL, copy data in above shell(take care in case of multiple consecutive NULLs) + some rand_num(100,600)
    - Implement D3js



## Conclusion
TODO: TBD//
 

![picture alt](./media/future-plane.png)
> "Oh, ma'am, you really shouldn't teleport when you're pregnant. I'm afraid your only choice is (*whispers*): AIR TRAVEL." <br>@The Simpsons: Holidays Of Future Passed










