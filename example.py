# Plot NZ-chart of weak decay rates at 1 GK and save as png
# Takes reaclib file as first command line argument
# Requires matplotlib 3.4+

import sys
import numpy as np
import matplotlib.pyplot as plt
from ratelib import Library, Rate, RateFilter


# Prepare filter function
def is_decay(r: Rate):
    return True if r.chapter in (1, 2, 3, 11) else False


# Load REACLIB and filter weak decays
try:
    database = Library(sys.argv[1])
except (IndexError, FileNotFoundError):
    print("Provide REACLIB database as argument")
    exit(1)

# Get library of weak decays
rate_filter = RateFilter(rtype="w", filter_function=is_decay)
weak_decay_lib = database.find_rates(rate_filter)

# Create rate matrix
decay_matrix = np.full((120, 240), np.nan)
for r in weak_decays.rates:
    rate = r.rval(1.)  # get rate at 1 GK
    z = r.initial[0].Z
    n = r.initial[0].N
    if np.isnan(rate_matrix[z, n]):
        rate_matrix[z, n] = rate
    else:
        rate_matrix[z, n] += rate

# Plot rate chart
fig, ax = plt.subplots()
im = ax.imshow(np.log(rate_matrix), cmap='hot_r', origin='lower',
               interpolation='none')
ax.set_xticks(range(0, 260, 40))
ax.set_yticks(range(0, 140, 40))
ax.set_xlabel("N")
ax.set_ylabel("Z")
ax.set_aspect('equal', adjustable='box')
fig.colorbar(im, location="top", label="ln Rate", ax=ax)
plt.savefig("weakdecay.png")
