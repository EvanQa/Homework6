import random
player1_name: str = input("Enter first palyer name")
player2_name: str = input("Enter first palyer name")
player3_name: str = input("Enter first palyer name")
player4_name: str = input("Enter first palyer name")
name: str = random.choice([player1_name, player2_name, player3_name, player4_name] )
print(f'Winner is {name}')