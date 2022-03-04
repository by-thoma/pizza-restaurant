from Terminal import Terminal


try:
    t = Terminal()
    t.show_menu()
    t.get_player_input()
except ValueError as er:
    print('Внимание! ',type(er),er)
except:
    print('Неизвестная ошибка')




