audi=float(0)
visual=float(0)
kine=float(0)
idk=float(0)
print("Bienvenido al programa de la encuestas de este modulo escolar, donde el estudante podra concentrar sus puntos debiles de estudios para que al final el profesor guie al alumno con un nuevo sistema de aprendizaje")
print("En caso de no poner los incisos indicados, se los tomara como NO RESPONDIDOS")
print("\nCOMENZAMOS\n")
print("Pregunta 1: Cual de las siguientes actividades disfrutas mas?")
print("a) Escuchar musica")
print("b) Ver peliculas")
print("c) Bailar con buena musica")
r=input("Ingresa un inciso: ")
if (r == "a"):
    audi = audi + 1
elif (r == "b"):
    visual = visual + 1
elif (r == "c"):
    kine = kine + 1
else:
    idk = idk + 1
print("\nPregunta 2: Que programa de television prefieres?")
print("a) Reportajes de descubrimientos y lugares")
print("b) Comico y de entretenimiento")
print("c) Noticias del mundo")
r=input("Ingresa un inciso: ")
if (r == "a"):
    visual = visual + 1
elif (r == "b"):
    kine = kine + 1
elif (r == "c"):
    audi = audi + 1
else:
    idk = idk + 1
print("\nPregunta 3: Cuando conversas con otra persona, tu")
print("a) La escuchas atentamente")
print("b) La observas")
print("c) Tiendes a tocarla")
r=input("Ingresa un inciso: ")
if (r == "a"):
    audi = audi + 1
elif (r == "b"):
    visual = visual + 1
elif (r == "c"):
    kine = kine + 1
else:
    idk = idk + 1
print("\nPregunta 4: Si pudieras adquirir uno de los siguientes articulos, cual elegirias?")
print("a) Un jacuzzi")
print("b) Un estereo")
print("c) Un televisor")
r=input("Ingresa un inciso: ")
if (r == "a"):
    kine = kine + 1
elif (r == "b"):
    audi = audi + 1
elif (r == "c"):
    visual = visual + 1
else:
    idk = idk + 1
print("\nPregunta 5: Que prefieres hacer un sabado en la tarde?")
print("a) Quedarte en casa")
print("b) Ir a un concierto")
print("c) Ir al cine")
r=input("Ingresa un inciso: ")
if (r == "a"):
    kine = kine + 1
elif (r == "b"):
    audi = audi + 1
elif (r == "c"):
    visual = visual + 1
else:
    idk = idk + 1
print("\nPregunta 6: Que tipo de examenes te facilitan mas?")
print("a) Examen oral")
print("b) Examen escrito")
print("c) Examen de opcion multiple")
r=input("Ingresa un inciso: ")
if (r == "a"):
    audi = audi + 1
elif (r == "b"):
    visual = visual + 1
elif (r == "c"):
    kine = kine + 1
else:
    idk = idk + 1
print("\nPregunta 7: Como te orientas mas facilmente?")
print("a) Mediante el uso de un mapa")
print("b) Pidiendo indicaciones")
print("c) A traves de la intuicion")
r=input("Ingresa un inciso: ")
if (r == "a"):
    visual = visual + 1
elif (r == "b"):
    audi = audi + 1
elif (r == "c"):
    kine = kine + 1
else:
    idk = idk + 1
print("\nPregunta 8: En que prefieres ocupar tu tiempo en un lugar de descanso?")
print("a) Pensar")
print("b) Caminar por los alrededores")
print("c) Descansar")
r=input("Ingresa un inciso: ")
if (r == "a"):
    audi = audi + 1
elif (r == "b"):
    visual = visual + 1
elif (r == "c"):
    kinr = kine + 1
else:
    idk = idk + 1
print("\nPregunta 9: Que te halaga mas?")
print("a) Que te digan que tienes buen aspecto")
print("b) Que te digan que tienes un trato muy agradable")
print("c) Que te digan que tienes una conversacion interesante")
r=input("Ingresa un inciso: ")
if (r == "a"):
    visual = visual + 1
elif (r == "b"):
    kine = kine + 1
elif (r == "c"):
    audi = audi + 1
else:
    idk = idk + 1
print("\nPregunta 10: Cual de estos ambientes te atrae mas?")
print("a) clima agradable")
print("b)olas del mar")
print("c) hermosa vista al oceano")
r=input("Ingresa un inciso: ")
if (r == "a"):
    kine = kine + 1
elif (r == "b"):
    audi = audi + 1
elif (r == "c"):
    visual = visual + 1
else:
    idk = idk + 1
if (idk == 0):
    from matplotlib import pyplot

    lenguajes = ("Audio", "Visual", "Kinestesico")
    slices = (audi, visual, kine)
    colores = ("Red", "Blue", "Green")

    pyplot.pie(slices, colors=colores, labels=lenguajes, autopct='%1.1f%%')

    pyplot.axis("Equal")
    pyplot.title("Resultados de la evaluacion")
    # pyplot.legend(labels=lenguajes)
    pyplot.show()
else:
    from matplotlib import pyplot

    lenguajes = ("Audio", "Visual", "Kinestesico", "INVALIDO")
    slices = (audi, visual, kine, idk)
    colores = ("Red", "Blue", "Green", "Gray")

    pyplot.pie(slices, colors=colores, labels=lenguajes, autopct='%1.1f%%')

    pyplot.axis("Equal")
    pyplot.title("Resultados de la evaluacion")
    # pyplot.legend(labels=lenguajes)
    pyplot.show()
print("\t\t\t Sumas y Restas \n")

print("\t\t Kinesico \n")

if (kine == 1):
    print("https://www.youtube.com/watch?v=35arstsomnc \n")

elif (kine == 2):
    print("https://www.youtube.com/watch?v=12IQZnWsL8E \n")
    print("https://www.youtube.com/watch?v=35arstsomnc \n")
elif (kine == 3):
    print("https://www.youtube.com/watch?v=boNv5VhAr7E \n")
    print("https://www.youtube.com/watch?v=12IQZnWsL8E \n")
    print("https://www.youtube.com/watch?v=d1U8Cke2oAE \n")
elif (kine == 4):
    print("https://www.youtube.com/watch?v=35arstsomnc \n")
    print("https://www.youtube.com/watch?v=i8Wbwf39Ti0 \n")
    print("https://www.youtube.com/watch?v=_tqjU_P_HlM \n")
    print("https://www.youtube.com/watch?v=86tboGybGcI \n")
elif (kine == 5):
    print("https://www.youtube.com/watch?v=boNv5VhAr7E \n")
    print("https://www.youtube.com/watch?v=d1U8Cke2oAE \n")
    print("https://www.youtube.com/watch?v=12IQZnWsL8E \n")
    print("https://www.youtube.com/watch?v=i8Wbwf39Ti0 \n")
    print("https://www.youtube.com/watch?v=_tqjU_P_HlM \n")
elif (kine == 6):
    print("https://www.youtube.com/watch?v=35arstsomnc \n")
    print("https://www.youtube.com/watch?v=boNv5VhAr7E \n")
    print("https://www.youtube.com/watch?v=d1U8Cke2oAE \n")
    print("https://www.youtube.com/watch?v=12IQZnWsL8E \n")
    print("https://www.youtube.com/watch?v=i8Wbwf39Ti0 \n")
    print("https://www.youtube.com/watch?v=_tqjU_P_HlM \n")
elif (kine == 7):
    print("https://www.youtube.com/watch?v=12IQZnWsL8E \n")
    print("https://www.youtube.com/watch?v=35arstsomnc \n")
    print("https://www.youtube.com/watch?v=boNv5VhAr7E \n")
    print("https://www.youtube.com/watch?v=d1U8Cke2oAE \n")
    print("https://www.youtube.com/watch?v=i8Wbwf39Ti0 \n")
    print("https://www.youtube.com/watch?v=JMTI_3ay-Og \n")
    print("https://www.youtube.com/watch?v=JMTI_3ay-O7 \n")
elif (kine == 8):
    print("https://www.youtube.com/watch?v=AMNACNvN8vc \n")
    print("https://www.youtube.com/watch?v=JMTI_3ay-Og \n")
    print("https://www.youtube.com/watch?v=f4f37hjiWc4 \n")
    print("https://www.youtube.com/watch?v=86tboGybGcI \n")
    print("https://www.youtube.com/watch?v=_tqjU_P_HlM \n")
    print("https://www.youtube.com/watch?v=i8Wbwf39Ti0 \n")
    print("https://www.youtube.com/watch?v=d1U8Cke2oAE \n")
    print("https://www.youtube.com/watch?v=12IQZnWsL8E \n")
elif (kine == 9):
    print("https://www.youtube.com/watch?v=boNv5VhAr7E \n")
    print("https://www.youtube.com/watch?v=d1U8Cke2oAE \n")
    print("https://www.youtube.com/watch?v=i8Wbwf39Ti0 \n")
    print("https://www.youtube.com/watch?v=_tqjU_P_HlM \n")
    print("https://www.youtube.com/watch?v=86tboGybGcI \n")
    print("https://www.youtube.com/watch?v=f4f37hjiWc4 \n")
    print("https://www.youtube.com/watch?v=JMTI_3ay-Og \n")
    print("https://www.youtube.com/watch?v=AMNACNvN8vc \n")
    print("https://www.youtube.com/watch?v=12IQZnWsL8E \n")
elif (kine == 10):
    print("https://www.youtube.com/watch?v=35arstsomnc \n")
    print("https://www.youtube.com/watch?v=12IQZnWsL8E \n")
    print("https://www.youtube.com/watch?v=boNv5VhAr7E \n")
    print("https://www.youtube.com/watch?v=d1U8Cke2oAE \n")
    print("https://www.youtube.com/watch?v=i8Wbwf39Ti0 \n")
    print("https://www.youtube.com/watch?v=_tqjU_P_HlM \n")
    print("https://www.youtube.com/watch?v=86tboGybGcI \n")
    print("https://www.youtube.com/watch?v=f4f37hjiWc4 \n")
    print("https://www.youtube.com/watch?v=JMTI_3ay-Og \n")
    print("https://www.youtube.com/watch?v=AMNACNvN8vc \n")
else:
    print("No es kinesico \n")

print("Visual")



if (visual == 1):
    print("https://www.youtube.com/watch?v=5-8xAn9RxyU \n")

elif (visual == 2):
    print("https://www.youtube.com/watch?v=5-8xAn9RxyU \n")
    print("https://www.youtube.com/watch?v=2Iy92z6WOqI \n")
elif (visual == 3):
    print("https://www.youtube.com/watch?v=5-8xAn9RxyU \n")
    print("https://www.youtube.com/watch?v=2Iy92z6WOqI \n")
    print("https://www.youtube.com/watch?v=1ktyVZthSX4 \n")
elif (visual == 4):
    print("https://www.youtube.com/watch?v=5-8xAn9RxyU \n")
    print("https://www.youtube.com/watch?v=2Iy92z6WOqI \n")
    print("https://www.youtube.com/watch?v=1ktyVZthSX4 \n")
    print("https://www.youtube.com/watch?v=CSlkZpoy5s8 \n")
elif (visual == 5):
    print("https://www.youtube.com/watch?v=5-8xAn9RxyU \n")
    print("https://www.youtube.com/watch?v=2Iy92z6WOqI \n")
    print("https://www.youtube.com/watch?v=1ktyVZthSX4 \n")
    print("https://www.youtube.com/watch?v=CSlkZpoy5s8 \n")
    print("https://www.youtube.com/watch?v=aGJ00fU5Cik \n")
elif (visual == 6):
    print("https://www.youtube.com/watch?v=5-8xAn9RxyU \n")
    print("https://www.youtube.com/watch?v=2Iy92z6WOqI \n")
    print("https://www.youtube.com/watch?v=1ktyVZthSX4 \n")
    print("https://www.youtube.com/watch?v=CSlkZpoy5s8 \n")
    print("https://www.youtube.com/watch?v=aGJ00fU5Cik \n")
    print("https://www.youtube.com/watch?v=szmjdS1Whz0 \n")
elif (kine == 7):
    print("https://www.youtube.com/watch?v=5-8xAn9RxyU \n")
    print("https://www.youtube.com/watch?v=CSlkZpoy5s8 \n")
    print("https://www.youtube.com/watch?v=1ktyVZthSX4 \n")
    print("https://www.youtube.com/watch?v=CSlkZpoy5s8 \n")
    print("https://www.youtube.com/watch?v=aGJ00fU5Cik \n")
    print("https://www.youtube.com/watch?v=szmjdS1Whz0 \n")
    print("https://www.youtube.com/watch?v=uLulA91jt_A \n")
elif (visual == 8):
    print("https://www.youtube.com/watch?v=5-8xAn9RxyU \n")
    print("https://www.youtube.com/watch?v=2Iy92z6WOqI \n")
    print("https://www.youtube.com/watch?v=1ktyVZthSX4 \n")
    print("https://www.youtube.com/watch?v=CSlkZpoy5s8 \n")
    print("https://www.youtube.com/watch?v=aGJ00fU5Cik \n")
    print("https://www.youtube.com/watch?v=szmjdS1Whz0 \n")
    print("https://www.youtube.com/watch?v=uLulA91jt_A \n")
    print("https://www.youtube.com/watch?v=Cv3T6QTnofs \n")
elif (visual == 9):
    print("https://www.youtube.com/watch?v=5-8xAn9RxyU \n")
    print("https://www.youtube.com/watch?v=2Iy92z6WOqI \n")
    print("https://www.youtube.com/watch?v=1ktyVZthSX4 \n")
    print("https://www.youtube.com/watch?v=CSlkZpoy5s8 \n")
    print("https://www.youtube.com/watch?v=aGJ00fU5Cik \n")
    print("https://www.youtube.com/watch?v=szmjdS1Whz0 \n")
    print("https://www.youtube.com/watch?v=uLulA91jt_A \n")
    print("https://www.youtube.com/watch?v=Cv3T6QTnofs \n")
    print("https://www.youtube.com/watch?v=LVHo5xvsvO0 \n")
elif (visual == 10):
    print("https://www.youtube.com/watch?v=5-8xAn9RxyU \n")
    print("https://www.youtube.com/watch?v=2Iy92z6WOqI \n")
    print("https://www.youtube.com/watch?v=1ktyVZthSX4 \n")
    print("https://www.youtube.com/watch?v=CSlkZpoy5s8 \n")
    print("https://www.youtube.com/watch?v=aGJ00fU5Cik \n")
    print("https://www.youtube.com/watch?v=szmjdS1Whz0 \n")
    print("https://www.youtube.com/watch?v=uLulA91jt_A \n")
    print("https://www.youtube.com/watch?v=Cv3T6QTnofs \n")
    print("https://www.youtube.com/watch?v=LVHo5xvsvO0 \n")
    print("https://www.youtube.com/watch?v=BWK6NLFQYzA \n")
else:
    print("No es visual")

print("Auditivo")

if (audi == 1):
    print("https://www.youtube.com/watch?v=OBD9io9Z02A \n")

elif (audi == 2):
    print("https://www.youtube.com/watch?v=OBD9io9Z02A \n")
    print("https://www.youtube.com/watch?v=3S4lsk6gqeY \n")
elif (audi == 3):
    print("https://www.youtube.com/watch?v=OBD9io9Z02A \n")
    print("https://www.youtube.com/watch?v=3S4lsk6gqeY \n")
    print("https://www.youtube.com/watch?v=p_-TitDXrmY \n")
elif (audi == 4):
    print("https://www.youtube.com/watch?v=OBD9io9Z02A \n")
    print("https://www.youtube.com/watch?v=3S4lsk6gqeY \n")
    print("https://www.youtube.com/watch?v=p_-TitDXrmY \n")
    print("https://www.youtube.com/watch?v=rXF5yQ7HYVQ \n")
elif (audi == 5):
    print("https://www.youtube.com/watch?v=OBD9io9Z02A \n")
    print("https://www.youtube.com/watch?v=3S4lsk6gqeY \n")
    print("https://www.youtube.com/watch?v=p_-TitDXrmY \n")
    print("https://www.youtube.com/watch?v=rXF5yQ7HYVQ \n")
    print("https://www.youtube.com/watch?v=R0XQ8AbtZbo \n")
elif (audi == 6):
    print("https://www.youtube.com/watch?v=OBD9io9Z02A \n")
    print("https://www.youtube.com/watch?v=3S4lsk6gqeY \n")
    print("https://www.youtube.com/watch?v=p_-TitDXrmY \n")
    print("https://www.youtube.com/watch?v=rXF5yQ7HYVQ \n")
    print("https://www.youtube.com/watch?v=R0XQ8AbtZbo \n")
    print("https://www.youtube.com/watch?v=zB62w5cRpUQ \n")
elif (audi == 7):
    print("https://www.youtube.com/watch?v=OBD9io9Z02A \n")
    print("https://www.youtube.com/watch?v=3S4lsk6gqeY \n")
    print("https://www.youtube.com/watch?v=p_-TitDXrmY \n")
    print("https://www.youtube.com/watch?v=rXF5yQ7HYVQ \n")
    print("https://www.youtube.com/watch?v=R0XQ8AbtZbo \n")
    print("https://www.youtube.com/watch?v=zB62w5cRpUQ \n")
    print("https://www.youtube.com/watch?v=_ciH9pOnJYs \n")
elif (audi == 8):
    print("https://www.youtube.com/watch?v=OBD9io9Z02A \n")
    print("https://www.youtube.com/watch?v=3S4lsk6gqeY \n")
    print("https://www.youtube.com/watch?v=p_-TitDXrmY \n")
    print("https://www.youtube.com/watch?v=rXF5yQ7HYVQ \n")
    print("https://www.youtube.com/watch?v=R0XQ8AbtZbo \n")
    print("https://www.youtube.com/watch?v=zB62w5cRpUQ \n")
    print("https://www.youtube.com/watch?v=_ciH9pOnJYs \n")
    print("https://www.youtube.com/watch?v=1p4TecYqtwI \n")
elif (audi == 9):
    print("https://www.youtube.com/watch?v=OBD9io9Z02A \n")
    print("https://www.youtube.com/watch?v=3S4lsk6gqeY \n")
    print("https://www.youtube.com/watch?v=p_-TitDXrmY \n")
    print("https://www.youtube.com/watch?v=rXF5yQ7HYVQ \n")
    print("https://www.youtube.com/watch?v=R0XQ8AbtZbo \n")
    print("https://www.youtube.com/watch?v=zB62w5cRpUQ \n")
    print("https://www.youtube.com/watch?v=_ciH9pOnJYs \n")
    print("https://www.youtube.com/watch?v=1p4TecYqtwI \n")
    print("https://www.youtube.com/watch?v=OetrABNO3T4 \n")
elif (audi == 10):
    print("https://www.youtube.com/watch?v=OBD9io9Z02A \n")
    print("https://www.youtube.com/watch?v=3S4lsk6gqeY \n")
    print("https://www.youtube.com/watch?v=p_-TitDXrmY \n")
    print("https://www.youtube.com/watch?v=rXF5yQ7HYVQ \n")
    print("https://www.youtube.com/watch?v=R0XQ8AbtZbo \n")
    print("https://www.youtube.com/watch?v=zB62w5cRpUQ \n")
    print("https://www.youtube.com/watch?v=_ciH9pOnJYs \n")
    print("https://www.youtube.com/watch?v=1p4TecYqtwI \n")
    print("https://www.youtube.com/watch?v=OetrABNO3T4 \n")
    print("https://www.youtube.com/watch?v=YiRst8TZgEE \n")
else:
    print("No es auditivo")


print("\t\t Evaluacion \n")
print("\t\t https://www.matesfacil.com/interactivos/primaria/sumas-restas-primaria-ejercicios-interactivos-autocorreccion-online-test-examen-llevada-huecos-TIC.html")

