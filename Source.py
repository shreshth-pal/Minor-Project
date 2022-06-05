#1st equation
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#Raw Data
  s = np.array([1.,2.,3.,5.,7.,10.]) #substrate concentration (micromoles)
  v = np.array([.2,.22,.30,.45,.41,.5]) #velocity at corresponding concentration (micromoles/sec)
# s = np.array([.005,.01,.02,.033,.1]) #substrate concentration (micromoles)
# v = np.array([.56,.9,1.47,1.92,2.63]) #velocity at corresponding concentration (micromoles/sec)
# s = np.array([2.73,5.45,8.17,10.90,40.40]) #substrate concentration (micromoles)
# v = np.array([0.124,0.181,.212,.228,.303]) #velocity at corresponding concentration (micromoles/sec)

#take reciprocal of Michaelis-Menten to plot in Langmuir Plot
Recip_S = s
Recip_V = np.reciprocal(v)
Recip_V = [x*y for x,y in zip(Recip_S,Recip_V)]

#Calculate linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(Recip_S, Recip_V)


#Draw linear regression
x = np.linspace(0., max(Recip_S)*1.5, 1000)
y = (slope * x) + intercept


print("Vmax = ", 1/slope)
print("\n1/Vmax (slope): ", slope)


plt.scatter(0, intercept, color='red')
print("\nKm/Vmax = ", intercept)
print("Km = ", intercept/slope)

km1=intercept/slope
vmax1=1/slope


#Draw x & y origins
plt.axhline(0, color='black')
plt.axvline(0, color='black')

#Graph scatter points
plt.scatter(Recip_S, Recip_V)

#Graph linear regresison
plt.plot(x, y)

#Titles and labels
plt.xlabel('[S] ($\mu$M)')
plt.ylabel('[S]/v ($\mu$M/s)')
plt.title('The Langmuir plot')

plt.show()



#2nd equation


#take reciprocal of Michaelis-Menten to plot in Lineweaver-Burke
Recip_S = np.reciprocal(s)
Recip_V = np.reciprocal(v)

#Calculate linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(Recip_S, Recip_V)


#Draw linear regression
x = np.linspace(0., max(Recip_S)*1.5, 1000)
y = (slope * x) + intercept

plt.scatter(0, intercept, color='red')
print("\n1/Vmax = ", intercept)
print("Vmax = ", 1/intercept)


print("\nKm/Vmax (slope): ", slope)
print("Km = ", slope/intercept)


km2=slope/intercept
vmax2=1/intercept

#Draw x & y origins
plt.axhline(0, color='black')
plt.axvline(0, color='black')

#Graph scatter points
plt.scatter(Recip_S, Recip_V)

#Graph linear regresison
plt.plot(x, y)

#Titles and labels
plt.xlabel('1/[S] (1/$\mu$M)')
plt.ylabel('1/v (s/$\mu$M)')
plt.title('Lineweaver-Burk plot')

plt.show()



#3rd equation Eadie hofstee



#take reciprocal of Michaelis-Menten to plot in Eadie Hofstee
Recip_S = np.reciprocal(s)
Recip_V = v
Recip_S = [x*y for x,y in zip(Recip_S,Recip_V)]

#Calculate linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(Recip_S, Recip_V)


#Draw linear regression
x = np.linspace(0., max(Recip_S)*1.5, 1000)
y = (slope * x) + intercept
print('\nmax',max(Recip_S))

print("\n-Km (slope): ", slope)
print("Km = ", 0-slope)


plt.scatter(0, intercept, color='red')
print("\nVmax = ", intercept)

km3=0-slope
vmax3=intercept


#Draw x & y origins
plt.axhline(0, color='black')
plt.axvline(0, color='black')

#Graph scatter points
plt.scatter(Recip_S, Recip_V)

#Graph linear regresison
plt.plot(x, y)

#Titles and labels
plt.xlabel('v ($\mu$M)')
plt.ylabel('v/[S] (1/s)')
plt.title('The Eadie-Hofstee plot')

plt.show()



print('\n')
print('\n')

#drawing Michelis Menten Curve

#Draw x & y origins
plt.axhline(0, color='black')
plt.axvline(0, color='black')
#Graph scatter points
plt.scatter(s,v)

#Draw michelis km and rmax value
x = np.linspace(0., max(s)*1.5, 1000)
y = (vmax1*x)/(km1+x)

#Graph Michelis curve
plt.plot(x, y)

#Draw michelis km and rmax value
x = np.linspace(0., max(s)*1.5, 1000)
y = (vmax2*x)/(km2+x)

#Graph Michelis curve
plt.plot(x, y)

#Draw michelis km and rmax value
x = np.linspace(0., max(s)*1.5, 1000)
y = (vmax3*x)/(km3+x)

#Graph Michelis curve
plt.plot(x, y)
#Titles and labels
plt.xlabel('[S] ($\mu$M)')
plt.ylabel('v ($\mu$M/s)')
plt.title('Cumulative Michaelis Menten plot')

plt.show()


#Best Model fitting
#function to return expected v for a given km and vmax

def expected_v(km,vmax):
  
  
  arr_y = (vmax*s)/(km+s)
  return arr_y

#function to find root mean square erro from a given array and data given

def rmse(arr=[]):

  sum=0
  for i in range(len(arr)):
    sum=sum+(v[i]-arr[i])**2
  sum/=len(arr)
  return math.sqrt(sum) 




  





#km and vmax
arr_km=[km1,km2,km3]
arr_vmax=[vmax1,vmax2,vmax3]
rmse_min=10000009
best_km,best_vmax=10000009,10000009
a=0
b=0
for i in arr_km:
  a+=1
  b=0
  for j in arr_vmax:
      b+=1
      arr_expected_v=expected_v(i,j)
      print("Km%d : %8f, Vmax%d : %8f, RMSE : %8f " % (a,i,b,j,rmse(arr_expected_v)))
      
      if rmse(arr_expected_v) < rmse_min:
        best_km=i
        best_vmax=j
        rmse_min=rmse(arr_expected_v)



#best km and vmax
print("\nKm(final) = ", best_km)  
print("\nVmax(final) = ", best_vmax)
#drawing Michelis Menten Curve

#Draw x & y origins
plt.axhline(0, color='black')
plt.axvline(0, color='black')
#Graph scatter points
plt.scatter(s,v)

#Draw michelis km and rmax value
x = np.linspace(0., max(s)*1.5, 1000)
y = (best_vmax*x)/(best_km+x)
#Graph Michelis curve
plt.plot(x, y)
#Titles and labels
plt.xlabel('[S] ($\mu$M)')
plt.ylabel('v ($\mu$M/s)')
plt.title('Michelis Menten best curve')

plt.show()


