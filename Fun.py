import pandas as pd 


class Employee_Attrition:

    def __init__(self):
        pass

    def clean(self,df):
        df.drop_duplicates(inplace=True)

        # Change Column Names and object column's value to lower case
        df.columns =[i.lower() for i in df.columns]  
        for i in df.select_dtypes(['object']).columns:
            df[i] = df[i].str.lower()       
            
        df.set_index('employeenumber',inplace=True)
                    
        return df
    
    def Gen_df(self,df):
        Gen_df = df[['age','gender','maritalstatus','educationfield','department','jobrole',
                    'joblevel','numcompaniesworked','totalworkingyears','trainingtimeslastyear','yearsatcompany','yearsincurrentrole',
                    'yearssincelastpromotion','yearswithcurrmanager','percentsalaryhike','hourlyrate','dailyrate','monthlyrate','monthlyincome',
                    'businesstravel','overtime','distancefromhome','worklifebalance','environmentsatisfaction','jobinvolvement','relationshipsatisfaction',
                    'performancerating','stockoptionlevel','jobsatisfaction','attrition','employeecount']]
        return Gen_df
    
    def Att_df(self,df):    
        Att_df = df[['age', 'gender', 'maritalstatus', 'educationfield', 'department',
                'jobrole', 'joblevel','numcompaniesworked','percentsalaryhike','monthlyincome',
                'jobsatisfaction','performancerating','overtime','distancefromhome','businesstravel','attrition']]
        return Att_df
    
    def PR_df(self,df):    
        PR_df = df[['department', 'jobrole', 'joblevel','trainingtimeslastyear', 'yearsatcompany', 'yearsincurrentrole',
                        'yearssincelastpromotion', 'yearswithcurrmanager', 'percentsalaryhike', 'businesstravel', 'overtime',
                        'worklifebalance', 'environmentsatisfaction', 'jobinvolvement', 'relationshipsatisfaction',
                        'stockoptionlevel', 'jobsatisfaction','performancerating']]

        return PR_df
    
    
        

        
        


                

