def getViewController(menuOption, views):
    if(menuOption == '1'):
        return (
            views.generateGraphMenu,
            generateGraphController,
        )

    if(menuOption == '2'):
        views.addEdgeMenu()

    if(menuOption == '3'):
        views.removeEdgeMenu()

    if(menuOption == '4'):
        views.checkEdgeExistenceMenu()

    if(menuOption == '5'):
        views.showGraphMenu()

    if(menuOption == '6'):
        views.showEdgeAndNodesLengthMenu()

    if(menuOption == '7'):
        views.checkNodeDegreeMenu()

    if(menuOption == '8'):
        views.runAlgorithmsMenu()


def generateGraphController(view):
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
