def current_age(birth_year):
    Age = 2026 - birth_year
    return Age


def hundred_year(birth_year):
    hundred_age = 100 + birth_year
    return hundred_age


def get_generation(birth_year):

    if 2013 <= birth_year:
        g = "Generation Alpha"
    elif 1997 <= birth_year <= 2012:
        g = "Generation Z"
    elif 1981 <= birth_year <= 1996:
        g = "Millennial"
    elif 1965 <= birth_year <= 1980:
        g = "Generation X"
    elif 1946 <= birth_year <= 1964:
        g = "Baby Boomer"
    elif 1928 <= birth_year <= 1945:
        g = "Silent Generation"
    else:
        g = "Greatest Generation"
    return g

print("--- 🎂 Age & Generation Finder ---")

try:
    birth_year = int(input("Enter your birth year : "))
    
    if birth_year > 2026:
        print("⚠️ Future years are not allowed!")
    else:
        gen = get_generation(birth_year)
        age = current_age(birth_year)
        h_year = hundred_year(birth_year)

        print("-" * 35)
        print(f"🌟 You belong to : {gen}")
        print(f"📅 Your current age : {age} years")
        print(f"💯 You will turn 100 in the year : {h_year}")
        print("-" * 35)

except ValueError:
    print("⚠️ Please enter a valid year (Number only)!")

print("-------------Thank you-------------")