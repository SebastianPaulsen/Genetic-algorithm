import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def Plot3DCallback(GA_ENGINE):
  """
  función de callback que generar un plot 3D de la población en el espacio
  de busqueda determinado por la función f(x,y).
  """
  # obtener generación actual
  # solo se graficará cada 5 generaciones
  if GA_ENGINE.getCurrentGeneration()%5 != 0:
    return None

  # definir límites del espacio cartesiano X, Y
  res = 256
  X = np.linspace(0.0, 10.0, res)
  Y = np.linspace(0.0, 10.0, res)
  Z = np.zeros( (res, res) )

  # para cado punto x, y en el espacio
  for i in range(res):
    for j in range(res):
      # valores x, y
      x, y = X[i], Y[j]

      # evaluar función
      Z[j, i] = np.sin(x*3*np.pi/10)*np.sin(y*3*np.pi/10)*np.exp(-((x - 5)**2)/36)

  # visualizar superficie de la función
  X, Y = np.meshgrid(X, Y)

  fig = plt.figure( figsize=(8,8) )
  ax = fig.gca(projection='3d')

  ax.contour(X, Y, Z, 50, cmap='jet')
  ax.set_xlabel('X'); ax.set_ylabel('Y')

  # ----------------------------------------------------------------------------
  # agregar población al gráfico
  POPULATION = GA_RUN.getPopulation().internalPop
  for indiv in POPULATION:
    chromosome = indiv.getInternalList()
    x, y = chromosome
    z = indiv.getRawScore() - 5.0

    ax.scatter(x, y, z, c='b', s=70)

  return None
