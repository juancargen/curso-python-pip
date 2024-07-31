import chart
import read_csv as mod_read_csv


def get_separate_population(country):
  population = {}
  try:
    #print('separate => ', country)
    population_dict = country[0] # se obtiene el dictionario de la lista
    #print('dict =>', population_dict)

    #se arma el dictionario con la poblacion por año
    population = {
      '2022' : int(population_dict.get('2022 Population')),
      '2020' : int(population_dict.get('2020 Population')),
      '2015' : int(population_dict.get('2015 Population')),
      '2010' : int(population_dict.get('2010 Population')),
      '2000' : int(population_dict.get('2000 Population')),
      '1990' : int(population_dict.get('1990 Population')),
      '1980' : int(population_dict.get('1980 Population')),
      '1970' : int(population_dict.get('1970 Population'))
    }
  except Exception as error:
    print(error)
  finally:
    #print('var => ', population_2022)
    return population

    

if __name__ == '__main__':
  data = mod_read_csv.read_csv('data.csv')
  # print(data[0])
  country = input('Digite el pais abreviado a obtener => ')
  country_filter = filter(lambda item: item['CCA3'] == country, data)
  # print(country_filter)

  separate_population = get_separate_population(list(country_filter))
print(separate_population)

labels = list(separate_population.keys())
print(labels)
values = list(separate_population.values())
print(values)

chart.generate_bar_chart(country, labels, values)
chart.generate_pie_chart(country, labels, values)