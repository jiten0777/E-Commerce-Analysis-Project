import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.colors as colors
pio.templates.default = "plotly_white"
data=pd.read_csv(r'C:\Users\Jitendra\PycharmProjects\pythonProject4\Sample  Superstore.csv' , encoding ="latin-1")
print(data.head())
print(data.describe())
print(data.info())

#Converting Date Coloumn
data['Order Date']= pd.to_datetime(data['Order Date'])
data['Date']=pd.to_datetime(data['Order Date'])

data['Ship Date']= pd.to_datetime(data['Ship Date'])
data['Date']=pd.to_datetime(data['Ship Date'])
print(data.info())

data['Order Month'] = data['Order Date'].dt.month
data['Order Year'] = data['Order Date'].dt.year
data['Order Week of Day'] = data['Order Date'].dt.dayofweek
print(data.info())

##Monthly Sales Analysis
Sales_by_month = data.groupby('Order Month')['Sales'].sum().reset_index()
print(Sales_by_month)

# Monthly Sales Analysis Line Chart
fig = px.line(Sales_by_month,
              x='Order Month',
              y='Sales',
              title='📈 Monthly Sales Trend',
              markers=True,
              line_shape='spline')  # Smooth curve

fig.update_traces(line=dict(width=3, color='royalblue'), marker=dict(size=8, symbol='circle'))
fig.update_layout(title_font=dict(size=26, family='Arial'),
                  xaxis_title='Order Month',
                  yaxis_title='Sales (₹)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  paper_bgcolor='rgba(0,0,0,0)',
                  font=dict(size=14),
                  hovermode='x unified',
                  margin=dict(l=60, r=60, t=80, b=60))
fig.show()

#Sales Analysis by Sub Category
sales_by_subcategory = data.groupby('Sub-Category')['Sales'].sum().reset_index()
sales_by_subcategory = sales_by_subcategory.sort_values(by='Sales', ascending=False)  # High to low order
fig = px.bar(sales_by_subcategory,
             x='Sub-Category',
             y='Sales',
             text='Sales',  # Show value on bars
             title='📊 Sales Analysis by Sub Category',
             color='Sales',
             color_continuous_scale='Blues')  # Gradient blue
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(title_font=dict(size=26, family='Verdana'),
    xaxis_title='Sub-Category',
    yaxis_title='Total Sales (₹)',
    xaxis_tickangle=-45,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(size=14),
    margin=dict(l=50, r=50, t=80, b=120))
fig.show()

# Pie Chart For Sales By Category
sales_by_category = data.groupby('Category')['Sales'].sum().reset_index()
fig = px.pie(sales_by_category,
             values='Sales',
             names='Category',
             hole=0.3,
             color_discrete_sequence=px.colors.qualitative.Pastel,
             title='🧁 Sales Distribution by Category')
fig.update_traces(textposition='inside',
                  textinfo='percent+label',
                  pull=[0.05, 0.05, 0.05],  # Slight pop-out for each slice
                  marker=dict(line=dict(color='white', width=2)))
fig.update_layout(title_font=dict(size=26, family='Verdana'),
                  legend_title_text='Category',
                  font=dict(size=14),
                  margin=dict(l=50, r=50, t=80, b=50))
fig.show()


#Monthly Profit Analysis
profit_by_month = data.groupby('Order Month')['Profit'].sum().reset_index()
fig = px.line(profit_by_month,
              x='Order Month',
              y='Profit',
              title='📈 Monthly Profit Analysis',
              markers=True,  # Show dots on the line
              line_shape='spline',  # Smooth curved line
              color_discrete_sequence=['#636EFA'])  # Custom color (blue)

fig.update_traces(line=dict(width=3),  # Thicker line
                  marker=dict(size=8))  # Bigger dots

fig.update_layout(
    title_font=dict(size=26, family='Arial Black'),
    xaxis_title='Month',
    yaxis_title='Total Profit (₹)',
    xaxis_tickangle=-45,  # Rotate x-axis labels
    plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(size=14),
    hoverlabel=dict(bgcolor="white", font_size=13, font_family="Arial"),
    margin=dict(l=50, r=50, t=80, b=100)
)

fig.show()


# Profit by Category Bar Chart
profit_by_category = data.groupby('Category')['Profit'].sum().reset_index()

fig = px.bar(profit_by_category,
             x='Category',
             y='Profit',
             text='Profit',
             color='Category',
             color_discrete_sequence=px.colors.qualitative.Set2,
             title='💰 Profit Analysis by Category')
fig.update_traces(
    texttemplate='₹%{text:.2f}',
    textposition='outside',
    marker=dict(line=dict(color='black', width=1.5)))
fig.update_layout(
    title_font=dict(size=26, family='Verdana'),
    xaxis_title='Product Category',
    yaxis_title='Total Profit (₹)',
    font=dict(size=14),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    yaxis=dict(gridcolor='lightgrey'),
    margin=dict(l=60, r=60, t=80, b=60))
fig.show()


#profit by subcategory
profit_by_subcategory = data.groupby('Sub-Category')['Profit'].sum().reset_index()
# Plotting pie chart
fig = px.pie(profit_by_subcategory,
             values='Profit',
             names='Sub-Category',
             hole=0.3,  # donut chart style
             title='💰 Profit Analysis by Sub-Category',
             color_discrete_sequence=px.colors.qualitative.Pastel)
fig.update_traces(textposition='inside',
                  textinfo='percent+label',
                  marker=dict(line=dict(color='black', width=1)))
fig.update_layout(
    title_font=dict(size=24, family='Verdana'),
    font=dict(size=14),
    showlegend=True,
    legend_title_text='Sub-Category',
    margin=dict(t=80, l=40, r=40, b=40))
fig.show()

#Sales profit By Customer Segment
import plotly.graph_objects as go
import plotly.express as px
sales_profit_by_segment = data.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
colors = px.colors.qualitative.Set2  # Softer and modern palette
fig = go.Figure()
fig.add_trace(go.Bar(
    x=sales_profit_by_segment['Segment'],
    y=sales_profit_by_segment['Sales'],
    name='🛒 Sales',
    marker_color=colors[0],
    text=sales_profit_by_segment['Sales'],
    texttemplate='₹%{text:.2s}',
    textposition='outside'))
fig.add_trace(go.Bar(
    x=sales_profit_by_segment['Segment'],
    y=sales_profit_by_segment['Profit'],
    name='💰 Profit',
    marker_color=colors[1],
    text=sales_profit_by_segment['Profit'],
    texttemplate='₹%{text:.2s}',
    textposition='outside'))
fig.update_layout(
    title='📊 Sales vs Profit by Customer Segment',
    xaxis_title='Customer Segment',
    yaxis_title='Amount (₹)',
    barmode='group',
    title_font=dict(size=26, family='Verdana'),
    font=dict(size=14))
fig.show()

#Sales to Profit Ratio
sales_profit_by_segment = data.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
sales_profit_by_segment['Sales_to_Profit_Ratio']=(
        sales_profit_by_segment['Sales']/sales_profit_by_segment['Profit'])
print(sales_profit_by_segment[['Segment','Sales_to_Profit_Ratio']])
fig = px.bar(
    sales_profit_by_segment,
    x='Segment',
    y='Sales_to_Profit_Ratio',
    text='Sales_to_Profit_Ratio',
    title='📊 Sales-to-Profit Ratio by Segment',
    color='Segment',
    color_discrete_sequence=px.colors.qualitative.Set2)
fig.update_traces(
    texttemplate='%{text:.2f}',
    textposition='outside')
fig.update_layout(
    xaxis_title='Customer Segment',
    yaxis_title='Sales / Profit Ratio',
    showlegend=False,
    font=dict(size=14),
    title_font=dict(size=22),
    plot_bgcolor='white',
    paper_bgcolor='white',
    margin=dict(l=40, r=40, t=60, b=60))
fig.show()
