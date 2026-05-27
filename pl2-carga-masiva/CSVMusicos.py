import csv
import random

NUM_MUSICOS = 1_000_000
NUM_GRUPOS = 200_000
NUM_DISCOS = 1_000_000
NUM_CONCIERTOS = 100_000
NUM_ENTRADAS = 24_000_000

GENEROS = ["clásica", "blues", "jazz", "rock&roll", "góspel", "soul", "rock", 
           "metal", "funk", "disco", "techno", "pop", "reggae", "hiphop", "salsa"]

PAISES = ["España", "Francia", "Italia", "Alemania", "Reino Unido", "Portugal", 
          "EEUU", "México", "Argentina", "Brasil", "Japón", "China", "Australia", 
          "Canadá", "Holanda", "Bélgica", "Suecia", "Noruega", "Irlanda", "Grecia"]

print("Generando datos ajustados al esquema de pgModeler...")

# 1. GRUPO (Codigo_grupo, Nombre, Genero_musical, Pais, Sitio_web)
print("1/7 - Generando Grupos...")
with open('grupos.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for i in range(1, NUM_GRUPOS + 1):
        writer.writerow([i, f"Grupo_{i}", random.choice(GENEROS), random.choice(PAISES), f"www.grupo{i}.com"])

# 2. MUSICOS (codigo_musico, DNI, Nombre, Direccion, Codigo_Postal, Ciudad, Provincia, telefono, Instrumentos, Codigo_grupo_Grupo)
print("2/7 - Generando Músicos...")
with open('musicos.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for i in range(1, NUM_MUSICOS + 1):
        id_grupo = ((i - 1) // 5) + 1
        dni = f"{i:08d}{chr(65 + (i % 26))}" # DNI Único
        writer.writerow([i, dni, f"Musico_{i}", "Calle Musica 123", 28000, "Madrid", "Madrid", 600000000, "Guitarra", id_grupo])

# 3. CONCIERTOS (Codigo_concierto, Fecha_realizacion, Pais, Ciudad, Recinto)
print("3/7 - Generando Conciertos...")
with open('conciertos.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for i in range(1, NUM_CONCIERTOS + 1):
        mes = random.randint(1, 12)
        dia = random.randint(1, 28)
        writer.writerow([i, f"2025-{mes:02d}-{dia:02d}", random.choice(PAISES), "Ciudad de Gira", "Estadio Municipal"])

# 4. DISCOS (Codigo_disco, Titulo, Fecha_edicion, Genero, Formato, Codigo_grupo_Grupo)
print("4/7 - Generando Discos...")
with open('discos.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for i in range(1, NUM_DISCOS + 1):
        id_grupo = random.randint(1, NUM_GRUPOS)
        writer.writerow([i, f"Disco_{i}", "2025-01-01", random.choice(GENEROS), "Vinilo", id_grupo])

# 5. CANCIONES (Codigo_cancion, Nombre, Compositor, Fecha_grabacion, Duracion, Codigo_disco_Discos)
print("5/7 - Generando Canciones (12M)...")
with open('canciones.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for i in range(1, 12_000_001):
        id_disco = ((i - 1) // 12) + 1
        minutos = random.randint(2, 6)
        segundos = random.randint(10, 59)
        duracion_time = f"00:0{minutos}:{segundos}" # Formato TIME de PostgreSQL
        writer.writerow([i, f"Cancion_{i}", "Compositor Anonimo", "2025-01-01", duracion_time, id_disco])

# 6. ENTRADAS (Codigo_entrada, Localidad, Precio, Usuario, Codigo_concierto_Conciertos)
print("6/7 - Generando Entradas (24M)...")
with open('entradas.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for i in range(1, NUM_ENTRADAS + 1):
        id_concierto = random.randint(1, NUM_CONCIERTOS)
        precio = random.randint(20, 100)
        writer.writerow([i, "Pista General", precio, f"Usuario_{i}", id_concierto])

# 7. GRUPOS_TOCAN_CONCIERTOS (Codigo_grupo_Grupo, Codigo_concierto_Conciertos)
print("7/7 - Generando Relación Grupos-Conciertos...")
with open('grupos_conciertos.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for id_grupo in range(1, NUM_GRUPOS + 1):
        conciertos_asignados = random.sample(range(1, NUM_CONCIERTOS + 1), 10)
        for id_concierto in conciertos_asignados:
            writer.writerow([id_grupo, id_concierto])

print("¡Archivos perfectos para tu pgModeler generados!")




