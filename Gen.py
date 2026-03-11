def current_age(year):
    Age = 2026 - year
    return Age


def hundred_year(year):
    hundred_age = 100 + year
    return hundred_age


g1 = "Generation Alpha"
g2 = "Generation Z"
g3 = "Millennial"
g4 = "Generation X"
g5 = "Baby Boomer"
g6 = "Silent Generation"
g7 = "Greatest Generation"

birth_year = int(input("Enter your birth year : "))

if 2013 <= birth_year:
    print("You are a", g1, "Person.")

elif 1997 <= birth_year <= 2012:
    print("You are a", g2, "Person.")

elif 1981 <= birth_year <= 1996:
    print("You are a", g3, "Person.")

elif 1965 <= birth_year <= 1980:
    print("You are a", g4, "Person.")

elif 1946 <= birth_year <= 1964:
    print("You are a", g5, "Person.")

elif 1928 <= birth_year <= 1945:
    print("You are a", g6, "Person.")

else:
    print("You are a", g7, "Person.")

print("You are", current_age(birth_year), "years old now.")

print("In", hundred_year(birth_year), "you are 100 years old.")
