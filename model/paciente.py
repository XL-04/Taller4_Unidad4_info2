class Paciente:
    def __init__(self, nombre, id_paciente, edad, bpm, spo2, temperatura):
        # Validaciones básicas
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        if not isinstance(id_paciente, str) or id_paciente.strip() == "":
            raise ValueError("El ID no puede estar vacío.")

        # Validación fisiológica mínima
        if edad <= 0 or edad > 120:
            raise ValueError("Edad fuera de rango lógico.")
        if bpm < 20 or bpm > 250:
            raise ValueError("BPM fuera de rango permitido.")
        if spo2 < 50 or spo2 > 100:
            raise ValueError("SpO2 fuera de rango permitido.")
        if temperatura < 25 or temperatura > 45:
            raise ValueError("Temperatura fuera de rango permitido.")

        # Asignación privada
        self.__nombre = nombre
        self.__id = id_paciente
        self.__edad = edad
        self.__bpm = bpm
        self.__spo2 = spo2
        self.__temperatura = temperatura

    # Getters
    def get_nombre(self): return self.__nombre
    def get_id(self): return self.__id
    def get_edad(self): return self.__edad
    def get_bpm(self): return self.__bpm
    def get_spo2(self): return self.__spo2
    def get_temperatura(self): return self.__temperatura

    # Setters
    def set_bpm(self, v): self.__bpm = v
    def set_spo2(self, v): self.__spo2 = v
    def set_temperatura(self, v): self.__temperatura = v

    # Cálculo de riesgo
    def calcular_riesgo(self):
        if self.__spo2 < 90 or self.__bpm > 140 or self.__temperatura > 39:
            return "Crítico"
        elif self.__spo2 < 94 or self.__bpm > 110 or self.__temperatura > 38:
            return "Alerta"
        else:
            return "Normal"

    def __str__(self):
        return (f"Paciente({self.__nombre}, ID={self.__id}, Edad={self.__edad}, "
                f"BPM={self.__bpm}, SpO2={self.__spo2}, Temp={self.__temperatura})")
