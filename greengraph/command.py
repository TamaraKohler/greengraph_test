from argparse import ArgumentParser
from .graph import Greengraph
from matplotlib import pyplot as plt

def process():
    parser = ArgumentParser(description = "Determine starting and ending locations")
    
    parser.add_argument('start')
    parser.add_argument('end')
    parser.add_argument('steps')
    
    mygraph = Greengraph(arguments.start,arguments.end)
    data = mygraph.green_between(arguments.steps)
    plt.plot(data)
    
if __name__ = "__main__":
    process()