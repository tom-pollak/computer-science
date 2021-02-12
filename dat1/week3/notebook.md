---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.10.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region id="rpxHdvCRsrYk" -->
# DATA 1 Practical 2 - Questions

Simos Gerasimou


## Classic Cars & Co

Classic Cars & Co is a UK company that has a large collection of classic cars from the 1980s. 

DataVision (the company you are working as a Data Scientist) has been contracted to analyse the data available for the cars and provide insights by analysing the different characteristics of the cars (e.g., speed, price). 

This Jupyter Notebook will be presented to the Classic Cars & Co main stakeholders who have limited knowledge about data science. So, your findings should be complemented by a suitable justification explaining what you observe and, when applicable, what does this observation mean and, possibly, why it occurs. The analysis along with the explanation will help them to understand whether they need to invest more to expand their collection.
<!-- #endregion -->

<!-- #region id="Hk3xhSRIzz1L" -->
### **Important Information**

(1) To answer these exercises, you **must first read Chapter 2: Introduction to NumPy from the Python Data Science Handbook** (https://jakevdp.github.io/PythonDataScienceHandbook/02.00-introduction-to-numpy.html)


(2) For each question (task) a description is provided accompanied (most of the time) by two cells: one for writing the Python code and another for providing the justification. Feel free to add more cells if you feel they are needed, but keep the cells corresponding to the same question close by.

**Hint 1**: If you find difficulties in solving a task, look at Chapter 2 from the Python Data Science Handbook.

**Hint 2**: Solving each task using NumPy should require less than 10 lines of code
<!-- #endregion -->

<!-- #region id="vX1Wmo8A7Lhm" -->
#### **T1) Explore the dataset and for each column write its name, data type (categorical/numerical - nominal,ordinal,discrete,continuous) and its meaning (i.e., what does it capture?)**

* You may want to open the CSV file using a text editor (e.g., Notepad) or a spreadsheet editor (e.g., Excel)
<!-- #endregion -->

<!-- #region id="cIkkf9Hi_XQb" -->
**Write your answer here (the first is given)**
* Make: Categorical (Nominal) - The model of the car
* ....
<!-- #endregion -->

<!-- #region id="QAMj3BTLz5TJ" -->
### 1) Reading dataset

The classic cars dataset is available on VLE (look for classicCars.csv in the Practicals section)
<!-- #endregion -->

```python id="PMju2Rd-nb6R"
#Using NumPy to read the dataset
import numpy as np
#Define the path to the dataset
data_path = "ClassicCars.csv"
#Define the type of each dataset column. 
#This is needed because NumPy arrays cannot directly read files with different data types
#Hence, we are using Structured arrays. 
#But, we will soon move to Pandas which makes data manipulation easier
types = ['U20', 'U10', 'U5', 'U20', 'U3', 'f4', 'f4', 'f4', 'f4', 'U10', 'i4', 'i4', 'i4', 'i4', 'i4']
#Read the dataset
data = np.genfromtxt(data_path, dtype=types, delimiter=',', names=True)
```

<!-- #region id="2iEJBv9kdIiI" -->
**Structured Arrays**
* Read more about structured arrays:
  * https://jakevdp.github.io/PythonDataScienceHandbook/02.09-structured-data-numpy.html
  * https://numpy.org/doc/stable/user/basics.rec.html
<!-- #endregion -->

<!-- #region id="yHoM-NXN-puT" -->
### Analysing the dataset

<!-- #endregion -->

<!-- #region id="0gqds3bJAfIu" -->
#### **Extracting the column names**
<!-- #endregion -->

```python id="DT1aEd9q0t8-"
data.dtype.names
```

<!-- #region id="vPfhK50f7qEQ" -->
#### **Extracting the shape of the array**
<!-- #endregion -->

```python id="4CkIj9Yq-0a-"
print("The shape of the array is: ", data.shape)
```

<!-- #region id="Fg3CoWGC--_q" -->
#### **T2) What do you see?**
* How many entries does the array have?
* What does each entry include? 
* Hint: Print the elements of an entry

<!-- #endregion -->

<!-- #region id="VIdMJvfD_Otb" -->
**Write your answer here**
205
fueltype, numofdoors etc.
.......
<!-- #endregion -->

<!-- #region id="XhUpJlMf_wV8" -->
#### **Extracting the entries of a column given its name**

* By specifying the name of a column, you can get all the entries within the array for this column (reminder: you are using Structured Arrays)

<!-- #endregion -->

```python id="6QMPnMLo_QwO"
#Print the entries within the 'make' column
print(data['make'])
```

<!-- #region id="yOO8Q7W5A9Cf" -->
#### **T3) Extract the bodystyles within the dataset**

<!-- #endregion -->

```python id="O18vqYhL0_91"
#Write your answer here
data['bodystyle']
```

<!-- #region id="bIcT8mO1gIca" -->
### How do the car prices look like?

<!-- #endregion -->

<!-- #region id="yDfhYbopgUZ6" -->
#### **T4) Calculate the range of car prices for the entire dataset**

<!-- #endregion -->

```python id="QQcVX89v9uZ3"
#Write your answer here
np.max(data['price']) - np.min(data['price'])
```

<!-- #region id="KpIcl1T0kpIS" -->
#### **T5) Calculate the min, max, mean and median prices of the cars**

<!-- #endregion -->

```python id="KAm74_4ShDA_"
#Write your answer here
np.min(data['price']), np.max(data['price']), np.mean(data['price']), np.median(data['price'])
```

<!-- #region id="HCy66heJlRw9" -->
#### **T6) Considering the values calculated above, what insights can you extract? Where do you think the majority of car prices will be clustered?**

<!-- #endregion -->

<!-- #region id="DcaTJEKIlroR" -->
**Write your answer here**
the cars are distributed fairly evenly throughout the range of values as the mean and median
.......
<!-- #endregion -->

<!-- #region id="fAjvb8alhtHm" -->
#### **T7) Write code to calculate the standard deviation for the car prices. Then use the corresponding NumPy function to confirm the correctness of your calculation**


<!-- #endregion -->

```python id="JDwSTd5Zggg_"
#Write your answer here
np.std(data['price'])
```

<!-- #region id="W7tcuWdtnZGV" -->
#### **T8) Find the details of cars with the smallest and largest car volumes**
* Hint: see how to calculate the volume of a car https://info.japanesecartrade.com/content-item/297-what-is-m3-cubic-meter-size-of-a-vehicle

<!-- #endregion -->

```python id="mXdzNLqnhfQX"
#Write your answer here
volumes = np.prod([data['width'], data['height'], data['length']], axis=0)
print(data[np.argmin(volumes)])
print(data[np.argmax(volumes)])
```

<!-- #region id="cmck40GQqfoR" -->
#### **T9) Find the different types of bodystyles for the cars in the dataset**

* Hint: You may want to check: https://numpy.org/doc/stable/reference/generated/numpy.unique.html
<!-- #endregion -->

```python id="DeTMBSCJp3gD"
#Write your answer here
np.unique(data['bodystyle'])
```

<!-- #region id="BXF8kjW-sJaq" -->
#### **T10) Find the number of different car *brands* (makes)**

<!-- #endregion -->

```python id="zJTWSXxrsJE3"
#Write your answer here
np.unique(data['make']).size
```

<!-- #region id="h4Ab2ovntRV-" -->
#### **T11) Find the engine size and the horsepower for the most and least efficient cars when driven in the city and the highway (i.e., the cars with the smallest and largest difference in fuel consumption when driven in the city and the highway)**
<!-- #endregion -->

```python id="fzzrezV8rQ3O"
#Write your answer here
mpg_diff = np.subtract(data['highwaympg'], data['citympg'])
most_effiecent = np.argmin(mpg_diff)
least_effiecent = np.argmax(mpg_diff)
print(data[most_effiecent]['enginesize'], data[most_effiecent]['horsepower'])
print(data[least_effiecent]['enginesize'], data[least_effiecent]['horsepower'])
```

<!-- #region id="Er9o39z8xge3" -->
#### **T12) Find the make with the largest number of cars and how many they are**
<!-- #endregion -->

```python id="pWyEz0bTueot"
#Write your answer here
car_makers = np.unique(data['make'], return_counts=True)
i = np.argmax(car_makers[1])
print(car_makers[0][i], car_makers[1][i])
```

<!-- #region id="Kmy1NtyW0tzm" -->
#### **T13) Find how many cars have a wheel base greater than 100**

* Hint: See https://jakevdp.github.io/PythonDataScienceHandbook/02.06-boolean-arrays-and-masks.html
<!-- #endregion -->

```python id="ZG-vBKvjxrR7"
#Write your answer here
mask = (data['wheelbase'] > 100)
np.count_nonzero(mask)
```

<!-- #region id="t3-PcX9C4VLi" -->
#### **T14) Find if there are any convertible cars that cost less than £15000**

* Hint: See https://jakevdp.github.io/PythonDataScienceHandbook/02.06-boolean-arrays-and-masks.html
<!-- #endregion -->

```python id="CkVfwmoG4ewY"
#Write your answer here
np.any((data['bodystyle'] == 'convertible') & (data['price'] < 15000))
```

<!-- #region id="ywJYQraH1onP" -->
#### **T15) Calculate the interquartile range for the price of all cars**
<!-- #endregion -->

```python id="8M9_FnENyWWU"
#Write your answer here
quartiles = np.percentile(data['price'], [25, 75])
quartiles[1] - quartiles[0]
```

<!-- #region id="K81ZLhTh2jyc" -->
#### **T16) Calculate the 50th percentile range for the horsepower of all cars. Which value is the 50th percentile equal to?**
<!-- #endregion -->

```python id="q1QNhunw2Lnr"
#Write your answer here
# median
np.percentile(data['price'], 50)
```

<!-- #region id="GporTyn66Rkz" -->
### Ideas for practicing further at home

* Find the engine and horsepower of 4wd cars
* Find whether diesel or gas cars are more efficient in the city/highway
* Any other analysis that you might could generate some useful insight.

<!-- #endregion -->
