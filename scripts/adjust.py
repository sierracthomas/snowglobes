import numpy as np
import sys

# first arg: csv name second arg: nc_Ar40_1n

data = np.loadtxt(str(sys.argv[1]),
                 delimiter=",", dtype=float)


print(f"Starting {str(sys.argv[1])}")

col_1 = data.T[0] / 1000 # get to units of GeV

other_cols = data.T[1] * 10000 # match units to get to 10^-38


# need to extend cross section to 0.2000 GeV

print(min(col_1), max(col_1))

new_x = np.linspace(min(col_1), max(col_1), 1000)#1001)


# divide by corresponding energy to get to units with 1/GeV
xs = [i/j for i,j in zip(other_cols, col_1)]


# interpolate between xs numbers to match number of entries in other xs's
# also, extend the number by one
interp_xs = np.interp(new_x, col_1, xs)

interp_xs = np.append(interp_xs, interp_xs[-1])


# log(GeV) and extend the last entry to last entry
energy = np.log(new_x)

energy = np.append(energy, -1.0)

print(energy, interp_xs)

print(len(energy), len(interp_xs))

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

