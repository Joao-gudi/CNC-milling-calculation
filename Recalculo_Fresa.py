# |=================================================================|
# |            PROGRAMA MANIPULADOR DE PLANO DE CORTE               |
# |                       PARA CNC NANXING                          |
# |                    (COMPENSADOR DE FRESA)                       |
# |                                                                 |
# |                      -= MANIPULADOR =-                          |
# |                                                                 |
# |                                 Autor: João Gabriel Gudilunas   |
# |                                                                 |
# |                                        Esteves ; João Gabriel   |
# |                                                                 |
# |=================================================================|

# Importando bibliotecas necessárias
import os
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import simpledialog
import codecs

# Função para ajustar as coordenadas no XML
def adjust_coordinates(xml_path, new_diameter):
    # Parseando o XML
    tree = ET.parse(xml_path.strip('"'))
    root = tree.getroot()

    # Iterando sobre os elementos do XML para fazer os ajustes
    for pattern in root.iter('Pattern'):
        for workpiece in pattern.iter('Workpiece'):
            # Obtendo o diâmetro da ferramenta do XML original
            tool_diameter = float(pattern.get('ToolDiameter'))
            print(f"Old ToolDiameter: {tool_diameter}")  # Imprime o valor antigo

            # Calculando o fator de ajuste com base no novo diâmetro
            factor = new_diameter / tool_diameter

            # Iterando sobre os pontos para ajustar as coordenadas
            for point in workpiece.iter('Point'):
                x = float(point.get('X'))
                y = float(point.get('Y'))

                # Calculando as novas coordenadas
                new_x = x * factor
                new_y = y * factor

                # Atualizando as coordenadas no XML
                point.set('X', str(new_x))
                point.set('Y', str(new_y))

            # Atualizando o diâmetro da ferramenta no XML
            pattern.set('ToolDiameter', str(new_diameter))
            print(f"New ToolDiameter: {new_diameter}")  # Imprime o novo valor

    # Gerando o caminho de saída
    output_path = generate_output_path(xml_path)

    # Salvando o XML ajustado
    save_xml(tree, output_path)
    print(f"Coordenadas ajustadas. Novo arquivo salvo em: {output_path}")

# Função para gerar o caminho de saída
def generate_output_path(input_path):
    # Removendo as aspas do diretório de entrada
    dir_name, _ = os.path.split(input_path.strip('"'))

    # Obtendo o nome do arquivo sem a extensão
    base_name, _ = os.path.splitext(os.path.basename(input_path))

    # Criando o diretório de saída
    output_dir = os.path.join(dir_name, "New_Xml")

    # Garantindo que o diretório de saída exista
    os.makedirs(output_dir, exist_ok=True)

    # Incorporando o nome do arquivo ao caminho de saída
    output_path = os.path.join(output_dir, f"{base_name}_adjusted.xml")
    return output_path

# Função para salvar o XML ajustado
def save_xml(tree, output_path):
    with codecs.open(output_path, 'w', encoding='utf-8') as file:
        tree.write(file, encoding='unicode', xml_declaration=True)

# Função para obter a entrada do usuário
def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Solicitando o caminho do arquivo XML
    xml_path = simpledialog.askstring("Caminho", "Informe o caminho do arquivo XML:")
    if xml_path is None:  # Se o usuário pressionar "Cancelar"
        exit()

    # Solicitando o novo diâmetro da ferramenta
    new_diameter = simpledialog.askfloat("Diâmetro", "Informe o novo diâmetro da ferramenta:")
    if new_diameter is None:  # Se o usuário pressionar "Cancelar"
        exit()

    return xml_path, new_diameter

# Função principal
def main():
    # Obtendo a entrada do usuário
    xml_path, new_diameter = get_user_input()

    # Realizando os ajustes no XML
    adjust_coordinates(xml_path, new_diameter)

# Executando a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()