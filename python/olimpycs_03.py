'''
(This was in Spanish and I did traduce using ChatGPT - I wont do again, feel like I do not want to show that I barely speak English)

In the skeleton competition at the Winter Olympics, there are three finalists.
The stopwatch records the following times:

Hannah Neise: 8 minutes, 3 seconds, and 10 hundredths
Jackie Narracott: 12 minutes, 7 seconds, and 8 hundredths
Kimberley Bos: 9 minutes, 14 seconds, and 3 hundredths

'''

# 1. Create a script that asks the user to enter the times for each finalist

# Ask for the athlete's name and format it.
atleta1 = str(input("Athlete's name: "))
atleta1 = atleta1.title()

# Ask for the first athlete's times

print("---------------------------------------------")
print("Enter the times for", atleta1, ": ")
tiempo_atl11 = float(input("Hundredths: "))
tiempo_atl12 = float(input("Seconds: "))
tiempo_atl13 = float(input("Minutes: "))

# Create a variable to store the athlete's total time
msg_tiempos1 = (f"The time for {atleta1} is as follows: {tiempo_atl13} minutes, {tiempo_atl12} seconds, and {tiempo_atl11} hundredths.")

print("---------------------------------------------")

# Repeat the same process for athlete 2 and athlete 3
atleta2 = str(input("Athlete's name: "))
atleta2 = atleta2.title()

print("---------------------------------------------")
print("Enter the times for", atleta2, ": ")
tiempo_atl21 = float(input("Hundredths: "))
tiempo_atl22 = float(input("Seconds: "))
tiempo_atl23 = float(input("Minutes: "))
msg_tiempos2 = (f"The time for {atleta2} is as follows: {tiempo_atl23} minutes, {tiempo_atl22} seconds, and {tiempo_atl21} hundredths.")

print("---------------------------------------------")

atleta3 = str(input("Athlete's name: "))
atleta3 = atleta3.title()

print("---------------------------------------------")
print("Enter the times for", atleta3, ": ")
tiempo_atl31 = float(input("Hundredths: "))
tiempo_atl32 = float(input("Seconds: "))
tiempo_atl33 = float(input("Minutes: "))
msg_tiempos3 = (f"The time for {atleta3} is as follows: {tiempo_atl33} minutes, {tiempo_atl32} seconds, and {tiempo_atl31} hundredths.")

# Print the athletes' times (optional)
# print(msg_tiempos1)
# print(msg_tiempos2)
# print(msg_tiempos3)

# 2. Convert the times from minutes-seconds-hundredths into seconds

cenSeg_tiempo_atl11 = tiempo_atl11 / 100
minSeg_tiempo_atl13 = tiempo_atl13 * 60
totalSeg_atl1 = cenSeg_tiempo_atl11 + tiempo_atl12 + minSeg_tiempo_atl13

cenSeg_tiempo_atl21 = tiempo_atl21 / 100
minSeg_tiempo_atl23 = tiempo_atl23 * 60
totalSeg_atl2 = cenSeg_tiempo_atl21 + tiempo_atl22 + minSeg_tiempo_atl23

cenSeg_tiempo_atl31 = tiempo_atl31 / 100
minSeg_tiempo_atl33 = tiempo_atl33 * 60
totalSeg_atl3 = cenSeg_tiempo_atl31 + tiempo_atl32 + minSeg_tiempo_atl33

print("---------------------------------------------")
print(f"The total time for {atleta1} is {totalSeg_atl1}")
print(f"The total time for {atleta2} is {totalSeg_atl2}")
print(f"The total time for {atleta3} is {totalSeg_atl3}")
print("---------------------------------------------")

# 3. Knowing that the track is 100 meters long, calculate the average speed
# of each athlete in meters per second and print the results on the screen

metros_seg1 = 100 / totalSeg_atl1
metros_seg2 = 100 / totalSeg_atl2
metros_seg3 = 100 / totalSeg_atl3

print("-----------------------------------------------------")

print(f"The average speed of {atleta1} is {metros_seg1:.2f}")
print(f"The average speed of {atleta2} is {metros_seg2:.2f}")
print(f"The average speed of {atleta3} is {metros_seg3:.2f}")

print("-----------------------------------------------------")
