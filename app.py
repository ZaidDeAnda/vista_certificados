import streamlit as st
import os

st.header("Certificados para donantes!")

cols = st.columns(2)

image_formats = ["png","jpg","jpeg"]

cols[0].subheader("Haga click en la imagen para acceder a su certificado")

for file in os.listdir("Assets/Logos 87 donantes/"):
    with cols[0]:
        st.image("Assets/Logos 87 donantes/" + file)
        for format in image_formats:
            if format in file:
                file = file.replace(format,"pdf")
                break
        with open("Assets/Reconocimientos 87/"+file, "rb") as open_file:
            btn = st.download_button(
                    label="Acceder al certificado",
                    data=open_file,
                    file_name="certificado.pdf",
                    key=file
                )
        st.divider()
