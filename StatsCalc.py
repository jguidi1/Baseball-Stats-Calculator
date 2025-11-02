#calcing BA OBP SLG OPS

import csv

print("Howdy, partner!")
player_name = input("Enter player name: ")
user_AB = int(input("Enter at bats: "))
user_H = int(input("Enter hits: "))
user_doubles = int(input("Enter # of doubles: "))
user_triples = int(input("Enter # of triples: "))
user_HR = int(input("Enter # of home runs: "))
user_BB = int(input("Enter # of walks: "))
user_hbp = int(input("Enter # of hit by pitch: "))
user_sf = int(input("Enter # of sacrifice flies: "))

BA = user_H/user_AB
OBP = ((user_H+user_BB+user_hbp)/(user_AB+user_BB+user_hbp+user_sf))
SLG = (((user_H-user_doubles-user_triples-user_HR)+(2*user_doubles)+(3*user_triples)+(4*user_HR))/user_AB)
OPS = ((((user_H+user_BB+user_hbp)/(user_AB+user_BB+user_hbp+user_sf))+(((user_H-user_doubles-user_triples-user_HR)+(2*user_doubles)+(3*user_triples)+(4*user_HR))/user_AB)))

print(f"---{player_name}'s Calculated Stats ---")
print(f"Batting Average (BA): {BA:.3f}") #limited to 3 decimal places
print(f"On Base Percentage (OBP): {OBP:.3f}")
print(f"Slugging Percentage (SLG): {SLG:.3f}")
print(f"On Base Plus Slugging (OPS): {OPS:.3f}")

#write to csv
with open('player_stats.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([player_name, f"{BA:.3f}", f"{OBP:.3f}", f"{SLG:.3f}", f"{OPS:.3f}"])
print("Player stats have been saved to player_stats.csv")