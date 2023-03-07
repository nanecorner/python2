import utils
import read_csv
import charts

data = read_csv.read_csv('./data.csv')

option = int(input("Select an option with number:\n1. Draw chart by country\n2. Draw world population\n\n"))
if option == 1:
    country = input("Type Country: ")
    information = list(filter(lambda item: item['Country/Territory'] == country,data))[0]
    result = utils.filter_years(information)
    labels,values = utils.get_labels_values(result)
    charts.generate_bar_chart(labels,values)
else:
    result = {item['Country/Territory']:item['World Population Percentage'] for item in data}
    labels,values = utils.get_labels_values(result)
    charts.generate_pie_chart(labels,values)

