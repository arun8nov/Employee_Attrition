import pandas as pd 




class Employee_Attrition:

    def __init__(self):
        pass

    def clean(self,df):
        df.drop_duplicates(inplace=True)
        df.dropna(inplace=True)

        # Change Column Names and object column's value to lower case
        df.columns =[i.lower() for i in df.columns]  
        for i in df.select_dtypes(['object']).columns:
            df[i] = df[i].str.lower()

        df = df.drop(columns=['over18','standardhours','education'])

        df = df[['employeenumber','age','gender','maritalstatus','educationfield','department','jobrole',
                'joblevel','numcompaniesworked','totalworkingyears','trainingtimeslastyear','yearsatcompany','yearsincurrentrole',
                'yearssincelastpromotion','yearswithcurrmanager','percentsalaryhike','hourlyrate','dailyrate','monthlyrate','monthlyincome',
                'businesstravel','overtime','distancefromhome','worklifebalance','environmentsatisfaction','jobinvolvement','relationshipsatisfaction',
                'performancerating','stockoptionlevel','jobsatisfaction','attrition','employeecount']]
        
        df.set_index('employeenumber',inplace=True)
                    
        return df
    
    def selection(self,df):
        Att_df = df[['age', 'gender', 'maritalstatus', 'educationfield', 'department',
                'jobrole', 'joblevel','numcompaniesworked','percentsalaryhike','monthlyincome',
                'performancerating','overtime','distancefromhome','businesstravel','attrition']]
        
        Job_sat_df = df[['department', 'jobrole', 'joblevel','trainingtimeslastyear', 'yearsatcompany', 'yearsincurrentrole',
                        'yearssincelastpromotion', 'yearswithcurrmanager', 'percentsalaryhike', 'businesstravel', 'overtime',
                        'worklifebalance', 'environmentsatisfaction', 'jobinvolvement', 'relationshipsatisfaction',
                        'performancerating', 'stockoptionlevel', 'jobsatisfaction']]

        return Att_df, Job_sat_df
    
    def Attrition_FE(self,df):

        from sklearn.pipeline import Pipeline
        from sklearn.compose import ColumnTransformer
        from sklearn.impute import SimpleImputer
        from sklearn.preprocessing import StandardScaler
        from sklearn.preprocessing import OrdinalEncoder

        order_list = [  ['female', 'male'],
              
                        ['single', 'married', 'divorced'],

                        ['marketing',
                        'medical',
                        'life sciences',
                        'technical degree',
                        'human resources',
                        'other'
                        ],

                        ['sales', 'research & development', 'human resources'],

                        ['sales representative',
                        'laboratory technician',
                        'research scientist',
                        'human resources',
                        'sales executive',
                        'manufacturing director',
                        'healthcare representative',
                        'research director',
                        'manager'],

                        ['no', 'yes'],

                        ['non-travel','travel_rarely','travel_frequently'],


                        ]
        
        cat_col = df.select_dtypes(include=['object'])
        cat_col_num = df[['joblevel','performancerating']]
        num_col = df.select_dtypes(exclude=['object']).drop(columns=['joblevel','performancerating'])

        num_trans = Pipeline(
                    steps=[
                        ('imputer', SimpleImputer(strategy='median')),
                        ('scaler', StandardScaler()),
                    ]
                    )
        cat_trans = Pipeline(
                    steps=[
                        ('imputer', SimpleImputer(strategy='most_frequent')),
                        ('encoder', OrdinalEncoder(categories=order_list, dtype='int'))
                    ]
                    )
        cat_trans1 = Pipeline(
                    steps=[
                        ('imputer', SimpleImputer(strategy='most_frequent')),
                    ]
                    )
        
        preprocess = ColumnTransformer(
                    transformers=[
                        ('num',num_trans,num_col.columns),
                        ('cat',cat_trans,cat_col.columns),
                        ('cat1',cat_trans1,cat_col_num.columns)
                    ]
                )
        
        pipe = Pipeline(
                steps=[
                    ('preprocess', preprocess),
                ])
        
        return pd.DataFrame(pipe.fit_transform(df),columns=pipe.get_feature_names_out())
        

        
        


                

