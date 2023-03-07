def filter_years(information):
    years = ['2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population','1970 Population']
    result = {item[:4]:int(information.get(item)) for item in years if item in information}
    return result

def get_labels_values(data):
    labels = data.keys()
    values = data.values()
    return labels,values