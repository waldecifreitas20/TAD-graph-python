from controllers import view_controller as controllers
from utils import checkers as check
from views import menu as VIEWS

MENU_OPTION = -1

while MENU_OPTION != 0:
    VIEWS.renderMainMenu()
    MENU_OPTION = input('ESCOLHA UMA OPCAO: ')

    VIEWS.clearScreen()
    if (MENU_OPTION == '0'):
        break

    if (check.isValidMenuOption(MENU_OPTION)):
        (view, controller) = controllers.getViewController(MENU_OPTION, VIEWS)
        controller(view)
    else:
        print('ESCOLHA UMA OPCAO VALIDA! DE 0 ATE 8')

VIEWS.clearScreen()
print('OBRIGADO!')
