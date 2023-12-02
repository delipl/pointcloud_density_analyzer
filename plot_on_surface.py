import matplotlib.pyplot as plt
import numpy as np


def plot_on_xy(title: str, cloud: np.array):
    x = cloud[:, 0]
    y = cloud[:, 1]
    plt.figure("Plot on xy")
    ax = plt.axes()
    plt.grid()
    ax.set_xlabel("Oś Y", fontsize=8)
    ax.set_ylabel("Oś X", fontsize=8)
    ax.tick_params(axis="both", labelsize=8)
    plt.title(title)
    ax.plot(x, y, marker=".", linestyle="")
    plt.tight_layout()
    plt.show(block=False)


def plot_on_yz(title: str, cloud: np.array):
    y = cloud[:, 1]
    z = cloud[:, 2]
    plt.figure("Plot on yz")
    ax = plt.axes()
    plt.grid()
    ax.set_xlabel("Oś Y", fontsize=8)
    ax.set_ylabel("Oś Z", fontsize=8)
    ax.tick_params(axis="both", labelsize=8)
    plt.title(title)

    ax.plot(y, z, marker=".", linestyle="")
    plt.tight_layout()
    plt.show(block=False)
