import pandas as pd
from pandas import DataFrame, read_csv, read_excel
import streamlit as st
import numpy as np
import base64
import openpyxl
import datetime as dt


#set date & day format
today = dt.datetime.today()
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
now = dt.datetime.now()
format = "%d/%m/%Y"
date1 = now.strftime(format)
todays_date = days[today.weekday()],date1




#set up title and basic skeleton
st.title("Customer Service Tracker") 
try:  
    file = st.file_uploader("Upload and visualise the data ... .xlxs/csv")
except:
    pass
  


try:
    
    df = pd.read_excel(file)
    #mask_matched = df.isna(df["Date on database"])
    df = df[df["Date on database"].isnull()]

    matched = df
    #late matches
    late = matched[["Our Due Date","Service","Product Line","Brand Reference", "Colourist"]]


    late['Our Due Date'] = late['Our Due Date'].dt.strftime('%d-%m-%Y')
    late = late[["Our Due Date","Service","Product Line","Brand Reference", "Colourist"]].dropna()
    late = late.sort_values(by='Our Due Date')
    mask = (df["Our Due Date"] >= now)
    filtered = df=df.loc[mask]

    #Due matches
    df['Our Due Date'] = df['Our Due Date'].dt.strftime('%d-%m-%Y')
    df[["Brand Reference","Product Line"]] = df[["Brand Reference", "Product Line"]].astype(str)
    due = df[["Our Due Date","Service","Product Line","Brand Reference", "Colourist"]].dropna()
    due = due.sort_values(by='Our Due Date')

    st.header("Matches due  " + todays_date[0] +" " + todays_date[1])
    st.write(due)

    st.header("Overdue matches  " )
    st.write(late)

except: 
    st.write("Error processing file, try again with a differnt file ")


# try:
# 	df = pd.read_excel(file)
# except:
# 	df = pd.read_csv(file)

# finally:
# 	st.write("error")


