import backward_iteration as bi
import forward_iteration as fi
import scipy_calculate as sc
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    resultB=bi.backward_iteration()
    resultF=fi.forward_iteration()
    resultB=np.array(resultB)
    resultF=np.array(resultF)
    resultR=np.array(sc.calculate_Integral())
    stabilityB=resultB-resultR
    stabilityF=resultF-resultR
    x=np.arange(0,16)
    plt.figure()
    plt.title("stability")
    plt.xlabel("n")
    plt.ylabel("stability")
    plt.plot(x,stabilityB,linestyle='-',color='blue',label="backward")
    plt.plot(x,stabilityF,linestyle='--',color='green',label="forward")
    plt.legend()
    plt.show()
    
    plt.figure()
    plt.title("plotresult")
    plt.xlabel("n")
    plt.ylabel("result")
    plt.plot(x,resultB,linestyle='-',color='blue',label="backward")
    plt.plot(x,resultF,linestyle='-',color='green',label="forward")
    plt.plot(x,resultR,linestyle='--',color='red',label="SCIPY")
    plt.legend()
    plt.show()




