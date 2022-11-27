import random

bag = [str(i).ljust(3) for i in range(1, 100)]

def make_ticket():
    numbers = [str(i).ljust(3) for i in range(1, 100)]
    ticket = []
    for i in range(3):
        string = []
        for j in range(5):
            num = random.choice(numbers)
            string.append(num)
            numbers.remove(num)
        ticket.append(string)
    return ticket

def check_ticket(ticket, barrel):
  for i in range(len(ticket)):
    for j in range(len(ticket[i])):
      if barrel == ticket[i][j]:
        ticket[i][j] = '[] '
  print_ticket(ticket)
  return(ticket)

def print_ticket(ticket):
    print('_'*18)
    for i in ticket:
        print('| ', *i, '|', sep='')
    print('T'*18)

def check_count(ticket):
    counter = 0
    for i in ticket:
        counter += i.count('[] ')
    return counter

ticket_one = make_ticket()
print_ticket(ticket_one)

ticket_two = make_ticket()
print_ticket(ticket_two)

while bag and check_count(ticket_one) < 15 and check_count(ticket_two) < 15:
    if input('Взять бочонок?\n(Если просто нажать "Enter" - игра закончится)\n'):
        barrel = random.choice(bag)
        bag.remove(barrel)
        print('Вы взяли бочонок №', barrel, 'В мешке осталось', len(bag), 'бочонков')
        check_ticket(ticket_one, barrel)
        check_ticket(ticket_two, barrel)
    else:
        break

print(f'Счет по билетам\nБилет №1: {check_count(ticket_one)}\nБилет №2: {check_count(ticket_two)}')
if check_count(ticket_one) > check_count(ticket_two):
    res = 'Выиграл билет №1'
elif check_count(ticket_one) < check_count(ticket_two):
    res = 'Выиграл билет №2'
else:
    res = 'Ничья'
print(res)