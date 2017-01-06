
import sys
import os
import types
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import lanDB

def hello_world():
    print('from graph1')

if __name__ == '__main__':
    hello_world()
    print([a for a in dir(lanDB) if isinstance(lanDB.__dict__.get(a), types.FunctionType)])


