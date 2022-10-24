# https://www.codechef.com/LP0TO101/problems/FLOW010

# cook your dish here

dict = {'b' : "BattleShip", 'B' : "BattleShip", 'c' : "Cruiser", 'C': 'Cruiser', 'd':'Destroyer', 'D':'Destroyer', 'f':'Frigate', 'F':'Frigate'}

for _ in range(int(input())):
    print(dict[input()])
