import streamlit as st
from PIL import Image, ImageOps
from io import BytesIO

# Configuración de la página
st.title("Agrega Empresa B a tu Linkedin")
st.write("Sube una imagen, ajusta la posición y tamaño del logo Empresa B, descarga el resultado ¡y comparte el orgullo de ser parte del movimiento que busca un nuevo modelo económico con Triple Impacto!")

# Subir la imagen principal
uploaded_file = st.file_uploader("Carga la imagen principal (PNG recomendado)", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    # Cargar la imagen principal
    main_image = Image.open(uploaded_file).convert("RGBA")

    # Mostrar la imagen principal procesada
    st.image(main_image, caption="Imagen Principal", use_container_width=True)  # Cambio aquí

    # Cargar la marca de agua directamente
    try:
        watermark = Image.open("SistemaBLkdn copia.png")  # Marca de agua subida (no se altera)
    except FileNotFoundError:
        st.error("No se encontró el archivo 'marca_agua.png'. Asegúrate de colocarlo en la misma carpeta que este script.")
        watermark = None

    # Continuar si la marca de agua existe
    if watermark:
        # Ajustar tamaño de la marca de agua
        scale_factor = st.slider("Tamaño del logo (porcentaje del ancho):", 10, 100, 30)
        watermark_width = int(main_image.width * (scale_factor / 100))
        watermark_height = int(watermark.size[1] * (watermark_width / watermark.size[0]))
        watermark_resized = watermark.resize((watermark_width, watermark_height))

        # Botón para aplicar la marca de agua
        if st.button("Aplicar"):
            # Crear capa para la marca de agua
            overlay = Image.new("RGBA", main_image.size, (0, 0, 0, 0))  # Capa transparente
            
            # Combinar capa de la marca de agua con la imagen principal
            final_image = Image.alpha_composite(main_image, overlay)

            # Mostrar la imagen con la marca de agua
            st.image(final_image, caption="Imagen con Marca de Agua", use_container_width=True)  # Cambio aquí

            # Descargar la imagen con la marca de agua
            buffer = BytesIO()
            final_image.save(buffer, format="PNG")
            buffer.seek(0)
            st.download_button(
                label="Descargar Imagen final",
                data=buffer,
                file_name="imagen_final.png",
                mime="image/png",
            )

