import numpy as np
import sys

# first arg: csv name second arg: nc_Ar40_1n

data = np.loadtxt(str(sys.argv[1]),
                 delimiter=",", dtype=float)


print(f"Starting {str(sys.argv[1])}")

col_1 = data.T[0]/1000 # get to units of GeV

other_cols = data.T[1] / 10000 # match units to get to 10^-38/GeV


print(min(col_1), max(col_1))

new_x = np.linspace(min(col_1), max(col_1), 1001)

print(len(new_x))


xs = [i/j for i,j in zip(other_cols, col_1)]


interp_xs = np.interp(new_x, col_1, xs)

energy = np.log(new_x)


print(energy, interp_xs)



# make cross section


with open(f"xs_{str(sys.argv[2])}.dat","w") as writer:
    # Header information
    writer.write(f"# Neutrino-Ar40 nc cross section (10^-38 cm^2/GeV, natural abundance) # \n")
    writer.write("# log(energy in GeV)  nu_e      nu_mu      nu_tau      nu_e_bar      nu_mu_bar    nu_tau_bar # \n")
    writer.write("\n")
    # Data
    for i in range(len(energy)):#1,1002):
          writer.write(f"{energy[i]}   {interp_xs[i]}   {interp_xs[i]}   {interp_xs[i]}   {interp_xs[i]}   {interp_xs[i]}   {interp_xs[i]}\n")


# need to extend xs to higher energy levels 
