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
        self.grafica = Canvas_grafica()
        self.ui.grafica_tmm.addWidget(self.grafica)

        # Barra de grados
        self.ui.slider_grados.valueChanged.connect(self.slider_graditos)

        # Enviar datos
        self.ui.send_value.clicked.connect(self.send_data)
        self.data()

    def slider_graditos(self, event):
        gradito = int(event*720/99)
        self.grafica.setGraditos(gradito) 
        if gradito < 360:
            self.ui.rot_data.setText(str(gradito)+"°")
        else:
            self.ui.rot_data.setText(str(gradito-360)+"°")

    
    def send_data(self):  
        self.grafica.setL2(self.ui.l2_value.currentText())
        self.grafica.setRelacion(self.ui.relacion_value.currentText())
        self.grafica.setGanma(self.ui.ganma_value.currentText())
        self.ui.l2_data.setText(str(self.ui.l2_value.currentText()))
        self.ui.relacion_data.setText(str(self.ui.relacion_value.currentText()))
        self.ui.ganma_data.setText(str(self.ui.ganma_value.currentText()))
    
    def data(self):
        L2_list = ['10','20','30','40','50','60']
        relacion_list = ['1.5','2','2.5','3','3.5','4','4.5','5']
        ganma_list = ['36','72','108','144','180','216','252','288','324']
        # self.l2_value.clear()
        self.ui.relacion_value.clear()
        self.ui.l2_value.clear()
        self.ui.l2_value.addItems(L2_list)
        self.ui.relacion_value.addItems(relacion_list)
        self.ui.ganma_value.addItems(ganma_list)
        self.ui.l2_value.setCurrentText('10')
        self.ui.relacion_value.setCurrentText('1.5')   
        self.ui.ganma_value.setCurrentText('36')



class Canvas_grafica(FigureCanvas):
    def __init__(self, parent=None):     
        self.fig , self.ax = plt.subplots(facecolor='gray')
        super().__init__(self.fig) 
        self.ax.grid(alpha=0.5)
        self.ax.margins(x=0)
        self.s=1

        #Variables
        self.new_L2 = 10
        self.new_relacion = 1.5
        self.new_ganma = 32
        self.new_rotacion = 0

        self.grafica_datos()

    def setGraditos(self, valor_grad):
        self.new_rotacion = valor_grad*pi/180

    def setL2(self, valor_L2):
        self.new_L2 = int(valor_L2)
    
    def setRelacion(self, valor_relacion):
        self.new_relacion = float(valor_relacion)
    
    def setGanma(self, valor_ganma):
        self.new_ganma = int(valor_ganma)

    def grafica_datos(self):

        #Valores de los eslabones
        self.r_manivela = self.new_L2
        self.r_biela = self.new_L2*self.new_relacion
        self.r_balancin = self.new_L2*self.new_relacion
        self.r_bancada = self.new_L2*2

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
        self.theta3 = self.phi1 - self.s * self.phi2
        self.x3 = self.r_balancin * cos(self.theta3) + self.r_bancada
        self.y3 = self.r_balancin * sin(self.theta3)
        
        plt.title("Grafica del mecanismo\n")
        arr_x=np.arange(1,5,1)
        self.x_value = [self.x1,self.x2,self.x3,self.x4]
        for i in range(len(arr_x)):
            arr_x[i] = self.x_value[i]

        arr_y=np.arange(1,5,1)
        self.y_value = [self.y1,self.y2,self.y3,self.y4]
        for i in range(len(arr_y)):
            arr_y[i] = self.y_value[i]

        line, =self.ax.plot(arr_x, arr_y , color='r',linewidth=4)

        self.draw()
        line.set_ydata(np.sin(arr_x)+500)     
        QtCore.QTimer.singleShot(100, self.grafica_datos)


if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())  