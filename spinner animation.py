# HELLO!!! Thx for downloading ME! I hope I serve you well :3
# Note: if you make the time.sleep value too small the animation will become Janky so dont blame the Duck

import sys
import time


def spinning_animation():
	# spinner characters
	spinner = ['|', '/', '-', '\\']
	
	# No. of spins
	num_spins = 19
	
	# loop / do the animation
	for i in range(num_spins):
		# Print the spinner character
		sys.stdout.write(f'\rPolishing {spinner[i % len(spinner)]}')
		sys.stdout.flush()
		
		# Sleep for a short time
		time.sleep(0.35)

spinning_animation()
