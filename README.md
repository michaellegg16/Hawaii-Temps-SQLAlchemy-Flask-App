# **Hawaii-Temps-SQLAlchemy-Flask-App**

## Task

* Explore the "hawaii.sqlite" database and create a Flask App that can be used for weather analysis.

#### Step 1:
* Use Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database ("hawaii.sqlite").

* Precipiation Analysis
    * Design a query to retrieve the last 12 months of precipitation data.

    * Select only the `date` and `prcp` values.

    * Load the query results into a Pandas DataFrame and set the index to the date column.

    * Sort the DataFrame values by `date`.

    * Plot the results using the DataFrame `plot` method.
    
    ![precipitation](https://github.com/michaellegg16/sqlalchemy-challenge/blob/master/Images/precipitation.png)
    
* Station Analysis

* Design a query to calculate the total number of stations.

* Design a query to find the most active stations.

  * List the stations and observation counts in descending order.

  * Determine which station has the highest number of observations.
  
  ![highestobservations](https://github.com/michaellegg16/sqlalchemy-challenge/blob/master/Images/MostActiveStations.png)

* Design a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filter by the station with the highest number of observations.

  * Plot the results as a histogram with `bins=12`.
  
  ![stations-histogram](https://github.com/michaellegg16/sqlalchemy-challenge/blob/master/Images/station-histogram.png)
  
#### Step 2:
* Design a Flask App capable of providing basic weather analysis (Highs, Lows, Avgs, etc.) for Honolulu, Hawaii.

* Routes:

* '/'
   * Home page.

  * List all routes that are available.
  
  ![homepage](https://github.com/michaellegg16/sqlalchemy-challenge/blob/master/Images/HomePage.png)
  
* `/api/v1.0/precipitation`

  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.
  
  ![precipitationpage](https://github.com/michaellegg16/sqlalchemy-challenge/blob/master/Images/PrecipitationPage.png)
  
* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.
  
  ![stationspage](https://github.com/michaellegg16/sqlalchemy-challenge/blob/master/Images/StationsPage.png)

* `/api/v1.0/tobs`

  * Query the dates and temperature observations of the most active station for the last year of data.
  
  * Return a JSON list of temperature observations (TOBS) for the previous year.
  
  ![tobspage](https://github.com/michaellegg16/sqlalchemy-challenge/blob/master/Images/TOBSPage.png)

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
  
  ![startpage](https://github.com/michaellegg16/sqlalchemy-challenge/blob/master/Images/StartDatePage.png)

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
  
  ![startendpage](https://github.com/michaellegg16/sqlalchemy-challenge/blob/master/Images/StartEndDatePage.png)
  
  
  
## Instructions

1. In order to run this code make sure that you have the proper dependencies installed.
1. If you want, run the jupyter notebook to view the data exploration and precipitation graph.
1. To run the flask app, navigate the the directory with the "app.py" file.
1. Type "python app.py" in your terminal.
1. A test server should start running. Click the link to go to the home page.
1. Once at the home page, you can navigate the the page you want to use for analysis by using the provided url routes.


## Conclusion

Based on this analysis Honolulu, Hawaii seems to host both a temperate and consistent climate with averages staying around 70 degrees fahrenheit year-round. However, more analysis into the precipitation is needed to have a more full picture of the climate. This project is limitied in scope and while the temperatures seem ideal for vacation, the high precipitation around the year could be a cause for concern as it seems highly unpredictable and subject to spikes based on the graphs created. Additionally, humidity would be a concern for myself, and this analysis does not provide any information about humidity. This project does a great job of using SQLAlchemy and Flask to create a live app capable of analysis, but the analysis itself is fairly simplistic and only provides a glimpse into the whole climate of Honolulu. 
