import os
import subprocess
import streamlit as st

st.title("Generador de música con LilyPond")

lilypond_code = st.text_area("Escribe tu código LilyPond aquí:")

if st.button("Generar PDF"):
    # with open("temp.ly", "w") as f:
    #     f.write(lilypond_code)

    # subprocess.run(["lilypond", "temp.ly"])
    subprocess.run(["lilypond", "--version"])

    # with open("temp.pdf", "rb") as pdf_file:
    #     st.download_button("Descargar PDF", data=pdf_file, file_name="output.pdf")
