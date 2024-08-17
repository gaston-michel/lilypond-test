import streamlit as st
import abjad
import subprocess
from PIL import Image

st.title("Generador de Partituras con Abjad y LilyPond")

# Botón para generar el archivo .ly
if st.button("Generar Partitura"):
    # Crear un contenedor de Abjad
    staff = abjad.Staff("c'4 d'4 e'4 f'4")
    score = abjad.Score([staff])

    # Escribir el archivo .ly
    abjad.persist.as_ly(score, "output.ly")

    # Usar LilyPond para generar un archivo SVG
    subprocess.run(["lilypond", "-dbackend=svg", "-o", "output", "output.ly"])

    # Leer y mostrar la imagen SVG generada en Streamlit
    with open("output.svg", "r") as svg_file:
        svg_content = svg_file.read()
        st.image(svg_content, format="svg")
