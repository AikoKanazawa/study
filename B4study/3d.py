import numpy as np
import math

x = np.linspace(-2, 2, 11)
y = np.linspace(-2, 2, 11)
z = np.linspace(-2, 2, 11)

t = 10
b = 10

def E1(t):
    return 1/2 - (16*t**2 + 1)**0.5/2

def E2(t):
    return 1/2 + (16*t**2 + 1)**0.5/2

E3 = 0

def T11(t):
    return (4*((0.5 - (16*t**2 + 1)**(0.5)/2)/(4*t) - 1/(4*t))**2 + 1)**(-0.5)*((0.5 - (16*t**2 + 1)**(0.5)/2)/(4*t) - 1/(4*t))

def T12(t):
    return (4*(((16*t**2 + 1)**(0.5)/2 + 0.5)/(4*t) - 1/(4*t))**2 + 1)**(-0.5)*(((16*t**2 + 1)**(0.5)/2 + 0.5)/(4*t) - 1/(4*t))

T13 = 2**(-0.5)

def T51(t):
    return (4*((0.5 - (16*t**2 + 1)**(0.5)/2)/(4*t) - 1/(4*t))**2 + 1)**(-0.5)

def T52(t):
    return (4*(((16*t**2 + 1)**(0.5)/2 + 0.5)/(4*t) - 1/(4*t))**2 + 1)**(-0.5)

T53 = 0

def B1(b):
    return np.exp(-b*E1(t))

def B2(b):
    return np.exp(-b*E2(t))

def B3(b):
    return np.exp(-b*E3)

f = (B1(b)+B2(b)+B3(b))**-1

def R1(x, y, z):
    return np.exp(-np.pi*((x-1)**2 + (y-1)**2 + (z-1)**2))*(B1(b)*T11(t)*T11(t)+B2(b)*T12(t)*T12(t)+B3(b)*T13*T13)

def R2(x, y, z):
    return np.exp(-np.pi*((x+1)**2 + (y-1)**2 + (z+1)**2))*(B1(b)*T11(t)*T11(t)+B2(b)*T12(t)*T12(t)+B3(b)*T13*T13)

def R3(x, y, z):
    return np.exp(-np.pi*((x+1)**2 + (y+1)**2 + (z-1)**2))*(B1(b)*T11(t)*T11(t)+B2(b)*T12(t)*T12(t)+B3(b)*T13*T13)

def R4(x, y, z):
    return np.exp(-np.pi*((x-1)**2 + (y+1)**2 + (z+1)**2))*(B1(b)*T11(t)*T11(t)+B2(b)*T12(t)*T12(t)+B3(b)*T13*T13)

def R5(x, y, z):
    return np.exp(-np.pi*((x)**2 + (y)**2 + (z)**2))*(B1(b)*T51(t)*T51(t)+B2(b)*T52(t)*T52(t)+B3(b)*T53*T53)

def P0(x, y, z):
    return f*(R1(x, y, z)+R2(x, y, z)+R3(x, y, z)+R4(x, y, z)+R5(x, y, z))

def create_grid(grid_min, grid_max, grid_n, endpoint=True):
    if endpoint:
        slope = [(grid_max[d]-grid_min[d])/(grid_n[d]-1) for d in range(3)]
    else:
        slope = [(grid_max[d]-grid_min[d])/grid_n[d] for d in range(3)]
    lst = []
    for i2 in range(grid_n[2]):
        z = slope[2]*i2 + grid_min[2]
        for i1 in range(grid_n[1]):
            y = slope[1]*i1 + grid_min[1]
            for i0 in range(grid_n[0]):
                x = slope[0]*i0 + grid_min[0]
                lst.append([x, y, z, P0(x, y, z)])

    return lst

grid_min = [-2, -2, -2]
grid_max = [2, 2, 2]
grid_n = [11, 11, 11]

create_grid(grid_min, grid_max, grid_n, endpoint=True)
lst = create_grid(grid_min, grid_max, grid_n, endpoint=True)

print(lst)