import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# Título de la aplicación
st.title("Búsqueda de Ancestros")

# Solicitar información del usuario
nombre = st.text_input("Ingrese el nombre de su ancestro:")
apellido = st.text_input("Ingrese el apellido de su ancestro:")
fecha_nacimiento = st.date_input("Ingrese la fecha de nacimiento de su ancestro:")

# Convertir fecha de nacimiento a cadena en formato requerido por la API (si es necesario)
fecha_nacimiento_str = fecha_nacimiento.strftime("%Y-%m-%d")

# Botón para iniciar la búsqueda
if st.button("Buscar"):
    if nombre and apellido and fecha_nacimiento:
        # Placeholder para la URL de la API de FamilySearch u otro servicio
        url = "https://api.familysearch.org/search"

        # Parámetros de consulta a la API
        params = {
            "nombre": nombre,
            "apellido": apellido,
            "fecha_nacimiento": fecha_nacimiento_str
        }

        try:
            # Hacer la solicitud a la API
            response = requests.get(url, params=params)
            
            # Verifica si la respuesta es exitosa
            if response.status_code == 200:
                data = response.json()
                # Verificar si hay resultados en la respuesta
                if 'resultados' in data and len(data['resultados']) > 0:
                    # Mostrar los resultados en un DataFrame
                    df = pd.DataFrame(data['resultados'])
                    st.dataframe(df)
                else:
                    st.warning("No se encontraron resultados. Por favor, intente de nuevo.")
            else:
                st.error(f"Error en la solicitud: {response.status_code}")
        except requests.RequestException as e:
            st.error(f"Error en la solicitud: {e}")
    else:
        st.warning("Por favor, completa todos los campos antes de realizar la búsqueda.")
