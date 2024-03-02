from typing import List

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.visited = False
        self.children : List[Node] = [] 

def busqueda_profundidad(value:str,current:Node) -> Node:
    print(f"Se evalua el nodo {current.data}")
    if(current.data == value):
        return current

    current.visited = True
    for node in current.children:
        if(node.visited == False):
            final = busqueda_profundidad(value,node)
            if(final != None):
                return final
    return None

#         A
#      /  |  \
#     B   C   E
#    / \  |   |
#   D   F G   F
def main():
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    g = Node("G")

    a.children.append(b)
    a.children.append(c)
    a.children.append(e)

    b.children.append(d)
    b.children.append(f)
    
    c.children.append(g)

    e.children.append(f)

    value_to_search = input("Ingrese el valor a buscar: ")
    result = busqueda_profundidad(value_to_search,a)
    if(result == None):
        print("No se encontro el nodo")
    else:
        print(f"Se encontro el nodo {result.data}")

if __name__ == "__main__":
    main()