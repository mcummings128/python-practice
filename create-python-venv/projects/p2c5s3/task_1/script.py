# Another script that has been made for you. From OpenClassrooms exercise "Manage Virtual Environments Using Requirements Files", Task 1

import scipy.special


cube_root = scipy.special.cbrt(27)
print('The cube root of 27 is {cube_root} because {cube_root} * {cube_root} * {cube_root} is 27'
      .format(**{'cube_root': cube_root}))
