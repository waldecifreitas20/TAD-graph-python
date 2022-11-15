from controllers import view_controller as controllers
from utils import checkers as checker
from utils.menu_options import MAIN_MENU_OPTIONS
from views import menu as VIEWS

MENU_OPTION = -1

while MENU_OPTION != 0:
    VIEWS.clearScreen()
    VIEWS.renderMainMenu()
    MENU_OPTION = input('ESCOLHA UMA OPCAO: ')

    VIEWS.clearScreen()
    if (MENU_OPTION == '0'):
        break

    if (checker.isValidMenuOption(MENU_OPTION, MAIN_MENU_OPTIONS)):
        (view, controller) = controllers.getViewController(MENU_OPTION, VIEWS)
        controller(view) # Controlador de acoes da view selecionada
    else:
        print('ESCOLHA UMA OPCAO VALIDA! DE 0 ATE 8')

VIEWS.clearScreen()
print('OBRIGADO!')
