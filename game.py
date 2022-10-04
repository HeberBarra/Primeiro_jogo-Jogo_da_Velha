from functions import *
import colorama


def main(players_list=None, add_new_players=True):

    if players_list is None:
            players_list = []

    try:
        while True:
            if add_new_players:
                players_list = addPlayers()

            board, starter = firstMatch()

            for times in range(9):
                turn_player = turnDecider(starter)

                clear()

                board.print_board()
                print(f'Vez do jogador{turn_player + 1}: {players_list[turn_player].player_name}')

                setPlay(board, players_list[turn_player], turn_player)
                msg = detectGameConclusion(board, players_list, turn_player)

                if msg is not None:
                    clear()
                    board.print_board()
                    print(msg)
                    for index, value in enumerate(players_list):
                        print(f'Jogador{index + 1}: {value.player_name} | \033[34mVitorias: {value.victories}\033[m| '
                              f'\033[91mDerrotas: {value.defeats}\033[m | \033[33mEmpates: {value.draws}\033[m')

                    break

            start_new_match, players_list, add_new_players = newMatch(board, players_list)

            if not start_new_match:
                break

            else:
                print('Iniciando nova partida...')

    except KeyboardInterrupt:
        print('\nVolte mais tarde por favor!')
        print('---FIM-DO-PROGRAMA---')
        colorama.deinit()
        exit()


if __name__ == '__main__':
    colorama.init()
    main()
    print('\nVolte mais tarde por favor!')
    print('---FIM-DO-PROGRAMA---')
    colorama.deinit()
