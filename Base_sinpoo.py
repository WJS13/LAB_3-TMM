import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parametros de entrada
L2 = int(input("Ingrese longitud de la manivela: "))  #manivela
r = float(input("Ingrese relación: "))
L3 = r*L2  #acoplador
L4 = r*L2  #balancin
L1 = 2*L2  #bancada
BP = r*L2  #acoplador curvado
ganma = int(input("Ingrese el angulo del acoplador: ")) #angulo acoplador

rot_num = 50  #rotaciones
increment = 0.1  # incremento de angulo

# Matriz de ángulos
R_Angles = np.arange(0, rot_num * 2 * np.pi, increment)

# Coordenadas del punto central de la manivela
x1 = 0
y1 = 0

# Coordenadas del punto central del balancin
x4 = L1 
y4 = 0

X2 = np.zeros(len(R_Angles))
Y2 = np.zeros(len(R_Angles))
RR_Angle = np.zeros(len(R_Angles))
X3 = np.zeros(len(R_Angles))
Y3 = np.zeros(len(R_Angles))
X5 = np.zeros(len(R_Angles))
Y5 = np.zeros(len(R_Angles))

# Recorrido del acoplador curvado
acoplador_curvado_x = []
acoplador_curvado_y = []

# Posiciones para el punto 3 y 4
for index, R_Angle in enumerate(R_Angles, start=0):
    theta1 = R_Angle
    x2 = L2 * np.cos(theta1)
    y2 = L2 * np.sin(theta1)
    e = np.sqrt((x2 - L1) ** 2 + (y2 ** 2))
    phi2 = np.arccos((e ** 2 + L4 ** 2 - L3 ** 2) / (2 * e * L4))
    phi1 = np.arctan(y2 / (x2 - L1)) + (1 - np.sign(x2 - L1)) * np.pi / 2
    theta3 = phi1 - phi2
    RR_Angle[index] = theta3

    x3 = L4 * np.cos(theta3) + L1
    y3 = L4 * np.sin(theta3)

    theta2 = np.arctan((y3 - y2) / (x3 - x2)) + (1 - np.sign(x3 - x2)) * np.pi / 2
    x5 = x3 + BP * -np.cos(theta2 - ganma*np.pi/180)  # Coordenada x del extremo libre
    y5 = y3 + BP * -np.sin(theta2 - ganma*np.pi/180)  # Coordenada y del extremo libre

    X2[index] = x2
    Y2[index] = y2
    X3[index] = x3
    Y3[index] = y3
    X5[index] = x5
    Y5[index] = y5

    # Agregar puntos al recorrido del acoplador curvado
    acoplador_curvado_x.append(x5)
    acoplador_curvado_y.append(y5)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(
    111, aspect="equal", autoscale_on=False, xlim=(-100, 150), ylim=(-100,150)
)
ax.grid(alpha=0.5)
ax.set_title("Curva de acoplador")
ax.set_xticklabels([])
ax.set_yticklabels([])

# Estilizar las líneas y puntos
line1, = ax.plot([], [], '-', lw=3, color='g')
line2, = ax.plot([], [], '-', lw=3, color='g')
line3, = ax.plot([], [], '-', lw=3, color='g')
line4, = ax.plot([], [], '-', lw=2, markersize=8, color='r')
line5, = ax.plot([], [], '-', lw=2, markersize=8, color='r')
points4, = ax.plot([], [], 'bo', markersize=8)

# Agregar líneas para el recorrido del acoplador curvado
acoplador_curvado_line, = ax.plot([], [], '--', lw=2, color='m')

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    line4.set_data([], [])
    line5.set_data([], [])
    points4.set_data([], [])
    acoplador_curvado_line.set_data([], [])
    return line1, line2, line3, line4,line5, points4, acoplador_curvado_line


def animate(i):
    x_points_manivela = [x1, X2[i]]
    y_points_manivela = [y1, Y2[i]]
    x_points_biela = [X2[i], X3[i]]
    y_points_biela = [Y2[i], Y3[i]]
    x_points_balancin = [X3[i], x4]
    y_points_balancin = [Y3[i], y4]
    x_points_punto_movil = [X3[i], X5[i]]

    line1.set_data(x_points_manivela, y_points_manivela)
    line2.set_data(x_points_biela, y_points_biela)
    line3.set_data(x_points_balancin, y_points_balancin)
    line4.set_data(x_points_punto_movil, [Y3[i], Y5[i]])
    line5.set_data([X5[i], X2[i]], [Y5[i], Y2[i]])

    # Actualizar puntos
    points4.set_data([X5[i]], [Y5[i]])

    # Actualizar líneas para el recorrido
    
    if i <= (len(R_Angles)/rot_num + 2):  
        acoplador_curvado_line.set_data(acoplador_curvado_x[:i], acoplador_curvado_y[:i])

    return line1, line2, line3, line4, line5, points4, acoplador_curvado_line

ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=len(X2), interval=40, blit=True, repeat=False
)

plt.show()