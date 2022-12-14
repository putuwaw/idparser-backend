import graphviz

def hello():
    return "Hello, World!"

def content():
    return '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            '''
def is_palindrome(string):
    if (string[::-1] == string):
        return True
    else:
        return False

def draw_graph():
    g = graphviz.Digraph('G')
    g.edge('Hello', 'World')
    g.edge('Hello', 'Halo')
    g.edge('World', 'Dunia')
    return g