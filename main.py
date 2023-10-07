import sys
import numpy as np
import matplotlib.pyplot as plt
from untitled import*
from numpy import pi, sin, cos, sqrt, arccos, arctan, sign
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import QTimer

class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.grafica = Canvas_grafica()
        self.ui.grafica_tmm.addWidget(self.grafica)

        # Slider rotamecanismo
        self.ui.slider_rotador.valueChanged.connect(self.slider_mov)

        #Slider ganma
        self.ui.slider_ganma.valueChanged.connect(self.slider_ganmita) 

        # Enviar datos
        self.ui.pushButton.clicked.connect(self.send_data)

    def slider_ganmita(self, event):
        ganma = int(event)
        self.ui.lcdNumber.display(ganma)
        
    def slider_mov(self, event):
        grado = int(event)
        self.grafica.setGrado(grado) 
        self.ui.label_11.setText(str(grado)+"°")
        self.grafica.grafica_datos()

    def send_data(self):  
        self.grafica.setL2(self.ui.entrada_longitud.text())
        self.grafica.setRazon(self.ui.entrada_relacion.text())
        self.grafica.setGanma(self.ui.lcdNumber.value())
        self.ui.entrada_longitud.setText(str(self.ui.entrada_longitud.text()))
        self.ui.entrada_relacion.setText(str(self.ui.entrada_relacion.text()))
        self.ui.lcdNumber.value()
        QTimer.singleShot(25000, self.clear_inputs)
    
    def clear_inputs(self):
        self.ui.entrada_longitud.clear()
        self.ui.entrada_relacion.clear()
        self.ui.lcdNumber.display(0)

class Canvas_grafica(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(facecolor='#0b0f47')
        super().__init__(self.fig) 
        self.ax.grid(alpha=0.25)
        self.ax.margins(x=0)

        self.new_L2 = 25
        self.new_relacion = 1.5
        self.new_rotacion = 90
        self.new_ganma = 10
        
        self.trayectoria_x = []
        self.trayectoria_y = []

        self.grafica_datos()

    def setGrado(self, valor_grado):
        self.new_rotacion = valor_grado*pi/180

    def setL2(self, valor_L2):
        self.new_L2 = int(valor_L2)
    
    def setRazon(self, valor_relacion):
        self.new_relacion = float(valor_relacion)
    
    def setGanma(self, valor_ganma):
        self.new_ganma = int(valor_ganma)

    def grafica_datos(self):
        
        #Valores de los eslabones
        self.r_manivela = self.new_L2
        self.r_biela = self.new_L2*self.new_relacion
        self.r_balancin = self.new_L2*self.new_relacion
        self.r_bancada = self.new_L2*2
        self.r_BP = self.new_L2*self.new_relacion

        #Coordenadas manivela
        self.x1 = 0
        self.y1 = 0
        
        #Coordenadas balancin
        self.x4 = self.r_bancada
        self.y4 = 0

        #Mecanismo
        self.theta1 = self.new_rotacion
        self.x2 = self.r_manivela * cos(self.theta1)
        self.y2 = self.r_manivela * sin(self.theta1)
        self.e = sqrt((self.x2 - self.r_bancada) ** 2 + (self.y2 ** 2))
        self.phi2 = arccos((self.e ** 2 + self.r_balancin ** 2 - self.r_biela ** 2) / (2 * self.e * self.r_balancin))
        self.phi1 = arctan(self.y2 / (self.x2 - self.r_bancada)) + (1 - sign(self.x2 - self.r_bancada)) * pi / 2
        self.theta3 = self.phi1 - self.phi2
        self.x3 = self.r_balancin * cos(self.theta3) + self.r_bancada
        self.y3 = self.r_balancin * sin(self.theta3)
        self.theta2 = arctan((self.y3 - self.y2) / (self.x3 - self.x2)) + (1 - sign(self.x3 - self.x2)) * pi / 2
        self.x5 = self.x3 - self.r_BP*cos(self.theta2 - self.new_ganma*pi/180)
        self.y5 = self.y3 - self.r_BP*sin(self.theta2 - self.new_ganma*pi/180) 
        
        plt.title(None)
        arr_x=np.arange(1,5,1)
        self.x_value = [self.x1,self.x2,self.x3,self.x4]
        for i in range(len(arr_x)):
            arr_x[i] = self.x_value[i]

        arr_y=np.arange(1,5,1)
        self.y_value = [self.y1,self.y2,self.y3,self.y4]
        for i in range(len(arr_y)):
            arr_y[i] = self.y_value[i]

        self.ax.clear()

        line_x = [self.x3, self.x5, self.x2]
        line_y = [self.y3, self.y5, self.y2]

        self.trayectoria_x.append(self.x5)
        self.trayectoria_y.append(self.y5)

        self.ax.scatter(self.x5, self.y5, color='b', s=50)
        line, = self.ax.plot(arr_x, arr_y , color='g',linewidth=3)
        self.ax.plot(line_x, line_y, color='r', linewidth=3)
        self.ax.set_xlim(-100,150)
        self.ax.set_ylim(-100,150)
        self.ax.tick_params(colors='white')
        self.ax.plot(self.trayectoria_x, self.trayectoria_y, "--" ,color='m', linewidth=1)
        self.draw()
        line.set_ydata(np.sin(arr_x)+500)
        QtCore.QTimer.singleShot(100, self.grafica_datos)
        
if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())  