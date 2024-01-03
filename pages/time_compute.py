import streamlit as st
 
from datetime import datetime,timedelta

# Define the two times as strings
 
st.title("Time Compute")

# Specify the time format
time_format = "%H:%M:%S"

time1_str = st.text_input("please put later time here like 17:34:06")
time2_str = st.text_input("please put hours 6:30:00")


def make_unique_format(input_str):
    input_str = input_str.replace(".",":")
    input_str = input_str.replace("-",":")
    return input_str

def get_time_in_format(input_str):
    time_split= input_str.split(":")
    if len(time_split) == 1:
        input_str = input_str+":00:00"
    elif len(time_split) == 2:
        input_str = input_str+":00"
    
    return input_str


time1_str = make_unique_format(time1_str) 
fmt_time1_str = get_time_in_format(time1_str) 

time2_str = make_unique_format(time2_str) 
fmt_time2_str = get_time_in_format(time2_str) 

previous_submit = st.button("Compute Previous Time")
future_submit = st.button("Compute Future Time")

if previous_submit:
    # Convert the string times to datetime objects
    time1 = datetime.strptime(fmt_time1_str, time_format)
    time2 = datetime.strptime(fmt_time2_str, time_format)
    #print(time1, time2)
    # Calculate the time difference
    time_difference = time1 - time2

    # Print the result
    st.write("Previous Time is :", time_difference)

if future_submit:
    # Convert the string times to datetime objects
    h1,m1,s1 = fmt_time1_str.split(":")
    h2,m2,s2 = fmt_time2_str.split(":")

    a = timedelta(hours=int(h1), minutes=int(m1), seconds=int(s1))
    b = timedelta(hours=int(h2), minutes=int(m2), seconds=int(s2))

    # d = [time1, time2]
    # new_time = d[0] + sum((d_i-d[0] for d_i in d), timedelta(0)) / len(d)


    print("here",a, b)
    # Calculate the time difference
    #time_difference = time1 + time2

    # Print the result
    st.write("Future Time is :", a+b)