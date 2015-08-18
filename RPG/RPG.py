name = "Benn " + "Hower"
hit_points = 100
monster = "Squid"
attack_points = 25
magic_points = 30
attack_mod = 2
monster1 = 'Demon'
attack_points1 = 30
magic_points1 = 50
potion = 40
print "My first monster is %s and has %d magic points and %d attack points"%(monster, magic_points, attack_points)
print "My second monster is %s and has %d magic points and %d attack points"%(monster1, magic_points1, attack_points1)
print monster, 'attacks', name
hit_points = hit_points - attack_points * attack_mod
print "hit_points are", hit_points
print monster1, 'attacks', name
hit_points = hit_points - attack_points1
print "hit_points are", hit_points
print name,"drinks potion"
hit_points = hit_points + potion
print "hit_points are", hit_points
user_attack = input ("type a number; ")
hit_points = hit_points + user_attack
print "hit_points are", hit_points
is_alive = True
if (hit_points <= 00):
	is_alive = False
	
if (is_alive == False):
	print name, "has Died. Good Try"

if (hit_points >= 0):
	is_alive = True

if (is_alive == True):
	print name, "has won the Battle."

