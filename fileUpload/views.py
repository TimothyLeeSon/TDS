from django.shortcuts import render, HttpResponse
import openpyxl
from .forms import InputForm
import pandas as pd
import sqlite3
from sqlite3 import Error
import plotly.graph_objs as go
from plotly.offline import iplot
import plotly.offline as opy

# Establish DB connection
def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return connection

# Select all finance information and display it
def select_all_finances(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM fileupload_finance")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

# Retrieve data from DB and visually display it
def graph_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM fileUpload_finance")
    data = cursor.fetchall()
    month = []
    income = []
    expenditure = []

    for row in data:
        month.append(row[1])
        income.append(row[2])
        expenditure.append(row[3])
    #    print(f"Month: {month}")
    #    print(f"Income: {income}")
    #    print(f"Expenditure: {expenditure}")

    trace1 = go.Bar(
        x = month,
        y = income,
        name = "Income"
    )

    trace2 = go.Bar(
        x = month,
        y = expenditure,
        name = "Expenditure"
    )

    data = [trace1, trace2]
    layout = go.Layout(barmode = "group")    
    figure = go.Figure(data = data, layout = layout)
    div = opy.plot(figure,  output_type = "div")
    return div

def index(request):
    if request.method == "POST":
        # Pass form data to the form class
        details = InputForm(request.POST)

        if details.is_valid():
            post = details.save(commit = False)

            # Finally write changes into the DB
            post.save()
        else:
            print("error")
            return render(request, 'index.html', {"form" : InputForm(None)})

        excel_file = request.FILES["excel_file"]

        # Connect to database and write excel data
        database = sqlite3.connect("db.sqlite3")
        dfs = pd.read_excel(excel_file, sheet_name=None)
        for table, df in dfs.items():
            df.to_sql("fileUpload_finance", database, if_exists="replace")

        database.commit()
        database.close()
        
        # Accessing database
        database = r".\db.sqlite3"

        connection = create_connection(database)
        with connection:
            #print("Display Finances")
            #select_all_finances(connection)
            print("Test")
            my_graph = graph_data(connection)
            # connection.close()

        workBook = openpyxl.load_workbook(excel_file, data_only=True)

        # Acquire a specific worksheet
        workSheet = workBook["Sheet1"]
        excelData = list()

        # Iterating over the rows and acquiring value from each cell in the row
        for row in workSheet.iter_rows():
            rowData = list()

            for cell in row:
                rowData.append(str(cell.value))

            excelData.append(rowData)
        
        return render(request, 'index.html', {"excel_data" : excelData, "form" : InputForm(None), "graph" : my_graph})
    else:       
        return render(request, 'index.html', {"form" : InputForm(None)})


