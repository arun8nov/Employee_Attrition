import pandas as pd
import plotly.express as px

my_col = ('#c7e9b4', '#40E0D0', '#D2B48C', '#EEE8AA','#FAFAD2','#FAEBD7', '#D8BFD8','#F4A460','#F08080')

class chart:
    def __init__(self):
        pass

    def gender(self,df):
        fig = px.pie(df.gender.value_counts().reset_index(), 
            values='count', 
            names='gender',
            hole=0.5,
            color_discrete_sequence=my_col,
            title='Gender')
        fig.update_layout(
            title ={'x':0.4},
            showlegend=False
            )
        fig.update_traces(textposition="inside", textinfo="label+percent")
        return fig
    
    def marital(self,df):
        t_df = df.groupby(['maritalstatus','attrition'])['employeecount'].sum().reset_index().sort_values(by=['maritalstatus'], ascending=False)
        fig = px.bar(t_df,
                     x='maritalstatus',
                     y='employeecount',
                     color='attrition',
                     barmode='group',
                     title='Marital Status vs Attrition',
                     color_discrete_map={'no': '#c7e9b4','yes': '#40E0D0'})
        fig.update_layout(
            title ={'x':0.2},
            showlegend=True,
            legend=dict(
            orientation="h",    
            x=0.7,              
            xanchor="center",
            y=1.15,            
            yanchor="bottom"
            )
           )
        return fig

    def edu(self,df):
        t_df = df.groupby(['educationfield','attrition'])['employeecount'].sum().reset_index().sort_values(by=['educationfield'], ascending=False)
        fig = px.bar(t_df,
                     y='educationfield',
                     x='employeecount',
                     color='attrition',
                     barmode='group',
                     orientation='h',
                     title='Education Field vs Attrition',
                     color_discrete_map={'no': '#c7e9b4','yes': '#40E0D0'})
        fig.update_layout(
            title ={'x':0.08},
            showlegend=True,
            legend=dict(
            orientation="h",    
            x=0.7,              
            xanchor="center",
            y=1.15,            
            yanchor="bottom"
            )
           )
        return fig
        
    def dep(self,df):
        t_df = df.groupby(['department','attrition'])['employeecount'].sum().reset_index().sort_values(by=['department'], ascending=False)
        fig = px.bar(t_df,
                     y='department',
                     x='employeecount',
                     color='attrition',
                     barmode='group',
                     orientation='h',
                     title='Department vs Attrition',
                     color_discrete_map={'no': '#c7e9b4','yes': '#40E0D0'})
        fig.update_layout(
            title ={'x':0.15},
            showlegend=True,
            legend=dict(
            orientation="h",    
            x=0.7,              
            xanchor="center",
            y=1.15,            
            yanchor="bottom"
            )
           )
        return fig
    
    def job(self,df):
        t_df = df.groupby(['jobrole','attrition'])['employeecount'].sum().reset_index().sort_values(by=['jobrole'], ascending=False)
        fig = px.bar(t_df,
                     y='jobrole',
                     x='employeecount',
                     color='attrition',
                     barmode='group',
                     orientation='h',
                     title='Jobrole vs Attrition',
                     color_discrete_map={'no': '#c7e9b4','yes': '#40E0D0'})
        fig.update_layout(
            title ={'x':0.15},
            showlegend=True,
            legend=dict(
            orientation="h",    
            x=0.7,              
            xanchor="center",
            y=1.15,            
            yanchor="bottom"
            )
           )
        return fig
        
    def job_heat(self,df):
        fig = px.imshow(pd.crosstab(df['jobrole'], df['joblevel']),
                text_auto=True,
                aspect='auto',title="Jobrole vs Joblevel",
                color_continuous_scale=my_col)
        fig.update_xaxes(side="bottom")
        fig.update_layout(coloraxis_showscale=False,
                          title = {'x':0.4})
        
        return fig
    
    def month(self,df):
        fig = px.scatter(
                    df,x ='totalworkingyears',
                    y = 'monthlyincome',
                    color='jobrole',
                    
                    )
        fig.update_layout(
            showlegend=True,
            legend=dict(
            orientation="h",    
            x=0.5,              
            xanchor="center",
            y=1.15,            
            yanchor="bottom"
            )
           )
        return fig
    
    def travel(self,df):
        fig =  px.box(df, x='businesstravel',
                      y='age',
                      color='attrition',
                      color_discrete_map={'no': '#c7e9b4','yes': '#40E0D0'},
                      title="TravelFrequency vs Age by attrition")
        fig.update_layout(
            title ={'x':0.09},
            showlegend=True,
            legend=dict(
            orientation="h",    
            x=0.8,              
            xanchor="center",
            y=1.15,            
            yanchor="bottom"
            )
           )
        return fig
    
    def age_inc(self,df):
        fig = px.scatter(df,
                         x='age',y='monthlyincome',
                         color='jobrole')
        fig.update_layout(
            
            showlegend=True,
            legend=dict(
            orientation="h",    
            x=0.8,              
            xanchor="center",
            y=1.15,            
            yanchor="bottom"
            )
           )
        return fig
    
    def wor_lif(self,df):
        fig = px.bar(df,
                     x='worklifebalance',y='employeecount',
                     color='attrition',
                     barmode='group',
                     color_discrete_map={'no': '#c7e9b4','yes': '#40E0D0'},
                     title="Worklife Balance")
        fig.update_layout(
            title ={'x':0.15},
            showlegend=True,
            legend=dict(
            orientation="h",    
            x=0.7,              
            xanchor="center",
            y=1.15,            
            yanchor="bottom"
            )
           )
        return fig
    
    def env_sat(self,df):
        fig = px.bar(df,
                     x='environmentsatisfaction',y='employeecount',
                     color='attrition',
                     barmode='group',
                     color_discrete_map={'no': '#c7e9b4','yes': '#40E0D0'},
                     title="Environment Satisfaction")
        fig.update_layout(
            title ={'x':0.06},
            showlegend=True,
            legend=dict(
            orientation="h",    
            x=0.7,              
            xanchor="center",
            y=1.15,            
            yanchor="bottom"
            )
           )
        return fig
    
    def job_invo(self,df):
        fig = px.bar(df,
                     x='jobinvolvement',y='employeecount',
                     color='attrition',
                     barmode='group',
                     color_discrete_map={'no': '#c7e9b4','yes': '#40E0D0'},
                     title="Jobinvolvement")
        fig.update_layout(
            title ={'x':0.15},
            showlegend=True,
            legend=dict(
            orientation="h",    
            x=0.7,              
            xanchor="center",
            y=1.15,            
            yanchor="bottom"
            )
           )
        return fig
    
    def rela_sat(self,df):
        fig = px.bar(df,
                     x='relationshipsatisfaction',y='employeecount',
                     color='attrition',
                     barmode='group',
                     color_discrete_map={'no': '#c7e9b4','yes': '#40E0D0'},
                     title="Relationship Satisfaction")
        fig.update_layout(
            title ={'x':0.07},
            showlegend=True,
            legend=dict(
            orientation="h",    
            x=0.7,              
            xanchor="center",
            y=1.15,            
            yanchor="bottom"
            )
           )
        return fig
    
    def per_rat(self,df):
        fig = px.bar(df,
                     x='performancerating',y='employeecount',
                     color='attrition',
                     barmode='group',
                     color_discrete_map={'no': '#c7e9b4','yes': '#40E0D0'},
                     title="Performance Rating")
        fig.update_layout(
            title ={'x':0.15},
            showlegend=True,
            legend=dict(
            orientation="h",    
            x=0.7,              
            xanchor="center",
            y=1.15,            
            yanchor="bottom"
            )
           )
        return fig
    
    def job_sat(self,df):
        fig = px.bar(df,
                     x='jobsatisfaction',y='employeecount',
                     color='attrition',
                     barmode='group',
                     color_discrete_map={'no': '#c7e9b4','yes': '#40E0D0'},
                     title="Job Satisfaction")
        fig.update_layout(
            title ={'x':0.15},
            showlegend=True,
            legend=dict(
            orientation="h",    
            x=0.7,              
            xanchor="center",
            y=1.15,            
            yanchor="bottom"
            )
           )
        return fig
    
# Prdiction Dashboards
    def Att_mar(self,df):
        fig = px.bar(df.groupby('maritalstatus')['employeenumber'].count().sort_values().reset_index(),
             x='maritalstatus',y='employeenumber',
             title='Marrital Status',
             color_discrete_sequence=['#40E0D0'])
        fig.update_layout(
            title ={'x':0.5},
            yaxis_title ='Count'  
           )
        return fig
    
    def Att_dep(self,df):
        fig = px.bar(df.groupby('department')['employeenumber'].count().sort_values().reset_index(),
                x = 'department',y='employeenumber',
                title = 'Department',
                color_discrete_sequence=['#D2B48C'])
        fig.update_layout(
            title ={'x':0.5},
            yaxis_title ='Count'   
           )
        return fig
        
    def Att_job(self,df):
        fig = px.bar(df.groupby('jobrole')['employeenumber'].count().sort_values().reset_index(),
                x = 'jobrole',y='employeenumber',
                title = 'Jobrole',
                color_discrete_sequence=['#EEE8AA'])
        fig.update_layout(
            title ={'x':0.5},
            yaxis_title ='Count'  
           )
        return fig
    
    def Att_mon(self,df):
        fig = px.histogram(df,x='monthlyincome',
                           title='Monthly Income',
                           color_discrete_sequence=['#FAFAD2'])
        fig.update_layout(
            title ={'x':0.5},
            yaxis_title ='Count' 
           )
        return fig
    
    def PR_per(self,df):
        fig = px.histogram(df,x='performancerating',
                           title='Performance Rating')
        fig.update_layout(
            title ={'x':0.5},
            xaxis_title ='Performancerating value' 
           )
        return fig
    
    def PR_dep(self,df):
        fig = px.imshow(df.pivot_table(index='department',columns='performancerating',values='employeenumber',aggfunc='count'),
                text_auto=True,
                title='Department wise Performance Rating'
                )
        
        fig.update_layout(
            title ={'x':0.4},
            xaxis_title ='Performancerating value' 
           )
        
        return fig
    
    def PR_job(self,df):
        fig = px.imshow(df.pivot_table(index='jobrole',columns='performancerating',values='employeenumber',aggfunc='count'),
                text_auto=True,
                title='Department wise Performance Rating'
                )
        
        fig.update_layout(
            title ={'x':0.4},
            xaxis_title ='Performancerating value' 
           )
        
        return fig
    
    def PR_year(sel,df):
        fig = px.histogram(df,
                           x='yearsatcompany',
                           color='performancerating',
                           title='Years At The Company Performance Rating')
        fig.update_layout(
            title ={'x':0.4},
            showlegend=True,
            legend=dict(
            orientation="h",    
            x=0.7,              
            xanchor="center",
            y=1.15,            
            yanchor="bottom"
            )
           )
        return fig
    
    def PR_hike(sel,df):
        fig = px.histogram(df,
                           x='percentsalaryhike',
                           color='performancerating',
                           title='Salary Hike Vs Performance rating')
        fig.update_layout(
            title ={'x':0.4},
            showlegend=True,
            legend=dict(
            orientation="h",    
            x=0.7,              
            xanchor="center",
            y=1.15,            
            yanchor="bottom"
            )
           )
        return fig
    
    def PR_age(sel,df):
        fig = px.histogram(df,
                           x='age',
                           color='performancerating',
                           title='Age Vs Performance rating')
        fig.update_layout(
            title ={'x':0.4},
            showlegend=True,
            legend=dict(
            orientation="h",    
            x=0.7,              
            xanchor="center",
            y=1.15,            
            yanchor="bottom"
            )
           )
        return fig