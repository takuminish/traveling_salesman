import numpy as np
import matplotlib.pyplot as plt

def plot_start():
    
    x = np.asarray([1,2,3,4,5,6])
    y = np.asarray([1,2,3,4,5,6])

    fig = plt.figure()

    ax1 = fig.add_subplot(111)


    ax1.plot(x,y,"-o")

    plt.show()

if __name__ == '__main__':
    print("plot start")
    plot_start()
