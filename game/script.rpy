# NEXUS: 宿命の瞳 (Los Ojos del Destino)
# Guion Principal - Novela Visual ambientada en la región central de Japón
# Capítulo 1: El Despertar de Shinshu y la Aguja del Destino

# -----------------------------------------------------------------------------
# Declaración de Personajes
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Declaración de Personajes - Ruta Shinshu (Hombre)
# -----------------------------------------------------------------------------
define p = Character("Ren", color="#e63946", who_outlines=[(1, "#2b0709", 0, 0)], what_color="#ffffff")
define aoi = Character("Aoi", color="#38bdf8", who_outlines=[(1, "#082f49", 0, 0)], what_color="#f8fafc")
define madre = Character("Madre", color="#f472b6", who_outlines=[(1, "#500724", 0, 0)], what_color="#f8fafc")
define kenji = Character("Dr. Kenji Ogata", color="#60a5fa", who_outlines=[(1, "#172554", 0, 0)], what_color="#f8fafc")
define enf = Character("Enfermera Sato", color="#c084fc", who_outlines=[(1, "#3b0764", 0, 0)], what_color="#f8fafc")
define doc = Character("Dr. Moriyama", color="#34d399", who_outlines=[(1, "#022c22", 0, 0)], what_color="#f8fafc")
define kuroda = Character("Sr. Kuroda", color="#94a3b8", who_outlines=[(1, "#0f172a", 0, 0)], what_color="#f8fafc")
define misterio = Character("???", color="#f87171", who_outlines=[(1, "#450a0a", 0, 0)], what_color="#fecaca")

# -----------------------------------------------------------------------------
# Declaración de Personajes - Ruta Aoi (Mujer)
# -----------------------------------------------------------------------------
define aoi_p = Character("Aoi", color="#c084fc", who_outlines=[(1, "#3b0764", 0, 0)], what_color="#ffffff")
define shinshu = Character("Shinshu", color="#e63946", who_outlines=[(1, "#2b0709", 0, 0)], what_color="#ffffff")
define yuna = Character("Yuna", color="#38bdf8", who_outlines=[(1, "#0c4a6e", 0, 0)], what_color="#f0f9ff")
define padre_yuna = Character("Sr. Tachibana", color="#94a3b8", who_outlines=[(1, "#1e293b", 0, 0)], what_color="#f8fafc")

# -----------------------------------------------------------------------------
# Siluetas de los Personajes
# -----------------------------------------------------------------------------
image silueta_ren = "images/silueta_ren.png"
image silueta_aoi = "images/Aoi.png"
image aoi_base = "images/Aoi.png"
image aoi_agachada_melancolica = "images/aoi_agachada_melancolica.png"
image aoi_sentada_suelo = "images/aoi_sentada_suelo.png"
image aoi_de_pie_abrazandose = "images/aoi_de_pie_abrazandose.png"
image aoi_caminando_desanimada = "images/aoi_caminando_desanimada.png"
image aoi_llorando_manga = "images/aoi_llorando_manga.png"
image aoi_abrazando_rodillas = "images/aoi_abrazando_rodillas.png"
image aoi_sentada_piernas_desganadas = "images/aoi_sentada_piernas_desganadas.png"
image aoi_sentada_costado_mano = "images/aoi_sentada_costado_mano.png"
image aoi_arrodillada_desolada = "images/aoi_arrodillada_desolada.png"
image aoi_acurrucada_llorando_mano = "images/aoi_acurrucada_llorando_mano.png"
image aoi_de_pie_correa_bolso = "images/aoi_de_pie_correa_bolso.png"
image silueta_madre = "images/silueta_madre.png"
image silueta_kenji = "images/silueta_kenji.png"
image silueta_enfermera = "images/silueta_enfermera.png"
image silueta_doctor = "images/silueta_doctor.png"

# Fondos Cinematográficos del Menú Principal (Alternancia Continua 3.5s / 1.5s disolución)
image bg_menu_mano_sangre = "images/nexus_destino_mano_sangre.png"
image bg_menu_mariposa_rosa = "images/nexus_destino_mariposa_rosa.png"

image main_menu_animated_bg:
    "images/nexus_destino_mano_sangre.png"
    pause 3.5
    choice:
        pass
    "images/nexus_destino_mariposa_rosa.png" with Dissolve(1.5)
    pause 3.5
    "images/nexus_destino_mano_sangre.png" with Dissolve(1.5)
    repeat

# Posicionamiento y escalado suave de siluetas
transform silueta_left:
    xalign 0.18
    yalign 1.0
    zoom 0.88

transform silueta_floor_center:
    xalign 0.5
    yalign 1.0
    zoom 0.95

transform silueta_floor_left:
    xalign 0.2
    yalign 1.0
    zoom 0.95

transform silueta_right:
    xalign 0.82
    yalign 1.0
    zoom 0.88

transform silueta_center:
    xalign 0.5
    yalign 1.0
    zoom 0.88

# -----------------------------------------------------------------------------
# Fondos y Efectos Visuales Nativos
# -----------------------------------------------------------------------------
image bg negro = Solid("#07080a")
image bg vacio_mental = Solid("#0d0d12")
image bg hospital_dia = Solid("#181b24")
image bg hospital_tarde = Solid("#231a1a")
image bg hospital_noche = Solid("#0d0f14")
image bg hospital_pasillo = Solid("#11151f")
image bg hospital_morado = Solid("#181026")
image bg hospital_habitacion_aoi = Solid("#130f1e")
image bg bano_espejo = Solid("#0d121c")
image bg destello_rojo = Solid("#7a0b0b")
image bg destello_morado = Solid("#581c87")
image bg sangre_visceral = Solid("#4a0505")
image bg sangre_espejo = Solid("#3b0764")
image bg habitacion_aislamiento = Solid("#110a1c")

# Efectos de transición personalizados
define eye_pulse = Fade(0.2, 0.1, 0.3, color="#8a0f0f")
define vision_flash = Fade(0.15, 0.2, 0.4, color="#a30e0e")
define eye_pulse_aoi = Fade(0.2, 0.1, 0.3, color="#6b21a8")
define vision_flash_aoi = Fade(0.15, 0.2, 0.4, color="#9333ea")
define fade_muerte = Fade(1.5, 1.2, 2.0, color="#050000")
define fade_lento = Fade(1.0, 0.5, 1.0, color="#000000")

# -----------------------------------------------------------------------------
# Entrada Inicial del Juego (Antes del Menú Principal)
# -----------------------------------------------------------------------------
label splashscreen:
    if persistent.selected_gender is None:
        call screen protagonist_selection
    return

# -----------------------------------------------------------------------------
# Inicio de la Partida - Prólogo Conceptual
# -----------------------------------------------------------------------------
label start:

    # -------------------------------------------------------------------------
    # PRÓLOGO CONCEPTUAL EN PANTALLA COMPLETA (SIN CAJA DE DIÁLOGO)
    # -------------------------------------------------------------------------
    scene bg negro
    with fade_lento

    stop music fadeout 1.5

    play sound "audio/heartbeat.wav"
    call screen cinematic_prologue_epigraph

    play sound "audio/glass_break.wav"
    call screen cinematic_butterfly_effect

    play sound "audio/eye_vision.wav"
    call screen cinematic_nexus_event

    play sound "audio/rain.wav" loop

    # -------------------------------------------------------------------------
    # EL ECO DEL ASFALTO Y LA NIEBLA DE CHŪBU (RECUERDO COMPARTIDO)
    # -------------------------------------------------------------------------
    "Hay un vacío helado en el fondo de mi memoria."
    "No es la simple ausencia de recuerdos. Es algo mucho más siniestro: la certidumbre asfixiante de que el día del impacto, algo humano murió dentro de mí... y algo antiguo e inhumano despertó para ocupar su lugar."

    "Lo único que sobrevive de mi infancia es un retazo fragmentado, empapado por el frío glacial de las cordilleras de Nagano, en la región central de Chūbu..."

    scene bg vacio_mental
    with Dissolve(1.5)

    "La lluvia caía como agujas líquidas aquella tarde sobre el asfalto grisáceo de Matsumoto."
    "Aoi, mi hermana menor, apenas tenía siete años. Caminaba dos pasos delante de mí, dando saltitos torpes mientras el viento sacudía su pequeño paraguas amarillo."

    # Silueta de Aoi infantil en el cruce de peatones
    show silueta_aoi at silueta_center with Dissolve(1.0)

    aoi "¡Mira, hermano! Si pisas solo las líneas blancas del paso de peatones, los monstruos de la niebla no te alcanzan..."

    shinshu "Aoi, camina despacio. El suelo está resbaladizo y mamá nos espera al otro lado de la estación."

    "Y entonces... la atmósfera se quebró."
    "El aire se volvió denso, oliendo a ozono quemado y óxido ferroso."
    "El sonido de las gotas de lluvia pareció detenerse en seco a escasos centímetros del suelo."

    "Un chirrido ensordecedor de neumáticos desgarrando el asfalto helado resonó desde la curva."
    "A través de la niebla espesa no surgieron luces comunes. Eran dos faros deformes, cegadores y rojizos, como las pupilas incandescentes de una bestia de acero lanzada a tumba abierta."

    # Efecto sonoro de impacto brutal
    play sound "audio/crash.wav"

    if persistent.selected_gender == "mujer":
        # ---------------------------------------------------------------------
        # BIFURCACIÓN ALPHA: ATROPELLO DE AOI (RUTA MUJER)
        # ---------------------------------------------------------------------
        with vpunch

        hide silueta_aoi
        scene bg destello_rojo
        with vision_flash_aoi

        "El tiempo no me concedió espacio para reaccionar."
        "Un impacto atronador de acero y velocidad embistió mi pequeño cuerpo de lleno. El paraguas amarillo salió volando por los aires hacia la niebla..."
        "En mi último segundo de lucidez, vi la silueta desesperada de mi hermano Shinshu corriendo hacia mí con los brazos extendidos, desgarrándose la voz al gritar mi nombre antes de que mi cabeza se estrellara contra el bordillo del asfalto helado."

        stop sound fadeout 1.5

        scene bg negro
        with fade_muerte

        "Y luego... el silencio más absoluto. Un abismo de oscuridad infinita."

        jump chapter1_aoi

    else:
        # ---------------------------------------------------------------------
        # BIFURCACIÓN OMEGA: IMPACTO RECIBIDO POR SHINSHU (RUTA HOMBRE)
        # ---------------------------------------------------------------------
        "El tiempo no me concedió espacio para la vacilación."
        "Un impulso ciego y visceral se apoderó de mis músculos: me arrojé hacia adelante con toda la desesperación de mis manos infantiles, empujando a Aoi fuera de la trayectoria mortal hacia la acera."

        with vpunch

        hide silueta_aoi
        scene bg destello_rojo
        with vision_flash

        "Un crujido espantoso. Huesos pulverizándose contra el parachoques blindado."
        "Mi cuerpo suspendido en el aire antes de estrellarse contra el pavimento congelado."
        "Recuerdo la sangre tibia escurriéndose entre el agua de lluvia... y sobre todo, una figura inmóvil detrás del parabrisas del camión. Una silueta sin rostro que me miraba con fijeza espectral."

        misterio "{i}«La muerte no se cancela, niño... solo transfiere sus ojos a quien la desafía.»{/i}"

        stop sound fadeout 1.8

        scene bg negro
        with fade_lento

        "Después de aquella voz gutural... no hubo dolor. Solo un abismo insondable de coma profundo que devoró años enteros de mi existencia."

        jump chapter1_shinshu_despertar

    # -------------------------------------------------------------------------
    # EL DESPERTAR EN EL HOSPITAL GENERAL DE SHINSHU (HABITACIÓN 304)
    # -------------------------------------------------------------------------
label chapter1_shinshu_despertar:
    # Pitido del monitor cardíaco al recuperar el conocimiento
    play sound "audio/monitor.wav"

    scene bg hospital_dia
    with Dissolve(1.8)

    # Entra el tema musical principal melancólico de la historia (Piano puro)
    play music "audio/piano_sad_theme.wav" fadein 2.5 loop

    $ grant_achievement("despertar")

    "Un zumbido monótono y constante me arrancó de la penumbra."
    "Cuando mis párpados finalmente cedieron, la luz blanquecina y desabrida de los tubos fluorescentes me quemó las córneas."
    "El olor era inconfundible: éter, alcohol yodado, humedad esterilizada y metal quirúrgico."
    "Habitación 304. Pabellón Oeste del Hospital General de Shinshu."

    "Al lado de mi camilla, dos siluetas temblaban entre sollozos ahogados."

    # Siluetas de la Madre y la Hermana menor junto a la cama
    show silueta_madre at silueta_left with Dissolve(0.8)
    show silueta_aoi at silueta_right with Dissolve(0.8)

    madre "¡Ren...! ¡Oh, dioses del cielo... Ren! ¡Despertó... el médico dijo que su actividad cerebral era irreversible...!"

    aoi "¡Hermano...! Pensé... pensé que te habías marchado para siempre... ¡Todo fue por mi culpa! ¡Si no hubiera insistido en cruzar bajo la tormenta...!"

    p "Aoi... Mamá..."

    "Mi garganta ardía como si hubiese tragado arena volcánica. Al intentar mover los brazos, sentí una pesadez antinatural, como si mi cuerpo no me perteneciera por completo."

    madre "No te esfuerces en hablar, hijo mío. Iré a buscar de inmediato al doctor de guardia. No te muevas..."

    hide silueta_madre with Dissolve(0.6)

    "La puerta corrediza se cerró tras ella con un chasquido hueco. En la habitación solo quedamos Aoi y yo."
    "La penumbra de la tarde comenzaba a devorar la luz que entraba por el ventanal exterior. Afuera, las sombras de las montañas de Nagano parecían estirarse como garras sobre el valle."

    aoi "Hermano... durante estos meses que estuviste dormido... sentí mucho miedo."
    aoi "Cada noche venía a sentarme aquí. Pero a veces... a veces cuando las luces del pasillo se apagaban, tus ojos se entreabrían."

    p "¿Mis ojos...?"

    aoi "Sí... pero no me miraban a mí. Brillaban bajo las sábanas con un fulgor rojo... como dos rescoldos encendidos en la ceniza. Me daba un escalofrío horrible."

    p "Debieron ser alucinaciones por el cansancio, Aoi. El accidente nos dejó secuelas a ambos."

    "Aoi apretó los labios con fuerza, tratando de borrar la inquietud de su rostro con una sonrisa infantil forzada."

    aoi "¡Tienes razón! ¡Ya no quiero pensar en cosas tétricas! Para demostrarme que tus reflejos están intactos y que sigues siendo mi hermano mayor... ¿qué tal una partida de Piedra, Papel o Tijera como antes de aquel día?"
    aoi "¡El que pierda tendrá que comprarle al otro un té verde helado con mochi en la cafetería del centro de Matsumoto cuando te den el alta!"

    p "El té de Matsumoto... de acuerdo, Aoi. Veamos si sigues leyendo mis intenciones como de costumbre."

    # -------------------------------------------------------------------------
    # EL MINIJUEGO DE JANKEN: LA PRIMERA MANIFESTACIÓN DEL PODER
    # -------------------------------------------------------------------------
    $ aoi_options = ["piedra", "papel", "tijera"]
    $ aoi_juega = renpy.random.choice(aoi_options)

    "Aoi alzó su puño cerrado frente a la camilla. Sus dedos temblaban con una inocencia desarmante."
    "Y en ese milisegundo... algo se sacudió detrás de mis retinas."
    "El flujo del tiempo pareció condensarse en una sustancia espesa. El sonido del segundero de la pared se alargó en un retumbo sordo y grave."

    menu:
        "¿Cómo decides enfrentar el juego del destino?"

        "Jugar limpiamente confiando en tu intuición fraternal":
            "Decido ignorar el extraño hormigueo en mis pupilas y confío en mis reflejos humanos ordinarios."
            window hide
            $ ren_choice = renpy.call_screen("janken_minigame", aoi_choice=aoi_juega, foresight_active=False)
            window auto

        "Concentrarte e intentar usar la visión carmesí de tus ojos para anticipar su jugada":
            play sound "audio/eye_vision.wav"
            with eye_pulse
            $ grant_achievement("ojo_premonicion")
            "Una descarga incandescente atraviesa tu nervio óptico con el filo de un escalpelo."
            "El mundo pierde toda saturación: las paredes del hospital se vuelven cenicientas, y sobre la mano derecha de Aoi se dibujan tenues filamentos escarlatas que trazan la contracción exacta de sus tendones antes de moverse."
            "Por una fracción de segundo, vislumbras el eco espectral de su jugada proyectado en el aire."
            window hide
            $ ren_choice = renpy.call_screen("janken_minigame", aoi_choice=aoi_juega, foresight_active=True)
            window auto

    $ grant_achievement("janken_jugar")

    # Evaluación y Resolución del Duelo
    if ren_choice == aoi_juega:
        $ persistent.janken_draws += 1
        "Ambos extendieron sus manos simultáneamente: [ren_choice.upper()] contra [aoi_juega.upper()]."
        aoi "¡Empate! ¡Aiko de shou! ¡Ja, ja, ja! Parece que nuestras mentes siguen conectadas por el mismo hilo, hermano."
        p "Tus reflejos siguen siendo rápidos, Aoi."
    elif (ren_choice == "piedra" and aoi_juega == "tijera") or (ren_choice == "papel" and aoi_juega == "piedra") or (ren_choice == "tijera" and aoi_juega == "papel"):
        $ persistent.janken_wins += 1
        $ grant_achievement("janken_victoria")
        "¡Tu [ren_choice.upper()] supera al [aoi_juega.upper()] de Aoi con precisión milimétrica!"
        aoi "¡Ahhh, no puede ser! ¡¿Cómo supiste exactamente qué iba a sacar?! ¡Parecía que estabas mirando mi mente antes de que yo misma decidiera mover los dedos!"
        p "Te advertí que el coma no oxidó mis sentidos."
        aoi "¡Eso no es justo! Pero una promesa es una promesa... el té verde helado va por mi cuenta."
    else:
        $ persistent.janken_losses += 1
        "El [aoi_juega.upper()] de Aoi supera limpiamente a tu [ren_choice.upper()]."
        aoi "¡Toma ya! ¡Gané! ¡El té helado y el mochi corren por tu bolsillo cuando salgas de aquí, hermano!"
        p "Bien jugado, Aoi... acepto mi derrota con honor."

    "Por unos instantes, la calidez de un hogar parecía haber regresado a la gélida habitación 304."
    "Pero justo antes de bajar la mano, Aoi dio un paso atrás, clavando su mirada en mi rostro con un estremecimiento repentino."

    aoi "Hermano... tus pupilas... por una décima de segundo destellaron en rojo vivo... Fue idéntico a lo que vi durante mis pesadillas."

    p "Debe ser el reflejo de la luz del pasillo, Aoi. Descansa."

    hide silueta_aoi with Dissolve(0.8)

    # -------------------------------------------------------------------------
    # EL ESPEJO DEL BAÑO Y LA CONDENA INTERIOR
    # -------------------------------------------------------------------------
    scene bg hospital_tarde
    with Dissolve(1.0)

    # Silueta de Ren en el baño
    show silueta_ren at silueta_center with Dissolve(0.8)

    "Cuando Aoi y mi madre se marcharon por la noche, me arrastré con dificultad hacia el pequeño cuarto de baño de la habitación."
    "Apoyé ambas manos sobre la loza húmeda del lavabo y alcé la vista hacia el espejo empañado."

    play sound "audio/heartbeat.wav"

    "Aquel reflejo me devolvió una imagen que apenas reconocía."
    "No era solo la palidez cadavérica de quien ha dormido al borde del abismo. Era el fondo de mis ojos: en la oscuridad, las pupilas no reflejaban el cristal. Vibraban con un anillo escarlata tenue, como el rescoldo de un fuego maldito."

    p "(¿Qué me hicieron durante aquel choque...? ¿Por qué sobreviví cuando todo mi cuerpo debió haber quedado destrozado?)"

    hide silueta_ren with Dissolve(0.6)

    # -------------------------------------------------------------------------
    # EL PASILLO EN PENUMBRA Y EL ANCIANO KURODA
    # -------------------------------------------------------------------------
    scene bg hospital_pasillo
    with Dissolve(1.2)

    "El insomnio se volvió un veneno en las noches siguientes."
    "Cada vez que cerraba los ojos, el sonido de huesos partiéndose y aquel susurro en la lluvia volvían a resonar en mi cráneo."

    "Caminaba apoyado en un bastón de aluminio por el pasillo oeste cuando una figura decrépita llamó mi atención."
    "El Sr. Kuroda. Un paciente octogenario internado en el pabellón de cardiología."
    "Estaba descalzo sobre el piso de linóleo gélido, murmurando con la mirada perdida hacia el final del corredor."

    kuroda "No escuches a las enfermeras cuando vengan con las bandejas plateadas... El agua de este hospital está bendecida con muerte..."

    p "Señor Kuroda, no debería estar de pie sin zapatillas. Hace demasiado frío en este pasillo."

    "El anciano volteó el rostro lentamente. Su cuello crujió con la rigidez de una rama seca. Sus ojos apagados se fijaron en los míos."

    kuroda "Tú... tú tienes el hedor del cruce de caminos en la ropa. Tú estuviste muerto... y la parca te puso sus pupilas para no perderte de vista."

    p "¿De qué está hablando...?"

    # Sonido espectral de visión ocular
    play sound "audio/eye_vision.wav"
    with eye_pulse

    "Una quemadura brutal estalló detrás de mi globo ocular izquierdo."
    "El pasillo se distorsionó como si una gota de tinta negra cayera en un vaso de agua."
    "Dentro de los ojos del anciano Kuroda, la realidad se desgarró:"

    # PROYECCIÓN DE LA MUERTE DE KURODA
    scene bg destello_rojo
    with vision_flash

    "No vi su reflejo. Vi una proyección espantosa, lúcida e implacable: él mismo, a las 20:15 de esa misma noche, encerrado en el cubículo tres del baño de caballeros."
    "Lo veía caer de rodillas contra el inodoro, desgarrándose el camisón con uñas amoratadas mientras un infarto fulminante le aplastaba el miocardio. Su lengua hinchada asomando entre dientes crispados, asfixiándose en su propia saliva sin poder gritar auxilio."

    scene bg hospital_pasillo
    with Dissolve(0.6)

    play sound "audio/heartbeat.wav"

    "Parpadeé con el pulso martillándome las sienes. El sudor frío me empapaba la nuca."
    "Kuroda me miró una última vez antes de que una enfermera lo tomara del brazo y se lo llevara de regreso a su cama."

    "A las 20:15 en punto... una sirena médica de código azul rasgó el silencio sepulcral del pabellón oeste."
    "Tres médicos y dos enfermeros corrieron con el desfibrilador hacia el baño de caballeros."
    "El anciano Kuroda yacía muerto en el suelo del cubículo tres. Exactamente en la misma posición, con el camisón desgarrado y los labios violetas que mis ojos habían contemplado horas antes."

    $ grant_achievement("mirada_carmesi")

    p "(No fue una pesadilla... No fue un delirio postraumático...)"
    "El pavor me paralizó hasta la médula de los huesos. Mis ojos no predecían el futuro: contemplaban la ejecución inexorable de la muerte antes de que ocurriera."

    # -------------------------------------------------------------------------
    # LA HABITACIÓN COMPARTIDA Y KENJI TAKAHASHI
    # -------------------------------------------------------------------------
    scene bg hospital_tarde
    with Dissolve(1.2)

    "Mi compañero de cuarto era Kenji Takahashi, un chico de diecinueve años internado por una doble fractura de tibia tras una excursión por los senderos alpinos de Kamikochi."
    "En medio de la pesadez de aquel hospital, Kenji era el único rayo de normalidad."

    # Silueta de Kenji
    show silueta_kenji at silueta_right with Dissolve(0.8)

    kenji "¡Oye, Ren! Te juro que la gelatina de este hospital sabe a plástico derretido. En dos días me quitan la escayola y te juro que lo primero que haré será comerme un tazón gigante de ramen picante en Matsumoto."

    p "Tienes buen apetito para alguien con clavos de titanio en la pierna, Kenji."

    kenji "¡Hay que mantener el espíritu alto, amigo! Además, a las seis en punto me toca la última dosis del antibiótico de amplio espectro por vía intravenosa y quedaré libre de agujas."

    "Kenji me sonrió con una franqueza tan limpia y juvenil que me recordó a los veranos que yo había olvidado."
    "Sus ojos brillaban bajo el sol mortecino que teñía los ventanales de un color carmesí apagado."

    "Y entonces... volví a cometer el error."
    "Mis ojos se clavaron involuntariamente en sus pupilas."

    with vpunch
    play sound "audio/eye_vision.wav"

    scene bg destello_rojo
    with vision_flash

    "Un dolor ensordecedor me perforó el cráneo, como si alguien hubiera introducido un clavo ardiente en mi cerebro."
    "En las pupilas de Kenji, el futuro no era una única línea de tiempo."
    "La realidad se bifurcaba salvajemente en dos senderos incompatibles:"

    # PRIMER SENDERO
    "SENDERO A (EL HILO VIVO):"
    "Si la aguja no entraba en su vía intravenosa a las 18:00, Kenji se recuperaba. Lo veía dos años después, riendo bajo la nevada de Matsumoto con su familia, subiendo a los miradores de Nagano con su cámara fotográfica."

    with vision_flash

    # SEGUNDO SENDERO
    "SENDERO B (EL CADÁVER EN LA CAMILLA):"
    "Si la enfermera cerraba la puerta y presionaba el émbolo a las 18:00... una agonía despiadada y química lo desgarraba en segundos."
    "Vi en sus ojos cómo el fármaco descompuesto coagulaba su sangre: sus venas convirtiéndose en cordones negros bajo la piel del cuello, sus pulmones deshaciéndose en espuma hemorrágica mientras se retorcía como un animal sacrificado sobre las sábanas empapadas."

    scene bg hospital_tarde
    with Dissolve(0.5)

    show silueta_kenji at silueta_right

    play sound "audio/heartbeat.wav"

    "Regresé a la realidad temblando de forma incontrolable, con el corazón golpeando mi pecho como un animal enjaulado."
    "El reloj analógico de la pared marcaba las 17:52."
    "Ocho minutos. Ocho minutos exactos antes de que la enfermera cruzara esa puerta con la muerte sellada en una jeringa."

    p "(Si guardo silencio... Kenji morirá ahogado en su propia sangre... pero si hablo, ¿quién le creería a un convaleciente con traumatismo craneal?)"

    # -------------------------------------------------------------------------
    # LA GRAN ENCRUCIJADA DEL DESTINO
    # -------------------------------------------------------------------------
    $ grant_achievement("encrucijada_kenji")

    p "(¿Qué sendero elijo para desafiar la profecía de mis ojos...?)"

    menu:
        "¿Qué camino tomas ante la inminente llegada de las 18:00?"

        "Advertir directamente a Kenji y exigirle que rechace la inyección":
            jump ruta_decir_a_kenji

        "Permanecer en silencio paralizado por el terror a ser tomado por demente":
            jump ruta_guardar_silencio

        "Arrancarte las vías intravenosas, salir al pasillo y alertar a los médicos jefes":
            jump ruta_avisar_doctores


# -----------------------------------------------------------------------------
# RUTA 1: ADVERTIR DIRECTAMENTE A KENJI
# -----------------------------------------------------------------------------
label ruta_decir_a_kenji:

    "El pánico me desbordó. Me incliné sobre el borde de mi camilla con los ojos dilatados por el horror."

    p "¡Kenji, mírame bien! ¡Por lo que más quieras en este mundo, no dejes que te toquen la vía a las seis! ¡Tienes que rechazar esa ampolla!"

    kenji "¿Eh? ¿Ren? Oye... cálmate, estás temblando como si hubieras visto un fantasma."

    p "¡No es un delirio! ¡Lo vi en tus propios ojos! Si esa aguja entra en tu brazo... ¡vas a morir asfixiado en menos de tres minutos! ¡Tu sangre se va a coagular viva!"

    "Kenji se quedó en silencio durante unos segundos. Pero luego, una sonrisa nerviosa y compasiva asomó a sus labios."

    kenji "Ren... entiendo que el choque te causó un trauma severo y que tienes alucinaciones por los sedantes... pero es solo un antibiótico rutinario. Me lo ponen todos los días."

    p "¡Esta vez es diferente! ¡Kenji, te lo suplico de rodillas...!"

    "18:00 en punto."
    "La puerta corrediza se abrió con un deslizamiento helado."

    # Silueta de la Enfermera Sato
    show silueta_enfermera at silueta_left with Dissolve(0.8)

    "La enfermera Sato entró con paso mecánico y semblante inexpresivo. En su bandeja de acero reposaba una jeringa cargada con un líquido incoloro y denso."

    enf "Buenas tardes, Takahashi-kun. Tu dosis programada de las dieciocho horas."

    kenji "Adelante, enfermera Sato. Mi amigo casi me hace creer que venía un verdugo, jajaja."

    p "¡NO! ¡DETENTE, SATO! ¡NO SE LO PONGAS!"

    "Intenté saltar de la cama, pero mis piernas convalecientes fallaron y caí de rodillas al suelo. La aguja penetró la cánula de Kenji sin vacilación."
    "El émbolo descendió lentamente hasta el tope."

    hide silueta_enfermera with Dissolve(0.5)

    # LA AGONÍA VISCERAL
    scene bg destello_rojo
    with vision_flash

    play sound "audio/eye_vision.wav"

    "Al principio, Kenji esbozó una mueca de alivio. Pero dos segundos después... su mandíbula se trabó con un chasquido sordo."

    kenji "Cof... ¿Qué... qué es esto...? Me quema... el pecho... no puedo..."

    with vpunch
    play sound "audio/heartbeat.wav"

    "Sus pupilas se dilataron hasta cubrir todo el iris. Un estertor líquido y desgarrador brotó de su garganta."
    "Sus dos manos se dispararon hacia las barandillas de hierro con una fuerza salvaje, quebrando sus propias uñas contra el metal y manchándolo de sangre fresca."

    with hpunch

    "Bajo la piel de su cuello y su rostro, las venas se hincharon y adquirieron un color negro azabache, como raíces podridas extendiéndose bajo la carne."
    "La toxina estaba destruyendo sus alvéolos en una combustión química despiadada."

    kenji "¡Aaaagh...! ¡Ggghh... a-aire...! ¡R-Ren...!"

    "Una espuma densa y purpúrea brotó entre sus dientes apretados, empapando la almohada mientras su espina dorsal se arqueaba en un espasmo inhumano."
    "Durante tres minutos eternos, cada respiración de Kenji fue un lamento ahogado en su propia sangre... mientras sus ojos ensangrentados se clavaban en mí con el terror tardío de quien sabe que ignoró la verdad."

    hide silueta_kenji

    play sound "audio/flatline.wav"
    with fade_muerte

    "Un último estertor estremeció su caja torácica antes de desplomarse inerte sobre la cama ensangrentada."
    "Sus ojos vacíos quedaron fijos en el techo blanco de Shinshu."

    scene bg sangre_visceral
    with Dissolve(1.5)

    $ grant_achievement("tragedia_kenji")

    p "Se lo advertí... le rogué que me creyera... y murió delante de mis ojos..."
    "El peso de su muerte cayó como una losa de plomo sobre mi alma rota. Mis ojos no eran un milagro; eran la sentencia del verdugo."

    jump final_capitulo_tragedia


# -----------------------------------------------------------------------------
# RUTA 2: GUARDAR SILENCIO POR MIEDO
# -----------------------------------------------------------------------------
label ruta_guardar_silencio:

    "El terror me atenazó la laringe como una soga helada."
    "Las palabras se negaron a salir de mi boca."

    p "(Si hablo... me trasladarán al pabellón psiquiátrico de Nagano. Dirán que el coma me destruyó la cordura...)"
    p "(Tal vez solo fue una pesadilla... tal vez el futuro no es real...)"

    play sound "audio/heartbeat.wav"

    "Me cobijé bajo las sábanas, mordiéndome los nudillos mientras el sudor frío me goteaba por la frente."
    "El tic-tac del reloj de la pared retumbaba en mis oídos como martillazos sobre un ataúd."

    "17:59."
    "18:00."

    "La puerta corrediza se abrió."

    # Silueta de la Enfermera
    show silueta_enfermera at silueta_left with Dissolve(0.8)

    "La enfermera Sato entró con semblante frío. Desinfectó la vía de Kenji con movimientos autómatas y descargó el líquido transparente en su brazo."

    enf "Listo, Takahashi-kun. Descanse."

    hide silueta_enfermera with Dissolve(0.6)

    "Durante unos segundos, la habitación quedó en un silencio sepulcral."
    "Y entonces... la pesadilla cobró su tributo."

    play sound "audio/glass_break.wav"
    with vpunch

    "El vaso de agua de Kenji se estrelló contra las baldosas en mil fragmentos cristalinos."

    kenji "Gh... ah... ¿R-Ren...?"

    "Me incorporé aterrado. El rostro de Kenji se había tornado de un color gris ceniciento a una velocidad antinatural."
    "Se llevó ambas manos a la tráquea, pero de sus cuerdas vocales deshechas solo escapaba un silbido agónico."

    play sound "audio/eye_vision.wav"
    with eye_pulse

    "Kenji cayó de la cama al suelo entre los cristales rotos, golpeándose la cabeza en una convulsión violenta que le dislocó el hombro."
    "Se arrastró lentamente sobre el linóleo helado, arañando el piso con dedos ensangrentados hacia el borde de mi camilla."

    kenji "Khhh... ghh... ¡A-ayú... da...!"

    with vpunch

    "Un vómito espeso de coágulos negros encharcó el suelo. Y en medio de aquella agonía interminable, Kenji alzó la vista y clavó sus ojos inyectados en sangre en los míos."
    "Una mirada que parecía desgarrarme el alma en dos mientras preguntaba en silencio:"
    "{i}«¿Por qué te quedaste callado...? ¿Por qué me dejaste morir...?»{/i}"

    hide silueta_kenji

    play sound "audio/flatline.wav"
    with fade_muerte

    "Sus dedos dieron un último temblor espasmódico sobre el charco de su propia sangre antes de quedar inmóviles para siempre."

    scene bg sangre_visceral
    with Dissolve(1.5)

    $ grant_achievement("tragedia_kenji")

    p "Pude haberlo evitado... Sabía exactamente lo que iba a ocurrir... y mi cobardía lo asesinó."
    "La culpa me quemó las entrañas como ácido puro. Mis ojos no eran un don; eran una maldición imperdonable."

    jump final_capitulo_tragedia


# -----------------------------------------------------------------------------
# RUTA 3: ESCAPAR AL PASILLO Y ALERTAR A LOS MÉDICOS
# -----------------------------------------------------------------------------
label ruta_avisar_doctores:

    "El pánico a la muerte ajena pulverizó cualquier miedo al ridículo o al juicio de los demás."
    "Con un movimiento desesperado, me arranqué los sensores del tórax y la vía del brazo. El monitor cardíaco estalló en una alarma estridente."

    play sound "audio/monitor.wav"

    kenji "¡Oye, Ren! ¿Qué estás haciendo? ¡No puedes levantarte así, te vas a desangrar!"

    hide silueta_kenji with Dissolve(0.5)

    "Ignoré su advertencia. Mis piernas temblaban como ramas quebradas, pero el terror me dio fuerzas sobrehumanas."
    "Abrí la puerta corrediza de golpe y salí tambaleándome al pasillo central del hospital."

    scene bg hospital_pasillo
    with vpunch

    p "¡MÉDICO! ¡AYUDA! ¡DETENGAN A LA ENFERMERA DEL PABELLÓN OESTE AHORA MISMO!"

    "Varios pacientes y enfermeros voltearon a mirarme con alarma. Dos enfermeros jóvenes corrieron hacia mí para inmovilizarme contra la pared."

    misterio "¡Tranquilícese, joven Kasugai! Por favor, vuelva a su cama, su condición es crítica..."

    p "¡No me toquen! ¡La enfermera Sato va a inyectar una toxina mortal a Takahashi a las seis de la tarde! ¡Si esa aguja entra en su torrente sanguíneo, morirá asfixiado en tres minutos!"

    misterio "Son delirios postraumáticos... El traumatismo craneal severo del accidente todavía le genera alucinaciones persecutorias..."

    p "¡NO SON ALUCINACIONES! ¡SE LOS JURO POR MI ALMA, VI SU SANGRE NEGRA EN SUS OJOS! ¡DETÉNGANLA!"

    # Silueta del Doctor Moriyama
    show silueta_doctor at silueta_center with Dissolve(0.8)

    "En ese instante, una figura imponente de bata blanca inmaculada salió del despacho de jefatura médica: el Dr. Moriyama, jefe supremo de cirugía del Hospital General de Shinshu."

    doc "¿Qué significa esta falta de disciplina en mi corredor médico?"

    misterio "Dr. Moriyama, el paciente Kasugai sufre un brote psicótico agudo sobre la medicación de su compañero..."

    "El Dr. Moriyama me miró fijamente a los ojos. Había algo glacial y profundamente calculador en su pupila. No me miraba como a un paciente demente... me observaba como a un espécimen bajo el microscopio."

    doc "¿Las dieciocho horas dijiste, muchacho? Esa es la ronda de suministros especiales de Sato."

    "El doctor consultó su reloj suizo de muñeca: 17:58."

    doc "No tolero irregularidades en mis pabellones. Quirófano dos en alerta. Yo mismo verificaré ese lote."

    # INTERVENCIÓN MILAGROSA A LAS 17:59
    scene bg hospital_tarde
    with Dissolve(0.8)

    show silueta_kenji at silueta_right
    show silueta_enfermera at silueta_left

    "17:59."
    "Dentro de la habitación 304, la enfermera Sato ya desinfectaba el catéter de Kenji. La punta metálica de la aguja estaba a escasos milímetros de su piel cuando la voz atronadora del Dr. Moriyama quebró el silencio desde la entrada."

    show silueta_doctor at silueta_center with Dissolve(0.5)
    with vpunch

    doc "¡Enfermera Sato! ¡Detenga esa inoculación inmediatamente!"

    enf "¿Doctor Moriyama...? ¿Ocurre algún problema?"

    doc "Esa ampolla queda incautada bajo custodia médica de jefatura. Diríjase a urgencias de inmediato para preparar la recepción del helicóptero de Chūbu. ¡Ahora mismo, Sato!"

    enf "Entendido, doctor..."

    hide silueta_enfermera with Dissolve(0.5)
    hide silueta_doctor with Dissolve(0.5)

    "La enfermera Sato guardó la jeringa en el estuche hermético de seguridad y abandonó la habitación con paso apresurado tras el cirujano."

    # RESOLUCIÓN Y EL DESTINO ROTO
    scene bg hospital_noche
    with Dissolve(1.5)

    show silueta_kenji at silueta_right with Dissolve(0.8)

    "Minutos después, con los vendajes de mis brazos repuestos, me ayudaron a regresar a mi camilla."
    "El reloj marcó las 18:05... luego las 18:30... y aquella aguja jamás regresó."

    kenji "Cielos, Ren... no sé qué fue todo ese escándalo allá afuera, pero parecías un poseso furioso. Aunque... gracias a tu locura me salvé de un pinchazo desagradable, jaja."

    p "Kenji..."

    "Alcé la mirada hacia él en la penumbra de la noche."

    play sound "audio/eye_vision.wav"
    with vision_flash

    "Miré fijamente las pupilas de Kenji Takahashi."
    "La masa de coágulos ennegrecidos, los espasmos brutales, las venas hinchadas y la asfixia atroz... se habían disuelto como humo en el viento."
    "En sus ojos solo se reflejaba la luna serena sobre las cordilleras nevadas de Nagano, y un futuro luminoso donde caminaba libre fuera del hospital."

    $ grant_achievement("salvar_kenji")

    p "(El destino... no estaba escrito en piedra. La muerte puede ser desafiada...)"

    "Una lágrima solitaria rodó por mi mejilla, cargada de un alivio sobrecogedor."
    "Mis ojos eran una maldición... pero también el único filo capaz de cortar los hilos de la muerte."

    hide silueta_kenji with Dissolve(1.0)

    jump final_capitulo_esperanza


# -----------------------------------------------------------------------------
# FINALES DEL PRIMER CAPÍTULO
# -----------------------------------------------------------------------------
label final_capitulo_tragedia:

    stop music fadeout 2.5

    scene bg negro
    with fade_muerte

    $ grant_achievement("fin_capitulo_1")

    "Aquella misma noche, la policía científica y los forenses acordonaron la habitación 304."
    "La autopsia preliminar reveló que el fármaco administrado contenía una concentración letal de un reactivo paralizante no registrado en los libros de farmacia del hospital."

    "Nadie sospechó que yo lo sabía todo de antemano. Todos me trataron con condescendencia, como a un pobre muchacho traumatizado por presenciar el horror."

    "Pero yo sé la verdad."
    "Mis ojos cargan con el peso de los muertos. Y en la oscuridad helada de las montañas de Nagano, comprendí con pavor que Kenji era solo el primer nombre en una lista interminable de almas que el abismo pondrá frente a mi mirada..."

    scene bg negro
    with Dissolve(2.5)
    "{b}FIN DEL CAPÍTULO 1 - DESTINO CONSUMADO{/b}"
    return


label final_capitulo_esperanza:

    stop music fadeout 2.5

    scene bg negro
    with fade_lento

    $ grant_achievement("fin_capitulo_1")

    "Esa misma madrugada, la inspección de farmacia del hospital confiscó el lote de suministros del pabellón oeste tras descubrirse toxinas neurobloqueantes camufladas entre los analgésicos."
    "El Dr. Moriyama se acercó a mi camilla en el silencio de la guardia nocturna."
    "No pronunció una sola palabra de reproche ni hizo preguntas médicas. Se limitó a mirarme con una fijeza insondable antes de susurrar antes de retirarse:"

    doc "{i}«Interesante mirada la tuya, joven Kasugai... Nos volveremos a ver pronto en los pasillos de Shinshu.»{/i}"

    "Logré salvar una vida. Pero en el abismo de mi mente fragmentada, una inquietud mil veces más oscura comenzaba a devorarme:"

    "¿Quién colocó ese veneno en el hospital?"
    "¿Por qué mis ojos despertaron justo después de aquel choque infantil en el que salvé a Aoi?"
    "¿Y qué fue lo que verdaderamente pacté con la muerte en la lluvia de Matsumoto...?"

    scene bg negro
    with Dissolve(2.5)
    "{b}FIN DEL CAPÍTULO 1 - EL HILO DEL DESTINO ROTO{/b}"
    return


# =============================================================================
# CAPÍTULO 1 (MUJER): AOI KAZAMA - LA HERMANA DEL DESTINO
# =============================================================================
label chapter1_aoi:

    # -------------------------------------------------------------------------
    # PARTE 1: EL DESPERTAR TRAS UN MES DE SILENCIO
    # -------------------------------------------------------------------------
    scene bg negro
    with fade_lento

    stop music fadeout 2.0
    play sound "audio/monitor.wav" loop

    "Un pitido rítmico, lejano y metálico..."
    "El olor penetrante a antiséptico, sábanas almidonadas y ozono."

    scene bg hospital_habitacion_aoi
    with Dissolve(2.0)

    "Abro los párpados con un esfuerzo que parece desgarrar mis músculos."
    "La luz fluorescente del techo del Hospital General de Nagano hiere mis pupilas como cristales rotos."
    "Tengo la garganta reseca, vendajes oprimiendo mi frente y cables fríos conectados a mi pecho."

    aoi_p "D... ¿dónde...?"

    show silueta_madre at silueta_left with Dissolve(1.2)
    show aoi_acurrucada_llorando_mano at silueta_floor_center with Dissolve(1.2)

    "Un rostro desencajado se abalanza sobre la barandilla de la cama."
    "Las lágrimas de mi madre empapan las sábanas antes de que pueda articular una sola palabra."

    madre "¡Aoi...! ¡Hija mía...! ¡Dios mío, despertaste...! ¡Por fin abriste los ojos...!"

    aoi_p "Mamá... ¿qué hora es? El paso de peatones... la lluvia en la estación... ¿dónde está mi hermano? ¿Dónde está Shinshu?"

    "La madre se petrifica al instante."
    "El llanto de alivio se transforma de golpe en una mueca de espanto y dolor incontenible. Sus manos comienzan a temblar sobre mi manta."

    aoi_p "Mamá... ¿por qué no contesta? ¿Por qué no vino a verme? Shinshu siempre me cuidaba... ¿dónde está?"

    # -------------------------------------------------------------------------
    # PARTE 2: LA CONFESIÓN DE LA MADRE Y EL SALTO DEL HERMANO
    # -------------------------------------------------------------------------
    stop sound fadeout 1.5
    play music "audio/piano_sad_theme.wav" loop fadein 2.0

    madre "Aoi... mi pequeña... no han pasado unas horas..."
    madre "Has estado en coma profundo... durante un mes entero."

    aoi_p "¿U-un mes...?"

    madre "Aquel día... el camión derrapó en la curva de Matsumoto. Shinshu corrió desesperado hacia ti... pero no llegó a tiempo. El golpe te destrozó la cabeza contra el bordillo."

    scene bg hospital_tarde
    with Dissolve(1.5)

    "Mi madre se cubre el rostro, convulsionando en sollozos ahogados."

    madre "Durante semanas, Shinshu no salió de este hospital. No dormía. No comía. Se quedaba de rodillas junto a tu camilla sosteniendo tu mano inerte, repitiéndose una y otra vez que todo había sido culpa suya..."
    madre "{i}«Si hubiera corrido más rápido... si la hubiera tomado del brazo antes de cruzar... Aoi estaría despierta»{/i}... ese veneno se le metió en la cabeza..."

    aoi_p "No... Shinshu no tuvo la culpa... ¡yo fui la que corrió adelante jugando en las líneas blancas...!"

    show silueta_madre at silueta_left with Dissolve(0.8)
    show aoi_llorando_manga at silueta_center with Dissolve(0.8)

    madre "Y yo... ciega de dolor y desesperación... en lugar de abrazarlo, le grité."
    madre "Le grité en este mismo pasillo: {i}«¡Todo es culpa tuya! ¡Tú eres el hermano mayor! ¡Era tu deber proteger a tu hermana menor!»{/i}"

    scene bg azotea_lluvia
    with Dissolve(1.8)
    play sound "audio/rain.wav" loop

    "La voz de mi madre se quiebra en un susurro fantasmal. En mi mente, veo la silueta de mi hermano bajo el aguacero torrencial de la noche..."

    "Solo en la azotea de un bloque de viviendas en Nagano. El viento helado de los Alpes japoneses azotando su uniforme empapado."
    "Sin el perdón de nuestra madre. Sin mi voz para decirle que lo amaba."
    "Devorado por la culpa y el remordimiento de haber llegado un segundo tarde."

    play sound "audio/flatline.wav"
    scene bg destello_rojo
    with Dissolve(0.5)

    "Shinshu dio un paso al frente sobre el alféizar de cemento... y se dejó caer hacia el vacío infinito de la noche."

    stop sound fadeout 1.0

    scene bg hospital_habitacion_aoi
    with Dissolve(1.5)

    show aoi_abrazando_rodillas at silueta_floor_center with Dissolve(1.0)

    madre "Murió en el acto al estrellarse contra el pavimento... Hace tres semanas enterramos a tu hermano. ¡Y yo lo empujé a esa azotea, Aoi! ¡Fui yo...!"

    $ grant_achievement("despertar_aoi")

    "Las palabras caen sobre mi pecho como toneladas de plomo ardiente."
    "No puedo respirar. El aire no entra en mis pulmones."
    "Shinshu murió. Mi hermano... mi guardián... está bajo tierra. Y murió creyendo que fue su culpa, cuando fui yo quien dio el paso imprudente bajo la lluvia."

    aoi_p "(Si yo no hubiera caminado tan deprisa... si no me hubiera adelantado... Shinshu estaría vivo. Yo lo maté. Yo soy su asesina.)"

    # -------------------------------------------------------------------------
    # PARTE 3: LA ESPIRAL DE CULPA Y LA RETENCIÓN HOSPITALARIA
    # -------------------------------------------------------------------------
    scene bg negro
    with fade_muerte

    "Los días posteriores al despertar se convirtieron en un infierno sin fondo."
    "El hospital no era un lugar de recuperación: era una jaula de remordimientos donde cada respiración me quemaba el alma."

    scene bg hospital_pasillo
    with Dissolve(1.0)

    show aoi_caminando_desanimada at silueta_center with Dissolve(1.0)

    "Quería morir. Quería reunirme con Shinshu y pedirle perdón en la penumbra."
    "Varias veces intenté arrancarme los sueros para desangrarme en silencio. En dos ocasiones corrí hacia las ventanas del cuarto piso intentando abrir los pestillos para saltar al vacío, igual que hizo él."

    hide aoi_caminando_desanimada with Dissolve(0.3)
    show silueta_enfermera at silueta_left
    show aoi_arrodillada_desolada at silueta_floor_center
    show silueta_doctor at silueta_right
    with Dissolve(0.8)

    doc "¡Sujétenla de los brazos! ¡Administren cinco miligramos de diazepam de inmediato!"
    enf "¡Tranquila, Aoi! ¡Por favor, no lo hagas!"

    "Los enfermeros y doctores tuvieron que placarme contra el suelo en más de una guardia nocturna."
    "Me sujetaron con correas a la camilla. Me colocaron vigilancia estricta las veinticuatro horas. Mi madre apenas podía mirarme sin desmoronarse."

    hide silueta_enfermera
    hide silueta_doctor
    hide aoi_arrodillada_desolada
    with Dissolve(0.8)

    # -------------------------------------------------------------------------
    # PARTE 4: LA NOCHE DEL LAVABO Y EL FILO OCULTO
    # -------------------------------------------------------------------------
    scene bg hospital_noche
    with Dissolve(1.5)

    show aoi_de_pie_abrazandose at silueta_center with Dissolve(1.0)

    "Una medianoche espesa y silenciosa en el pabellón oeste."
    "La enfermera de guardia acababa de pasar su ronda de control y cerró la puerta batiente."
    "En la camilla de al lado duerme Yuna Tachibana, mi compañera de habitación. Una chica ingresada por dolencias pulmonares que siempre intentaba hablarme con una sonrisa amable, aunque yo solo le respondía con monosílabos gélidos."

    "Me deslizo fuera de las sábanas sin hacer ruido."
    "Bajo una tablilla suelta del rodapié del lavabo, había escondido días atrás un pequeño filo metálico: una hoja de bisturí descartada que conseguí hurtar durante un cambio de apósitos."

    hide aoi_de_pie_abrazandose with Dissolve(0.5)

    scene bg bano_espejo
    with Dissolve(1.2)

    show aoi_base at silueta_center with Dissolve(0.8)

    "Entro al cuarto de baño y cierro el pestillo despacio."
    "Abro el grifo. Me lavo la cara con agua helada para detener el temblor de mis manos."
    "Saco el pequeño filo de mi bolsillo. El metal despide un destello plateado bajo el tubo fluorescente."

    aoi_p "(Shinshu... espérame. Ya voy a buscarte.)"

    "Alzo la vista hacia el espejo frente a mí con el filo apoyado contra la piel de mi muñeca."
    "Y entonces..."

    hide aoi_base with Dissolve(0.3)

    play sound "audio/eye_vision.wav"
    scene bg destello_morado
    with eye_pulse_aoi

    "El espejo del lavabo no devuelve mi rostro demacrado."
    "El cristal se ondula como agua hirviente y una punzada eléctrica atraviesa mis dos globos oculares con la violencia de un relámpago."

    $ grant_achievement("espejo_premonicion")

    # -------------------------------------------------------------------------
    # LA VISIÓN PREMONITORIA EN EL ESPEJO
    # -------------------------------------------------------------------------
    play sound "audio/heartbeat.wav"
    scene bg vacio_mental
    with Dissolve(0.6)

    "En la superficie del espejo presencio una escena que aún no ha ocurrido:"
    "Es la tarde de mañana. El sol entra oblicuo por los ventanales de nuestra habitación."

    show silueta_doctor at silueta_right with Dissolve(0.5)
    "Un hombre corpulento y con el rostro crispado de furia entra al cuarto: el padre de Yuna."

    padre_yuna "¡Estoy harto de tus quejas y de tus gastos médicos! ¡Desde que naciste no has hecho más que arruinar a esta familia!"

    show silueta_aoi at silueta_left with Dissolve(0.5)
    yuna "¡Tú nunca estuviste para mí! ¡Ojalá mamá no te hubiera conocido jamás!"

    "El padre pierde por completo el control. Con un alarido de cólera, extiende ambos brazos y empuja a Yuna con fuerza brutal hacia atrás."

    play sound "audio/crash.wav"
    scene bg destello_rojo
    with eye_pulse

    "Yuna sale despedida de la cama y cae de espaldas hacia el suelo."
    "Y justo allí... en el espacio ciego entre la pata metálica de su cama y el rodapié... hay una varilla metálica afilada, rota de un antiguo soporte de suero, apuntando hacia arriba."

    play sound "audio/glass_break.wav"
    scene bg sangre_espejo
    with vision_flash_aoi

    "El impacto es espeluznante."
    "La varilla de acero perfora la base del cráneo de Yuna, penetrando directamente en la masa cerebral."
    "Yuna ni siquiera alcanza a gritar. Sus pupilas se dilatan instantáneamente y un reguero espeso de sangre carmesí inunda las baldosas blancas."

    padre_yuna "¡¿Y-Yuna...?! ¡Yuna, levántate! ¡¿Qué es esto?! ¡¡AYUDA!! ¡¡ENFERMERAS, POR FAVOR, UN MÉDICO!!"

    play sound "audio/flatline.wav"

    "El padre retrocede aterrorizado al ver sus manos empapadas de sangre."
    "Entran enfermeros y médicos corriendo a toda velocidad. Intentan maniobras de reanimación, gritan por una camilla de quirófano... pero el electrocardiógrafo marca una línea plana irremediable."
    "Dos vigilantes de seguridad reducen al padre contra el suelo mientras el doctor grita al teléfono: {i}«¡Llamen a la policía del distrito! ¡Ha matado a su hija!»{/i}"

    stop sound fadeout 1.0

    # -------------------------------------------------------------------------
    # RETORNO A LA REALIDAD DEL LAVABO
    # -------------------------------------------------------------------------
    scene bg bano_espejo
    with Dissolve(1.5)

    "El espejo vuelve a la normalidad de golpe. Jadeo sobre el lavabo con el corazón golpeando mi pecho a doscientos latidos por minuto."
    "Mis ojos arden como brasas encendidas. No fue una alucinación... fue una premonición exacta del futuro."
    "Mañana por la tarde... Yuna morirá perforada por ese objeto oculto debajo de su cama si nadie interviene."

    aoi_p "(He visto la muerte antes de que ocurra... igual que si el hilo del destino se hubiera dibujado delante de mis ojos.)"

    # -------------------------------------------------------------------------
    # LA TRIPLE ENCRUCIJADA DE AOI
    # -------------------------------------------------------------------------
    "Miro el filo que sostengo en mis dedos temblorosos. La muerte me rodea, pero por primera vez desde el coma... tengo el poder de actuar."
    "¿Qué debo hacer con este don maldito?"
    "¿Qué camino eliges para enfrentar la muerte inminente de Yuna?"

    menu:
        "1. Advertir desesperadamente a Yuna sobre la discusión con su padre y el objeto mortal.":
            jump aoi_decision_advertir

        "2. Tirar mi propio filo, esperar a la noche y retirar el objeto punzante debajo de la cama de Yuna.":
            jump aoi_decision_retirar

        "3. No intervenir; convencerme de que solo fue una pesadilla o un delirio provocado por mi trauma.":
            jump aoi_decision_ignorar


# -----------------------------------------------------------------------------
# RAMA 1: ADVERTIR A YUNA
# -----------------------------------------------------------------------------
label aoi_decision_advertir:

    scene bg hospital_dia
    with Dissolve(1.2)

    "A la mañana siguiente, me acerco a la cama de Yuna con las manos temblando de ansiedad."
    "Ella está sentada leyendo una revista, sorprendida de verme dar el primer paso para hablarle."

    aoi_p "Yuna... escúchame bien. Tienes que creerme. Esta tarde vendrá tu padre a visitarte."

    show aoi_de_pie_correa_bolso at silueta_center with Dissolve(0.8)

    yuna "¿Mi padre? Sí... dijo que pasaría después del trabajo. ¿Cómo lo sabes?"

    aoi_p "¡Van a discutir fuertemente! Él te empujará de la cama... y debajo hay un metal afilado que te perforará la cabeza si caes. ¡Por favor, no discutas con él, aléjate de esa cama o sal de la habitación!"

    "Yuna baja la revista despacio. Sus ojos no muestran gratitud ni asombro: muestran desconcierto, pena y temor."

    yuna "Aoi... sé por lo que estás pasando. Sé lo de tu hermano Shinshu... y las enfermeras me contaron las veces que tuvieron que retenerte por intentar hacerte daño..."
    yuna "Estás medicada y muy sensible. Por favor... no te metas en las cosas de mi familia. Mi padre tiene mal genio, pero jamás me haría daño. Estás delirando."

    aoi_p "¡No estoy loca, Yuna! ¡Lo vi con mis propios ojos en el espejo!"

    yuna "¡Basta, Aoi! ¡Por favor, déjame en paz o llamaré a la enfermera!"

    hide aoi_de_pie_correa_bolso with Dissolve(0.6)

    "Nadie me cree. Para el mundo, soy solo una paciente rota por el duelo con alucinaciones paranoides."

    # La tragedia se consuma
    scene bg hospital_tarde
    with Dissolve(1.5)

    "La tarde cae inexorable sobre Nagano."
    "La puerta se abre de golpe. El padre de Yuna entra con paso pesado y ceño fruncido."
    "La discusión empieza con las mismas frases exactas que presencié en el reflejo."

    padre_yuna "¡Estoy harto de tus quejas y de tus gastos médicos! ¡Desde que naciste no has hecho más que arruinar a esta familia!"
    yuna "¡Tú nunca estuviste para mí! ¡Ojalá mamá no te hubiera conocido jamás!"

    aoi_p "¡¡YUNA, CUIDADO, ATRÁS!!"

    "Intento saltar de mi camilla para interponerme, pero mis piernas débiles por el coma ceden contra el suelo."

    play sound "audio/crash.wav"
    scene bg destello_rojo
    with eye_pulse

    "El empujón ocurre en una fracción de segundo. El cuerpo de Yuna vuela de espaldas hacia el hueco bajo la cama."

    play sound "audio/glass_break.wav"
    scene bg sangre_visceral
    with vision_flash_aoi

    "El crujido óseo resuena en toda la habitación."
    "La varilla de hierro oculta perfora su cráneo al instante. La sangre inunda las baldosas idéntica a la visión."

    padre_yuna "¡¡YUNA!! ¡¡NO, DIOS MÍO, QUÉ HICE... AYUDA!!"

    $ grant_achievement("tragedia_yuna")

    jump final_capitulo_aoi_tragedia


# -----------------------------------------------------------------------------
# RAMA 2: RETIRAR EL OBJETO EN LA NOCHE (SALVACIÓN Y SACRIFICIO)
# -----------------------------------------------------------------------------
label aoi_decision_retirar:

    scene bg bano_espejo
    with Dissolve(1.0)

    "Comprendo la amarga verdad: nadie creerá la palabra de una chica suicida que acaba de despertar de un coma."
    "Si quiero salvarla, no puedo confiar en las palabras. Debo actuar con hechos."

    "Miro el filo que guardaba para cortarme... y lo arrojo al cubo de basura del lavabo sin dudar."

    aoi_p "(Shinshu... si no pude salvarte a ti, al menos no permitiré que otra vida se apague delante de mis ojos.)"

    scene bg hospital_noche
    with Dissolve(1.5)

    "Son las dos de la madrugada. El hospital duerme bajo un silencio sepulcral."
    "Me deslizo como una sombra fuera de mi cama. El suelo helado quema la planta de mis pies descalzos."
    "Me arrastro lentamente hacia la cama de Yuna. Me agacho en la penumbra y deslizo mi brazo bajo el armazón de hierro."

    show aoi_agachada_melancolica at silueta_floor_center with Dissolve(0.8)

    "Mis dedos tantean el polvo y los cables... hasta que rozan un borde frío y punzante."
    "Es la varilla metálica rota de soporte. Afilada como un arpón oxidado."
    "La aferro con fuerza y comienzo a extraerla despacio..."

    # Yuna despierta
    play sound "audio/heartbeat.wav"

    "Pero el metal raspa contra el marco de la cama produciendo un leve chillido."
    "Yuna abre los ojos de golpe en la oscuridad."
    "Me ve agachada a escasos centímetros de su rostro, con la mirada desorbitada y un objeto largo y afilado de metal empuñado en mi mano."

    yuna "¡¡¡AAAAAAAHHHH!!! ¡¡¡SOCORRO!!! ¡¡ME QUIERE MATAR!! ¡¡¡AUXILIO!!!"

    play sound "audio/flatline.wav"

    "Las luces de emergencia se encienden al unísono. La puerta se abre de par en par con estrépito."

    show silueta_doctor at silueta_right
    show silueta_enfermera at silueta_left
    with Dissolve(0.5)

    doc "¡Sujétenla! ¡Tiene un objeto punzante! ¡Aseguren a la paciente Tachibana!"
    enf "¡Aoi, suelta eso por favor! ¡No te muevas!"

    "Tres enfermeros se abalanzan sobre mí, arrojándome contra el suelo linóleo."
    "Me arrancan el hierro de las manos mientras un pinchazo ardiente atraviesa mi brazo: un sedante de choque."

    hide aoi_agachada_melancolica
    hide silueta_doctor
    hide silueta_enfermera
    with Dissolve(0.4)

    aoi_p "¡No... no entienden...! ¡La varilla... estaba debajo de su cama...!"

    "Mi vista se nubla en un torbellino púrpura mientras pierdo el conocimiento..."

    # Aislamiento y salvación al día siguiente
    scene bg habitacion_aislamiento
    with Dissolve(2.0)

    show aoi_sentada_costado_mano at silueta_floor_center with Dissolve(1.0)

    "Despierto horas después en una habitación acolchada de aislamiento preventivo en el pabellón psiquiátrico."
    "Tengo las muñecas aseguradas a la cama. Mi madre llora al otro lado del cristal tras ser notificada del incidente."
    "Para todos los médicos y para mi madre, he sufrido un brote psicótico homicida."

    "Pero a través de la pequeña ventanilla con barrotes de mi celda, puedo ver hacia el pabellón contiguo."
    "Es media tarde. El padre de Yuna acaba de llegar."
    "Discuten con la misma ferocidad."
    "El padre extiende los brazos con furia y empuja violentamente a Yuna fuera de la cama."

    play sound "audio/crash.wav"
    scene bg hospital_morado
    with Dissolve(0.5)

    "Yuna cae de espaldas exactamente en el mismo rincón..."
    "El golpe de su espalda contra el suelo plano retumba seco... pero no hay perforación. No hay varilla metálica. No hay sangre brotando de su cabeza."

    "Yuna llora de rabia y se frota la espalda magullada. Su padre se detiene avergonzado de haberla empujado, asustado de su propia violencia."
    "¡Está viva! ¡La muerte no pudo reclamar su tributo!"

    $ grant_achievement("salvar_yuna")

    jump final_capitulo_aoi_esperanza


# -----------------------------------------------------------------------------
# RAMA 3: NO HACER NADA (OMISIÓN)
# -----------------------------------------------------------------------------
label aoi_decision_ignorar:

    scene bg hospital_dia
    with Dissolve(1.2)

    show aoi_sentada_piernas_desganadas at silueta_floor_center with Dissolve(1.0)

    "Me quedo inmóvil en mi cama toda la mañana, temblando bajo las mantas."
    "Intento convencerme de que mi mente traumatizada por la muerte de Shinshu me está jugando una mala pasada."

    aoi_p "(Fue solo un delirio... la falta de oxígeno del coma. Los espejos no muestran el futuro. No puedo volverme loca...)"

    hide aoi_sentada_piernas_desganadas with Dissolve(0.8)

    scene bg hospital_tarde
    with Dissolve(1.5)

    "Las horas transcurren como una condena silenciosa."
    "A las cinco de la tarde, la puerta de la habitación se abre."
    "El padre de Yuna entra con la misma gabardina gris y los puños apretados."
    "Cada reproche, cada alarido y cada insulto se reproducen con una exactitud matemática aterradora."

    padre_yuna "¡Desde que naciste no has hecho más que arruinar a esta familia!"
    yuna "¡Ojalá mamá no te hubiera conocido jamás!"

    "El padre levanta las manos. En ese instante de terror puro, comprendo con horror que todo era real... pero ya es demasiado tarde."

    play sound "audio/crash.wav"
    scene bg destello_rojo
    with eye_pulse

    "El empujón violento lanza a Yuna hacia atrás."

    play sound "audio/glass_break.wav"
    scene bg sangre_visceral
    with vision_flash_aoi

    "El objeto punzante atraviesa la base de su cráneo en el suelo. La sangre salpica la pared blanca."
    "El padre entra en shock y los médicos no logran reanimarla. La policía lo esposa frente a mi camilla."

    $ grant_achievement("omision_yuna")

    jump final_capitulo_aoi_omision


# -----------------------------------------------------------------------------
# FINALES DEL CAPÍTULO 1 DE AOI
# -----------------------------------------------------------------------------
label final_capitulo_aoi_tragedia:

    stop music fadeout 2.5
    scene bg negro
    with fade_muerte

    "La habitación fue acordonada por la policía de la prefectura de Nagano."
    "El padre de Yuna fue detenido e imputado por homicidio involuntario."
    "Nadie me escuchó cuando intenté advertirle. Todos creyeron que mis advertencias eran desvaríos de una mente quebrada."

    show aoi_sentada_suelo at silueta_floor_center with Dissolve(1.5)

    "Comprendí con una amargura insoportable que ver el futuro no sirve de nada si las palabras no tienen fuerza para cambiarlo."
    "Shinshu murió por la culpa... y ahora yo cargo con la culpa de saber y no haber podido evitar la tragedia."

    scene bg negro
    with Dissolve(2.5)
    "{b}FIN DEL CAPÍTULO 1 (AOI) - ADVERTENCIA EN EL VACÍO{/b}"
    return


label final_capitulo_aoi_esperanza:

    stop music fadeout 2.5
    scene bg negro
    with fade_lento

    "Sola en la habitación de aislamiento, apoyé mi frente contra el cristal frío de la puerta."
    "Los médicos piensan que soy peligrosa. Mi expediente clínico ahora me etiqueta como paciente psiquiátrica inestable. Probablemente pasaré meses encerrada bajo vigilancia estricta."

    show aoi_base at silueta_center with Dissolve(1.5)

    "Pero en el rincón de mi alma, una lágrima de paz rodó por mi mejilla."
    "Yuna está viva. La muerte extendió sus garras y yo se las arranqué con mis propias manos en la oscuridad de la noche."

    "Mis ojos no son una simple secuela del coma. Son un arma capaz de torcer el tejido del destino."
    "Y por primera vez desde que perdí a mi hermano... encontré una razón para seguir viviendo en este mundo."

    scene bg negro
    with Dissolve(2.5)
    "{b}FIN DEL CAPÍTULO 1 (AOI) - EL SACRIFICIO QUE BURLÓ A LA MUERTE{/b}"
    return


label final_capitulo_aoi_omision:

    stop music fadeout 2.5
    scene bg negro
    with fade_muerte

    show aoi_acurrucada_llorando_mano at silueta_floor_center with Dissolve(1.5)

    "La imagen de los ojos vacíos de Yuna se grabó en mi retina para siempre."
    "Tuve la oportunidad de salvarla. Tuve la premonición en mis manos y elegí la cobardía de creer que solo era una pesadilla."

    "Mi hermano Shinshu saltó al vacío porque creyó que no llegó a tiempo para salvarme."
    "Y yo... teniendo el tiempo a mi favor, me quedé de brazos cruzados."

    "En la penumbra helada del hospital de Nagano, supe que el abismo del Nexus nunca me dejará en paz..."

    scene bg negro
    with Dissolve(2.5)
    "{b}FIN DEL CAPÍTULO 1 (AOI) - EL PESO DE LA OMISIÓN{/b}"
    return

