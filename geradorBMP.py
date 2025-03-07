# Programa para formatar imagens em BMP em resolução 320x240 (paisagem) ou 240x320 (retrato)
# Autor: Thiago de Oliveira Rodrigues

import os
from PIL import Image

def resize_with_aspect_ratio(img, target_width_landscape, target_height_portrait):
    # Verificação da resolução da imagem
    original_width, original_height = img.size
    if original_width > original_height:
        # Redimensiona para 320x240 (paisagem) mantendo a proporção
        new_width = target_width_landscape
        new_height = int(target_width_landscape * original_height / original_width)
    else:
        # Redimensiona para 240x320 (retrato) mantendo a proporção
        new_height = target_height_portrait
        new_width = int(target_height_portrait * original_width / original_height)
    
    # Redimensiona a imagem com as novas dimensões calculadas
    return img.resize((new_width, new_height))

def convert_and_resize_images():
    # Diretório para a pasta com as imagens convertidas
    bmp_directory = os.path.join(os.getcwd(), 'Imagens BMP')
    
    # Cria a pasta "Imagens BMP" se ela não existir
    if not os.path.exists(bmp_directory):
        os.makedirs(bmp_directory)
    
    file_counter = 0    # Contador para nomear os arquivos
    
    # Redimensiona todas as imagens no diretório atual
    for filename in os.listdir(os.getcwd()):
        # Verifica se é PNG ou JPG/JPEG
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                # Abre a imagem
                img = Image.open(os.path.join(os.getcwd(), filename))
                
                # Redimensiona mantendo a proporção da imagem
                if img.size != (320, 240) and img.size != (240, 320):
                    img = resize_with_aspect_ratio(img, 320, 320)
                
                # Converte para 24 bits RGB
                rgb_img = img.convert('RGB')
                
                # Nomeação da imagem para: "imagem_XX.bmp"
                bmp_filename = f"imagem{file_counter:02d}.bmp"
                bmp_path = os.path.join(bmp_directory, bmp_filename)
                
                # Salva a imagem em .BMP
                rgb_img.save(bmp_path, 'BMP')
                
                file_counter += 1
            except Exception as e:
                print(f"Erro ao converter {filename}: {e}")

print("Iniciando a Conversão...")
convert_and_resize_images()
input("Conversão Finalizada. Pressione Enter para sair...")