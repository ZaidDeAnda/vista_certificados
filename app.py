import streamlit as st
import os

from utils.database import get_mongo_client
from utils.config import Config

st.header("Certificados para donantes!")

config = Config()

client = get_mongo_client(config)
db = client.certificados
certificados_collection = db.certificados

busqueda = st.text_input("Introduzca el nombre a buscar:")

reiniciar = st.button("Reiniciar busqueda")

if reiniciar:
    busqueda = ""

cols = st.columns(2)

image_formats = ["png","jpg","jpeg"]

cols[0].subheader("Haga click en el botón para acceder a su certificado")

global_list = os.listdir("Assets/Reconocimientos 87/")

if busqueda:
    global_list = [brand for brand in global_list if busqueda.upper() in brand]

for file in global_list:
    with cols[0]:
        if os.path.exists(f"Assets/Logos 87 donantes/{file[:-3]}{image_formats[0]}"):
            st.image(f"Assets/Logos 87 donantes/{file[:-3]}{image_formats[0]}")
        elif os.path.exists(f"Assets/Logos 87 donantes/{file[:-3]}{image_formats[1]}"):
            st.image(f"Assets/Logos 87 donantes/{file[:-3]}{image_formats[1]}")
        elif os.path.exists(f"Assets/Logos 87 donantes/{file[:-3]}{image_formats[2]}"):
            st.image(f"Assets/Logos 87 donantes/{file[:-3]}{image_formats[2]}")
        else:
            st.markdown(f"# {file[:-3]}")
        pwd_input = st.text_input("Introduce tú código", type="password",key=file)

        query = {
            "donante" : file
        }

        doc = certificados_collection.find(query)


        if pwd_input:
            if pwd_input == doc[0]['pwd']:

                with open(f"Assets/Reconocimientos 87/{file}", "rb") as open_file:
                    btn = st.download_button(
                            label="Acceder al certificado",
                            data=open_file,
                            file_name="certificado.pdf"
                        )
        st.divider()
