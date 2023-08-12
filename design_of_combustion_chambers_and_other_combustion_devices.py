
# Determine design value of c* (characteristic velocity) for an engine thrust chamber given:
# 1. Propellant combination
# 2. Thrust chamber O/F mixture ratio
# 3. Chamber total pressure at nozzle inlet/nozzle stagnation pressure
# 4. Nozzle expansion area ratio
# 5. Properties of the product gas at the nozzle inlet (specific heat ratio ¨gamma¨, molecular mass ¨M¨ and temperature
# at nozzle inlet Tc_ns), determined from the previous design parameters from design tables or other sources

import math

g = 32.2 # [ft/s^2], at sea level

print("Assuming conditions at nozzle inlet...\n")
Tc_ns = float(input("Introduce chamber total temperature[R]: ")) # [Rankine]
M = float(input("Introduce molecular weight of the product gas[lb/mol]: ")) # [lb/mol]
gamma = float(input("Introduce specific heat ratio of the product gas: ")) # [adimensional]

R = 1544/M # [ft/Rankine]

c_star = math.sqrt(g*gamma*R*Tc_ns)/(gamma*math.sqrt((2/(gamma+1))**((gamma+1)/(gamma-1)))) # [ft/s]; Eq. 1-32a (Huzel, Huang)
c_star_corr = float(input("Introduce reaction efficiency: ")) # Carried from Sample calculation 4-1 (Huzel, Huang)
print("c_star[ft/s]: ",c_star*c_star_corr)

# Thrust coefficient (C_f) computation using Eq. 1.33a (Huzel, Huang). Inputs:
# 1. gamma
# 2. Chamber total pressure at nozzle inlet/nozzle stagnation pressure P_c_ns [psia]
# 3. Nozzle expansion area ratio (epsilon)
# 4. Ambient pressure (P_a) [psia] - Assumed
# 5. Pressure at nozzle exit (P_e) [psia] - Numerically computed using Eq. 1-20 or using a numerical solver (RPA)

P_c_ns = float(input("Introduce chamber total pressure[psia]: "))
epsilon = float(input("Introduce nozzle expansion area ratio: "))
P_a = float(input("Introduce ambient pressure to evaluate performance[psia]: "))
# Numerical solver to be implemented
P_e = float(input("Introduce total pressure at nozzle outlet[psia]: "))
# Numerical solver to be implemented

C_f = math.sqrt((2*gamma**2)/(gamma-1)*(2/(gamma+1))**((gamma+1)/(gamma-1))*(1-(P_e/P_c_ns)**((gamma-1)/gamma)))\
+ epsilon*((P_e-P_a)/P_c_ns)
C_f_corr = float(input("Introduce nozzle efficiency: ")) # Carried from Sample calculation 4-1 (Huzel, Huang)
print("C_f: ",C_f*C_f_corr)

# Compute specific impulse (I_s) using Eq. 1-31c (Huzel, Huang). Inputs:
# 1. g
# 2. c_star
# 3. C_f

I_s = (c_star*c_star_corr)*(C_f*C_f_corr)/g
print("I_s[s]:", I_s)

# After major thrust-chamber operating parameters (propellant combination, thrust level, chamber pressure) &
# performance parameter (c_star, C_f & I_s) have been established from engine system requirements and performance
# calculations, thrust-chamber configuration layout can begin, starting with the throat area usually being the
# starting point. Eq. 1-33 (Huzel, Huang) to be used. C_f, P_c_ns & F are the knowns.