# Aeroplot

![picture alt](./media/future-plane.png)
> "Oh, ma'am, you really shouldn't teleport when you're pregnant. I'm afraid your only choice is (*whispers*): AIR TRAVEL." 
<br>
@The Simpsons: Holidays Of Future Passed

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

## Conclusion
TODO: TBD//
 

![picture alt](./media/future-plane-1.png)
>  If you are seated in an exit row, please hold the door shut for the duration of the flight.


