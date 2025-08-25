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
            title ={'x':0.5},
            annotations=[dict(
                text="Gender",  
                x=0.5, y=0.5,       
                font_size=16, 
                showarrow=False
                            )],showlegend=False
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
                     color_discrete_sequence=my_col)
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
                     color_discrete_sequence=my_col)
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
                     color_discrete_sequence=my_col)
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
                     color_discrete_sequence=my_col)
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
        return fig