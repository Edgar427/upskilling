class Monster:
	def __init__(self, name,  health, attack):
		self.name = name
		self.health = health
		self.attack = attack

	def fight(self, target):
		target.health -= self.attack 
		print(f"{self.name} attacked for {self.attack}")
		print(f"{target.name} now has {target.health}")
		if target.health <= 0:
			print(f"{target.name} has now fallen")
			
		
	
monster1 = Monster(name="centaur", health=100, attack=20)
monster2 = Monster(name= "goblin",health=100 , attack= 50)

print(monster1.name, monster1.health , monster1.attack)
print(monster2.name, monster2.health , monster2.attack)

monster2.fight(monster1)
monster2.fight(monster1)

