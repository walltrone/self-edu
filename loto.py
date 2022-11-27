import random

ticket_count = int(input())
tickets = []
bag = [str(i).ljust(3) for i in range(100)]
counters = []


def make_ticket(n):
    numbers = [str(i).ljust(3) for i in range(100)]
    ticket = []
    for i in range(3):
        string = []
        for j in range(5):
            num = random.choice(numbers)
            string.append(num)
            numbers.remove(num)
        ticket.append(string)
    ticket.append(str(n + 1).rjust(2, "0"))
    print_ticket(ticket)
    return ticket


def check_ticket(ticket, barrel):
    for n in range(len(ticket)):
        for i in range(len(ticket[n]) - 1):
            for j in range(len(ticket[n][i])):
                if barrel == ticket[n][i][j]:
                    ticket[n][i][j] = '[] '
        print_ticket(ticket[n])
    return ticket


def print_ticket(ticket):
    print(f'____Билет № {ticket[3]}____')
    for i in ticket:
        if type(i) == list:
            print('| ', *i, '|', sep='')
    print('T' * 18)


def check_count(tickets):
    for n in range(len(tickets)):
        counter = 0
        for i in tickets[n]:
            counter += i.count('[] ')
        counters[n] = counter
    return counters


for i in range(ticket_count):
    tickets.append(make_ticket(i))
    counters.append(0)

while bag and 15 not in check_count(tickets):
    if input('Взять бочонок?\n(Если просто нажать "Enter" - игра закончится)\n'):
        barrel = random.choice(bag)
        bag.remove(barrel)
        print('Вы взяли бочонок №', barrel, 'В мешке осталось', len(bag), 'бочонков')
        check_ticket(tickets, barrel)
    else:
        break
res = check_count(tickets)
for n in range(len(res)):
    if res[n] == 15:
        print(f'Выиграл билет №{tickets[n][-1]}')
