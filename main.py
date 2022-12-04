from controllers import main_menu_controller as controllers
from utils import checkers as checker
from utils.menu_options import MAIN_MENU_OPTIONS
from views import main_menu as VIEWS

MENU_OPTION = -1

VIEWS.clearScreen()
# TELA DE GERAR GRAFO
controllers.generateGraphMenuController(VIEWS.generateGraphMenu)

while MENU_OPTION != 0:
    VIEWS.renderMainMenu()
    MENU_OPTION = input('ESCOLHA UMA OPCAO: ')

    VIEWS.clearScreen()
    if (MENU_OPTION == '0'):
        break

    if (checker.isValidMenuOption(MENU_OPTION, MAIN_MENU_OPTIONS)):
        (view, controller) = controllers.getMenuViewController(MENU_OPTION)
        controller(view)  # Controlador de acoes da view selecionada
    else:
        print('ESCOLHA UMA OPCAO VALIDA! DE 0 ATE 8')
    VIEWS.clearScreen()

VIEWS.clearScreen()
print('OBRIGADO!')
