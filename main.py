#!/usr/bin/env python
# coding: utf-8

# In[20]:


import requests
import json
from datetime import datetime, timedelta


# In[24]:


# Get today's date and current time
date_and_time_today = datetime.today()
print(date_and_time_today)


# In[28]:


# For fetching the information with the help of pincodes make a list of pincodes 
pincodes = ['180001', '482004']
# Number of days starting from today, whose information we need to fetch
num_days = 7


# In[48]:


# Generate dates of these seven days (including today)
dates = []
for i in range(num_days):
    dates.append(date_and_time_today + timedelta(i))

# Convert dates in a simple string format
for i,date in enumerate(dates):
    dates[i] = date.strftime("%d%m%y")
dates


# In[ ]:


# Continuously fetch the information from the CoWin API

while True:
    for pin in pincodes:
        for date in dates:
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pin, date)
            response = requests.get(URL)
            
            # Check for the status of the response
            if response.status_code == 500:
                print("CoWin server is Down..!!")
            if response.status_code == 401:
                print("Unauthorized access.")
            if response.status_code == 200:
                json_data = response.json()
                
            # Extract information
            if json_data["centers"]:
                for center in json_data["centers"]:
                    for session in center["sessions"]:
                        dashed_date = date[:2]+'-'+date[2:4]+'-'+date[4:]
                        if session["available_capacity"]:
                            print("\nPIN : ", pin)
                            print("Date: ", dashed_date)
                            print("Center Name: ", center["name"])
                            print("Center Address: ", center["address"])
                            print("Name of Vaccine: ", session["vaccine"])
                            print("Quantity of vaccines :", session["available_capacity"])


# In[ ]:




