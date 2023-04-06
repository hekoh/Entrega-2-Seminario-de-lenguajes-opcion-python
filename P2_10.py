nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

def promedio(dicci):
    prom = lambda dicci: (dicci[0]+dicci[1])/2
    return (prom(dicci))

def maxMin(promedios,alumnos):
    max = -9999
    min = 9999     
    i=0                                                 
    for elem in promedios:
        for i in range(1):       
            if alumnos[elem][i] < min:
                min = alumnos[elem][i]
                minK = elem
        if promedios[elem] > max:
            max = promedios[elem]
            maxK = elem       
    return(maxK,minK)

promediosDict = {}
nombres = nombres.split(",")
i = 0
total = 0
alumnos = {}
for i in range(len(nombres)):                                               
    buildList = lambda x,y: (x[i],y[i])
    alumnos[nombres[i]] = buildList(notas_1,notas_2)
#print(alumnos,"\n")                                                                    print para comprobar el diccionario de alumnos

for elem in alumnos:
    aux = promedio(alumnos[elem])
    total += aux
    promediosDict[elem] = aux
print("el promedio del curso es: ", total / len(nombres),"\n")
max,min= maxMin(promediosDict,alumnos)
print("el alumno con el mayor promedio del curso es: ", max,"\n","y el alumno que obtuvo la menor nota del curso fue: ", min)
