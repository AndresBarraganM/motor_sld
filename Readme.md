Este motor SLD determina segun los hechos indicados si un arbusto de fresas cuenta con una enfermedad. Este esta
basado en el proyecto que realizara el equipo de agricultura.

La base de conocimientos utilizada se encuentra en base_conocimiento.json y los hechos utilizados para determinar
si cuenta con una enfermedad o no se encuentran en el inicio de sld_practice.py en forma de un array

La estructura de la base de conocimientos es la siguiente:

      "id": "R16",          #Id unica de cada enfermedad
      "nombre": "Trips",    #Nombre comun para la enfermedad
      "condiciones": [      #Lista de condiciones
        {"hecho": "sintoma_fruto_joven", "valor": "rayas_plateadas"},   #Hecho: parte o fase en la que se presenta el sintoma
        {"hecho": "sintoma_fruto_maduro", "valor": "deformados_piel_fea"}#valor: lo que desvela el sintoma
      ],
      "conclusion": {       #listado de la conclusion del sistema
        "diagnostico": "Trips" #Mensaje que se dara como conclusion
      }

Los hechos son iguales que las condiciones en la base de conocimineto, por lo que se comparan directamente.

hechos_observados = [
        {"hecho": "sintoma_hoja", "valor": "danada"},
        {"hecho": "sintoma_hoja", "valor": "cubierta_gris"},
        {"hecho": "sintoma_petalo_pedunculo", "valor": "color_cafe"},
        {"hecho": "sintoma_fruto", "valor": "manchas_cafe"},
        {"hecho": "sintoma_fruto", "valor": "zonas_acuosas"}
    ]