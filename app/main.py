import utils
import read_csv as mod_read_csv
import chart
import pandas as pd

'''
data = [
  {
    'Country': 'Colombia',
    'Population': 500	
  },
  {
    'Country': 'Bolivia',
    'Population': 300	
  }
]

def run():
  keys, values = utils.get_population()
  print(keys, values)
  
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)
  print(result)
'''
def run():
  #usando pandas para grafica pie de Africa
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  chart.generate_pie_chart('Africa', countries, percentages)
  
  # sin usar pandas para graficas pie y bar del pais ingresado en el input
  data = mod_read_csv.read_csv('data.csv')
  # print(data[0])
  country = input('Digite el pais abreviado a obtener => ')
  country_filter = filter(lambda item: item['CCA3'] == country, data)
  # print(country_filter)

  separate_population = utils.get_separate_population(list(country_filter))
  print(separate_population)

  labels = list(separate_population.keys())
  print(labels)
  values = list(separate_population.values())
  print(values)

  chart.generate_bar_chart(country, labels, values)
  chart.generate_pie_chart(country, labels, values)


if __name__ == '__main__':
  run()

