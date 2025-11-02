#calcing BA OBP SLG OPS
print("Howdy, partner!")
user_AB = int(input("Enter at bats: "))
user_H = int(input("Enter hits: "))
user_doubles = int(input("Enter # of doubles: "))
user_triples = int(input("Enter # of triples: "))
user_HR = int(input("Enter # of home runs: "))
user_BB = int(input("Enter # of walks: "))
user_hbp = int(input("Enter # of hit by pitch: "))
user_sf = int(input("Enter # of sacrifice flies: "))

print("Batting Average (BA): "+(round((user_AB/user_H)/10,3)).__str__()) #limited to 3 decimal places
print("On Base Percentage (OBP): "+(round((user_H+user_BB+user_hbp)/(user_AB+user_BB+user_hbp+user_sf),3)).__str__())
print("Slugging Percentage (SLG): "+(((user_H-user_doubles-user_triples-user_HR)+(2*user_doubles)+(3*user_triples)+(4*user_HR))/user_AB).__str__())
print("On Base Plus Slugging (OPS): "+((((user_H+user_BB+user_hbp)/(user_AB+user_BB+user_hbp+user_sf))+(((user_H-user_doubles-user_triples-user_HR)+(2*user_doubles)+(3*user_triples)+(4*user_HR))/user_AB))).__str__())