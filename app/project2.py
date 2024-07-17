import charts
import read_csv as mod_read_csv


def get_world_population_percentage(world_population):
  population_percentage_country = []
  population_percentage_value = []
  
  #list_population_percentage_by_country = []
  try:
    
    #se itera sobre la lista total para obtener el pais y el porcentaje de cada pais
    
    for country in world_population:  
      #se arma el dictionario con el porcentaje de poblacion por pais
      population_percentage_country.append(country.get('CCA3'))
      population_percentage_value.append(float(country.get('World Population Percentage')))
      
      #list_population_percentage_by_country.append(population_percentage_by_country)
      
  except Exception as error:
    print(error)
  finally:
    #print('var => ', population_2022)
    return population_percentage_country, population_percentage_value



if __name__ == '__main__':
  data = mod_read_csv.read_csv('data.csv')
  
  world_population_percentage_country, world_population_percentage_value = get_world_population_percentage(data)
  #print(world_population_percentage_country)
  #print(world_population_percentage_value)


labels = world_population_percentage_country
print(labels)
values = world_population_percentage_value
print(values)

charts.generate_bar_chart('world', labels, values)
charts.generate_pie_chart('world', labels, values)
