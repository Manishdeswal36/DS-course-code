# Tableau Basic

- importing data
- measure or dimension
- sheets, dashboards and story
- levels of granularity = matlab dimension ka basics par aap measure ka draw kar sakta ho 
deko hamra dataset ma two columns 
state     profit 
haryana 71
delhi       50
up          62
..... 
ab ya repeeat ho aor bhi states .  ya tho ha categorical numerical variable relation
abh har state ma aggreate operation laga kar . total dek sakta ho
profit by state  haryana      delhi         up...
				512     600         812 ....
deko aap lower level par jakar variable ko anlysie kar skata ho 

jaha par aap graphs draw karta ho usa bolta ha worksheet.
sheets ko milo tho banta ha dashboards. . aor dashbaords mila gay tho banyga story. 
tho ek story ka andr multiple dahsboard , and har dashboard ka andr multiples graphs.

Dimension  = categorical variable and measrue is numerical variable 
green color = numerical ,blue color = categorical 

## draw graphs
- Customer Bar chart -> limit to 10
- How to clear
- Categories pi
- Increase size gap
- amount vs profit scatter plot -> remove aggreate.

we make a bar chart of top customers jinhina sabasa jada order place kiya
remember x axis mera columns hota ha aor y axis of graph mera rows hota ha 
customer name as column and order id as rows mera paas ek pivot table ayage .
fir count agg operation usma 

toolkit ma jkar hover ki information change kar sakta ha .

Question konsa customers sa muja sabsa jada profit hota ha 

Always thinking in terms of dimension and measure and ask fundamental 2 question to yourself.
What is Dimension and what is measure.
apka dimension kiya hoga ?
= kis chez ka basis par aap analysis kar raho ho
apka measure kiya hoga 
kiz cheez ko aap analyise kar raha ho.
aor usko measure kasa karoga 

tho pie chart ma category ko hum columns ma dala ga and numerical ko rows ma dala ga

to fit the pie chart use entire view
yadi ek aor level of granutity ya ek aor level ki details add karna chata hu tho

now muja month by month pie chart dekna ha 
create the filter by month . now filter bana nahi usko show karna hota ha . 

you can also change the filter into dropdown ,list ,slider

3.Scatter plot 
between amount and profit
by default tableau perfoem the aggreate operation you have to off it
ya seaborn plotly ma same . 
color scatter plot
bubble plot 

4.Map city chart 
city  or order id ka bitch .
jitna jada bada bubble utna jada order us city sa 



month on month line chart



most probitable subcategory .

## hirecharicl level of grinting 

category ka andr subcategory .
fir uska bar chart amount ka sath and color ma profit

order id ko add label ma karo