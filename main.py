import sys
from PySide6.QtWidgets import QApplication
from controllers.panel_main_controller import PanelMain

if __name__ == "__main__":
    """
    Punto de entrada de la aplicación.

    Este script inicia la aplicación Qt y muestra la ventana principal (`PanelMain`).
    La aplicación se ejecuta en un bucle de eventos hasta que el usuario cierra la ventana.

    Ejemplo:
        Para ejecutar la aplicación, simplemente ejecuta este script:
        >>> python main.py

    Notas:
        - `PanelMain` es la clase que define la ventana principal de la aplicación.
        - `QApplication` gestiona el flujo de la aplicación y los eventos de la interfaz gráfica.
        - `sys.exit(app.exec())` asegura que la aplicación se cierre correctamente al salir.
    """
    app = QApplication(sys.argv)
    window = PanelMain()
    window.show()
    sys.exit(app.exec())
