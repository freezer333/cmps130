# Scientific Programming with 
<img src="../../imgs/python.png"/>
## Programming Exercise 27 - Predicting Rainfall and Droughts

Given all of our rainfall data, we should able to make somewhat meaningful predictions about rainfall in the future, and the likelyhood of severe droughts to occur<sup>*</sup>.

We'll define a severe drought as 12 consecutive months with less than 5% of the average rainfall for that given month (based on the existing data).

1. Calculate the Mean and Standard Deviation for rainfall in each month based on the input file from previous exercises
2. Simulate the next 100 years (starting in January), by creating a random value of rainfall for each month based on a normal distribution.  
<br/>
A random value of rainfall is **not** a completely random value - it is based on the normal distribution curve (see textbook section 12.3.1).  What we want to do is get a random value, but whose average value will be equal to the average rainfall for the given month, and whose variance will follow the standard deviation from step 1.
<br/>
Fortunately, a library that comes with `matplotlib` makes this very easy for us to do!  To get a random value following a normal distribution, make the following function call, where mean and std are the values for the given month that you found in Step 1
<br/>
```
import numpy as np
sample = np.random.normal(mean, std)
```
<br/>

3. Now run a Monte-Carlo simulation where you predict 100 years 100,000 times.  Print out the likelyhood of a severe drought of occuring anytime in the next 100 years (the percentage of simulation runs that had at least one severe drought).


*Note - you might want to make your program a bit flexible, so you can try it with different drought thresholds (percent of mean, and consecutive months).  For example, you could easily figure out how likely it is to have 2 months in a row with exceptionally low (like < 5%) rain!*
<div class="highlight">** Reminder -  ** you learn by *doing* not watching.  Do this program yourself first!  Then watch how I did it!</div>

### Solution Video

### Solution Code
[pe27.py](pe27.py)

<sup>*</sup>We're going to take some liberties in our modeling - there are obviously a lot of underlying parameters that we will ignore!



