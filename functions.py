from Classes import players, boards
import os

PLAYER_1_SYMBOL  = 'X'
PLAYER_2_SYMBOL  = 'O'
PLAYER_1_COLOR   = '\033[91m'
PLAYER_2_COLOR   = '\033[34m'
YES_POSIBILITIES = 'ysapc'

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def addPlayers():
    players_list = []
    for time in range(2):
        while True:
            try:
                player_name = input(f'Digite o nome do jogador{time + 1}: ').strip().capitalize()
                is_right = input(f'O nome {player_name} para o jogador {time + 1} está correto?[Y/N]: ').lower()[0]

            except IndexError:
                print('Digite alguma coisa!')

            else:
                if is_right in YES_POSIBILITIES:
                    break
                else:
                    print('Digite novamente!')

        players_list.append(players.Player(player_name))

    return players_list


def firstMatch():
    return boards.Boards(), 1


def turnDecider(turn_player):
    if turn_player == 1:
        return 0

    else:
        return 1


def setPlay(board, player, turn_player):
    while True:
        try:
            position = int(input('Digite o número de uma posição do tabuleiro: ').strip())
            is_right = input('A posição colocada está certa?[Y/N]: ').strip().lower()[0]

        except ValueError:
            print('Digite um número!')

        except IndexError:
            print('Digite alguma coisa!')

        else:

            if is_right in YES_POSIBILITIES:

                if position in board.table:
                    break

                else:
                    print('Posição invalida!')

            else:
                print('Digite novamente!')

    position -= 1

    if turn_player == 0:
        board.add_play_on_board(position, f'{PLAYER_1_COLOR}{PLAYER_1_SYMBOL}\033[m')

    else:
        board.add_play_on_board(position, f'{PLAYER_2_COLOR}{PLAYER_2_SYMBOL}\033[m')

    player.add_play(position)


def detectGameConclusion(board, players_list, starter):
    if players_list[starter].detect_victory():
        if starter == 0:
            players_list[starter + 1].add_defeat()

        else:
            players_list[starter - 1].add_defeat()

        return f'Vitoria do jogador{starter + 1}: {players_list[starter].player_name}!'

    elif not board.verify_table():
        players_list[0].add_draw()
        players_list[1].add_draw()
        return 'Empate!'

    return None


def newMatch(board, players_list):
    while True:
        try:
            restart = input('Desejar iniciar uma nova partida?[Y/N]: ').strip().lower()[0]

        except IndexError:
            print('Digite alguma coisa!')

        else:
            if restart in YES_POSIBILITIES:
                break
            else:
                return False, players_list, False

    board.reset_board()

    while True:
        try:
            new_players = input('Desejar começar uma partida com novos jogadores?[Y/N}: ').strip().lower()[0]

        except IndexError:
            print('Digite alguma coisa!')

        else:
            if new_players in YES_POSIBILITIES:
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
