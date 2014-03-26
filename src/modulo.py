#! /usr/bin/python
#! encoding: UTF-8

PI35DT = 3.1415926535897932384626433832795028

def aprox(n):
  s = 0.0
  for i in range (1,n+1):
    xi = (i-0.5)/n
    fxi = 4.0/(1+xi**2)
    s += fxi
  r = 1.0/n*s
  return r



if __name__=="__main__":
  import sys
  print "%.35g" % PI35DT
  parametro1 = sys.argv[0]
  if (len(sys.argv)==1):
    print "El modo de uso es %s <numero intervalos> <numero veces>" % parametro1
    n = int (raw_input('Introduzca n: '))
    m = int (raw_input('Introduzca m: '))
  elif (len(sys.argv)==3):
    n = int(sys.argv[1])
    m = int(sys.argv[2])
  else:
    print "El modo de uso es %s <numero intervalos> <numero veces>" % parametro1
    n = 0
    m = 0
  l = [ ]
  for i in range (1, m+1):
    api = aprox(n*i)
    l = l+[api]
  print l