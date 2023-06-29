import matplotlib.pyplot as plt
import numpy as np
import csv


data = np.loadtxt("neutrino-xs.csv",
                 delimiter=",", dtype=float)

adata = np.loadtxt("aneutrino-xs.csv",
                 delimiter=",", dtype=float)

strengths = np.loadtxt("transition_strengths.csv",
           delimiter=",", dtype=float)

nu_curve_x = data.T[0]
nu_curve_y = data.T[1]

anu_curve_x = adata.T[0]
anu_curve_y = adata.T[1]

def step_xs(energy_ind, x, y, strengths = strengths.T):
    new = []
    energy_val = strengths[0][energy_ind]
    max_e = max(strengths[0])
    for i, val in enumerate(x):
        # go through list of x data
        if val > max_e:
            # check if current x energy is greater than  9.8 MeV
            # if it is, all energy stages can happen
            new.append(y[i]* ((strengths[1][energy_ind])/sum(strengths[1])))
            continue
            
        elif energy_val > val:
            # no cross section, since current energy value doesn't excite desired state
            new.append(0)
            continue
            
        else:
            # if current energy supplied is not greater than 9.8, adjustments to xs need to be made
            #if val < 4.473 or energy_val < 4.473:
            #    temp = 0
            if val >= 4.473 and val <= 5.393:
                # can only be 4.473 excited, so total cross section 
                if energy_val == 4.473:
                    temp = y[i]
                else:
                # this is probably redundant
                    temp = 0
            elif val >= 5.393 and val <= 6.085:
                temp = y[i] * (strengths[1][energy_ind] / sum(strengths[1][0:2]))
                #can be excited by either 4.473 or 5.393
            elif val >= 6.085 and val <= 7.25:
                temp = y[i] * (strengths[1][energy_ind] / sum(strengths[1][0:3]))
                # can be excited by 4.473, 5.393, and 6.085
            elif val >= 7.25 and val <= 9.8:
                temp = y[i] * (strengths[1][energy_ind] / sum(strengths[1][0:4]))
                # can be excited by 4.473, 5.393, 6.085, and 7.25
            else:
                print("Check case: ", energy_val, val, x[i], y[i])
                temp = 0
                
            new.append(temp)
            
    # missing values between these energy levels
    return new


for i, val in enumerate(strengths.T[0]):
    nu, anu = [], []
    nu = np.array((nu_curve_x, (step_xs(i, nu_curve_x, nu_curve_y))))
    anu = np.array((anu_curve_x, (step_xs(i, anu_curve_x, anu_curve_y))))
    np.savetxt(f"{val}_nu.csv", nu.T,
              delimiter = ",")
    np.savetxt(f"{val}_anu.csv", anu.T,
              delimiter = ",")



    
