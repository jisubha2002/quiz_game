import plotly.express as px

country = input("enter a country name :")

data = {
    'country' : [country],
    'values' : [100]

}


fig = px.choropleth(
    data,
    locations ='country',
    locationmode = 'country names',
    color = 'values',
    color_continuous_scale = 'Inferno',
    title = f"the map of  {country}"
)

fig.show()


