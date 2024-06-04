#formas de usar o módulo matematica
#importam tudo do módulo
import matematica

#importando elementos específicos do módulo
from matematica import somar, Pi as Pi_mat
#Pi no módulo matematica vem para INICIO como Pi_mat
#from matematica import somar as somar_mat, Pi as Pi_mat

from estatistica.descritiva import media, max, minimo
from estatistica.inferencial import valor

Pi = 39563

print(matematica.Pi)
print(matematica.multiplicar(4.0, 6.0))

print(Pi_mat)
print(somar(33, 67))