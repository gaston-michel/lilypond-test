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
    abjad.persist(score).as_ly("output.ly")

    # Usar LilyPond para generar un archivo PNG
    subprocess.run(["lilypond", "-dbackend=eps", "-dno-gs-load-fonts",
                    "-dinclude-eps-fonts", "-dpixmap-format=pngalpha",
                    "-dresolution=150", "-o", "output", "output.ly"])

    # Mostrar la imagen generada en Streamlit
    image = Image.open("output.png")
    st.image(image, caption="Partitura Generada", use_column_width=True)
