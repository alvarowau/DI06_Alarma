def aplicar_estilo_dialogo(dialogo):
    """
    Aplica un estilo consistente a los diálogos de la aplicación.

    Este método establece una hoja de estilo (stylesheet) para el diálogo proporcionado,
    asegurando que todos los diálogos de la aplicación tengan un aspecto uniforme y moderno.
    El estilo incluye colores oscuros para el fondo, texto claro, y botones con un diseño
    atractivo y responsive.

    Args:
        dialogo (QDialog): El objeto QDialog al que se aplicará el estilo. Este debe ser
                           un diálogo válido de PySide6.

    Ejemplo:
        Para aplicar el estilo a un diálogo, se puede llamar a la función así:
        >>> dialogo = QDialog()
        >>> aplicar_estilo_dialogo(dialogo)
    """
    dialogo.setStyleSheet(
        """
        QDialog { background-color: #303030; color: #e0e0e0; }
        QLabel { color: #e0e0e0; }
        QTimeEdit, QLineEdit { background-color: #424242; color: #e0e0e0; border: 1px solid #616161; }
        QPushButton { background-color: #2196f3; color: white; border: none; padding: 8px 16px; border-radius: 4px; }
        QPushButton:hover { background-color: #1976d2; }
        """
    )
