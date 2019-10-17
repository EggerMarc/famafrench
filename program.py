import numpy as np
import pandas as pd
#import statsmodel.api as sm
import matplotlib.pyplot as plt

data = pd.read_csv("dataset_hw02.csv",delimiter=';')

class regression:
    def __init__(self, dataset):
        self.dataset = dataset

    def setter_ind(self):
        i = 0
        variable_array = []
        while i < self.range_ind:
            value = input()
            variable_array.append(value)
            i += 1
        return variable_array

    def slr(self, ind, dep):
        #index = self.setter_ind()
        array_beta = []
        data_slr = self.dataset
        depend = data_slr[dep]
        indep = data_slr[ind]
        #if self.range_ind == 1:
        #    for i in range(len(index)):
        #        values = index[i]
        x_par = self.par(indep)
        beta1 = self.beta_solver(depend, indep)
        x1_array = []
        rng1 = np.sort(x_par)
        rng2 = rng1[-1] - rng1[0]
        beta0 = np.mean(depend) - np.mean(indep)*beta1
        print(np.mean(depend))
        segm = []
        index = []
        for k in range(len(rng1)):
            segm.append(rng1[k])
            x_out = rng1[k]*beta1 + beta0
            x1_array.append(x_out)
            index.append(round(k))

        plt.figure()
        plt.scatter(indep, depend)
        plt.plot(segm,x1_array ,color='red')
        plt.show()
        print("Beta 1 of value: " + str(beta1))
        print("Beta 0 of value: " + str(beta0))
        return

    def mlr(self, variables, depend):
        data_mlr = self.dataset
        dep = data_mlr[depend]
        data_array = []
        beta_array = []
        n = 0
        beta0 = np.mean(dep)
        while n < variables:
            print("Please input independent variable column name:")
            data_array.append(data_mlr[input()])
            n += 1
        for i in range(len(data_array)):
            x = data_array[i]
            beta_array.append(self.beta_solver(dep, x))
            beta_x = beta_array[i]
            beta0 -= beta_x*np.mean(data_array[i])
            print(beta_x)
        print(str(beta0) + " beta 0")
        return

    def beta_solver(self, y, x):
        x_var = self.par(x)
        y_var = self.par(y)
        div = []
        for n in range(len(y_var)):
            z = (x_var[n]-np.mean(x_var))*(y_var[n] - np.mean(y_var))
            div.append(z)
        up = np.sum(div)
        dw = []
        for n in range(len(x_var)):
            z = x_var[n]**2
            dw.append(z)
        down = np.sum(dw)
        beta1 = up/(down)
        return beta1


    def par(self, values):
        outp = []
        for i in range(len(values)):
            xi = values[i]
            xm = np.mean(values)
            outp.append(xi - xm)
        return outp


ind = data['Lead']
dep = data['mktrf']
regr = regression(data)
regr.slr('Lead', 'mktrf')
regr.mlr(6, 'mktrf')
