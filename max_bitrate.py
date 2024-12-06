# max_bitrate.py.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  tx_w: Transmitter Wattage
#  tx_gain_db: Transmitter Gain
#  freq_hz: Frequency in herz
#  dist_km: Distance in km
#  rx_gain_db: reciever gain
#  n0_j: Noise spectral density
#  bw_hz: channel bandwidth
#  ...
# Output:
#  max achievable bitrate
#
# Written by William Sosnowski
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math
# "constants"
# e.g., R_E_KM = 6378.137

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
tx_w=float('nan')
tx_gain_db=float('nan')
freq_hz=float('nan')
dist_km=float('nan')
rx_gain_db=float('nan')
n0_j=float('nan')
bw_hz=float('nan')

# parse script arguments
if len(sys.argv)==8:
 tx_w = sys.argv[1]
 tx_gain_db=sys.argv[2]
 freq_hz=sys.argv[3]
 dist_km=sys.argv[4]
 rx_gain_db=sys.argv[5]
 n0_j=sys.argv[6]
 bw_hz=sys.argv[7]
else:
 print(\
  'Usage: '\
  'python3 max_bitrate.py tx_w tx_gain freq_hz dist_km rx_gain_db n0_j bw_hz'\
 )
 exit()

# write script below this line
ll=-1 #line loss
atmo_loss=0
Speed_of_light=2.99792458*10**8
lamda=Speed_of_light/freq_hz
C=tx_w*ll*tx_gain_db*((lamda/(4*math.pi*dist_km)))**2*atmo_loss*rx_gain_db
N=n0_j*bw_hz
r_max=bw_hz*math.log2(1+(C/N))
print(math.floor(r_max))