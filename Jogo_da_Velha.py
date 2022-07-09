from os import name, system

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
players = []
starter = 1


class Player:

    def __init__(self, player_name, score=0, victories=0, defeats=0, draws=0, plays=None):
        if plays is None:
            plays = set()
        self.player_name = player_name
        self.score = score
        self.victories = victories
        self.defeats = defeats
        self.draws = draws
        self.plays = plays

    def add_victory(self):
        self.victories += 1

    def add_defeat(self):
        self.defeats += 1

    def add_draw(self):
        self.draws += 1

    def add_play(self, position):
        self.plays.add(position)


def clear():
    # Clears the screen
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def print_board():
    piece_one = f'|{"-" * 7}|{"-" * 7}|{"-" * 7}|'
    piece_two = f'|{" " * 7}|{" " * 7}|{" " * 7}|'

    clear()
    print(f'/{"-" * 23}\\')
    print(piece_two)
    print(f'|   {board[6]}   |   {board[7]}   |   {board[8]}   |')
    print(piece_two)
    print(piece_one)
    print(piece_two)
    print(f'|   {board[3]}   |   {board[4]}   |   {board[5]}   |')
    print(piece_two)
    print(piece_one)
    print(piece_two)
    print(f'|   {board[0]}   |   {board[1]}   |   {board[2]}   |')
    print(piece_two)
    print(f'\\{"-" * 23}/')


def add_players():
    for times in range(2):
        while True:
            try:
                name_p = input(f'Digite o nome do jogador{times + 1}: ')
                is_right = input(f'O nome ({name_p}) para o jogador{times + 1} esta certo?[S/N]: ').lower()[0]
            except KeyboardInterrupt:
                print('Por favor volte mais tarde!')
                print('---FIM---')
                exit()
            else:
                if is_right in 'yspc':
                    break
                else:
                    print(f'Digite o nome do jogador{times + 1} novamente')

        players.append(Player(name_p))

    print(f'/{"-" * 4}Lista de Jogadores{"-" * 4}/')
    for key, value in enumerate(players):
        print(f'Jogador{key + 1}: {value.player_name}')


def get_play():
    while True:
        try:
            play_position = int(input('Digite o numero de uma posicao do tabuleiro: '))
        except ValueError:
            print('Digite um valor valido!')
        except KeyboardInterrupt:
            print('Por favor volte mais tarde!')
            print('---FIM---')
            exit()
        else:
            if play_position in board:
                return play_position
            else:
                print('Digite uma posicao valida!')


def who_goes_first():
    global starter
    starter += 1
    result = starter % 2
    return result


def decide_turn_player(who_start):
    for turn in range(9):
        if turn in [0, 2, 4, 6, 8]:
            return who_start
        else:
            if who_start == 0:
                return who_start + 1
            else:
                return who_start - 1


def set_play_on_board(turn_player):
    play_position = get_play()
    play_position -= 1
    if turn_player == 0:
        board[play_position] = '\033[31mX\033[m'
    else:
        board[play_position] = '\033[34mO\033[m'
    players[turn_player].add_play(play_position)


def verify_board():
    for c in range(1, 10, 1):
        if c in board:
            return True
    return False


def detect_victory(turn_player):
    player_set = players[turn_player].plays
    if 6 in player_set and 7 in player_set and 8 in player_set:
        win(turn_player)
        return True
    elif 3 in player_set and 4 in player_set and 5 in player_set:
        win(turn_player)
        return True
    elif 0 in player_set and 1 in player_set and 2 in player_set:
        win(turn_player)
        return True
    elif 6 in player_set and 3 in player_set and 0 in player_set:
        win(turn_player)
        return True
    elif 7 in player_set and 4 in player_set and 1 in player_set:
        win(turn_player)
        return True
    elif 8 in player_set and 5 in player_set and 2 in player_set:
        win(turn_player)
        return True
    elif 6 in player_set and 4 in player_set and 2 in player_set:
        win(turn_player)
        return True
    elif 8 in player_set and 4 in player_set and 0 in player_set:
        win(turn_player)
        return True
    else:
        return False


def win(turn_player):
    players[turn_player].add_victory()
    if turn_player == 0:
        players[1].add_defeat()
    else:
        players[0].add_defeat()


def main():
    global board
    global vitoria

    add_players()

    while True:
        for c in range(9):
            print_board()
            player_turn = decide_turn_player(who_goes_first())

            print(f'Vez do jogador {player_turn + 1}: {players[player_turn].player_name}')

            set_play_on_board(player_turn)

            if detect_victory(player_turn):
                vitoria = True
                break

            if not verify_board():
                players[0].add_draw()
                players[1].add_draw()
                break

        print_board()
        
        if vitoria:
            print(f'\n\033[32mVitoria\033[m do jogador{player_turn + 1}: {players[player_turn].player_name}\n')

        else:
            print(f'\n\033[36mEmpate!\033[m\n')

        for key, value in enumerate(players):
            print(f'Jogador: {value.player_name} | \033[32mVitorias: {value.victories}\033[m'
                  f' | \033[31mDerrotas: {value.defeats}\033[m | \033[36mEmpates: {value.draws}\033[m')

        new_match = input('Nova partida?[S/N]: ').lower()[0]

        if new_match in 'syapc':
            print('Comecando nova partida...')

        else:
            break

    print('----FIM----')


if __name__ == '__main__':
    main()
