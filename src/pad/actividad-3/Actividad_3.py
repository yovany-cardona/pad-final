import numpy as np
import pandas as pd
import os
import kagglehub
from kagglehub import KaggleDatasetAdapter
import io 

class Actividad3:
    def __init__(self):
        self.ruta_raiz = os.path.abspath(os.getcwd())
        self.ruta_act2 = os.path.join(self.ruta_raiz, "src", "pad", "actividad-3")

        datos = {
            "n_punto": list(range(1, 13)),
            "detalle": [
                "Crea un DataFrame frutas que luzca así",
                "Crea un DataFrame ventas_frutas con los datos indicados",
                "Crea una Serie utensilios con los datos indicados",
                "Descarga el dataset 'wine review' desde Kaggle y cárgalo en un DataFrame llamado review, tal y como se muestra en la figura.",
                "Visualiza las primeras filas del DataFrame",
                "Utiliza el método .info() para averiguar cuántas entradas hay. ¿Cuántas encontraste?",
                "¿Cuál es el precio promedio?",
                "¿Cuál es el precio más alto pagado?",
                "Crea un DataFrame con todos los vinos de california.",
                "Utiliza idxmax() para encontrar el índice del vino con el precio más alto y luego utiliza loc para obtener toda la información de ese vino específico.",
                "¿Cuáles son los tipos de uva más comunesen California?",
                "¿Cuáles son los 10 tipos de uva más comunes en California?"
            ],
            "resultado": [0] * 12
        }
        self.df = pd.DataFrame(datos)
        self.df["resultado"] = self.df["resultado"].astype(object)

    def punto_1(self):
        df_frutas = pd.DataFrame([[20, 50]], columns=["Granadilla", "Tomates"])
        self.df.loc[0, "resultado"] = "Guardado en punto_1.csv"
        df_frutas.to_csv("punto_1.csv", index=False)  
        print(df_frutas)

    def punto_2(self):
        ventas_frutas = pd.DataFrame(
            [[20, 50], [49, 100]],
            index=["ventas 2021", "ventas 2022"],
            columns=["Granadilla", "Tomates"]
        )
        self.df.loc[1, "resultado"] = "Guardado en punto_2.csv"
        ventas_frutas.to_csv("punto_2.csv")
        print(ventas_frutas)

    def punto_3(self):
        utensilios = pd.Series(
            ["3 unidades", "2 unidades", "4 unidades", "5 unidades"],
            index=["Cuchara", "Tenedor", "Cuchillo", "Plato"],
            name="Cocina"
        )
        self.df.loc[2, "resultado"] = "Guardado en punto_3.csv"
        utensilios.to_csv("punto_3.csv")
        print(utensilios)

    def punto_4(self):
        print("Descargando dataset de Kaggle...")
        path = kagglehub.dataset_download("zynicide/wine-reviews")
        
        csv_file = None
        for file in os.listdir(path):
            if file.endswith(".csv"):
                csv_file = os.path.join(path, file)
                break

        if csv_file:
            print(f"Archivo encontrado: {csv_file}")
            
            review = pd.read_csv(csv_file)

            output_path = os.path.join(self.ruta_raiz, "punto_4.csv")
            self.df.loc[3, "resultado"] = "Guardado en punto_4.csv"
            review.to_csv(output_path, index=False)

            print(f"Dataset guardado en {output_path}")
        else:
            print("No se encontró archivo CSV en el dataset descargado")

    def punto_5(self):
        print("Descargando dataset de Kaggle...")
        path = kagglehub.dataset_download("zynicide/wine-reviews")
        
        csv_file = None
        for file in os.listdir(path):
            if file.endswith(".csv"):
                csv_file = os.path.join(path, file)
                break

        if csv_file:
            print(f"Archivo encontrado: {csv_file}")
            review = pd.read_csv(csv_file)

            print("Primeras filas del DataFrame:")
            self.df.loc[4, "resultado"] = "Guardado en punto_5.csv"
            print(review.head())

            output_path = os.path.join(self.ruta_raiz, "punto_5.csv")
            review.head().to_csv(output_path, index=False)

            print(f"Primeras filas guardadas en {output_path}")
        else:
            print("No se encontró un archivo CSV en el dataset descargado")

    def punto_6(self):
        input_path = os.path.join(self.ruta_raiz, "punto_4.csv")
        
        if not os.path.exists(input_path):
            print(f"Error: No se encontró {input_path}. Asegúrate de ejecutar primero el punto 4.")
            return
        
        review = pd.read_csv(input_path)

        buffer = io.StringIO()
        review.info(buf=buffer)
        info_text = buffer.getvalue()

        num_entradas = review.shape[0]

        output_path = os.path.join(self.ruta_raiz, "punto_6.csv")
        df_info = pd.DataFrame({"Descripción": ["Número de entradas", "Info"], "Valor": [num_entradas, info_text]})
        df_info.to_csv(output_path, index=False)
        self.df.loc[5, "resultado"] = "Guardado en punto_6.csv"
        print(f"Número de entradas: {num_entradas}")
        print(f"Información guardada en {output_path}")

    def punto_7(self):
        input_path = os.path.join(self.ruta_raiz, "punto_4.csv")

        if not os.path.exists(input_path):
            print(f"Error: No se encontró {input_path}. Asegúrate de ejecutar primero el punto 4.")
            return
        
        df = pd.read_csv(input_path)

        if "price" not in df.columns:
            print(f"Error: No se encontró la columna 'price' en {input_path}.")
            return

        precio_promedio = df["price"].mean()

        output_path = os.path.join(self.ruta_raiz, "punto_7.csv")
        df_resultado = pd.DataFrame({"Descripción": ["Precio Promedio"], "Valor": [precio_promedio]})
        df_resultado.to_csv(output_path, index=False)
        self.df.loc[6, "resultado"] = "Guardado en punto_7.csv"

        print(f"Precio promedio: {precio_promedio}")
        print(f"Información guardada en {output_path}")

    def punto_8(self):
        input_path = os.path.join(self.ruta_raiz, "punto_4.csv")

        if not os.path.exists(input_path):
            print(f"Error: No se encontró {input_path}. Asegúrate de ejecutar primero el punto 4.")
            return
        
        df = pd.read_csv(input_path)

        if "price" not in df.columns:
            print(f"Error: No se encontró la columna 'price' en {input_path}.")
            return

        precio_mas_alto = df["price"].max()

        output_path = os.path.join(self.ruta_raiz, "punto_8.csv")
        df_resultado = pd.DataFrame({"Descripción": ["Precio Más Alto"], "Valor": [precio_mas_alto]})
        df_resultado.to_csv(output_path, index=False)
        self.df.loc[7, "resultado"] = "Guardado en punto_8.csv"
        print(f"Precio más alto pagado: {precio_mas_alto}")
        print(f"Información guardada en {output_path}")

    def punto_9(self):
        input_path = os.path.join(self.ruta_raiz, "punto_4.csv")

        if not os.path.exists(input_path):
            print(f"Error: No se encontró {input_path}. Asegúrate de ejecutar primero el punto 4.")
            return
        
        df = pd.read_csv(input_path)

        if "province" not in df.columns:
            print(f"Error: No se encontró la columna 'province' en {input_path}.")
            return

        df_california = df[df["province"] == "California"]

        output_path = os.path.join(self.ruta_raiz, "punto_9.csv")
        df_california.to_csv(output_path, index=False)
        self.df.loc[8, "resultado"] = "Guardado en punto_9.csv"
        print(f"Se han filtrado {len(df_california)} vinos de California.")
        print(f"Información guardada en {output_path}")

    def punto_10(self):
        input_path = os.path.join(self.ruta_raiz, "punto_9.csv")

        if not os.path.exists(input_path):
            print(f"Error: No se encontró {input_path}. Asegúrate de ejecutar primero el punto 9.")
            return
        
        df = pd.read_csv(input_path)
        
        if "price" not in df.columns:
            print(f"Error: No se encontró la columna 'price' en {input_path}.")
            return
        
        indice_max_precio = df["price"].idxmax()
        
        vino_mas_caro = df.loc[[indice_max_precio]]
        
        output_path = os.path.join(self.ruta_raiz, "punto_10.csv")
        vino_mas_caro.to_csv(output_path, index=False)
        self.df.loc[9, "resultado"] = "Guardado en punto_10.csv"
        print("Información del vino más caro:")
        print(vino_mas_caro)
        print(f"Información guardada en {output_path}")

    def punto_11(self):
        input_path = os.path.join(self.ruta_raiz, "punto_9.csv")
        
        if not os.path.exists(input_path):
            print(f"Error: No se encontró {input_path}. Asegúrate de ejecutar primero el punto_9.")
            return
        df = pd.read_csv(input_path)
        
        if "variety" not in df.columns:
            print(f"Error: No se encontró la columna 'variety' en {input_path}.")
            return
        
        variedades_comunes = df["variety"].value_counts().reset_index()
        variedades_comunes.columns = ["variety", "count"]
        
        output_path = os.path.join(self.ruta_raiz, "punto_11.csv")
        variedades_comunes.to_csv(output_path, index=False)
        self.df.loc[10, "resultado"] = "Guardado en punto_11.csv"
        print(f"Se han identificado {len(variedades_comunes)} tipos de uva en California.")
        print(f"Información guardada en {output_path}")

    def punto_12(self):
        input_path = os.path.join(self.ruta_raiz, "punto_9.csv")
        
        if not os.path.exists(input_path):
            print(f"Error: No se encontró {input_path}. Asegúrate de ejecutar primero el punto 9.")
            return
        
        df = pd.read_csv(input_path)
        
        if "variety" not in df.columns:
            print(f"Error: No se encontró la columna 'variety' en {input_path}.")
            return
        
        variedades_comunes = df["variety"].value_counts().head(10)
        
        output_path = os.path.join(self.ruta_raiz, "punto_12.csv")
        variedades_comunes.to_csv(output_path, header=True)
        self.df.loc[11, "resultado"] = "Guardado en punto_12.csv"
        print("Las 10 variedades de uva más comunes en California han sido guardadas en punto_12.csv.")

    def ejecutar(self):
        self.punto_1()
        self.punto_2()
        self.punto_3()
        self.punto_4() 
        self.punto_5()
        self.punto_6()
        self.punto_7()
        self.punto_8()
        self.punto_9()
        self.punto_10()
        self.punto_11()
        self.punto_12()

        self.df.to_csv("actividad-3.csv", index=False)
        print("Resultados guardados en actividad-3.csv")

act = Actividad3()
act.ejecutar()