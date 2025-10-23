import json

hechos_observados = [
        {"hecho": "sintoma_hoja", "valor": "danada"},
        {"hecho": "sintoma_hoja", "valor": "cubierta_gris"},
        {"hecho": "sintoma_petalo_pedunculo", "valor": "color_cafe"},
        {"hecho": "sintoma_fruto", "valor": "manchas_cafe"},
        {"hecho": "sintoma_fruto", "valor": "zonas_acuosas"}
    ]


# Recive el tipo de consulta y el query a buscar
# tipo de consulta es "enfermedad" o "sintoma", o lo que espera resolver
# querry es el valor a buscar
# segun el tipo de consulta se resuelve diferente
def unificar(tipo_consulta, querry):
    if tipo_consulta == "enfermedad":
        #obtener los requisitos para esta enfermedad
        sintomas_esperados = obtener_base_conocimiento_enfermedad(querry).get("condiciones", [])

        print("Sintomas esperados:", sintomas_esperados)

        #realizar consulta de unificacion recusivamente a estas enfermedades
        for sintoma in sintomas_esperados:
            print(" Verificando sintoma:", sintoma)
            resultado = unificar("sintoma", sintoma)
            if resultado is None:
                print("     Sintoma no encontrado:", sintoma)
                return None
            else:
                print("     Sintoma encontrado:", sintoma)
        return True

    if tipo_consulta == "sintoma":
        #buscar si el sintoma existe en los hechos observados
        if querry in hechos_observados:
            return True
        else:
            return None
    
    return None

# Metodo para obtener la base de conocimiento desde un archivo JSON
def obtener_base_conocimiento_enfermedad(nombre_enfermedad):
    base_ruta = "base_conocimiento.json"
    data = {}
    try:
        with open(base_ruta, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {base_ruta}")
    except json.JSONDecodeError as e:
        print(f"Error parseando JSON en {base_ruta}: {e}")

    for item in data.get("hechos", []):
      if (item.get("nombre", "")) == nombre_enfermedad:
        return item
    return None

if __name__ == "__main__":
    #consulta, tiene X enfermedad?
    query = "Botrytis cinerea (Moho gris)"

    print("Consultando si la planta tiene la enfermedad:", query)

    resultado = unificar("enfermedad", query)

    print("Resultado de la consulta:", resultado)
    