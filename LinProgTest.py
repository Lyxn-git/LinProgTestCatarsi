import numpy as np
from scipy.optimize import linprog
import time
start_time = time.time()


'''
lemon : cantidad de limones

l = 20 cs_l + 11 cj_l


vid : cantidad de vid

v = 20 cs_v + 50 cj_v


Restriccion seg : campo de la vega del Segura 50 000 hec

cs_l + cs_v =< cs


Restrccion jum : campo de  Jumilla 20 000 hec

cj_l + cj_v <= cj


Restriccion maquinas

0.005 (cs_l + cs_v) + 0.01 (cj_l + cj_v) =< 750


Restriccción l : es la fuerza de trabajo total  5 500 trabajadores

0.1 cs + 0.05 l_cj =< 5 500
'''


x = np.array(["cs_l", "cs_v", "cj_l", "cj_v"])

c = np.array([-25, -18, -11, -35])


# max c @ x


#so A_ub x <= b

A_ub = np.array([[1, 1, 0, 0], 
                 [0, 0, 1, 1],
                 [0.005, 0.05, 0.005, 0.05],
                 [1, 0.05, 1, 0.05]])

b = np.array([50000, 20000, 1050, 10500])


optimization = linprog(c, A_ub, b)

print(optimization)
print("--- %s seconds ---" % (time.time() - start_time))