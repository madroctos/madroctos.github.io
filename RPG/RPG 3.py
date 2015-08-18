name = "Benn " + "Hower"
hit_points = 100
monster = "Squid"
attack_points = 25
magic_points = 30
attack_mod = 2
monster1 = 'Demon'
attack_points1 = 50
magic_points1 = 50
#potion = 40
is_alive = True
Characters = { 
               "Benn Hower":{"name":"Benn " + "Hower", "hit_points":100}, 
               "Squid":{"monster": "Squid", "attack_points":25,"magic_points": 30,"attack_mod":2}, 
			   "Demon":{"monster1": "Demon","attack_points1": 50, "magic_points1": 50}}

print "Characters are:"
for character in Characters:
	print character	
	print Characters[character]
			   
while is_alive == True:
	print Characters["Squid"]["monster"], 'attacks', Characters["Benn Hower"]["name"]
	Characters["Benn Hower"]["hit_points"] = Characters["Benn Hower"]["hit_points"] - Characters["Squid"]["attack_points"] * Characters["Squid"]["attack_mod"]
	print "hit_points are", Characters["Benn Hower"]["hit_points"]
	print monster1, 'attacks', name
	hit_points = hit_points - attack_points1
	#print "hit_points are", hit_points
	#print name,"drinks potion"
	#hit_points = hit_points + potion
	#print "hit_points are", hit_points
	user_attack = input ("type a number; ")
	hit_points = hit_points + user_attack
	print "hit_points are", hit_points
	
	if hit_points <=00:
		is_alive = False

	
print name, "is dead. Good Try"

