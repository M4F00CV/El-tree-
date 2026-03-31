import sys
import os
from PIL import Image
import pillow_heif

# Activar soporte HEIC
pillow_heif.register_heif_opener()

def convertir_heic_a_jpg(input_folder, output_folder):
    if not os.path.exists(input_folder):
        print(f"❌ La carpeta de entrada no existe: {input_folder}")
        return

    os.makedirs(output_folder, exist_ok=True)

    archivos = os.listdir(input_folder)
    convertidos = 0

    for archivo in archivos:
        if archivo.lower().endswith(".heic"):
            input_path = os.path.join(input_folder, archivo)
            output_name = os.path.splitext(archivo)[0] + ".jpg"
            output_path = os.path.join(output_folder, output_name)

            try:
                imagen = Image.open(input_path).convert("RGB")
                imagen.save(output_path, "JPEG", quality=95)
                print(f"✅ Convertido: {archivo}")
                convertidos += 1
            except Exception as e:
                print(f"⚠️ Error con {archivo}: {e}")

    print(f"\n🎉 Total convertidos: {convertidos}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso:")
        print("python convertir.py <carpeta_entrada> <carpeta_salida>")
        sys.exit(1)

    carpeta_entrada = sys.argv[1]
    carpeta_salida = sys.argv[2]

    convertir_heic_a_jpg(carpeta_entrada, carpeta_salida)