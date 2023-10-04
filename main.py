import sys
import numpy as np
from untitled import*
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, sqrt, absolute, arccos, arctan, sign

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
        if ganma <= 360:
            self.ui.lcdNumber.display(ganma)
        else:
            self.ui.lcdNumber.display(ganma-360)

    def slider_mov(self, event):
        grado = int(event*720/99)
        self.grafica.setGrado(grado) 
        if grado < 360:
            self.ui.rot_data.setText(str(grado)+"°")
        else:
            self.ui.rot_data.setText(str(grado-360)+"°")
            
    def send_data(self):  
        self.grafica.setL2(self.ui.l2_value.currentText())
        self.grafica.setRazon(self.ui.relacion_value.currentText())
        self.ui.l2_data.setText(str(self.ui.l2_value.currentText()))
        self.ui.relacion_data.setText(str(self.ui.relacion_value.currentText()))

class Canvas_grafica(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(facecolor='#0b0f47')
        super().__init__(self.fig) 
        self.ax.grid(alpha=1)
        self.ax.margins(x=0)

        self.new_L2 = 20
        self.new_relacion = 2.5
        self.new_rotacion = 45
        self.new_ganma = 36

        self.grafica_datos()

    def setGrado(self, valor_grad):
        self.new_rotacion = valor_grad*pi/180

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
        self.x5 = self.x3 + self.r_BP*cos(self.theta2 + self.new_ganma*pi/180)  # Coordenada x del extremo libre
        self.y5 = self.y3 + self.r_BP*sin(self.theta2 + self.new_ganma*pi/180)  # Coordenada y del extremo libr
        
        plt.title(None)
        arr_x=np.arange(1,5,1)
        self.x_value = [self.x1,self.x2,self.x3,self.x4,self.x5]
        for i in range(len(arr_x)):
            arr_x[i] = self.x_value[i]

        arr_y=np.arange(1,5,1)
        self.y_value = [self.y1,self.y2,self.y3,self.y4,self.y5]
        for i in range(len(arr_y)):
            arr_y[i] = self.y_value[i]

        line, =self.ax.plot(arr_x, arr_y , color='g',linewidth=3)
        self.ax.set_xlim(-100,150)
        self.ax.set_ylim(-100,150)
        self.ax.tick_params(colors='white')
        self.draw()
        line.set_ydata(np.sin(arr_x)+500)     
        QtCore.QTimer.singleShot(100, self.grafica_datos)


if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())  