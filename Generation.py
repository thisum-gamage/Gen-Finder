def current_age():
    Age = 2026 - birth_year
    return Age


def hundred_year():
    hundred_age = 100 + birth_year
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

print("You are", current_age(), "years old now.")

print("In", hundred_year(), "you are 100 years old.")


# Generation Alpha = 2013 +
# Generation Z = 1997 - 2012
# Millennials = 1981 - 1996
# Generation X = 1965 - 1980
# Baby Boomers = 1946 - 1964
# Silent Generation = 1928 - 1945
# Greatest Generation = - 1928
# Current age
# 100 years old year

# statement = ("You are a g person")
