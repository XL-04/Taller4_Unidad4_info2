from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QVBoxLayout
from PyQt5.QtCore import Qt
from model.paciente import Paciente
import random
import os
from datetime import datetime
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure


class Controlador:
    def __init__(self):

        # Cargar vistas
        self.ventana_principal = uic.loadUi("view/ventana_principal.ui")
        self.ventana_registro = uic.loadUi("view/ventana_registro.ui")

        # Lista de pacientes en memoria
        self.pacientes = []

        # Conexiones de la ventana principal
        self.ventana_principal.botonRegistrar.clicked.connect(self.abrir_registro)
        self.ventana_principal.tablaPacientes.itemSelectionChanged.connect(self.mostrar_detalles)
        self.ventana_principal.botonSimular.clicked.connect(self.simular_signos)
        self.ventana_principal.botonExportar.clicked.connect(self.exportar_txt)
        self.ventana_principal.botonGrafico.clicked.connect(self.ver_grafico)
        self.ventana_registro.botonGuardar.clicked.connect(self.guardar_paciente)
        self.ventana_principal.showMaximized()

    # Ventana de registro 
    def abrir_registro(self):
        self.limpiar_campos()
        self.ventana_registro.show()

    def limpiar_campos(self):
        self.ventana_registro.campoNombre.clear()
        self.ventana_registro.campoID.clear()
        self.ventana_registro.campoEdad.clear()
        self.ventana_registro.campoBPM.clear()
        self.ventana_registro.campoSpO2.clear()
        self.ventana_registro.campoTemp.clear()

    def guardar_paciente(self):
        try:
            nombre = self.ventana_registro.campoNombre.text().strip()
            idp = self.ventana_registro.campoID.text().strip()
            edad_text = self.ventana_registro.campoEdad.text().strip()
            bpm_text = self.ventana_registro.campoBPM.text().strip()
            spo2_text = self.ventana_registro.campoSpO2.text().strip()
            temp_text = self.ventana_registro.campoTemp.text().strip()

            # Validaciones básicas
            if not nombre or not idp or not edad_text or not bpm_text or not spo2_text or not temp_text:
                QMessageBox.warning(self.ventana_registro,
                                    "Campos incompletos",
                                    "Por favor, completa todos los campos.")
                return
            
            # Validar campos numéricos
            try:
                edad = int(edad_text)
                bpm = int(bpm_text)
                spo2 = int(spo2_text)
                temp = float(temp_text)
            except ValueError:
                QMessageBox.warning(self.ventana_registro,
                                    "Entrada inválida",
                                    "Edad, BPM, SpO₂ y Temperatura deben ser valores numéricos.")
                return

            # Validar ID único
            for pac in self.pacientes:
                if pac.get_id() == idp:
                    QMessageBox.warning(self.ventana_registro,
                                        "ID duplicado",
                                        "Ya existe un paciente registrado con ese ID.")
                    return

            # Crear y almacenar paciente
            nuevo = Paciente(nombre, idp, edad, bpm, spo2, temp)
            self.pacientes.append(nuevo)

            self.actualizar_tabla()
            self.ventana_registro.close()

        except Exception as e:
            QMessageBox.critical(self.ventana_registro,
                                "Error no esperado",
                                f"Ocurrió un error: {e}")


    # Tabla y panel de detalles
    def actualizar_tabla(self):
        tabla = self.ventana_principal.tablaPacientes
        tabla.setRowCount(len(self.pacientes))

        for i, p in enumerate(self.pacientes):
            tabla.setItem(i, 0, QTableWidgetItem(str(p.get_nombre())))
            tabla.setItem(i, 1, QTableWidgetItem(str(p.get_id())))
            tabla.setItem(i, 2, QTableWidgetItem(str(p.calcular_riesgo())))

    def mostrar_detalles(self):

        tabla = self.ventana_principal.tablaPacientes
        fila = tabla.currentRow()
        if fila == -1:
            return

        p = self.pacientes[fila]

        self.ventana_principal.labelBPM.setText(str(p.get_bpm()))
        self.ventana_principal.labelSpO2.setText(str(p.get_spo2()))
        self.ventana_principal.labelTemp.setText(str(p.get_temperatura()))

        riesgo = p.calcular_riesgo()
        panel = self.ventana_principal.PanelRiesgo

        if riesgo == "Normal":
            panel.setStyleSheet("background-color: green;")
        elif riesgo == "Alerta":
            panel.setStyleSheet("background-color: orange;")
        else:
            panel.setStyleSheet("background-color: red;")

    # Simulación de signos
    def simular_signos(self):

        tabla = self.ventana_principal.tablaPacientes
        fila = tabla.currentRow()

        if fila == -1:
            QMessageBox.warning(self.ventana_principal, "Atención", "Selecciona un paciente primero.")
            return

        p = self.pacientes[fila]

        p.set_bpm(random.randint(50, 130))
        p.set_spo2(random.randint(80, 100))
        p.set_temperatura(round(random.uniform(35.0, 40.3), 1))

        # Refrescar interfaz
        self.actualizar_tabla()
        self.mostrar_detalles()

    # Exportar datos a TXT
    def exportar_txt(self):

        carpeta = "exports"
        os.makedirs(carpeta, exist_ok=True)

        fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        ruta_archivo = os.path.join(carpeta, f"pacientes_{fecha}.txt")

        try:
            with open(ruta_archivo, "w", encoding="utf-8") as f:

                f.write("LISTADO DE PACIENTES EXPORTADOS\n")
                f.write("=====================================\n")
                f.write(f"Fecha de exportación: {datetime.now()}\n")
                f.write("\n\n")

                for p in self.pacientes:
                    f.write(f"Nombre: {p.get_nombre()}\n")
                    f.write(f"ID: {p.get_id()}\n")
                    f.write(f"Edad: {p.get_edad()}\n")
                    f.write(f"BPM: {p.get_bpm()}\n")
                    f.write(f"SpO₂: {p.get_spo2()}\n")
                    f.write(f"Temperatura: {p.get_temperatura()}\n")
                    f.write(f"Riesgo: {p.calcular_riesgo()}\n")
                    f.write("-------------------------------------\n")

            QMessageBox.information(None, 
                                    "Exportación exitosa",
                                    f"Datos guardados en:\n{ruta_archivo}")

        except Exception as e:
            QMessageBox.critical(None, "Error", f"No se pudo exportar:\n{e}")

    def ver_grafico(self):
        fila = self.ventana_principal.tablaPacientes.currentRow()
        if fila == -1:
            QMessageBox.warning(None, "Atención", "Selecciona un paciente primero")
            return

        p = self.pacientes[fila]
        self.ventana_grafico = uic.loadUi("view/ventana_grafico.ui")

        fig = Figure(figsize=(5, 4))
        canvas = Canvas(fig)
        ax = fig.add_subplot(111)

        # Datos del paciente
        labels = ["BPM", "SpO2", "Temp"]
        valores = [p.get_bpm(), p.get_spo2(), p.get_temperatura()]

        ax.bar(labels, valores)
        ax.set_title(f"Signos vitales de {p.get_nombre()}")
        ax.set_ylabel("Valor")

        # Insertar canvas 
        layout = QVBoxLayout()
        layout.addWidget(canvas)
        self.ventana_grafico.graficoWidget.setLayout(layout)

        self.ventana_grafico.show()
