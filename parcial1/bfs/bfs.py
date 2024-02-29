class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.children = [] 

def busqueda_amplitud(value:str,root:Node) -> Node:
    toEvaluate = [root]
    evaluated = []
    i = 0
    while len(toEvaluate) > 0:
        i += 1
        print(f"Iteracion {i}")
        current = toEvaluate.pop(0)
        if(current in evaluated):
            continue
        if current.data == value:
            return current
        evaluated.append(current)
        toEvaluate.extend(current.children)
    return None

#       A
#      / \
#     B - C
#    /         
#   D - E - F
def main():
    a = Node("A")
    b = Node("B")
    c = Node("C")
    a.children = [b,c]
    b.children = [a,c]
    c.children = [a,b]

    d = Node("D")
    e = Node("E")
    f = Node("F")

    b.children.append(d)
    d.children.append(e)
    e.children.append(f)

    value_to_search = input("Ingrese el valor a buscar: ")
    result = busqueda_amplitud(value_to_search,b)
    if(result == None):
        print("No se encontro el nodo")
    else:
        print(f"Se encontro el nodo {result.data}")

if __name__ == "__main__":
    main()