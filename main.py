import  sys
from PyQt5.QtWidgets  import  QApplication, QMainWindow

from Models.userModel import ModelUser
from Views.loginViews import Ui_ViewLogin
from Controllers.userController import ControllerUser


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_principal = QMainWindow()
    modelo = ModelUser()
    vista = Ui_ViewLogin()
    vista.setupUi(ventana_principal)
    controlador = ControllerUser(modelo, vista,ventana_principal)
    ventana_principal.show()
    sys.exit(app.exec_())
