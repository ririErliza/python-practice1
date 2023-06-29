# from packageName.moduleName import className
from space.planet import Planet
from space.calc import planet_mass, planet_vol

naboo = Planet('Naboo', 300000,8,  'Naboo system')

naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_vol = planet_vol(naboo.radius)


print(naboo.name) # Naboo
print(naboo_mass) # 1.0794602698650665e+22
print(naboo_vol) # 377040000000.0

