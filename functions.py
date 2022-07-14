from Classes import players, boards
import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def add_players(players_list):
    for time in range(2):
        while True:
            try:
                player_name = input(f'Digite o nome do jogador{time + 1}: ').strip().capitalize()
                is_right = input(f'O nome {player_name} para o jogador {time + 1} esta correto?[Y/N]: ').lower()[0]

            except IndexError:
                print('Digite alguma coisa!')

            else:
                if is_right in 'ysapc':
                    break
                else:
                    print('Digite novamente!')

        players_list.append(players.Player(player_name))


def first_match():
    board = boards.Boards()
    starter = 1
    return board, starter


def turn_decider(starter):

    if starter == 1:
        return 0

    else:
        return 1


def set_play(board, player, turn_player):
    while True:
        try:
            position = int(input('Digite o numero de uma posicao do tabuleiro: ').strip())
            is_right = input('A posicao colocada esta certa?[Y/N]: ').strip().lower()[0]

        except ValueError:
            print('Digite um numero!')

        except IndexError:
            print('Digite alguma coisa!')

        else:

            if is_right in 'ysapc':

                if position in board.table:
                    break

                else:
                    print('Posicao invalida!')

            else:
                print('Digite novamente!')

    position -= 1

    if turn_player == 0:
        board.add_play_on_board(position, "\033[91mX\033[m")

    else:
        board.add_play_on_board(position, "\033[34mO\033[m")

    player.add_play(position)


def detect_win(board, players_list, starter):
    if players_list[starter].detect_victory():
        if starter == 0:
            players_list[starter + 1].add_defeat()

        else:
            players_list[starter - 1].add_defeat()

        return f'Vitoria do jogador{starter + 1}: {players_list[starter].player_name}!'

    elif not board.verify_table():
        players_list[0].add_draw()
        players_list[1].add_draw()
        return f'Empate!'

    else:
        return None


def new_match(board, players_list):
    while True:
        try:
            restart = input('Desejar iniciar uma nova partida?[Y/N]: ').strip().lower()[0]

        except IndexError:
            print('Digite alguma coisa!')

        else:
            if restart in 'ysapc':
                break
            else:
                return False, players_list, False

    board.reset_board()

    while True:
        try:
            new_players = input('Desejar comecar uma partida com novos jogadores?[Y/N}: ').strip().lower()[0]

        except IndexError:
            print('Digite alguma coisa!')

        else:
            if new_players in 'ysapc':
                new_players = True
                break
            else:
                new_players = False
                break

    if new_players:
        players_list = []

    else:
        for value in players_list:
            value.reset_plays()

    return True, players_list, new_players
