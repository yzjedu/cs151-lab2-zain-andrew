# Programmers:  [Andrew, Zain]
# Course:  CS151, [Mr. Zee]
# Due Date: 9/18/2024
# Lab Assignment: 2
# Problem Statement: [Calculates the population after x amount of years]
# Data In: [Immigrants, Birthrate, deathrate, population, years.]
# Data Out:  [The population after X amount of years. ]
birth_rate = float(input("How many seconds between births? "))
death_rate = float(input("How many seconds between deaths? "))
immigration_rate = float(input("How many seconds between immigrations? "))
current_population = float(input("What is the current population? "))
years = int(input("How many years in the future? "))
seconds_per_year = 31536000

    # Calculate the number of births per year
births_per_year = seconds_per_year / birth_rate

    # Calculate the number of deaths per year
deaths_per_year = seconds_per_year / death_rate

    # Calculate the number of immigrants per year
immigrants_per_year = seconds_per_year / immigration_rate

    # Calculate the total number of births over the given years
total_births = births_per_year * years

    # Calculate the total number of deaths over the given years
total_deaths = deaths_per_year * years

    # Calculate the total number of immigrants over the given years
total_immigrants = immigrants_per_year * years

    # Calculate the future population
future_population = current_population + ((31536000 / birth_rate) * years) - ((31536000 / death_rate) * years) + (
            (31536000 / immigration_rate) * years)





print(f"The population in {years} years will be {future_population}")
if future_population > current_population:
    print("The population increased")
else:
    print("The population decreased")
