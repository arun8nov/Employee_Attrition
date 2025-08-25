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

import pickle
with open ('employee_attrition.pkl','rb') as f:
    Attrition_model = pickle.load(f)


    
def Home():

    with st.sidebar:
        st.header("Filters")

        sel_dep = st.multiselect('Department', df.department.unique(), default=df.department.unique())
        sel_jobrole = st.multiselect('Jobrole', df.jobrole.unique(), df.jobrole.unique())

        F_df = df[(df.department.isin(sel_dep)) & (df.jobrole.isin(sel_jobrole))]
        
    
    st.set_page_config(
            page_title = 'Employee Attrition Details',
            page_icon = 'B',
            layout='wide')
    
    c1,c2 = st.columns([0.2,2])
    c1.image('icon.png')
    c2.title("Employee Attrition and Job Satisfaction")

    st.dataframe(F_df)

    c3,c4,c5 = st.columns(3,border=True)
    c3.markdown("#### 🎓📚Education Level at the company")
    for i in F_df.educationfield.value_counts().reset_index().educationfield:
        c3.success(i)
    c4.markdown("#### 👥Department at the company")
    for i in F_df.department.value_counts().reset_index().department:
        c4.success(i)
    c5.markdown("#### 🤝Jobrole at the company")
    for i in F_df.jobrole.value_counts().reset_index().jobrole:
        c5.success(i)
        

def Analyse():

    from dash import chart
    c = chart()

    with st.sidebar:
        st.header("Filters")

        sel_dep = st.multiselect('Department', df.department.unique(), default=df.department.unique())
        sel_jobrole = st.multiselect('Jobrole', df.jobrole.unique(), df.jobrole.unique())

    F_df = df[(df.department.isin(sel_dep)) & (df.jobrole.isin(sel_jobrole))]

    t1,t2,t3 = st.columns(3,gap='small')
    with t1:
        st.info("Total Number of Employees",icon='🧑‍🤝‍🧑')
        st.metric("🧑‍🤝‍🧑 Total", F_df.shape[0],border=True,)
        
    with t2:
            st.info("Total Number of Attrition Employees", icon='✅')
            st.metric("✅ Non Attrition", F_df.attrition.value_counts()[0],border=True,)
    
    with t3:
        st.info("Total Number of Attrition Employees", icon='⚠️')
        st.metric("⚠️ Attrition", F_df.attrition.value_counts()[1],border=True,)
    
   




    c1,c2 = st.columns([2,3],border=True) 
    c1.plotly_chart(c.gender(F_df))
    c2.plotly_chart(c.marital(F_df))
        

    c4,c5,c6 = st.columns(3,border=True) 
    c4.plotly_chart(c.edu(F_df))
    c5.plotly_chart(c.dep(F_df))
    c6.plotly_chart(c.job(F_df))
    
    c7,c8 = st.columns(2,border=True)
    c7.plotly_chart(c.job_heat(F_df))
    c8.plotly_chart(c.month(F_df))

    
    

def Attrition():

    
    import pickle
    
    Att_df = EA.selection(df)[0]

    # From index assigning

    form_values = {
                'age' : None,
                'gender': None, 
                'maritalstatus': None, 
                'educationfield': None, 
                'department': None,
                'jobrole': None, 
                'joblevel': None, 
                'numcompaniesworked': None,
                'percentsalaryhike': None,
                'monthlyincome': None, 
                'performancerating': None, 
                'overtime': None, 
                'distancefromhome': None,
                'businesstravel': None, 
                }


    ############# Form Layout #############

    st.title("Attrition Prediction Form")

    with st.form(key="Attition Form"):
        # Get Values
        c1,c2,c3 = st.columns(3)
        form_values['age'] = c1.number_input("Age", min_value=18, max_value=100, value=25)
        form_values['gender'] = c2.selectbox("Gender", Att_df['gender'].unique().tolist())
        form_values['maritalstatus'] = c3.selectbox("Marital Status", Att_df['maritalstatus'].unique().tolist())

        c4,c5,c6 = st.columns(3)
        form_values['educationfield'] = c4.selectbox("Education Field", Att_df['educationfield'].unique().tolist())
        form_values['department'] = c5.selectbox("Department", Att_df['department'].unique().tolist())
        form_values['jobrole'] = c6.selectbox("Job Role", Att_df['jobrole'].unique().tolist())

        c7,c8,c9 = st.columns(3)
        form_values['joblevel'] = c7.selectbox("Job Level", Att_df['joblevel'].unique().tolist())
        form_values['numcompaniesworked'] = c8.number_input("Number of Companies Worked", min_value=0, max_value=50)
        form_values['percentsalaryhike'] = c9.number_input("Percent Salary Hike", min_value=0, max_value=50, value=0)
        
        c10,c11,c12 = st.columns(3)
        form_values['monthlyincome'] = c10.number_input("Monthly Income", min_value=1009, max_value=20000)
        form_values['performancerating'] = c11.selectbox("Performance Rating", Att_df['performancerating'].unique().tolist())
        form_values['overtime'] = c12.selectbox("Overtime", Att_df['overtime'].unique().tolist())

        c13,c14,c15 = st.columns(3)
        form_values['distancefromhome'] = c13.number_input("Distance from Home", min_value=0, max_value=50, value=0)
        form_values['businesstravel'] = c14.selectbox("Business Travel", Att_df['businesstravel'].unique().tolist())
        

        # Form Submmision and prediction
        submit_button = st.form_submit_button("Submit")
        if submit_button:  
            data = pd.DataFrame(form_values,index=[0])
            data_En = EA.Attrition_FE(data)
            st.write('### Info')
            st.table(form_values)
            result = Attrition_model.predict(data_En)[0]
            st.write(result)
            if result == 0:
                st.success('### ✅ 👍 Employee is not likely to Attrition ')
            else:
                st.error('### ❌ ‼️ 👎 Employee is likely to Attrition')

    ############# File Upload Layout #############

    file_upload = st.file_uploader('Upload a file', type=['csv', 'xlsx', 'xls'])
    if file_upload is not None:
        result_df = pd.DataFrame()
        temp_df = pd.read_csv(file_upload)
        
        temp_df = EA.clean(temp_df)
        result_df = pd.concat([result_df,pd.DataFrame(temp_df.index)],axis=1)

        temp_df = EA.selection(temp_df)[0]

        if 'attrition' in Att_df.columns :
            temp_df = Att_df.drop(columns='attrition')
        else:
            temp_df = Att_df

    
        temp_df = EA.Attrition_FE(temp_df)
        result_df = pd.concat([result_df,pd.DataFrame(Attrition_model.predict(temp_df),columns=['Attrition'])],axis=1)
        result_df.Attrition = result_df.Attrition.apply(lambda x: '✅ 👍 likely not Attrition' if x == 0 else ' ❌ ‼️ 👎 likely to Attrition')
        st.write('### Info')
        st.dataframe(result_df)
        
        


    


pg = st.navigation([Home,Analyse,Attrition,],position='top')
pg.run()



