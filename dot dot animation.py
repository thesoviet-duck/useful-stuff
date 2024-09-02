# Hello!! thanks for download this file I hope you enjoy :3
# Note: if the animation looks weird or isnt working properly try adjusting the time.sleep

import sys
import time

# dot dot function
def dot_animation():
	# Dot characters
	animation = ['.', '..', '...']
	
	# No. of cycles
	num_dots = 10
	
	# loop / do the animation
	for i in range(num_dots):
		for dots in animation:
			# Print the dot character
			sys.stdout.write(f'\rLoading{dots}')
			sys.stdout.flush()
			
			# Sleep for a short time
			time.sleep(0.5) # adjust me if stuff isnt working properly, if its too small it might not work

dot_animation()
