from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import images_rc

class MiAplicacion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Conecta las señales y ranuras aquí, si es necesario
        self.ui.pushButton.clicked.connect(self.simular)

    def simular(self):
        # Implementa la lógica de tu aplicación aquí
        # Por ejemplo, puedes obtener valores de los campos de texto:
        l2 = self.ui.lineEdit.text()
        r = self.ui.lineEdit_2.text()
        # Realiza el cálculo o la acción que necesites
        # y actualiza la interfaz si es necesario

if __name__ == "__main__":
    app = QApplication([])
    window = MiAplicacion()
    window.show()
    sys.exit(app.exec_())
