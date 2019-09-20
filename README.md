<p align="center">

<img src="https://vignette.wikia.nocookie.net/gravityfalls/images/8/83/Soos_appearance.png/revision/latest?cb=20150915080601" data-canonical-src="soos" width="200" height="380" />
<br>
Are flight tickets really the cheapest on Tuesday mornings?<br>
<a href="https://github.com/aayush4vedi/Aeroplot"><img src="https://img.shields.io/badge/version-0.1-f39f37" alt="Downloads"></a>
<a href="https://github.com/aayush4vedi/Aeroplot"><img src="https://img.shields.io/badge/Made With-python-1abc9c" alt="Downloads"></a>
<a href="https://github.com/aayush4vedi/Aeroplot"><img src="https://img.shields.io/badge/Made With-D3.js-yellow" alt="Downloads"></a>
<a href="https://github.com/aayush4vedi/Aeroplot"><img src="https://img.shields.io/badge/Made With-<3-red" alt="Downloads"></a>
</p>


## Idea
The project started as a bet among my friends when I told my observation about booking flights that they are the cheapest on Tuesday (office-time) mornings. So here I'll try to hypothesize my postulate by collecting data from multiple flight booking services for multiple future flights(holiday & non-holiday both) and analysing it graphically.

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

# Data Selection:
* Home(optimal departure time: early morning):Delhi <-> Work(optimal DT: night):Bangalore
* Websites: makemytrip, ixigo, google flights, paytm
* Day Types: around holiday(holiday just after weekend), normal
* 2 flights per day: cheaper(1) & costly(2) both

## Flights

| ID  | Date       |  Day  |   Day Type      | Flight Number |  From  |   To   |Dep.Time| 
|---- | -----      |  ---- |---------------  | --------------| :----: | :----: | ------ |
| f1  | 27 Sep '19 |  Fri  | Around Holiday  | Indigo-6E2625 |  Blr   |   Del  | 0025   |
| f2  | 27 Sep '19 |  Fri  | Around Holiday  | GoAir -G8518  |  Blr   |   Del  | 2235   |
| f3  | 28 Sep '19 |  Sat  | Around Holiday  | GoAir- G8518  |  Blr   |   Del  | 2235   |
| f4  | 28 Sep '19 |  Sat  | Around Holiday  | SpiceJ-SG6638 |  Blr   |   Del  | 2310   |
| f5  | 3 Oct '19  |  Tue  | Around Holiday  | GoAir-G8113   |  Del   |   Blr  | 0550   |
| f6  | 3 Oct '19  |  Tue  | Around Holiday  | AirIn-AI933   |  Del   |   Blr  | 0510   |
| f7  | 4 Oct '19  |  Fri  | Around Holiday  | Indigo-6E2808 |  Blr   |   Del  | 1930   |
| f8  | 4 Oct '19  |  Fri  | Around Holiday  | SpiceJ-SG6638 |  Blr   |   Del  | 2310   |
| f9  | 7 Oct '19  |  Mon  | Around Holiday  | SpiceJ-SG198  |  Blr   |   Del  | 2045   |
| f10 | 7 Oct '19  |  Mon  | Around Holiday  | Indigo-6E2305 |  Blr   |   Del  | 2125   |
| f11 | 9 Oct '19  |  Wed  | Around Holiday  | Indigo-6E2042 |  Del   |   Blr  | 0545   |
| f12 | 9 Oct '19  |  Wed  | Around Holiday  | GoAir-G8113   |  Del   |   Blr  | 0550   |
| f13 | 24 Oct '19 |  Fri  | Around Holiday  | AirIn-AI587   |  Blr   |   Del  | 2200   |
| f14 | 24 Oct '19 |  Fri  | Around Holiday  | GoAir-G8118   |  Blr   |   Del  | 2055   |
| f15 | 25 Oct '19 |  Fri  | Around Holiday  | GoAir-G8518   |  Blr   |   Del  | 2255   |
| f16 | 25 Oct '19 |  Fri  | Around Holiday  | Indigo-6E2716 |  Blr   |   Del  | 2000   |
| f17 | 29 Oct '19 |  Fri  | Around Holiday  | Indigo-6E5031 |  Del   |   Blr  | 0505   |
| f18 | 29 Oct '19 |  Fri  | Around Holiday  | AirIn-AI933   |  Del   |   Blr  | 0510   |
| f19 | 30 Oct '19 |  Fri  | Around Holiday  | Indigo-6E2701 |  Del   |   Blr  | 0655   |
| f20 | 30 Oct '19 |  Fri  | Around Holiday  | GoAir-G8207   |  Del   |   Blr  | 0500   |
| f21 | 25 Sep '19 |  Wed  |     Normal      | Indigo-6E5031 |  Del   |   Blr  | 0505   |
| f22 | 25 Sep '19 |  Wed  |     Normal      | AirIn-AI851   |  Del   |   Blr  | 0455   |
| f23 | 25 Sep '19 |  Wed  |     Normal      | GoAir-G8518   |  Blr   |   Del  | 2255   |
| f24 | 25 Sep '19 |  Wed  |     Normal      | Indigo-6E2716 |  Blr   |   Del  | 2000   |
| f25 | 10 Oct '19 |  Thu  |     Normal      | SpiceJ-SG8720 |  Blr   |   Del  | 2200   |
| f26 | 10 Oct '19 |  Thu  |     Normal      | GoAir-G8118   |  Blr   |   Del  | 2055   |
| f27 | 10 Oct '19 |  Thu  |     Normal      | Indigo-6E683  |  Del   |   Blr  | 0735   |
| f28 | 10 Oct '19 |  Thu  |     Normal      | GoAir-G82610  |  Del   |   Blr  | 0810   |
| f29 | 7 Nov '19  |  Thu  |     Normal      | Indigo-6E5031 |  Del   |   Blr  | 0505   |
| f30 | 7 Nov '19  |  Thu  |     Normal      | AirIn-AI933   |  Del   |   Blr  | 0510   |
| f31 | 7 Nov '19  |  Thu  |     Normal      | Indigo-6E2484 |  Blr   |   Del  | 2330   |
| f32 | 7 Nov '19  |  Thu  |     Normal      | AirIn-AI610   |  Blr   |   Del  | 1910   |


## Conclusion
TODO: TBD//
 

![picture alt](./media/future-plane.png)
> "Oh, ma'am, you really shouldn't teleport when you're pregnant. I'm afraid your only choice is (*whispers*): AIR TRAVEL." 