def ageCalculator(birth_year):
    current = 2018
    if isinstance(birth_year, int):

	    if birth_year <= current:

	        age = current - birth_year

	        return age
    return None    

print(ageCalculator(2000))