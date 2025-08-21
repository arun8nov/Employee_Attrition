import pandas as pd
import numpy as np
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

import plotly.express as px
from Fun import Employee_Attrition

EA = Employee_Attrition()
sheet_id = '1wLXAt2bZEGKIeE_mvg1zYUSAfQCjkrDOREjLKxL55ZE'
sheet_name = 'Employee-Attrition'
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = EA.clean(pd.read_csv(url))

st.set_page_config(
    page_title = 'Employee Attrition',
    page_icon = 'B'
                )


class chart:

    def __int__(self):
        pass


def Home():
    c1,c2 = st.columns(2)
    c1.image('icon.png')
    c2.title("Employee Attrition Dashboard")





Home()
