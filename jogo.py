from functions import *
import colorama


def main(players_list=None, add_new_players=True):

    try:

        if players_list is None:
            players_list = []

        while True:
            if add_new_players:
                add_players(players_list)

            board, starter = first_match()

            for times in range(9):
                starter = turn_decider(starter)

                clear()
                board.print_board()
                print(f'Vez do jogador{starter + 1}: {players_list[starter].player_name}')

                set_play(board, players_list[starter], starter)
                msg = detect_win(board, players_list, starter)

                if msg is not None:
                    clear()
                    board.print_board()
                    print(msg)
                    for index, value in enumerate(players_list):
                        print(f'Jogador{index + 1}: {value.player_name} | \033[34mVitorias: {value.victories}\033[m| '
                              f'\033[91mDerrotas: {value.defeats}\033[m | \033[33mEmpates: {value.draws}\033[m')

                    break

            start_new_match, players_list, add_new_players = new_match(board, players_list)

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
