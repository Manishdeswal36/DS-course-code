# Eda Steps
- Identify your coloumns 
    - numerical
    - categorical
    - mixed
- Univarite Analysis 
- Bivarite Analysis
- Multivarite Analysis
- Feature enginering -> missing values -> outliers
This cycle continues 

# Univarite 

## Univarite Numerical
### measure of center tendacy
It measures the balacing point in the data
- By Values mean
- By index = median
### measure of dispersion
it measure how spread out is my data from the mean 
- range, max,min
- by values = std,varience
- by index = quartiles ,percentiles



### Distribution shape of data
- it measue the overall pattern . what is the abstract structure in data
- is our observational ,experiment data mathces to famous theortical probabablity model
- like normal,uniform,binomal,exponetial ... etc
- it measures everything  shape 
- 4 moments center tendacy,dispersion,skewness,kurtosis

### Summary
#### Generalaise
we find the general pattern  using
- measure of center tendacy
- measure of dispersion

#### Speaclise
we find the special cases in pattern
- skewness = in which direction is our outlier
    - left skewed
    - right skewed
    - symmertic
- Kurtosis = how much the outlier in that direction

### Data Vislusation
we first make a frequency table and then the frequency distribution
#### histogram
tells you about 
- discreate reprenentation of the data
- shape. mathces expertimental data to theoritcal probability distribution that help you find the abstract repeated structure
- center tendacy = balacing point.mean
- dispersion = spread in data std ,varience
- skewness = in which direction the outleir
- kurtosis = how many outlier in that direction
- range = how much values in that range
- max = max values in data
- min = min values in data 


#### box plot 
it gives you the five number summary which will help you find outlier,center tendency ,dispersion
- max = max index values in the data
- q1 = 25 percentile data values in the data 
- q2 = median 50 percentile index value in the data
- q3 = 75 percentile index value in the data .
- min = minimum index values in the data.

#### kde plot
- continuous representation of data
- we actually done in our histogram 
- shape
- center tendacy
- dispersion
- skewness
- kurtosis
- range
- max
- min
#### violin plot
- combintion of kde plot + box plot
- you see both information by index and by values 
- shape,center tendacy,dispersion,

#### rough plot
- all are zoom out version of the data
- now you see the zoom in version of the data .




## Univarite Categorical
you just count the each cateogroy . and how many times it repeat .
frequency count of it.

### Bar chart
- Table stucture . Cateogory | count
- sort them ranking which is lowest which is higest
### pie chart
- table structure Cateogory | count | percentage
- now all values in same scale and proportion
- you do compariosn and tell what is the contribution of each cateogory
- Ques what is the percentage contribution of X cateogory.
### ecdf chart
- table structure Cateogory | count | percentage | cmf
ecdf

## Bivarite 
study two varibles and relationship between them 
### Numerical Numerical 


#### Scatter plot



### Categorical Numerical

when you do python groupby and apply the agg opration sum,mean,median,max,min,count ..etc
#### bar chart
- normal bar chart
- stack bar chart
- grouped bar chart 

#### pie chart

#### violin chart

#### ecdf chart


#### categorical categorical 
- crosstab
- Heatmap
