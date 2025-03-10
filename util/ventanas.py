from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QTimeEdit,
    QLineEdit,
    QPushButton,
    QWidget,
)
from PySide6.QtCore import QTime


def crear_dialogo_nueva_alarma(parent=None):
    """
    Crea un diálogo para agregar una nueva alarma.

    Este diálogo permite al usuario ingresar la hora y el mensaje de una nueva alarma.
    Incluye campos para editar la hora y el mensaje, así como botones para aceptar o cancelar.

    Args:
        parent (QWidget, optional): El widget padre sobre el cual se mostrará el diálogo.
                                    Si se proporciona, el diálogo heredará el estilo del padre.
                                    Defaults to None.

    Returns:
        tuple: Una tupla que contiene:
            - dialogo (QDialog): El diálogo creado.
            - hora_edit (QTimeEdit): El widget para editar la hora.
            - mensaje_edit (QLineEdit): El widget para editar el mensaje.
            - aceptar_btn (QPushButton): El botón para aceptar la nueva alarma.
            - cancelar_btn (QPushButton): El botón para cancelar la operación.
    """
    dialogo = QDialog(parent)
    dialogo.setWindowTitle("Nueva Alarma")
    dialogo.resize(450, 300)

    if parent:
        dialogo.setStyleSheet(parent.styleSheet())
    else:
        dialogo.setStyleSheet(
            """
            QDialog { background-color: #303030; color: #e0e0e0; }
            QLabel { color: #e0e0e0; font-size: 18px; }
            QTimeEdit, QLineEdit { background-color: #424242; color: #e0e0e0; border: 1px solid #616161; font-size: 18px; padding: 5px; }
            QPushButton {
                background-color: #2196f3;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 4px;
                font-size: 16px;
                text-transform: uppercase;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #1976d2; }
            """
        )

    layout = QVBoxLayout()
    hora_edit = QTimeEdit(QTime.currentTime())
    mensaje_edit = QLineEdit()

    layout.addWidget(QLabel("Hora:"))
    layout.addWidget(hora_edit)
    layout.addWidget(QLabel("Mensaje:"))
    layout.addWidget(mensaje_edit)

    botones = QWidget()
    layout_botones = QVBoxLayout()
    botones.setLayout(layout_botones)

    aceptar_btn = QPushButton("Aceptar")
    cancelar_btn = QPushButton("Cancelar")

    layout_botones.addWidget(aceptar_btn)
    layout_botones.addWidget(cancelar_btn)

    layout.addWidget(botones)
    dialogo.setLayout(layout)

    return dialogo, hora_edit, mensaje_edit, aceptar_btn, cancelar_btn


def crear_dialogo_editar_alarma(alarma, parent=None):
    """
    Crea un diálogo para editar una alarma existente.

    Este diálogo permite al usuario modificar la hora y el mensaje de una alarma existente.
    Incluye campos prellenados con los valores actuales de la alarma y botones para aceptar o cancelar.

    Args:
        alarma (dict): Un diccionario que contiene la información de la alarma a editar.
                       Debe tener las claves "hora" (QTime) y "mensaje" (str).
        parent (QWidget, optional): El widget padre sobre el cual se mostrará el diálogo.
                                    Si se proporciona, el diálogo heredará el estilo del padre.
                                    Defaults to None.

    Returns:
        tuple: Una tupla que contiene:
            - dialogo (QDialog): El diálogo creado.
            - hora_edit (QTimeEdit): El widget para editar la hora, prellenado con la hora actual de la alarma.
            - mensaje_edit (QLineEdit): El widget para editar el mensaje, prellenado con el mensaje actual de la alarma.
            - aceptar_btn (QPushButton): El botón para aceptar los cambios.
            - cancelar_btn (QPushButton): El botón para cancelar la operación.
    """
    dialogo = QDialog(parent)
    dialogo.setWindowTitle("Editar Alarma")
    dialogo.resize(450, 300)

    if parent:
        dialogo.setStyleSheet(parent.styleSheet())
    else:
        dialogo.setStyleSheet(
            """
            QDialog { background-color: #303030; color: #e0e0e0; }
            QLabel { color: #e0e0e0; font-size: 18px; }
            QTimeEdit, QLineEdit { background-color: #424242; color: #e0e0e0; border: 1px solid #616161; font-size: 18px; padding: 5px; }
            QPushButton {
                background-color: #2196f3;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 4px;
                font-size: 16px;
                text-transform: uppercase;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #1976d2; }
            """
        )

    layout = QVBoxLayout()
    hora_edit = QTimeEdit(alarma["hora"].addSecs(60))
    mensaje_edit = QLineEdit(alarma["mensaje"])

    layout.addWidget(QLabel("Hora:"))
    layout.addWidget(hora_edit)
    layout.addWidget(QLabel("Mensaje:"))
    layout.addWidget(mensaje_edit)

    botones = QWidget()
    layout_botones = QVBoxLayout()
    botones.setLayout(layout_botones)

    aceptar_btn = QPushButton("Aceptar")
    cancelar_btn = QPushButton("Cancelar")

    layout_botones.addWidget(aceptar_btn)
    layout_botones.addWidget(cancelar_btn)

    layout.addWidget(botones)
    dialogo.setLayout(layout)

    return dialogo, hora_edit, mensaje_edit, aceptar_btn, cancelar_btn
