
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from time_interval_helper import generate_x_ticks

def plot_power_curve(intervals, power, xscale: float, file):
    sns.set_style("whitegrid")
    plt.figure(figsize=(12,8))

    sns.lineplot(x=intervals**xscale, y=power)

    xvalues, xlabels = generate_x_ticks(intervals[-1], xscale)
    plt.xticks(xvalues, xlabels, rotation="horizontal")
    plt.xlim(1)
    plt.title("Power Curve")
    plt.xlabel("Time")
    plt.ylabel("Average Power - watts")
    plt.savefig(file)

def plot_run_time(run_time, title: str, file: str):
    sns.set_style("whitegrid")
    plt.figure(figsize=(12,8))
    sns.lineplot(x=np.arange(0, len(run_time)), y=run_time)
    plt.title(title, fontsize=14)
    plt.xlabel("Iteration")
    plt.ylabel("Time - milliseconds")
    plt.savefig(file)