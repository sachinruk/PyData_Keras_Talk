import matplotlib.pyplot as plt
import numpy as np

def plt_plot(x=None,y=None,title=""):
    if x==None:
        x = np.arange(len(y))
    plt.figure(figsize=(12,5))
    plt.plot(x,y)
    plt.title("")
    plt.show()
    
def plt_scatter(x,y):
    plt.figure(figsize=(12,5))
    plt.scatter(x,y)
    plt.show()
    
def plt_hist(x,nbins=100,title=""):    
    plt.figure(figsize=(12,5))
    plt.hist(x,nbins)
    plt.title(title)
    plt.show()    
    
def accuracy(y_pred,y_test):
    e = np.squeeze(y_pred) - np.squeeze(y_test)
    rmse = np.sqrt(np.mean(np.square(e)))
    return rmse    