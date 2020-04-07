from matplotlib import pyplot as plt

def r_graph(info):
    month = list()
    value = list()
    for i in range(1, len(info)+1):    
       if info[i] != 0:
           month.append(str(i)+"월")
           value.append(info[i])
    plt.bar
    plt.show()

