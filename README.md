<p align="center">

<img src="https://vignette.wikia.nocookie.net/gravityfalls/images/8/83/Soos_appearance.png/revision/latest?cb=20150915080601" data-canonical-src="soos" width="200" height="380" />
<br>
Are flight tickets really the cheapest on Tuesday mornings?<br>
<a href="https://github.com/aayush4vedi/Aeroplot"><img src="https://img.shields.io/badge/version-0.1-f39f37" alt="Downloads"></a>
<a href="https://github.com/aayush4vedi/Aeroplot"><img src="https://img.shields.io/badge/Made With-python-1abc9c" alt="Downloads"></a>
<a href="https://github.com/aayush4vedi/Aeroplot"><img src="https://img.shields.io/badge/Made With-javascript-yellow" alt="Downloads"></a>
<a href="https://github.com/aayush4vedi/Aeroplot"><img src="https://img.shields.io/badge/Made With-<3-red" alt="Downloads"></a>
</p>


## Idea
The project started as a bet among my friends when I told my observation about booking flights that they are the cheapest on Tuesday (office-time) mornings. So here I'll try to hypothesize my postulate by collecting data from multiple flight booking services for multiple future flights(holiday & non-holiday both) and analysing it graphically.

![picture alt](./media/future-plane.png)
> "Oh, ma'am, you really shouldn't teleport when you're pregnant. I'm afraid your only choice is (*whispers*): AIR TRAVEL." 
<br>
@The Simpsons: Holidays Of Future Passed

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

## Conclusion
TODO: TBD//
 

![picture alt](./media/future-plane-1.png)
>  If you are seated in an exit row, please hold the door shut for the duration of the flight.


