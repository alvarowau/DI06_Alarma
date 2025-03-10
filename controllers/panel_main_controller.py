from PySide6.QtCore import QTime, QTimer
from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from util.estilos import aplicar_estilo_dialogo
from util.mensajes import mostrar_mensaje_alarma
from util.ventanas import crear_dialogo_editar_alarma, crear_dialogo_nueva_alarma
from vistas.ui_panel_main import Ui_panel_main


class PanelMain(QWidget):
    """
    Clase principal que representa el panel de control de alarmas.

    Esta clase maneja la interfaz gráfica del usuario, la gestión de alarmas y la actualización
    del reloj en tiempo real. Permite al usuario agregar, editar y eliminar alarmas, así como
    recibir notificaciones cuando una alarma está programada.

    Atributos:
        ui (Ui_panel_main): Instancia de la interfaz de usuario generada por Qt Designer.
        timer (QTimer): Temporizador para actualizar el reloj cada segundo.
        alarmas (list): Lista de diccionarios que contienen las alarmas configuradas.
        ultimo_minuto_alarma (int): Último minuto en el que se activó una alarma.
        lista_alarmas_widget (QListWidget): Widget que muestra la lista de alarmas.

    Métodos:
        __init__(): Inicializa la clase y configura la interfaz de usuario.
        actualizar_reloj(): Actualiza la hora mostrada en el reloj y verifica si hay alarmas activas.
        editar_alarma(): Abre un diálogo para agregar una nueva alarma.
        guardar_alarma(hora_texto, mensaje, dialogo): Guarda una nueva alarma en la lista.
        mostrar_lista_alarmas(): Muestra la lista de alarmas en el widget correspondiente.
        editar_eliminar_alarma(item): Permite editar o eliminar una alarma seleccionada.
        editar_alarma_existente(index): Abre un diálogo para editar una alarma existente.
        actualizar_alarma(index, hora_texto, mensaje, dialogo): Actualiza los datos de una alarma.
        eliminar_alarma(index): Elimina una alarma de la lista.
        mostrar_dialogo(titulo, mensaje, opciones=False): Muestra un diálogo con opciones personalizadas.
    """

    def __init__(self):
        """
        Inicializa la clase y configura la interfaz de usuario.

        Configura el temporizador para actualizar el reloj, inicializa la lista de alarmas
        y conecta los eventos de los botones a sus respectivos métodos.
        """
        super().__init__()
        self.ui = Ui_panel_main()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_reloj)
        self.timer.start(1000)

        self.ui.btnActivar.setText("Nueva Alarma")
        self.ui.btnActivar.clicked.connect(self.editar_alarma)

        self.alarmas = [
            {"hora": QTime(9, 30), "mensaje": "¡Despierta para la reunión!"},
            {"hora": QTime(14, 1), "mensaje": "Hora del almuerzo"},
            {"hora": QTime(19, 31), "mensaje": "Cena"},
        ]

        self.ultimo_minuto_alarma = None

        self.lista_alarmas_widget = QListWidget()
        self.ui.gridLayout_2.addWidget(self.lista_alarmas_widget, 3, 0, 1, 3)
        self.mostrar_lista_alarmas()
        self.lista_alarmas_widget.itemDoubleClicked.connect(self.editar_eliminar_alarma)

    def actualizar_reloj(self):
        """
        Actualiza la hora mostrada en el reloj y verifica si hay alarmas activas.

        Este método se ejecuta cada segundo gracias al temporizador. Si el segundo actual es 0,
        verifica si alguna alarma está programada para la hora actual y muestra una notificación.
        """
        hora_actual = QTime.currentTime()
        formato_12h = self.ui.chck12H.isChecked()
        texto_hora = hora_actual.toString("hh:mm:ss AP" if formato_12h else "HH:mm:ss")
        self.ui.relojLbl.setText(texto_hora)

        if hora_actual.second() != 0:
            return

        if self.ultimo_minuto_alarma == hora_actual.minute():
            return

        self.ultimo_minuto_alarma = hora_actual.minute()

        for alarma in self.alarmas:
            if (
                alarma["hora"].hour() == hora_actual.hour()
                and alarma["hora"].minute() == hora_actual.minute()
            ):
                mostrar_mensaje_alarma(self, alarma["mensaje"])

    def editar_alarma(self):
        """
        Abre un diálogo para agregar una nueva alarma.

        Este método crea un diálogo que permite al usuario ingresar la hora y el mensaje
        de una nueva alarma. Si el usuario acepta, la alarma se guarda en la lista.
        """
        dialogo, hora_edit, mensaje_edit, aceptar_btn, cancelar_btn = (
            crear_dialogo_nueva_alarma()
        )
        aplicar_estilo_dialogo(dialogo)
        aceptar_btn.clicked.connect(
            lambda: self.guardar_alarma(hora_edit.text(), mensaje_edit.text(), dialogo)
        )
        cancelar_btn.clicked.connect(dialogo.reject)

        dialogo.exec()

    def guardar_alarma(self, hora_texto, mensaje, dialogo):
        """
        Guarda una nueva alarma en la lista.

        Args:
            hora_texto (str): La hora de la alarma en formato "HH:mm".
            mensaje (str): El mensaje asociado a la alarma.
            dialogo (QDialog): El diálogo que contiene los campos de entrada.

        Si la hora es válida, la alarma se agrega a la lista y se actualiza la interfaz.
        Si la hora no es válida, se muestra un mensaje de error.
        """
        hora = QTime.fromString(hora_texto, "HH:mm")
        if hora.isValid():
            self.alarmas.append({"hora": hora, "mensaje": mensaje})
            self.mostrar_lista_alarmas()
            dialogo.accept()
        else:
            self.mostrar_dialogo("Error", "Hora inválida")

    def mostrar_lista_alarmas(self):
        """
        Muestra la lista de alarmas en el widget correspondiente.

        Si no hay alarmas configuradas, se muestra un mensaje indicando que no hay alarmas.
        """
        self.lista_alarmas_widget.clear()
        if not self.alarmas:
            self.lista_alarmas_widget.addItem("No hay alarmas configuradas.")
            return
        for alarma in self.alarmas:
            self.lista_alarmas_widget.addItem(
                f"- {alarma['hora'].toString('HH:mm')}: {alarma['mensaje']}"
            )

    def editar_eliminar_alarma(self, item):
        """
        Permite editar o eliminar una alarma seleccionada.

        Args:
            item (QListWidgetItem): El ítem de la lista que representa la alarma seleccionada.

        Muestra un diálogo con opciones para editar o eliminar la alarma seleccionada.
        """
        index = self.lista_alarmas_widget.row(item)
        alarma = self.alarmas[index]
        respuesta = self.mostrar_dialogo(
            "Editar/Eliminar Alarma",
            f"¿Qué deseas hacer con la alarma {alarma['hora'].toString('HH:mm')}?",
            True,
        )

        if respuesta == "Editar":
            self.editar_alarma_existente(index)
        elif respuesta == "Eliminar":
            self.eliminar_alarma(index)

    def editar_alarma_existente(self, index):
        """
        Abre un diálogo para editar una alarma existente.

        Args:
            index (int): El índice de la alarma en la lista.

        Este método permite al usuario modificar la hora y el mensaje de una alarma existente.
        """
        alarma = self.alarmas[index]
        dialogo, hora_edit, mensaje_edit, aceptar_btn, cancelar_btn = (
            crear_dialogo_editar_alarma(alarma)
        )
        aplicar_estilo_dialogo(dialogo)

        aceptar_btn.clicked.connect(
            lambda: self.actualizar_alarma(
                index, hora_edit.text(), mensaje_edit.text(), dialogo
            )
        )
        cancelar_btn.clicked.connect(dialogo.reject)

        dialogo.exec()

    def actualizar_alarma(self, index, hora_texto, mensaje, dialogo):
        """
        Actualiza los datos de una alarma.

        Args:
            index (int): El índice de la alarma en la lista.
            hora_texto (str): La nueva hora de la alarma en formato "HH:mm".
            mensaje (str): El nuevo mensaje asociado a la alarma.
            dialogo (QDialog): El diálogo que contiene los campos de entrada.

        Si la hora es válida, la alarma se actualiza y se cierra el diálogo.
        Si la hora no es válida, se muestra un mensaje de error.
        """
        hora = QTime.fromString(hora_texto, "HH:mm")
        if hora.isValid():
            self.alarmas[index]["hora"] = hora
            self.alarmas[index]["mensaje"] = mensaje
            self.mostrar_lista_alarmas()
            dialogo.accept()
        else:
            self.mostrar_dialogo("Error", "Hora inválida")

    def eliminar_alarma(self, index):
        """
        Elimina una alarma de la lista.

        Args:
            index (int): El índice de la alarma en la lista.

        Este método elimina la alarma seleccionada y actualiza la interfaz.
        """
        del self.alarmas[index]
        self.mostrar_lista_alarmas()

    def mostrar_dialogo(self, titulo, mensaje, opciones=False):
        """
        Muestra un diálogo con opciones personalizadas.

        Args:
            titulo (str): El título del diálogo.
            mensaje (str): El mensaje que se muestra en el diálogo.
            opciones (bool): Si es True, muestra opciones de editar y eliminar.

        Returns:
            str: "Editar" si se selecciona editar, "Eliminar" si se selecciona eliminar, o None si se cancela.
        """
        dialogo = QDialog(self)
        aplicar_estilo_dialogo(dialogo)
        layout = QVBoxLayout()
        etiqueta = QLabel(mensaje)
        layout.addWidget(etiqueta)

        if opciones:
            dialogo.setWindowTitle("¿Qué desea ?")
            boton_editar = QPushButton("Editar")
            boton_eliminar = QPushButton("Eliminar")
            boton_cancelar = QPushButton("Cancelar")
            layout.addWidget(boton_editar)
            layout.addWidget(boton_eliminar)
            layout.addWidget(boton_cancelar)

            boton_editar.clicked.connect(lambda: dialogo.done(1))
            boton_eliminar.clicked.connect(lambda: dialogo.done(2))
            boton_cancelar.clicked.connect(dialogo.reject)

            dialogo.setLayout(layout)
            resultado = dialogo.exec()
            return (
                "Editar" if resultado == 1 else "Eliminar" if resultado == 2 else None
            )
        else:
            boton_ok = QPushButton("OK")
            boton_ok.clicked.connect(dialogo.accept)
            layout.addWidget(boton_ok)
            dialogo.setLayout(layout)
            dialogo.exec()
            return None
