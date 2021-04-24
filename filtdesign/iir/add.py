import numpy as np

def add(X,Y):
  m=len(X)
  n=len(Y)
  if m==n:
    z= m+n
  elif m>n:
    y_pad=np.append(np.zeros(m-n),Y)
    z=X+y_pad
  else:
    x_pad=np.append(np.zeros(m-n),X)
    z=x_pad + Y
  return z