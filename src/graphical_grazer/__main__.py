from graphical_grazer.graph import Graph


def main():
    g = Graph()
    for i in range(1, 40):
        g.clear_nodes()
        g.visit(i)
    print(g.vertices.values())
    print(len(g.vertices))


if __name__ == "__main__":
    main()
