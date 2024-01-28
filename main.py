
people = {}

rest = 'yes'
i= 0
while rest == 'yes':
  name = input("what is your name?: ").lower()
  bid = int(input("what's your bid?: "))
  i +=1
  people[i] = {"name": name, "bid": bid}
  rest = input("Are there any other bidders? type 'yes' or 'no':" ).lower()


highest = 0

for key in people:
  if people[key]["bid"] > highest:
    highest = people[key]["bid"]

for key in people:
  if people[key]["bid"] == highest:
    print(f"Highest bidder is {people[key]['name'].title()} and the bid is {people[key]['bid']}")