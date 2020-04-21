# taken from https://gist.github.com/Luminaar/a5b6706270fa7eb947ea136e7e5a38c1
# Problem: We have a huget CSV file (several GB)
# We want to process it without running out of RAM
# Ideally we would like to do all of the processing while using as little of RAM as possible.

# For example, we would like to get an average of all values from the 3rd column

total = 0
counter = 1

with open("soubor.txt") as loaded_file:
    
    for line in loaded_file:
        
        value = float(line.split(',')[2])
        total += value
        counter += 1
        
average = total / counter
print(average)