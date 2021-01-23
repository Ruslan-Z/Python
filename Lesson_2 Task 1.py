mine_liste = ['True', 334, 3.14, -20, None]
def type_is(i): # не додумался как можно ручным пересчетом списка определить тип
    # данных каждого элемента, и, т.к. немного знаю тему функций, воспользовался ею.
    for i in range(len(mine_liste)):
        print(type(mine_liste[i]))
    return
type_is(mine_liste)

