import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
# When using iPython Notebook, include:
#%matplotlib inline # iPython magic function for inline plotting

# NumPy module for unpacking data from a file:
M, Merr, V = np.loadtxt("Data/velocity_luminosity.txt", usecols=(1, 2, 3), unpack=True, skiprows=1)

logV = np.log10(V)

# Unpack values for the linear regression fit:
slope, intercept, r_value, p_value, slope_stg_error = stats.linregress(logV, M)

# Calculate linear regression fit:
predict_M = intercept + slope * logV
pred_error = M - predict_M
degrees_of_freedom = len(logV) - 2
residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)

# Plot results:
plt.scatter(logV, M)
plt.plot(logV, predict_M, "k-")
plt.errorbar(logV, M, yerr=Merr, fmt='o')
plt.xlabel("log(V) [km/s]")
plt.ylabel("$M_{B}$")

# When not using iPython Notebook, include:
plt.show()
