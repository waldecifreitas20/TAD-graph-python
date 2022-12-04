def _generateOptions(quantity):
    return {f'{option}' for option in range(0,quantity)}


MAIN_MENU_OPTIONS = _generateOptions(10)

GENERATE_GRAPH_MENU_OPTIONS = _generateOptions(8)