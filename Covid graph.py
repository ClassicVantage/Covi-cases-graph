import pandas as pd
import plotly.expres as px
df=pd.read_csv("line_chart.csv")

fig=px.scatter(df,x="date",y="no of cases",color = " Country",title="covid i9 case distribuition")
fig.show()