# get inputs from the user
time = float(input("Total duration of the trip (hours): "))
speed = float(input("Average speed of the car (mph): "))

#Calculate the distance
distance= speed * time

#display the total distance of travel
print(f"Total Distance of Travel: {distance:.1f}")