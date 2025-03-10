from PySide6.QtWidgets import QMessageBox, QWidget


def mostrar_mensaje_alarma(parent: QWidget, mensaje: str):
    """
    Muestra un cuadro de diálogo de alarma con un mensaje específico.

    Esta función crea y muestra un cuadro de diálogo de tipo `QMessageBox` con un ícono de información
    y un botón "OK". Es útil para notificar al usuario sobre eventos importantes, como la activación
    de una alarma.

    Args:
        parent (QWidget): El widget padre sobre el cual se mostrará el cuadro de diálogo.
                          Esto asegura que el diálogo esté correctamente centrado y modal.
        mensaje (str): El mensaje que se mostrará en el cuadro de diálogo.

    Ejemplo:
        Para mostrar una alarma con el mensaje "¡Es hora de despertar!", se puede llamar a la función así:
        >>> mostrar_mensaje_alarma(parent_widget, "¡Es hora de despertar!")
    """
    aviso = QMessageBox(parent)
    aviso.setWindowTitle("¡Alarma!")
    aviso.setText(mensaje)
    aviso.setIcon(QMessageBox.Icon.Information)
    aviso.setStandardButtons(QMessageBox.StandardButton.Ok)
    aviso.exec()
