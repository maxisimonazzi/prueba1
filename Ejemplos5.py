import matplotlib.pyplot as plt
import numpy as np






"""vanina.bienvenida()
print(vanina.areacuadrado(2,3))
"""

"""print(pi)
print(e)
print(tau)   # 2*pi"""
"""print(ceil(1.6))
print(floor(1.6))
print(fabs(-5))
print(abs(-5))
print(factorial(3))"""
"""print(gcd(27,90))
print(lcm(27,90))
print(trunc(9.9999999))
print(sin(pi))
print(cos(5))
print(tan(5))
print(degrees(pi))
print(radians(180))"""

""""print(m.sqrt(25))
print(m.log(m.e))   #log natural
print(m.log10(5))
print(m.log2(5))"""


###print(m.isfinite(354))


"""print(ran.uniform(5,11))    # >=1 y <10

print(ran.randrange(0,1001))    # >=0 y <10    0-9"""


"""print(ran.randrange(0,101,5))"""

""""print(ran.sample([1,5,8,9,12,23],3))

print(ran.choice("Bienvenido"))"""


"""lista = [1,5,8,9,12,23]
print(lista)
ran.shuffle(lista)
print(lista)"""



# cantidad de milisegundos transcurridos desde el 1 de enero de 1970


# print(ran.random())




"""plt.plot([1,3,4,8,7,6,5], 'go-.')
plt.fill_between([1,2,3,4,5,6,7],[1,6,5,9,8,3,2])
plt.plot([1,2,3,4,5,6,7],[1,6,5,9,8,3,2], 'r')
plt.title("Dibujo con puntitos")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.savefig("migrafico.png")
plt.show()"""


z = np.linspace(-10,10,100)
print(z)
y = (z**2)+2
plt.plot(z,y)
plt.show()





