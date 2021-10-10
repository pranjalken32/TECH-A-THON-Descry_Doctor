# TECH-A-THON
This project was built under the event “TECH-A-THON” organised by the ECE Society of BIT Mesra. The event “TECH-A-THON” was a 5-week long event in which the project belongs to the Domain- Machine Learning/AI.
*********************************************************************************************
# Descry Dcotor
### Theme:- Health and Safety
*********************************************************************************************
### Problem Statement/Objective: 
Nowadays people are sceptical about their health, they prefer being treated by the best doctor. Often, we are doubtful of being treated by the best doctor and here comes the need for a second opinion from someone better. Finding the ‘better’ nearby to you is a tough task.<br/>
### The reason behind selecting this project? 
The motivation behind choosing this theme and the project was to handle the real-life problem of getting a second opinion and predicting the best doctor. The healthcare sector and ML can bring new reforms to society.
### Solution To the Problem/Objective Stated:
ML model to work on with data set of doctors profile that contains fields such as doctor's experience, specialisation, achievements, location of the clinic and based on this we will ask the user to input certain data fields to predict the best/better doctor in that location (if any).
********************************************************
### Description Of the Project: (Unsupervised Learning)
#### Web Scraping
The first step was to scrape the data of doctors profile from https://www.vaidam.com/doctors/india by web scraping using python as no data set was readily available according to our requirements.<br/>
#### About the data set
The data set obtained contains 5526 entries with data fields as Name, Specialisation, City, Hospital/Clinic address, Experience and Awards.<br/>
#### Reading the data,cleaning, manipulation.
The second step was to read the CSV file obtained and convert it into a data frame using python library Pandas. <br/>
Then we used NumPy for data manipulation, cleaning of data and dropping non-essential data from the data frame by dropping the respective field. Mainly dropping the entries with Nan values. <br/>
#### Predicition
The next step was to use the scikit learn package to normalise(experience,awards) the data and Kmeans for the prediction, also matplotlib was used for graphs and mathematical uses, such as the Elbow method and scatter plot graph. <br/>
#### The Finale
The final part prints the best/better Doctor in the user's area according to the input, the input field contains the value as Name, Specialisation, City, Experience, Awards in the respective order.<br/>
************************************************************************************************
## Technologies used:
1. Python for Web scrapping and obtaining data set.<br/>
2. Pandas for importing data set from file format comma-separated values.(in our case "data.csv") <br/>
3. Numpy for data cleaning , we have dropped the entries with Nan values and dropped the fileds that are no relevant for us.(in our case dropna.)
4. from sklearn.preprocessing we have imported MinMaxScaler.(We have used it to normalise the Experience and Awards column.)
5. from matplotlib we have imported pyplot for graphs for visualisation of data and implementing Elbow method for best pick of cluster.(We have used it for scatter plot and SSE vs Kmeans graph)<br/>
6. Finally Kmeans for our ML model ,abelling our data set and predicitng.
************************************************************************************************
## Some useful theories
K-means clustering is a type of unsupervised learning, which is used when you have unlabeled data (i.e., data without defined categories or groups). The goal of this algorithm is to find groups in the data, with the number of groups represented by the variable K. The algorithm works iteratively to assign each data point to one of K groups based on the features that are provided. Data points are clustered based on feature similarity.<br/>
Elbow Method-A fundamental step for any unsupervised algorithm is to determine the optimal number of clusters into which the data may be clustered. The Elbow Method is one of the most popular methods to determine this optimal value of k.We demonstrate the given method using the K-Means clustering technique using the Sklearn library of python.<br/>
MinMaxScaler-Transform features by scaling each feature to a given range. This estimator scales and translates each feature individually such that it is in the given range on the training set, e.g. between zero and one.<br/>
************************************************************************************************
## Team Name:- Scooby Data
### Team Contributors
Team Leader - Suraj Gorai https://github.com/surajgorai2002<br />
Team Member - Pranjal Paira https://github.com/pranjalken32<br />
Team Member - Anurag Vaibhav https://github.com/Anurag15v<br />
