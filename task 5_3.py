# Создайте программу для игры в 'Крестики-нолики'.

print('''
Привет! Это игра "Крестики-нолики".
Чтобы сделать ход, введи номер клетки,
куда хочешь поставить свой символ:


''')
position = []
for i in range(1,10):
        position.append(i)

move = "O"

while True:
    if move == "O":
        move = "X"
    else:
        move = "O"
    print(f"{position[0]:^5}|{position[1]:^5}|{position[2]:^5}")
    print("---------------")
    print(f"{position[3]:^5}|{position[4]:^5}|{position[5]:^5}")
    print("---------------")
    print(f"{position[6]:^5}|{position[7]:^5}|{position[8]:^5}")
    step = int(input(f"\n\nХод {'игрока' if move == 'X' else 'противника'}: "))

    position[step - 1] = move
# осталось дописать логику игры
def winner(position):
    VAR_POBED=((0,1,2),
               (3,4,5),
               (6,7,8),
               (0,3,6),
               (1,4,7),
               (2,5,8),
               (0,4,8),
               (2,4,6))
    for i in varianti_pobed:
        if position[i[0]]==position[i[1]]==position[i[2]]!=HODI:
            winner=doska[i[0]]
            return winner
        if HODI not in doska:
            return NICHYA
    return None