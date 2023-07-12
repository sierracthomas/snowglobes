import numpy as np
import sys

# first arg: csv name second arg: nc_Ar40_1n

data = np.loadtxt(str(sys.argv[1]),
                 delimiter=",", dtype=float)


print(f"Starting {str(sys.argv[1])}")

col_1 = data.T[0] * (10**(-3)) # get to units of GeV

other_cols = (data.T[1] * 10**(-4)) # match units to get to 10^-38 cm^2

print("cols 1", col_1)

# need to extend cross section to 0.2000 GeV

print(min(col_1), max(col_1))

#new_x = np.linspace(min(col_1), max(col_1), 1001)

new_x = np.linspace(0, 0.1, 1001) # 0 -> 0.1 GeV

new_x[0] = 10**(-10)

bin_size = new_x[2] - new_x[1]

print(f"bin size is {bin_size}")
# divide by corresponding energy to get to units with 1/GeV
xs = [i/j for i,j in zip(other_cols, col_1)]
#xs = other_cols / bin_size

#xs = other_cols

# interpolate between xs numbers to match number of entries in other xs's
# also, extend the number by one

interp_xs = np.interp(new_x, col_1, xs)

#interp_xs = np.append(interp_xs, interp_xs[-1])


# log(GeV) and extend the last entry to last entry
energy = np.log10(new_x)

#energy = np.append(energy, -1.0)

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
          writer.write(f"{np.format_float_scientific(np.float32(energy[i]))}   {np.format_float_scientific(np.float32(interp_xs[i]))}   {np.format_float_scientific(np.float32(interp_xs[i]))}   {np.format_float_scientific(np.float32(interp_xs[i]))}   {np.format_float_scientific(np.float32(interp_xs[i]))}   {np.format_float_scientific(np.float32(interp_xs[i]))}   {np.format_float_scientific(np.float32(interp_xs[i]))}\n")


# need to extend xs to higher energy levels 

