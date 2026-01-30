import sys
import os
import json

class lector_permitidos:
    def __init__(self, ruta):
        with open(ruta, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            self.extensions = datos.get("extensions", [])
            self.ignorar = datos.get("ignorar", [])

class arvol:
    def __init__(self, permitidos, ignorar):
        self.permitidos = permitidos
        self.ignorar = ignorar
        if len(sys.argv) > 5 or len(sys.argv) < 2:
            return
        if len(sys.argv) > 2 and sys.argv[1] is None:
            sys.stdout = open(sys.argv[2], 'w', encoding='utf-8')
        else:
            sys.stdout.reconfigure(encoding='utf-8')    
        
        if  sys.argv[1] == "" or sys.argv[1].isspace() or not os.path.isdir(sys.argv[1]):
            return
        #print(sys.argv[1])
        print(f'{os.path.basename(sys.argv[1])}/')
        self.recorrer_carpetas(sys.argv[1])
                
    def recorrer_carpetas(self, raiz, prefijo=""):
        # Obtener lista de archivos y carpetas, ignorando los que no se desean
        lista = os.listdir(raiz)
        lista = [f for f in lista if f not in self.ignorar and (os.path.isdir(os.path.join(raiz, f)) or any(f.endswith(ext) for ext in self.permitidos))]
        # Recorrer la lista filtrada
        for i in range(len(lista)):
            ruta_completa = os.path.join(raiz, lista[i])
            if i== len(lista) -1:
                connector = "└──"
            else:
                connector = "├──"
                
            if os.path.isdir(ruta_completa):
                # Si es una carpeta, llamar recursivamente
                print(f"{prefijo}{connector} {lista[i]}/")
                self.recorrer_carpetas(ruta_completa, prefijo=prefijo + "│   " if connector == "├──" else prefijo + "    ")
            else:
                # Si es un archivo, imprimirlo
                print(f"{prefijo}{connector} {lista[i]}")
                
        # Imprimir la estructura de árbol
        
        
if __name__ == "__main__":
    arbol = arvol(permitidos = lector_permitidos("permitidos.json").extensions,
                  ignorar = lector_permitidos("permitidos.json").ignorar)
    #print(arbol.permitidos)
    #print(arbol.ignorar)
    
    