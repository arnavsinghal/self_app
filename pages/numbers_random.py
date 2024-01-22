import pandas as pd
import random 
from io import BytesIO 
import streamlit as st
import datetime

# Creating a list of numbers from 1 to 22

input_val = st.text_input("Enter Number (ex: 33)")

generate_excel = st.button("Generate Excel")

if generate_excel:
    input_eval_val = eval(input_val)
    numbers = [i for i in range(1, input_eval_val)]

    fname = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # Shuffling the numbers
    random.shuffle(numbers)

    df = pd.DataFrame([], columns=numbers)

    data = BytesIO(df.to_csv(index=False).encode('utf-8'))

    st.download_button(label="Click to Download Result",
                        data=data,
                        file_name=f"Shuffled_numbers_{fname}.csv",
                        mime='application/octet-stream')

    # Path for the CSV file
    # file_path = r"D:\OneDrive\Desktop\New System 2\Random\shuffled_numbers.csv"

    # # Writing the shuffled numbers to a CSV file
    # with open(file_path, mode='w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(numbers)

    # print(f"CSV file created at {file_path}")
