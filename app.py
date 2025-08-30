import pandas as pd
import numpy as np
import streamlit as st
import warnings
warnings.filterwarnings("ignore")
import pickle

from Fun import Employee_Attrition
EA = Employee_Attrition()

# import class named dash
from dash import chart
c = chart()

# page layout
st.set_page_config( 
            page_title = 'Employee Attrition Details',
            page_icon = 'B',
            layout='wide')

# Read Dataset
sheet_id = '1wLXAt2bZEGKIeE_mvg1zYUSAfQCjkrDOREjLKxL55ZE'
sheet_name = 'Employee-Attrition'
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = EA.Gen_df(EA.clean(pd.read_csv(url)))

# Heder
def Heater():
    c1,c2 = st.columns([0.2,2])
    c1.image('icon.png')
    c2.title("Employee Attrition")

# Home page layout
def Home():

    # Sidebar layout
    with st.sidebar:
        # Filters of Education,deparrtment,jobrole
        st.header("Filters")

        sel_edu = st.multiselect('Education', df.educationfield.unique(), default=df.educationfield.unique())
        sel_dep = st.multiselect('Department', df.department.unique(), default=df.department.unique())
        sel_jobrole = st.multiselect('Jobrole', df.jobrole.unique(), df.jobrole.unique())

    # Filter the data according to the user's selection
    F_df = df[(df.educationfield.isin(sel_edu) & df.department.isin(sel_dep)) & (df.jobrole.isin(sel_jobrole))]
        
    
    # Header with icon
    Heater()

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
    

# Dashboard Functon
def Analyse():
    

    # Side bar with filters
    with st.sidebar:
        st.header("Filters")

        sel_edu = st.multiselect('Education', df.educationfield.unique(), default=df.educationfield.unique())
        sel_dep = st.multiselect('Department', df.department.unique(), default=df.department.unique())
        sel_jobrole = st.multiselect('Jobrole', df.jobrole.unique(), df.jobrole.unique())

    F_df = df[(df.educationfield.isin(sel_edu) & df.department.isin(sel_dep)) & (df.jobrole.isin(sel_jobrole))]

    # Heder
    c1,c2 = st.columns([0.2,2])
    c1.image('icon.png')
    c2.title("Employee Attrition Dashboard")

    # KPIs
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
    
    # Chart Implimentation
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

    c9,c10 = st.columns([2,3],border=True)
    c9.plotly_chart(c.travel(F_df))
    c10.plotly_chart(c.age_inc(F_df))

    c11,c12,c13 = st.columns(3,border=True)
    c11.plotly_chart(c.wor_lif(F_df))
    c12.plotly_chart(c.env_sat(F_df))
    c13.plotly_chart(c.job_invo(F_df))

    c14,c15,c16 = st.columns(3,border=True)
    c14.plotly_chart(c.rela_sat(F_df))
    c15.plotly_chart(c.per_rat(F_df))
    c16.plotly_chart(c.job_sat(F_df))

    c17,c18 = st.columns(2)
    c17.plotly_chart(c.PR_dep(F_df.reset_index()))
    c18.plotly_chart(c.PR_job(F_df.reset_index()))

    st.plotly_chart(c.PR_age(F_df.reset_index()))
    st.plotly_chart(c.PR_year(F_df.reset_index()))
    st.plotly_chart(c.PR_hike(F_df.reset_index()))

def Analyse_Report():
    Heater()
    st.markdown("# 📊Dashboard Report")
    st.markdown(open('Dash_Report.md','r',encoding='utf-8').read(), unsafe_allow_html=True)

# Attrition page layout
def Attrition():
    Att_df = EA.Att_df(df)
    # Heder
    c1,c2 = st.columns([0.2,2])
    c1.image('icon.png')
    c2.title("Attrition Prediction Form")

    # Import Preprocess and Model
    Att_FE = pickle.load(open('Att_Preprocess.pkl','rb'))
    Att_model = pickle.load(open('Att_Model.pkl','rb') )
   
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
                'jobsatisfaction':None,
                'performancerating': None, 
                'overtime': None, 
                'distancefromhome': None,
                'businesstravel': None, 
                }

    ############# Form Layout #############

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

        c7,c8,c9,c10 = st.columns(4)
        form_values['joblevel'] = c7.selectbox("Job Level", Att_df['joblevel'].unique().tolist())
        form_values['numcompaniesworked'] = c8.number_input("Number of Companies Worked", min_value=0, max_value=50)
        form_values['jobsatisfaction'] = c9.selectbox("Job Satisfaction",Att_df['jobsatisfaction'].unique().tolist())
        form_values['percentsalaryhike'] = c10.number_input("Percent Salary Hike", min_value=0, max_value=50, value=0)
        
        c11,c12,c13,c14 = st.columns(4)
        form_values['monthlyincome'] = c11.number_input("Monthly Income", min_value=1009, max_value=20000)
        form_values['performancerating'] = c12.selectbox("Performance Rating", Att_df['performancerating'].unique().tolist())
        form_values['overtime'] = c13.selectbox("Overtime", Att_df['overtime'].unique().tolist())
        form_values['distancefromhome'] = c14.number_input("Distance from Home", min_value=0, max_value=50, value=0)

        c14,c15,c16 = st.columns(3)
        form_values['businesstravel'] = c14.selectbox("Business Travel", Att_df['businesstravel'].unique().tolist())
        

        # Form Submmision and prediction
        submit_button = st.form_submit_button("Submit")
        if submit_button:  
            data = pd.DataFrame(form_values,index=[0])
            data_En = pd.DataFrame(Att_FE.transform(data),columns=Att_FE.get_feature_names_out())
            st.write('### Info')
            st.table(form_values)
            result = Att_model.predict(data_En)[0]
            st.write(result)
            if result == 0:
                st.success('### ✅ 👍 Employee is not likely to Attrition ')
            else:
                st.error('### ❌ ‼️ 👎 Employee is likely to Attrition')

    ############# File Upload Layout to predict attrition #############
        
    file_upload = st.file_uploader('Upload a file', type=['csv'])
    if file_upload is not None:
        result_df = pd.DataFrame()
        temp_df = pd.read_csv(file_upload)
        
        temp_df = EA.clean(temp_df)
        result_df = pd.concat([result_df,pd.DataFrame(temp_df.index)],axis=1)

        temp_df = EA.Att_df(temp_df)

        if 'attrition' in temp_df.columns :
            temp_df = temp_df.drop(columns='attrition')
        else:
            temp_df = temp_df
        
        sm_df = temp_df.copy().reset_index()

        temp_df = pd.DataFrame(Att_FE.transform(df),columns=Att_FE.get_feature_names_out())
        result_df = pd.concat([result_df,pd.DataFrame(Att_model.predict(temp_df),columns=['attrition'])],axis=1)
        result_df['Descrption'] = result_df.attrition.apply(lambda x: '✅ 👍 likely not Attrition' if x == 0 else ' ❌ ‼️ 👎 likely to Attrition')
        st.write('### Info')
        result_df1 = pd.merge(result_df[result_df['attrition'] == 1],sm_df,how='inner',on='employeenumber')
        result_df2 = pd.merge(result_df[result_df['attrition'] == 0],sm_df,how='inner',on='employeenumber')
        c1,c2 = st.columns(2,border=True)
        c1.write('### Possible Attrition Employee Details')
        c1.dataframe(result_df1)
        
        
        c1.info("Total Number of Employees attrition count",icon='🧑‍🤝‍🧑')
        c1.metric("❌ ‼️ 👎 Total", result_df1.shape[0],border=True,)

        c1.plotly_chart(c.gender(result_df1))
        c1.plotly_chart(c.Att_mar(result_df1))
        c1.plotly_chart(c.Att_dep(result_df1))
        c1.plotly_chart(c.Att_job(result_df1))
        c1.plotly_chart(c.Att_mon(result_df1))

        c2.write('### Non Possible Attrition Employee Details')
        c2.dataframe(result_df2)
        
        c2.info("Total Number of Employees non attrition count",icon='🧑‍🤝‍🧑')
        c2.metric("✅ 👍 Total", result_df2.shape[0],border=True,)

        c2.plotly_chart(c.gender(result_df2))
        c2.plotly_chart(c.Att_mar(result_df2))
        c2.plotly_chart(c.Att_dep(result_df2))
        c2.plotly_chart(c.Att_job(result_df2))
        c2.plotly_chart(c.Att_mon(result_df2))

def PerformanceRating():

    PR_df = EA.PR_df(df)

    # Import preprocess and modl
    PR_FE = pickle.load(open('PR_Preprocess.pkl','rb'))
    PR_model = pickle.load(open('PR_Model.pkl','rb'))

    # Heder
    c1,c2 = st.columns([0.2,2])
    c1.image('icon.png')
    c2.title("Performance Rating Prediction Form")

    PR_df = EA.PR_df(df)

    form_values = {
            'department' : None, 
            'jobrole' : None, 
            'joblevel' : None, 
            'trainingtimeslastyear' : None,
            'yearsatcompany' : None, 
            'yearsincurrentrole' : None, 
            'yearssincelastpromotion' : None,
            'yearswithcurrmanager' : None, 
            'percentsalaryhike' : None, 
            'businesstravel' : None,
            'overtime' : None, 
            'worklifebalance' : None, 
            'environmentsatisfaction' : None,
            'jobinvolvement' : None, 
            'relationshipsatisfaction' : None, 
            'stockoptionlevel' : None,
            'jobsatisfaction' : None            
                }
    
    ############# Form Layout #############
    with st.form(key="Performance Rating Prediction"):
        c1,c2,c3 = st.columns(3)
        form_values['department'] = c1.selectbox("Department",PR_df['department'].unique().tolist())
        form_values['jobrole'] = c2.selectbox("jobrole",PR_df['jobrole'].unique().tolist())
        form_values['joblevel'] = c3.selectbox("Job Level",PR_df['joblevel'].unique().tolist())

        c4,c5,c6 = st.columns(3)
        form_values['trainingtimeslastyear'] = c4.number_input("Training Times Last Year", min_value=0, max_value=50)
        form_values['yearsatcompany'] = c5.number_input("Years at Company", min_value=0, max_value=50)
        form_values['yearsincurrentrole'] = c6.number_input("Year since Currentrole", min_value=0, max_value=50)

        c7,c8,c9 = st.columns(3)
        form_values['yearssincelastpromotion'] = c7.number_input("Years since Last Promotion", min_value=0, max_value=50)
        form_values['yearswithcurrmanager'] = c8.number_input("Years With Current Manager", min_value=0, max_value=50)
        form_values['percentsalaryhike'] = c9.number_input("Percent Salary H ike", min_value=0, max_value=50)

        c10,c11,c12 = st.columns(3)
        form_values['businesstravel'] = c10.selectbox("Business Travel",PR_df['businesstravel'].unique().tolist())
        form_values['overtime'] = c11.selectbox("Overtime",PR_df['overtime'].unique().tolist())
        form_values['worklifebalance'] = c12.selectbox("Worklife Balance",PR_df['worklifebalance'].unique().tolist())

        c13,c14,c15 = st.columns(3)
        form_values['environmentsatisfaction'] = c13.selectbox("Environment Satisfaction",PR_df['environmentsatisfaction'].unique().tolist())
        form_values['jobinvolvement'] = c14.selectbox("Jobinvolvement",PR_df['jobinvolvement'].unique().tolist())
        form_values['relationshipsatisfaction'] = c15.selectbox("Relationship Satisfaction",PR_df['relationshipsatisfaction'].unique().tolist())

        c16,c17,c18 = st.columns(3)
        form_values['stockoptionlevel'] = c16.selectbox("Stock Option Level",PR_df['stockoptionlevel'].unique().tolist())
        form_values['jobsatisfaction'] = c17.selectbox("Job Satisfaction",PR_df['jobsatisfaction'].unique().tolist())


        # Form Submmision and prediction
        submit_button = st.form_submit_button("Submit")
        if submit_button:  
            data = pd.DataFrame(form_values,index=[0])
            
            data_En = pd.DataFrame(PR_FE.transform(data),columns=PR_FE.get_feature_names_out())
            st.dataframe(data_En)
            PR_value = PR_model.predict(data_En)
            if PR_value == 1:
                st.success("### The Employee Performance Ratiing :1️⃣")
            elif PR_value == 2:
                st.success("### The Employee Performance Ratiing :2️⃣")
            elif PR_value == 3:
                st.success("### The Employee Performance Ratiing :3️⃣")
            elif PR_value == 4:
                st.success("### The Employee Performance Ratiing :4️⃣")

    ############# File Upload Layout to predict attrition #############
    file_upload = st.file_uploader('Upload a file', type=['csv'])
    if file_upload is not None:
        result_df = pd.DataFrame()
        temp_df = pd.read_csv(file_upload)
        
        temp_df = EA.clean(temp_df)
        result_df = pd.concat([result_df,pd.DataFrame(temp_df.index)],axis=1)

        temp_df = EA.PR_df(temp_df)

        if 'performancerating' in temp_df.columns :
            temp_df = temp_df.drop(columns='performancerating')
        else:
            temp_df = temp_df
        
        sm_df = temp_df.copy().reset_index()

        temp_df = pd.DataFrame(PR_FE.transform(df),columns=PR_FE.get_feature_names_out())
        result_df = pd.concat([result_df,pd.DataFrame(PR_model.predict(temp_df),columns=['performancerating'])],axis=1)
        result_df['Rating'] = result_df['performancerating'].apply(lambda x : '1️⃣' if x == 1
                                                                       else('2️⃣' if x == 2
                                                                            else( '3️⃣' if x == 3
                                                                                 else('4️⃣' if x==4
                                                                                      else '0️⃣'))))
        result_df1 = pd.merge(result_df,sm_df,how='inner',on='employeenumber')
        st.write('### Info')
        st.dataframe(result_df1)
        st.plotly_chart(c.PR_per(result_df1))
        st.plotly_chart(c.PR_dep(result_df1))
        st.plotly_chart(c.PR_job(result_df1))
        st.plotly_chart(c.PR_year(result_df1))
        st.plotly_chart(c.PR_hike(result_df1))

pg = st.navigation([Home,Analyse,Analyse_Report,Attrition,PerformanceRating],position='top')
pg.run()


