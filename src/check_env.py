import  sys
import numpy as np
import pandas as pd
import sklearn
import matplotlib


def main():
    print("Python version: ", sys.version.split()[0])
    print("numpy version: ", np.__version__)
    print("sklearn version: ", sklearn.__version__)
    print("matplotlib version: ", matplotlib.__version__)

    a = np.array([[1,2], [3,4]])
    print("A @ A.T =")
    print(a @ a.T)

if __name__ == "__main__":
    main()