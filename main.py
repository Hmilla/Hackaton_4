from json import load, decoder, dump
from uuid import uuid4

data = {
    'Alumnos': [],
    'Docentes':[]
}


class Docente:
    def __init__(self,nombre, edad, DNI) -> None:
        self.nombre=nombre
        self.edad=edad
        self.DNI=DNI
    def cargar_docentes(self):
        try:
            archivo = open("Docentes.json", "r")
            data["Docentes"] = load(archivo)
            archivo.close()
        except FileNotFoundError:
            print("\n Creando registro de docentes...")
            archivo = open("Docentes.json", "w")
            archivo.close()
        except decoder.JSONDecodeError:
            print("\n No hay información de docentes, puede crearlos ahora")

    def agregar_docente(self):
        print("Ingrese el nombre del docente")
        nombre_docente=input("> ")
        
        while True:
            print("Ingrese la edad del docente")
            try:
                edad_docente=int(input('> '))
                if edad_docente<20 or edad_docente>80:
                    print("Error, la edad del docente no puede ser menor a 18 ni mayor a 80")
                else:
                    break
            except (TypeError, ValueError) as e:
                print("Error, debe ingresarse un numero valido")  
            except Exception as e:
                print(e.__class__.__dict__)
                print(e.__class__.__name__)
                print("Error")

        while True:
            print("Ingrese el DNI del docente") 
            try:
                DNI_docente=input('> ')
                int(DNI_docente)
                if len(DNI_docente)!=8:
                    print("Error, el numero de DNI debe tener 8 digitos")
                elif int(DNI_docente)<0:
                    print("Error, debe ingresarse un numero de DNI valido") 
                else:
                    break 
            except (TypeError, ValueError) as e:
                print("Error, debe ingresarse un numero de DNI valido")  
            except Exception as e:
                print(e.__class__.__dict__)
                print(e.__class__.__name__)
                print("Error")
        self.crear_docente(nombre_docente, edad_docente, DNI_docente)
        
    def crear_docente(self, nombre, edad, DNI):
    
        nuevo_docente=Docente(nombre,edad, DNI)
        id=str(uuid4())
        datos = {
            "Nombre":nombre,
            "Edad":edad,
            "DNI":int(DNI),
            "id":id
        }
        print(f''' 
        Nombre: {nombre}
        Edad: {edad}
        DNI: {DNI}
        Id: {id}
        ''')
        self.guardar_docente(datos)    

    def guardar_docente(self, datos):
        data['Docentes'].append(datos)
        Prfs = data['Docentes']
        archivo = open("Docentes.json", "w")
        dump(Prfs, archivo, indent=4)
        archivo.close()
        print("Se guardaron los datos con exito")
    
    def ver_info_docentes(self):
        try:
            archivo = open("Docentes.json", "r")
            data["Docentes"] = load(archivo)
            for docentee in data["Docentes"]:
                print("Nombre: ", docentee["Nombre"])
                print("Edad: ", docentee["Edad"])
                print("DNI: ", docentee["DNI"])
                print("id: ", docentee["id"])
                print("")
            archivo.close()
        except decoder.JSONDecodeError:
            pass
        
class Alumno:
    def __init__(self,nombre, notas, nota_max, nota_min, promedio) -> None:
        self.nombre=nombre
        self.notas=notas
        self.nota_max=nota_max
        self.nota_min=nota_min
        self.promedio=promedio
    
    def cargar_alumnos(self):
        try:
            archivo = open("Alumnos.json", "r")
            data["Alumnos"] = load(archivo)
            archivo.close()
        except FileNotFoundError:
            print("\n Creando registro de alumnos...")
            archivo = open("Alumnos.json", "w")
            archivo.close()
        except decoder.JSONDecodeError:
            print("\n No hay información de alumnos, puede crearlos ahora")

    
    def ver_info_alumnos(self):
        try:
            archivo = open("Alumnos.json", "r")
            data["Alumnos"] = load(archivo)
            for alumnoo in data["Alumnos"]:
                print("Nombre: ", alumnoo["Nombre"])
                print("Notas: ", alumnoo["Notas"])
                print("Nota maxima: ", alumnoo["Nota maxima"])
                print("Nota minima: ", alumnoo["Nota minima"])
                print("Promedio: ", alumnoo["Promedio"])
                print("")
            archivo.close()
        except decoder.JSONDecodeError:
            pass

    def agregar_alumno(self):
        print("Ingrese el nombre del alumno")
        nombre_alumno=input("> ")
        self.notas_alumno(nombre_alumno)

    def notas_alumno(self, nombre):
        print(f'Ingrese las notas del alumno {nombre}')
        
        while True:
            print("¿Cuantas notas va a ingresar? (max 4 notas)")
            try:
                numero_notas=int(input('> '))
                if numero_notas<=0:
                    print('Error, debe ingresarse un numero mayor a 0')
                elif numero_notas>4:
                    print('Error, solo puedes ingresar hasta 4 notas')
                else:
                    break

            except (TypeError, ValueError) as e:
                print("Error, debe ingresarse un numero valido")  
            except Exception as e:
                print(e.__class__.__dict__)
                print(e.__class__.__name__)
                print("Error")
        
        notas=[]
        for i in range(1,numero_notas+1):
            while True:
                try:
                    nota=float(input(f'nota {i} '))
                    if nota<0 or nota>20:
                        print("La nota ingresada debe ser mayor a 0 y menor a 20")
                    else:
                        notas.append(nota)
                        break
                except (TypeError, ValueError) as e:
                    print("Debe ingresarse un numero ")  
                except Exception as e:
                    print(e.__class__.__dict__)
                    print(e.__class__.__name__)
                    print("Error")
                
        
        nota_max=max(notas)
        nota_min=min(notas)
        promedio=round(sum(notas)/len(notas),2)
        self.crear_alumno(nombre,notas, nota_max, nota_min, promedio)

    def crear_alumno(self, nombre,notas, nota_max, nota_min, promedio):
        
        nuevo_alumno = Alumno(nombre, notas, nota_max, nota_min, promedio)
        datos = {
            "Nombre":nombre,
            "Notas":notas,
            "Nota maxima":nota_max,
            "Nota minima":nota_min,
            "Promedio":promedio
        }
        print(f''' 
        Nombre :{nombre}
        Notas:{notas}
        Nota maxima:{nota_max}
        Nota minima:{nota_min}
        Promedio:{promedio}
        ''')
        self.guardar_alumno(datos)
        

    def guardar_alumno(self, datos):
        data['Alumnos'].append(datos)
        Alms = data['Alumnos']
        archivo = open("Alumnos.json", "w")
        dump(Alms, archivo, indent=4)
        archivo.close()
        print("Se guardaron los datos con exito")
       

class Start(Docente,Alumno):
    def __init__(self):
        try:
          
           while True:
                print('''
                ¿Que desea hacer?
                1)Agregar información de alumno 
                2)Ver información de alumnos    
                3)Agregar informacion de docente
                4)Ver informacion de docentes
                5)Salir
                 ''')
                opcion= input("> ")
                if opcion=="1":
                   self.cargar_alumnos()
                   self.agregar_alumno()
                elif opcion=="2":
                    self.cargar_alumnos()
                    self.ver_info_alumnos()
                    
                elif opcion=="3":
                   self.cargar_docentes()
                   self.agregar_docente()
                elif opcion=="4":
                    self.cargar_docentes()
                    self.ver_info_docentes()
                elif opcion=="5":
                    quit()
                else:
                    print("ingrese una opcion valida")
        except KeyboardInterrupt:
            print('\nAplicacion interrumpida')

Start()