# **Hawaii-Temps-SQLAlchemy-Flask-App**

### Task

* Design a Flask App capable of providing basic weather analysis (Highs, Lows, Avgs, etc.) for Honolulu, Hawaii.
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

  * Which station has the highest number of observations?

  * Hint: You may need to use functions such as `func.min`, `func.max`, `func.avg`, and `func.count` in your queries.

* Design a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filter by the station with the highest number of observations.

  * Plot the results as a histogram with `bins=12`.
  
  ![stations-histogram](https://github.com/michaellegg16/sqlalchemy-challenge/blob/master/Images/station-histogram.png)
  
  
