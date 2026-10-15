"""lab task 3"""
""" Weekend Temperature with a Tuple

Create a tuple containing the temperatures recorded on Saturday and Sunday
for three different times of the day.
Use a for loop to display each temperature.
Then calculate the highest and lowest temperature in the tuple."""


print("TEMPERATURE FOR SATURDAY-\n")
times = ["morning", "noon", "night"]
saturday_temp = []
for i in times:
    temp = float(input(f"enter saturday's temperature for {i}: "))
    saturday_temp.append(temp)


print()
print("TEMPERATURE FOR SUNDAY-\n")
sunday_temp = []
for i in times:
    temp = float(input(f"enter sunday's temperature for {i}: "))
    sunday_temp.append(temp)


saturday_max_temp = saturday_temp[0]
saturday_min_temp = saturday_temp[0]

sunday_max_temp = sunday_temp[0]
sunday_min_temp = sunday_temp[0]

for x in saturday_temp:
    if x > saturday_max_temp:
        saturday_max_temp = x
    if x < saturday_min_temp:
        saturday_min_temp = x

for x in sunday_temp:
    if x > sunday_max_temp:
        sunday_max_temp = x
    if x < sunday_min_temp:
        sunday_min_temp = x
        
# converting to tuple
saturday_temp = tuple(saturday_temp)
sunday_temp = tuple(sunday_temp)

print(f"saturday's temperatures {saturday_temp}\n")
print(f"sunday's temperatures {sunday_temp}\n")

print(f"maximum temperature of saturday: {saturday_max_temp}\n")
print(f"minimum temperature of saturday: {saturday_min_temp}\n")

print(f"maximum temperature of sunday: {sunday_max_temp}\n")
print(f"minimum temperature of saturday: {sunday_min_temp}")