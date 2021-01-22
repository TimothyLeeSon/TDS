# Required frameworks to be installed before running the solution

py -m pip install Django

py -m pip install openpyxl

py -m pip install pandas

py -m pip install plotly


## Additional Information

Tools: VS Code, Python 3.9.1, and Django 3.1.5, openpyxl 3.0.6, pandas, 1.2.1, plotly 4.14.3
Data storage is a relational database because the .xls file reveals three columns: Month, Income, and Expenses. A small dataset is observed and given the context (interview), a basic database will suffice.
Django officially supports the following databases:
1.	PostgreSQL (production environment, this database is recommended);
2.	MariaDB;
3.	MySQL;
4.	Oracle; and
5.	SQLite (default run).

By default, and using the selected framework discussed below, the SQLite database was used. Lightweight and easy to use for the task presented.
I went with Django framework because several websites listed it for full-stack development. I found the documentation around Django to be very comprehensive.

I selected plotly for the visualization aspect. Although the visualization was basic, plotly allows for more sophisticated graphing, analytics, and statistics.

I came across another framework that has peeked my interest and I think shows great potential: Dash. From a data visualization and user interface view point, this is the framework I would have selected to make UI aesthetically pleasing and enhanced visualizations.
