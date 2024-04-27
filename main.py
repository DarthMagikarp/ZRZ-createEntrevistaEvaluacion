# chat conversation
import json
import pymysql
import requests
import http.client
import os
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from itertools import cycle

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["POST"])
@cross_origin()
def function(self):
    load_dotenv()
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_DDBB = os.getenv("DB_DDBB")
    #try:
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_DDBB)
    cursor = connection.cursor()

    print("conexión exitosa")
    print("REQUEST: "+str(request.json))

    #try:
    cursor = connection.cursor()

    #"id_entrevista" = request.json['id_entrevista']
    
    id_profesional= str(request.json['id_profesional'])
    id_alumno= str(request.json['id_alumno'])
    profesional_evaluador= str(request.json['profesional_evaluador'])
    fecha= str(request.json['fecha'])
    numero_ficha= str(request.json['numero_ficha'])
    nombre_completo= str(request.json['nombre_completo'])
    rut= str(request.json['rut'])
    carrera= str(request.json['carrera'])
    ano_ingreso= str(request.json['ano_ingreso'])
    fecha_nacimiento= str(request.json['fecha_nacimiento'])
    edad= str(request.json['edad'])
    direccion= str(request.json['direccion'])
    correo= str(request.json['correo'])
    telefono= str(request.json['telefono'])
    nombre_contacto_emergencia1= str(request.json['nombre_contacto_emergencia1'])
    parentesco_contacto_emergencia1= str(request.json['parentesco_contacto_emergencia1'])
    celular_contacto_emergencia1= str(request.json['celular_contacto_emergencia1'])
    nombre_contacto_emergencia2= str(request.json['nombre_contacto_emergencia2'])
    parentesco_contacto_emergencia2= str(request.json['parentesco_contacto_emergencia2'])
    celular_contacto_emergencia2= str(request.json['celular_contacto_emergencia2'])
    prevision_salud_isapre= str(request.json['prevision_salud_isapre'])
    prevision_salud_fonasa= str(request.json['prevision_salud_fonasa'])
    prevision_salud_otro= str(request.json['prevision_salud_otro'])
    financiamiento_carrera= str(request.json['financiamiento_carrera'])
    vivienda_situacion_actual= str(request.json['vivienda_situacion_actual'])
    labores_cuidador= str(request.json['labores_cuidador'])
    financiamiento_gastos_personales= str(request.json['financiamiento_gastos_personales'])
    apoyo_economico_tratamiento= str(request.json['apoyo_economico_tratamiento'])
    pago_tratamiento_semanal= str(request.json['pago_tratamiento_semanal'])
    chequeos_salud_ultimo_ano= str(request.json['chequeos_salud_ultimo_ano'])
    motivo_chequeos_salud= str(request.json['motivo_chequeos_salud'])
    enfermedad_salud_fisica= str(request.json['enfermedad_salud_fisica'])
    diagnostico_salud_mental= str(request.json['diagnostico_salud_mental'])
    medicacion_permanente= str(request.json['medicacion_permanente'])
    atenciones_previas_salud_mental= str(request.json['atenciones_previas_salud_mental'])
    tratamientos_previos_salud_mental= str(request.json['tratamientos_previos_salud_mental'])
    tratamiento_actual_salud_mental= str(request.json['tratamiento_actual_salud_mental'])
    consume_alcohol= str(request.json['consume_alcohol'])
    tipo_alcohol_consumido= str(request.json['tipo_alcohol_consumido'])
    frecuencia_consumo_alcohol= str(request.json['frecuencia_consumo_alcohol'])
    consume_drogas= str(request.json['consume_drogas'])
    tipo_drogas_consumidas= str(request.json['tipo_drogas_consumidas'])
    frecuencia_consumo_drogas= str(request.json['frecuencia_consumo_drogas'])
    riesgo_suicida_escala= str(request.json['riesgo_suicida_escala'])
    motivo_consulta= str(request.json['motivo_consulta'])
    sintomatologia_motivo_consulta= str(request.json['sintomatologia_motivo_consulta'])
    expectativas_departamento= str(request.json['expectativas_departamento'])
    area_atencion_preferencia= str(request.json['area_atencion_preferencia'])
    primera_carrera= str(request.json['primera_carrera'])
    satisfecho_decision_carrera= str(request.json['satisfecho_decision_carrera'])
    desempeno_academico= str(request.json['desempeno_academico'])
    desafio_enfrentado_universidad= str(request.json['desafio_enfrentado_universidad'])
    redes_apoyo_personas_significativas= str(request.json['redes_apoyo_personas_significativas'])
    tipos_apoyo_actual= str(request.json['tipos_apoyo_actual'])
    actividades_gustan_realizar= str(request.json['actividades_gustan_realizar'])
    espacios_autocuidado= str(request.json['espacios_autocuidado'])
    tiempo_descanso_horas_sueno= str(request.json['tiempo_descanso_horas_sueno'])
    alimentacion_diaria_habitual= str(request.json['alimentacion_diaria_habitual'])
    modalidad_atencion_evaluacion= str(request.json['modalidad_atencion_evaluacion'])
    estado_animo_afectividad= str(request.json['estado_animo_afectividad'])
    tipo_pensamiento_observado= str(request.json['tipo_pensamiento_observado'])
    deteccion_condiciones_deficit_cognitivo= str(request.json['deteccion_condiciones_deficit_cognitivo'])
    consciencia_realidad= str(request.json['consciencia_realidad'])
    autoconcepto_autoestima= str(request.json['autoconcepto_autoestima'])
    situaciones_riesgo_relacional= str(request.json['situaciones_riesgo_relacional'])
    situaciones_riesgo_personal= str(request.json['situaciones_riesgo_personal'])
    observaciones= str(request.json['observaciones'])
    
    sql_insertar = 'INSERT INTO '+DB_DDBB+'.entrevista_evaluacion'+'''
                    (id_profesional, id_alumno, profesional_evaluador, fecha, numero_ficha, nombre_completo, rut, carrera, ano_ingreso, fecha_nacimiento, edad, direccion, correo, telefono, nombre_contacto_emergencia1, parentesco_contacto_emergencia1, celular_contacto_emergencia1, nombre_contacto_emergencia2, parentesco_contacto_emergencia2, celular_contacto_emergencia2, prevision_salud_isapre, prevision_salud_fonasa, prevision_salud_otro, financiamiento_carrera, vivienda_situacion_actual, labores_cuidador, financiamiento_gastos_personales, apoyo_economico_tratamiento, pago_tratamiento_semanal, chequeos_salud_ultimo_ano, motivo_chequeos_salud, enfermedad_salud_fisica, diagnostico_salud_mental, medicacion_permanente, atenciones_previas_salud_mental, tratamientos_previos_salud_mental, tratamiento_actual_salud_mental, consume_alcohol, tipo_alcohol_consumido, frecuencia_consumo_alcohol, consume_drogas, tipo_drogas_consumidas, frecuencia_consumo_drogas, riesgo_suicida_escala, motivo_consulta, sintomatologia_motivo_consulta, expectativas_departamento, area_atencion_preferencia, primera_carrera, satisfecho_decision_carrera, desempeno_academico, desafio_enfrentado_universidad, redes_apoyo_personas_significativas, tipos_apoyo_actual, actividades_gustan_realizar, espacios_autocuidado, tiempo_descanso_horas_sueno, alimentacion_diaria_habitual, modalidad_atencion_evaluacion, estado_animo_afectividad, tipo_pensamiento_observado, deteccion_condiciones_deficit_cognitivo, consciencia_realidad, autoconcepto_autoestima, situaciones_riesgo_relacional, situaciones_riesgo_personal, observaciones)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
                    '''
    print('INSERT:'+sql_insertar)
    print(id_profesional, id_alumno, profesional_evaluador, fecha, numero_ficha, nombre_completo, rut, carrera, ano_ingreso, fecha_nacimiento, edad, direccion, correo, telefono, nombre_contacto_emergencia1, parentesco_contacto_emergencia1, celular_contacto_emergencia1, nombre_contacto_emergencia2, parentesco_contacto_emergencia2, celular_contacto_emergencia2, prevision_salud_isapre, prevision_salud_fonasa, prevision_salud_otro, financiamiento_carrera, vivienda_situacion_actual, labores_cuidador, financiamiento_gastos_personales, apoyo_economico_tratamiento, pago_tratamiento_semanal, chequeos_salud_ultimo_ano, motivo_chequeos_salud, enfermedad_salud_fisica, diagnostico_salud_mental, medicacion_permanente, atenciones_previas_salud_mental, tratamientos_previos_salud_mental, tratamiento_actual_salud_mental, consume_alcohol, tipo_alcohol_consumido, frecuencia_consumo_alcohol, consume_drogas, tipo_drogas_consumidas, frecuencia_consumo_drogas, riesgo_suicida_escala, motivo_consulta, sintomatologia_motivo_consulta, expectativas_departamento, area_atencion_preferencia, primera_carrera, satisfecho_decision_carrera, desempeno_academico, desafio_enfrentado_universidad, redes_apoyo_personas_significativas, tipos_apoyo_actual, actividades_gustan_realizar, espacios_autocuidado, tiempo_descanso_horas_sueno, alimentacion_diaria_habitual, modalidad_atencion_evaluacion, estado_animo_afectividad, tipo_pensamiento_observado, deteccion_condiciones_deficit_cognitivo, consciencia_realidad, autoconcepto_autoestima, situaciones_riesgo_relacional, situaciones_riesgo_personal, observaciones)
    cursor.execute(sql_insertar,(id_profesional, id_alumno, profesional_evaluador, fecha, numero_ficha, nombre_completo, rut, carrera, ano_ingreso, fecha_nacimiento, edad, direccion, correo, telefono, nombre_contacto_emergencia1, parentesco_contacto_emergencia1, celular_contacto_emergencia1, nombre_contacto_emergencia2, parentesco_contacto_emergencia2, celular_contacto_emergencia2, prevision_salud_isapre, prevision_salud_fonasa, prevision_salud_otro, financiamiento_carrera, vivienda_situacion_actual, labores_cuidador, financiamiento_gastos_personales, apoyo_economico_tratamiento, pago_tratamiento_semanal, chequeos_salud_ultimo_ano, motivo_chequeos_salud, enfermedad_salud_fisica, diagnostico_salud_mental, medicacion_permanente, atenciones_previas_salud_mental, tratamientos_previos_salud_mental, tratamiento_actual_salud_mental, consume_alcohol, tipo_alcohol_consumido, frecuencia_consumo_alcohol, consume_drogas, tipo_drogas_consumidas, frecuencia_consumo_drogas, riesgo_suicida_escala, motivo_consulta, sintomatologia_motivo_consulta, expectativas_departamento, area_atencion_preferencia, primera_carrera, satisfecho_decision_carrera, desempeno_academico, desafio_enfrentado_universidad, redes_apoyo_personas_significativas, tipos_apoyo_actual, actividades_gustan_realizar, espacios_autocuidado, tiempo_descanso_horas_sueno, alimentacion_diaria_habitual, modalidad_atencion_evaluacion, estado_animo_afectividad, tipo_pensamiento_observado, deteccion_condiciones_deficit_cognitivo, consciencia_realidad, autoconcepto_autoestima, situaciones_riesgo_relacional, situaciones_riesgo_personal, observaciones))
    connection.commit()

    retorno = {
            "estado":True,
            "detalle":"success!!"
        }

    #except Exception as e:
    #    print('Error: '+ str(e))
    #    retorno = {
    #        "estado":False,
    #        "detalle":"fail!!"
    #    }
    return retorno

if __name__ == "__main__":
    app.run(debug=True, port=8002, ssl_context='adhoc')