## =============================================================================
## SISTEMA DE EXPLORACIÓN 2D Y CRUCE PRE-ACCIDENTE - NEXUS
## =============================================================================
## Proporciona:
## 1. screen street_2d_crossing: Cruce 2D interactivo a pantalla completa antes del impacto en Nagano.
## 2. screen hospital_2d_exploration: Exploración 2D hospitalaria MULTI-PISO a pantalla completa (1920x1080).
## =============================================================================

default hospital_pos_x = 960
default hospital_pos_y = 540
default hospital_current_floor = 3
default hospital_player_facing = "down"
default hospital_investigated = set()
default hospital_modal_clue = None
default hospital_events_done = set()

default street_pos_x = 420
default street_pos_y = 620
default street_investigated = set()
default street_modal_clue = None

init python:

    # -------------------------------------------------------------------------
    # DATOS: CRUCE PEATONAL PRE-ACCIDENTE EN NAGANO (2D)
    # -------------------------------------------------------------------------
    STREET_AREAS = [
        {
            "id": "aoi_umbrella",
            "name": "Aoi Kazama • Paraguas Amarillo",
            "x": 680, "y": 620, "radius": 110,
            "icon": "☂️",
            "tag": "HERMANA",
            "color": "#facc15",
            "title": "La Inocencia al Borde del Abismo",
            "text": "Aoi da pequeños saltos infantiles sobre las líneas blancas del cruce peatonal de Matsumoto.\n\n«¡Mira, hermano! Si pisas solo las líneas blancas, los monstruos de la niebla no te alcanzan...»\n\nEl viento helado de las montañas azota su paraguas amarillo. Su risa pura contrasta con el hedor a gasolina y caucho quemado que empieza a filtrarse entre la neblina."
        },
        {
            "id": "puddle_blood",
            "name": "Charco en el Asfalto • Reflejo Sangriento",
            "x": 980, "y": 620, "radius": 110,
            "icon": "🩸",
            "tag": "PREMONICIÓN",
            "color": "#ef4444",
            "title": "El Presagio Escarlata en el Agua",
            "text": "Miras hacia el charco de agua de lluvia acumulado sobre el asfalto agrietado.\n\nEn lugar de reflejar el cielo plomizo de la tarde, la superficie se torna espesa y viscosa como un charco de sangre arterial fresca.\n\nUn sonido espectral de huesos pulverizándose resuena dentro de tu cráneo. Un dolor punzante te desgarra el nervio óptico."
        },
        {
            "id": "traffic_light",
            "name": "Semáforo Peatonal Averiado",
            "x": 1360, "y": 500, "radius": 110,
            "icon": "🚦",
            "tag": "ANOMALÍA",
            "color": "#f97316",
            "title": "La Señal Eléctrica Quebrada",
            "text": "La luz peatonal verde titila de manera errática, chisporroteando bajo la lluvia torrencial.\n\nPor un instante se apaga por completo, y en su lugar la silueta roja de la mano estalla en un destello carmesí violento.\n\nLa electricidad de la farola zumba con un chillido agudo. Algo no encaja en la atmósfera: el tiempo parece ralentizarse a cada paso."
        },
        {
            "id": "engine_fog",
            "name": "La Curva de la Niebla • Rugido Mortal",
            "x": 1550, "y": 680, "radius": 120,
            "icon": "🚛",
            "tag": "AMENAZA",
            "color": "#dc2626",
            "title": "Dos Faros Ciegos en la Oscuridad",
            "text": "Desde la curva cerrada de la carretera desciende un camión pesado a velocidad suicida.\n\nEl chirrido de los frenos bloqueados desgarrando el pavimento helado es ensordecedor. Las luces delanteras penetran la niebla como dos ojos incandescentes sedientos de sangre.\n\n¡Está directo en curso de colisión contra el paso peatonal!"
        }
    ]

    # -------------------------------------------------------------------------
    # DATOS: HOSPITAL MULTI-PISO (PISOS 1, 2 Y 3)
    # -------------------------------------------------------------------------
    HOSPITAL_FLOORS_DATA = {
        # ---------------------------------------------------------------------
        # PISO 3: TRAUMATOLOGÍA, HABITACIONES Y PABELLÓN DE INTERNACIÓN
        # ---------------------------------------------------------------------
        3: [
            {
                "id": "kenji_room_304",
                "floor": 3,
                "name": "Habitación 304 • Camilla de Kenji Takahashi",
                "x": 520, "y": 420, "radius": 110,
                "icon": "🛏️",
                "tag": "COMPAÑERO",
                "color": "#38bdf8",
                "title": "Kenji Takahashi y la Aguja de las 18:00",
                "text": "Kenji descansa con una férula rígida de titanio en su pierna izquierda.\n\n«¡Oye, Ren! A las seis en punto viene Sato con la última dosis intravenosa. Dicen que es un tratamiento concentrado para asegurar que los huesos suelden rápido...»\n\nAl mirar el gotero con tu ojo izquierdo, la solución salina se ve turbia, burbujeante y pestilente. En tus retinas arde la visión de Kenji retorciéndose entre vómitos de sangre negra si esa dosis ingresa a su torrente venoso.",
                "action_choice": "Revisar la etiqueta química del suero N-4"
            },
            {
                "id": "room_302_agony",
                "floor": 3,
                "name": "Habitación 302 • Paciente en Delirio Terminal",
                "x": 260, "y": 420, "radius": 110,
                "icon": "⚠️",
                "tag": "DELIRIO",
                "color": "#ef4444",
                "title": "El Agónico Grito de las Sombras Rojas",
                "text": "Un hombre de mediana edad está amarrado a la camilla con correas de cuero reforzadas. Sus muñecas sangran de tanto forcejear.\n\n«¡NO DEJEN QUE APAGUEN LAS LUCES! ¡LOS OJOS ROJOS ESTÁN EN LAS PAREDES! ¡EL DOCTOR ME METIÓ AGUJAS NEGRAS EN EL CUELLO!»\n\nSus ojos inyectados en sangre se clavan en ti. Espuma sanguinolenta gotea por su barbilla mientras convulsiona frenéticamente.",
                "action_choice": "Sujetar sus correas e intentar calmar sus espasmos"
            },
            {
                "id": "nursing_station_floor3",
                "floor": 3,
                "name": "Estación Central de Enfermería (Piso 3)",
                "x": 1080, "y": 420, "radius": 110,
                "icon": "📋",
                "tag": "MEDICACIÓN",
                "color": "#f59e0b",
                "title": "Bandeja Quirúrgica de la Enfermera Sato",
                "text": "Sobre el mostrador de acero inoxidable reposa una bandeja con jeringas de vidrio precargadas.\n\nUna ampolla de vidrio ámbar tiene la etiqueta arrancada con bisturí, dejando visible solo una inscripción roja: «Tox-NB7 • Dosis letal fulminante». Está asignada a la camilla 304 para las 18:00.\n\n¿Por qué el personal de guardia tiene orden de inocular un veneno paralizante en un pabellón de traumatología ordinario?",
                "action_choice": "Registrar en sigilo los expedientes confidenciales"
            },
            {
                "id": "room_305_yuna",
                "floor": 3,
                "name": "Habitación 305 / 201 • Camilla de Yuna Sasaki",
                "x": 1420, "y": 420, "radius": 110,
                "icon": "🛏️",
                "tag": "COMPAÑERA",
                "color": "#c084fc",
                "title": "Yuna Sasaki y la Visita Violenta",
                "text": "Yuna está sentada con la cabeza baja, apretando sus rodillas contra el pecho con terror en la mirada.\n\n«Aoi... mi padre viene en camino. Dijo que si la aseguradora no cubre los gastos, me sacará arrastrándome del hospital... Tengo miedo de lo que me haga cuando entre por esa puerta...»\n\nJunto a su puerta, una varilla metálica de un gotero roto sobresale en el suelo con una punta afilada capaz de atravesar un cráneo.",
                "action_choice": "Ofrecerle protección y retirar la varilla puntiaguda"
            },
            {
                "id": "elevator_floor3",
                "floor": 3,
                "name": "Ascensor Central & Escaleras de Emergencia",
                "x": 800, "y": 720, "radius": 120,
                "icon": "🛗",
                "tag": "NEXUS VERTICAL",
                "color": "#10b981",
                "title": "Acceso a Pisos Inferiores",
                "text": "El ascensor chirría pesadamente entre los pisos. Al lado, la puerta metálica de las escaleras de emergencia conduce hacia abajo.\n\n• PISO 2: UCI de Aislamiento Crítico, Quirófano 2 y Farmacia de Toxicología.\n• PISO 1: Urgencias de Choque, Morgue Fría y Sala de Desechos Biológicos.\n\nPuedes cambiar de piso directamente con los botones de la barra superior o las opciones de interacción.",
                "action_choice": "Descender al Piso 2 (UCI & Quirófanos)"
            },
            {
                "id": "storm_window_floor3",
                "floor": 3,
                "name": "Gran Ventanal Sur • Vistas a la Azotea",
                "x": 1660, "y": 720, "radius": 110,
                "icon": "🌧️",
                "tag": "MEMORIA",
                "color": "#94a3b8",
                "title": "El Vacío Helado de Shinshu",
                "text": "El temporal golpea con furia salvaje los ventanales reforzados. Relámpagos lívidos iluminan las cordilleras de Nagano.\n\nAbajo, el tejado de urgencias se ve empapado en penumbra. Desde esta altura exacta fue donde ocurrió el salto mortal hacia el vacío.\n\nLa culpa y el remordimiento pesan como plomo derretido en el pecho.",
                "action_choice": "Contemplar la lluvia y afilar la concentración mental"
            }
        ],

        # ---------------------------------------------------------------------
        # PISO 2: UCI DE AISLAMIENTO, QUIRÓFANOS Y TOXICOLOGÍA
        # ---------------------------------------------------------------------
        2: [
            {
                "id": "icu_critical_floor2",
                "floor": 2,
                "name": "UCI de Aislamiento • Monitor en Alarma",
                "x": 340, "y": 420, "radius": 110,
                "icon": "⚡",
                "tag": "CRÍTICO",
                "color": "#ef4444",
                "title": "El Paciente en Taquicardia Ventricular",
                "text": "El monitor cardíaco emite un pitido frenético: 168 pulsaciones por minuto.\n\nEl paciente intubado en la cama 3 tiembla con convulsiones clónicas. Por la comisura de sus labios escurre saliva teñida de sangre oscura.\n\nEn su bolsa de suero cuelga la misma etiqueta roja: «Reactivo Experimental Nexus Causal». El personal lo observa a través del cristal sin intervenir, cronometrando su resistencia.",
                "action_choice": "Intervenir la válvula de oxígeno para estabilizarlo"
            },
            {
                "id": "operating_room_floor2",
                "floor": 2,
                "name": "Quirófano 2 • Luces Cialíticas y Sangre Fresca",
                "x": 720, "y": 420, "radius": 110,
                "icon": "🩸",
                "tag": "HORROR QUIRÚRGICO",
                "color": "#dc2626",
                "title": "Mesa Quirúrgica Manchada de Rojo",
                "text": "La puerta vaivén del quirófano está encajada con una pinza de campo. El olor es repugnante: carne quemada por electrobisturí, antiséptico rancio y sangre tibia.\n\nSobre la camilla metálica hay un charco de sangre arterial fresca que gotea lentamente hacia el sumidero del suelo. Bandejas con sierras de hueso y separadores costales manchados de rojo atestiguan una cirugía brutal que acaba de terminar.",
                "action_choice": "Examinar los rastros biológicos y las muestras de tejido"
            },
            {
                "id": "pharmacy_toxic_floor2",
                "floor": 2,
                "name": "Depósito de Farmacia y Toxicología",
                "x": 1180, "y": 420, "radius": 110,
                "icon": "☣️",
                "tag": "TOXICOLOGÍA",
                "color": "#f97316",
                "title": "Armario de Sustancias de Restricción",
                "text": "El armario blindado de fármacos controlados tiene la cerradura forzada.\n\nFrascos de toxinas paralizantes de acción rápida (Tox-NB7) yacen alineados en cajas con el sello del «Hospital General de Chūbu - División Quirúrgica Especial».\n\nEste hospital no está curando pacientes: los está utilizando como conejillos de indias para experimentos de muerte inducida y reanimación causal.",
                "action_choice": "Confiscar una ampolla de reactivo como prueba irrefutable"
            },
            {
                "id": "dr_office_floor2",
                "floor": 2,
                "name": "Despacho de Jefatura Quirúrgica (Dr. Moriyama)",
                "x": 1560, "y": 420, "radius": 110,
                "icon": "🚪",
                "tag": "CONSPIRACIÓN",
                "color": "#a855f7",
                "title": "Los Informes Secretos del Dr. Moriyama",
                "text": "Sobre el escritorio de roble hay un expediente marcado con cinta de seguridad roja: «Proyecto Sujetos Despiertos • Kasugai y Takahashi».\n\n«El sujeto Kasugai exhibe alteraciones retinianas fotomórficas tras el traumatismo masivo. Capacidad premonitoria confirmada. La eliminación de Takahashi mediante Tox-NB7 a las 18:00 servirá como prueba de campo para evaluar si el sujeto es capaz de alterar el flujo causal».\n\n¡Moriyama planeó el asesinato de Kenji deliberadamente para probar tus ojos!",
                "action_choice": "Sustraer el informe confidencial antes de ser descubierto"
            },
            {
                "id": "elevator_floor2",
                "floor": 2,
                "name": "Ascensor Central (Piso 2)",
                "x": 960, "y": 720, "radius": 120,
                "icon": "🛗",
                "tag": "CONEXIÓN",
                "color": "#10b981",
                "title": "Distribuidor Central del Edificio",
                "text": "Desde aquí puedes subir al Piso 3 (Pabellón de Internación y Camillas) o descender al Piso 1 (Urgencias y Morgue Fría subterránea).",
                "action_choice": "Cambiar de Piso"
            }
        ],

        # ---------------------------------------------------------------------
        # PISO 1: URGENCIAS, MORGUE FRÍA Y DESECHOS BIOLÓGICOS
        # ---------------------------------------------------------------------
        1: [
            {
                "id": "er_triage_floor1",
                "floor": 1,
                "name": "Sala de Urgencias y Triage Masivo",
                "x": 360, "y": 420, "radius": 110,
                "icon": "🚑",
                "tag": "URGENCIAS",
                "color": "#ef4444",
                "title": "Heridos de Autopista y Gritos de Dolor",
                "text": "La planta baja es un caos dantesco. Dos camillas ingresan a toda prisa con heridos de un choque múltiple en la ruta alpina.\n\nUn joven grita desgarrándose la voz mientras médicos comprimen una arteria femoral rota. La sangre empapa el linóleo blanco.\n\nEl olor a gasas ensangrentadas y alcohol yodado te transporta de golpe al instante en que tu propio cuerpo fue pulverizado por el camión.",
                "action_choice": "Ayudar a despejar el pasillo para la camilla crítica"
            },
            {
                "id": "morgue_cold_floor1",
                "floor": 1,
                "name": "Morgue Fría • Depósito de Cadáveres",
                "x": 780, "y": 420, "radius": 110,
                "icon": "⚰️",
                "tag": "MORGUE",
                "color": "#38bdf8",
                "title": "Las Bandejas Frías y el Anciano Kuroda",
                "text": "La temperatura desciende a 3°C al abrir la pesada puerta hermética de la morgue subterránea.\n\nEn la gaveta de acero número 7 reposa el cuerpo del anciano Kuroda bajo una sábana blanca manchada de fluido biológico. Su rostro conserva la mueca de terror con la que murió en el baño a las 20:15.\n\nEn su cuello divisas una pequeña marca violácea: el orificio exacto de una punción letal con reactivo Tox-NB7. No fue un simple infarto natural: ¡Kuroda también fue asesinado!",
                "action_choice": "Inspeccionar las marcas forenses del cuello del cadáver"
            },
            {
                "id": "bio_waste_floor1",
                "floor": 1,
                "name": "Sala de Incineración y Residuos Peligrosos",
                "x": 1220, "y": 420, "radius": 110,
                "icon": "🔥",
                "tag": "INCINERACIÓN",
                "color": "#dc2626",
                "title": "El Fuego Que Borra las Pruebas",
                "text": "El horno incinerador ruge en el fondo de la sala, irradiando una ola de calor asfixiante.\n\nUn contenedor de residuos biológicos contiene batas ensangrentadas, frascos vacíos de Tox-NB7 y expedientes clínicos quemados a medias.\n\nEstán destruyendo a toda prisa las evidencias de los pacientes que fallecieron misteriosamente durante la última semana.",
                "action_choice": "Rescatar fragmentos de expedientes del contenedor"
            },
            {
                "id": "security_checkpoint_floor1",
                "floor": 1,
                "name": "Control de Seguridad y Salida Bloqueada",
                "x": 1600, "y": 420, "radius": 110,
                "icon": "👮",
                "tag": "VIGILANCIA",
                "color": "#64748b",
                "title": "Guardias Armados en la Salida Oeste",
                "text": "Dos guardias de seguridad privada vigilan la salida trasera con porras eléctricas y radios de onda corta.\n\nHablan en voz baja: «Nadie del pabellón oeste sale sin el sello de Moriyama. Si el muchacho de los ojos raros intenta cruzar el perímetro, inmovilícenlo de inmediato».\n\nEl hospital es una prisión sellada. Salvar a Kenji y escapar con vida requerirá astucia y determinación implacable.",
                "action_choice": "Registrar sus frecuencias de radio y patrullaje"
            },
            {
                "id": "elevator_floor1",
                "floor": 1,
                "name": "Ascensor Central (Piso 1)",
                "x": 960, "y": 720, "radius": 120,
                "icon": "🛗",
                "tag": "CONEXIÓN",
                "color": "#10b981",
                "title": "Retorno a Pabellones Superiores",
                "text": "El ascensor te permite regresar rápidamente al Piso 2 (Cirugía y Toxicología) o al Piso 3 (Habitación 304 con Kenji Takahashi).",
                "action_choice": "Subir al Piso 3 (Habitaciones)"
            }
        ]
    }

    def get_current_floor_areas(floor):
        return HOSPITAL_FLOORS_DATA.get(floor, HOSPITAL_FLOORS_DATA[3])

    def get_nearest_floor_area(floor, px, py):
        areas = get_current_floor_areas(floor)
        for a in areas:
            ax = a.get("x", 0)
            ay = a.get("y", 0)
            rad = a.get("radius", 110)
            dist = ((ax - px) ** 2 + (ay - py) ** 2) ** 0.5
            if dist <= rad:
                return a
        return None

    def move_hospital_player(dx, dy, facing, perspective):
        global hospital_pos_x, hospital_pos_y, hospital_player_facing
        hospital_player_facing = facing
        new_x = hospital_pos_x + dx
        new_y = hospital_pos_y + dy
        # Límites de movimiento en pantalla completa 1920x1080
        hospital_pos_x = max(120, min(1800, new_x))
        hospital_pos_y = max(180, min(860, new_y))
        renpy.restart_interaction()

    def set_hospital_floor(floor):
        global hospital_current_floor, hospital_pos_x, hospital_pos_y
        hospital_current_floor = floor
        hospital_pos_x = 960
        hospital_pos_y = 660
        renpy.play("audio/heartbeat.wav")
        renpy.restart_interaction()

    def inspect_floor_area(area):
        global hospital_modal_clue, hospital_investigated
        if area:
            hospital_modal_clue = area
            area_id = area.get("id", "")
            if area_id:
                hospital_investigated.add(area_id)
            tag = area.get("tag", "")
            if "TOXICOLOGÍA" in tag or "HORROR" in tag or "MORGUE" in tag:
                renpy.play("audio/eye_vision.wav")
            else:
                renpy.play("audio/heartbeat.wav")
            renpy.restart_interaction()

    def close_hospital_modal():
        global hospital_modal_clue
        hospital_modal_clue = None
        renpy.restart_interaction()

    def trigger_clue_event(event_key):
        global hospital_events_done
        hospital_events_done.add(event_key)
        renpy.play("audio/eye_vision.wav")
        renpy.restart_interaction()

    # Funciones para la calle 2D previa al accidente
    def move_street_player(dx, dy):
        global street_pos_x, street_pos_y
        street_pos_x = max(180, min(1740, street_pos_x + dx))
        street_pos_y = max(420, min(800, street_pos_y + dy))
        renpy.restart_interaction()

    def inspect_street_area(area):
        global street_modal_clue, street_investigated
        if area:
            street_modal_clue = area
            area_id = area.get("id", "")
            if area_id:
                street_investigated.add(area_id)
            if area_id in ["puddle_blood", "engine_fog"]:
                renpy.play("audio/crash.wav")
            else:
                renpy.play("audio/heartbeat.wav")
            renpy.restart_interaction()

    def close_street_modal():
        global street_modal_clue
        street_modal_clue = None
        renpy.restart_interaction()


## =============================================================================
## 1. PANTALLA 2D PRE-ACCIDENTE EN NAGANO: EL PASO DE PEATONES BAJO LA LLUVIA
## =============================================================================
screen street_2d_crossing(perspective="hombre"):
    modal True
    tag menu

    $ is_male = (perspective != "mujer")
    $ theme_tint = "#e63946" if is_male else "#c084fc"
    $ near_street_area = None
    python:
        for a in STREET_AREAS:
            ax = a.get("x", 0)
            ay = a.get("y", 0)
            dist = ((ax - street_pos_x) ** 2 + (ay - street_pos_y) ** 2) ** 0.5
            if dist <= a.get("radius", 110):
                near_street_area = a
                break

    # Controles por Teclado (WASD y Flechas)
    key "K_UP" action Function(move_street_player, 0, -36)
    key "w" action Function(move_street_player, 0, -36)
    key "W" action Function(move_street_player, 0, -36)

    key "K_DOWN" action Function(move_street_player, 0, 36)
    key "s" action Function(move_street_player, 0, 36)
    key "S" action Function(move_street_player, 0, 36)

    key "K_LEFT" action Function(move_street_player, -36, 0)
    key "a" action Function(move_street_player, -36, 0)
    key "A" action Function(move_street_player, -36, 0)

    key "K_RIGHT" action Function(move_street_player, 36, 0)
    key "d" action Function(move_street_player, 36, 0)
    key "D" action Function(move_street_player, 36, 0)

    if near_street_area and not street_modal_clue:
        key "K_SPACE" action Function(inspect_street_area, near_street_area)
        key "K_RETURN" action Function(inspect_street_area, near_street_area)
        key "e" action Function(inspect_street_area, near_street_area)
        key "E" action Function(inspect_street_area, near_street_area)

    # Fondo oscuro de noche de tormenta
    add Solid("#070b14")

    # --- REPRESENTACIÓN 2D DEL CRUCE PEATONAL A PANTALLA COMPLETA ---
    fixed:
        xfill True
        yfill True

        # Acera superior (Farolas y comercios borrosos)
        frame:
            xpos 0
            ypos 0
            xsize 1920
            ysize 380
            background Solid("#0f172a")

            # Carteles luminosos lejanos de Matsumoto
            hbox:
                xpos 80
                ypos 70
                spacing 40
                frame:
                    background Solid("#1e293b")
                    padding (16, 8, 16, 8)
                    text "松本駅前通り • MATSUMOTO STATION":
                        size 12
                        color "#64748b"
                        bold True
                frame:
                    background Solid("#31101d")
                    padding (16, 8, 16, 8)
                    text "⚠️ AVISO METEOROLÓGICO: TEMPORAL SEVERO EN CHŪBU":
                        size 12
                        color "#f43f5e"
                        bold True

        # Calzada de asfalto mojado (Paso peatonal y carretera)
        frame:
            xpos 0
            ypos 380
            xsize 1920
            ysize 460
            background Solid("#090d16")

            # Franjas blancas del paso de peatones (Cebra)
            hbox:
                xpos 380
                ypos 40
                spacing 48
                for i in range(11):
                    frame:
                        xsize 60
                        ysize 380
                        background Solid("#e2e8f018" if i % 2 == 0 else "#f8fafc25")

        # Acera inferior de seguridad
        frame:
            xpos 0
            ypos 840
            xsize 1920
            ysize 240
            background Solid("#0b1222")

        # --- DIBUJADO DE PUNTOS INTERACTIVOS EN LA CALLE ---
        for spot in STREET_AREAS:
            $ is_inspected = (spot["id"] in street_investigated)
            $ mark_color = "#10b981" if is_inspected else spot["color"]

            button:
                xpos spot["x"] - 65
                ypos spot["y"] - 65
                xsize 130
                ysize 130
                background Solid("#060a14b0")
                hover_background Solid(mark_color)
                action Function(inspect_street_area, spot)

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 4
                    text spot["icon"]:
                        size 32
                        xalign 0.5
                    text spot["tag"]:
                        size 10
                        color mark_color
                        bold True
                        xalign 0.5

        # --- AVATAR DEL JUGADOR EN LA CALLE 2D ---
        frame:
            xpos street_pos_x - 30
            ypos street_pos_y - 30
            xsize 60
            ysize 60
            background Solid(theme_tint)

            text ("♂" if is_male else "♀"):
                size 24
                color "#ffffff"
                bold True
                xalign 0.5
                yalign 0.5

        # Silueta de Aoi infantil caminando a unos pasos
        frame:
            xpos 700
            ypos 600
            xsize 44
            ysize 44
            background Solid("#facc15")
            text "☂️":
                size 22
                xalign 0.5
                yalign 0.5

    # --- BARRA SUPERIOR HUD ---
    frame:
        xfill True
        ysize 76
        background Solid("#060a14f0")
        padding (32, 12, 32, 12)

        hbox:
            xfill True
            yalign 0.5

            hbox:
                spacing 16
                yalign 0.5
                text ("🌧️ MATSUMOTO, CHŪBU • CRUCE PEATONAL PREVIO AL IMPACTO"):
                    font gui.name_text_font
                    size 16
                    bold True
                    color "#f8fafc"

                frame:
                    background Solid("#1e293b")
                    padding (10, 4, 10, 4)
                    text "EXPLORACIÓN 2D PRE-ACCIDENTE":
                        size 11
                        bold True
                        color theme_tint

            # Indicador de peligro inminente
            frame:
                background Solid("#450a0a")
                padding (14, 6, 14, 6)
                text "⚠️ PELIGRO INMINENTE • 18:00 TORMENTA":
                    size 11
                    bold True
                    color "#fca5a5"

    # --- BARRA INFERIOR DE ACCIÓN Y DECISIÓN ---
    frame:
        xfill True
        yalign 1.0
        ysize 90
        background Solid("#070b16f2")
        padding (24, 12, 24, 12)

        hbox:
            xfill True
            yalign 0.5

            # Controles táctiles para celulares
            hbox:
                spacing 6
                yalign 0.5

                button:
                    action Function(move_street_player, -36, 0)
                    background Solid("#1e293b")
                    padding (12, 8, 12, 8)
                    text "◀ A":
                        size 12
                        bold True
                        color "#e2e8f0"

                button:
                    action Function(move_street_player, 0, -36)
                    background Solid("#1e293b")
                    padding (12, 8, 12, 8)
                    text "▲ W":
                        size 12
                        bold True
                        color "#e2e8f0"

                button:
                    action Function(move_street_player, 0, 36)
                    background Solid("#1e293b")
                    padding (12, 8, 12, 8)
                    text "▼ S":
                        size 12
                        bold True
                        color "#e2e8f0"

                button:
                    action Function(move_street_player, 36, 0)
                    background Solid("#1e293b")
                    padding (12, 8, 12, 8)
                    text "▶ D":
                        size 12
                        bold True
                        color "#e2e8f0"

                if near_street_area:
                    button:
                        action Function(inspect_street_area, near_street_area)
                        background Solid(theme_tint)
                        padding (14, 8, 14, 8)
                        text "🔍 INSPECCIONAR":
                            size 12
                            bold True
                            color "#ffffff"

            # Instrucciones
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 2
                text _("• Muévete con [[W, A, S, D]] o [[Flechas]] • [[Espacio]] para inspeccionar señales y hablar con Aoi") substitute False:
                    size 11
                    color "#94a3b8"

            # Botón Decisivo del Destino: Provocar la reacción al camión
            button:
                action Return("decision_accidente")
                background Solid("#b91c1c")
                hover_background Solid("#ef4444")
                padding (20, 12, 20, 12)
                text "⚡ ¡EL CAMIÓN SE ACERCA! ACTUAR AHORA ▶":
                    size 12
                    bold True
                    color "#ffffff"

    # --- MODAL FLOTANTE DE DETALLE EN LA CALLE ---
    if street_modal_clue:
        button:
            xfill True
            yfill True
            background Solid("#000000ba")
            action Function(close_street_modal)

        frame:
            xalign 0.5
            yalign 0.5
            xsize 920
            background Frame(Solid("#0d1322fa"), 12, 12)
            padding (36, 28, 36, 28)

            vbox:
                spacing 14
                xfill True

                hbox:
                    xfill True
                    yalign 0.5
                    hbox:
                        spacing 12
                        text street_modal_clue.get("icon", "✦"):
                            size 28
                        vbox:
                            spacing 2
                            text street_modal_clue.get("name", ""):
                                size 12
                                bold True
                                color street_modal_clue.get("color", "#facc15")
                            text street_modal_clue.get("title", ""):
                                size 18
                                bold True
                                color "#ffffff"

                frame:
                    xfill True
                    ysize 2
                    background Solid(street_modal_clue.get("color", "#facc15"))

                text street_modal_clue.get("text", ""):
                    size 14
                    color "#cbd5e1"
                    line_spacing 5

                null height 6

                button:
                    action Function(close_street_modal)
                    xalign 1.0
                    background Solid("#1e293b")
                    padding (20, 8, 20, 8)
                    text "✕ CONTINUAR EN LA CALLE [[ESC]]" substitute False:
                        size 12
                        bold True
                        color "#ffffff"


## =============================================================================
## 2. EXPLORACIÓN 2D DEL HOSPITAL A PANTALLA COMPLETA MULTI-PISO (1920x1080)
## =============================================================================
screen hospital_2d_exploration(perspective="hombre"):
    modal True
    tag menu

    $ is_male = (perspective != "mujer")
    $ theme_tint = "#e63946" if is_male else "#c084fc"
    $ current_areas = get_current_floor_areas(hospital_current_floor)
    $ near_area = get_nearest_floor_area(hospital_current_floor, hospital_pos_x, hospital_pos_y)
    $ progress_count = len(hospital_investigated)
    $ can_continue = (progress_count >= 2)

    # Teclas de movimiento WASD y Flechas
    key "K_UP" action Function(move_hospital_player, 0, -36, "up", perspective)
    key "w" action Function(move_hospital_player, 0, -36, "up", perspective)
    key "W" action Function(move_hospital_player, 0, -36, "up", perspective)

    key "K_DOWN" action Function(move_hospital_player, 0, 36, "down", perspective)
    key "s" action Function(move_hospital_player, 0, 36, "down", perspective)
    key "S" action Function(move_hospital_player, 0, 36, "down", perspective)

    key "K_LEFT" action Function(move_hospital_player, -36, 0, "left", perspective)
    key "a" action Function(move_hospital_player, -36, 0, "left", perspective)
    key "A" action Function(move_hospital_player, -36, 0, "left", perspective)

    key "K_RIGHT" action Function(move_hospital_player, 36, 0, "right", perspective)
    key "d" action Function(move_hospital_player, 36, 0, "right", perspective)
    key "D" action Function(move_hospital_player, 36, 0, "right", perspective)

    # Teclas de interacción
    if near_area and not hospital_modal_clue:
        key "K_SPACE" action Function(inspect_floor_area, near_area)
        key "K_RETURN" action Function(inspect_floor_area, near_area)
        key "e" action Function(inspect_floor_area, near_area)
        key "E" action Function(inspect_floor_area, near_area)

    # Fondo oscuro global de la pantalla completa 1920x1080
    add Solid("#040711")

    # --- PLANO ARQUITECTÓNICO DEL PISO COMPLETO (1920x1080 TOTAL) ---
    fixed:
        xfill True
        yfill True

        # Pasillo principal de baldosas gélidas
        frame:
            xpos 80
            ypos 100
            xsize 1760
            ysize 740
            background Frame(Solid("#080f20f2"), 8, 8)

            # Rejilla arquitectónica del plano
            fixed:
                xfill True
                yfill True

                # Corredor transversal
                frame:
                    xpos 0
                    ypos 280
                    xsize 1760
                    ysize 180
                    background Solid("#0d172fe0")

                    text ("CORREDOR CENTRAL • " + ("PISO 3: PABELLÓN DE TRAUMATOLOGÍA" if hospital_current_floor == 3 else ("PISO 2: CIRUGÍA Y AISLAMIENTO" if hospital_current_floor == 2 else "PISO 1: URGENCIAS Y MORGUE"))):
                        size 11
                        color "#334155"
                        bold True
                        xalign 0.5
                        yalign 0.5
                        kerning 2

        # --- DIBUJADO DE LAS SALAS Y HABITACIONES DEL PISO ACTUAL ---
        for area in current_areas:
            $ is_found = (area.get("id") in hospital_investigated)
            $ spot_color = "#10b981" if is_found else area.get("color", theme_tint)

            # Tarjeta de sala interactiva en el mapa
            button:
                xpos area["x"] - 130
                ypos area["y"] - 90
                xsize 260
                ysize 160
                background Solid("#091024d8")
                hover_background Solid(spot_color)
                action Function(inspect_floor_area, area)

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 6
                    text area.get("icon", "✦"):
                        size 30
                        xalign 0.5
                    text area.get("name", "Habitación"):
                        size 11
                        bold True
                        color "#f8fafc"
                        xalign 0.5
                        textalign 0.5
                    frame:
                        background Solid("#050812")
                        padding (8, 3, 8, 3)
                        xalign 0.5
                        text area.get("tag", "PABELLÓN"):
                            size 9
                            bold True
                            color spot_color

        # --- AVATAR DEL PROTAGONISTA EN TIEMPO REAL ---
        frame:
            xpos hospital_pos_x - 32
            ypos hospital_pos_y - 32
            xsize 64
            ysize 64
            background Solid(theme_tint)

            text ("♂" if is_male else "♀"):
                size 26
                bold True
                color "#ffffff"
                xalign 0.5
                yalign 0.5

    # --- BARRA SUPERIOR HUD CON NAVEGADOR DE PISOS (1, 2, 3) ---
    frame:
        xfill True
        ysize 84
        background Solid("#060a16f6")
        padding (28, 12, 28, 12)

        hbox:
            xfill True
            yalign 0.5

            hbox:
                spacing 16
                yalign 0.5

                text ("♂ LÍNEA CARMESÍ" if is_male else "♀ LÍNEA AMATISTA"):
                    size 13
                    bold True
                    color theme_tint

                text "•":
                    color "#475569"

                text "HOSPITAL GENERAL DE CHŪBU • PANTALLA COMPLETA":
                    size 15
                    bold True
                    color "#f8fafc"

            # SELECTOR DIRECTO DE PISOS HOSPITALARIOS (PISO 1, 2, 3)
            hbox:
                spacing 10
                yalign 0.5

                button:
                    padding (14, 6, 14, 6)
                    background Solid(theme_tint if hospital_current_floor == 1 else "#0f172a")
                    action Function(set_hospital_floor, 1)
                    text "PISO 1: Morgue & Urgencias":
                        size 11
                        bold True
                        color ("#ffffff" if hospital_current_floor == 1 else "#94a3b8")

                button:
                    padding (14, 6, 14, 6)
                    background Solid(theme_tint if hospital_current_floor == 2 else "#0f172a")
                    action Function(set_hospital_floor, 2)
                    text "PISO 2: UCI & Quirófanos":
                        size 11
                        bold True
                        color ("#ffffff" if hospital_current_floor == 2 else "#94a3b8")

                button:
                    padding (14, 6, 14, 6)
                    background Solid(theme_tint if hospital_current_floor == 3 else "#0f172a")
                    action Function(set_hospital_floor, 3)
                    text "PISO 3: Habitaciones 301-305":
                        size 11
                        bold True
                        color ("#ffffff" if hospital_current_floor == 3 else "#94a3b8")

            # CONTADOR TOTAL DE EVIDENCIAS REUNIDAS
            frame:
                background Solid("#0b1222")
                padding (12, 6, 12, 6)
                hbox:
                    spacing 8
                    text "EXPEDIENTES DESCUBIERTOS:":
                        size 10
                        color "#94a3b8"
                        bold True
                    text str(progress_count):
                        size 13
                        color theme_tint
                        bold True

    # --- BARRA INFERIOR DE NAVEGACIÓN Y AVANCE DE TRAMA ---
    frame:
        xfill True
        yalign 1.0
        ysize 92
        background Solid("#060a16f6")
        padding (24, 12, 24, 12)

        hbox:
            xfill True
            yalign 0.5

            # CRUCETA TÁCTIL VIRTUAL PARA CELULARES
            hbox:
                spacing 6
                yalign 0.5

                button:
                    action Function(move_hospital_player, -36, 0, "left", perspective)
                    background Solid("#1e293b")
                    padding (12, 8, 12, 8)
                    text "◀ A":
                        size 12
                        bold True
                        color "#e2e8f0"

                button:
                    action Function(move_hospital_player, 0, -36, "up", perspective)
                    background Solid("#1e293b")
                    padding (12, 8, 12, 8)
                    text "▲ W":
                        size 12
                        bold True
                        color "#e2e8f0"

                button:
                    action Function(move_hospital_player, 0, 36, "down", perspective)
                    background Solid("#1e293b")
                    padding (12, 8, 12, 8)
                    text "▼ S":
                        size 12
                        bold True
                        color "#e2e8f0"

                button:
                    action Function(move_hospital_player, 36, 0, "right", perspective)
                    background Solid("#1e293b")
                    padding (12, 8, 12, 8)
                    text "▶ D":
                        size 12
                        bold True
                        color "#e2e8f0"

                if near_area:
                    button:
                        action Function(inspect_floor_area, near_area)
                        background Solid(theme_tint)
                        padding (14, 8, 14, 8)
                        text "🔍 INVESTIGAR":
                            size 12
                            bold True
                            color "#ffffff"

            # GUÍA DE CONTROL
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 2
                text _("• Teclado: [[W, A, S, D]] o [[Flechas]] • [[Espacio / E]] para investigar • Haz clic en salas para moverte") substitute False:
                    size 11
                    color "#94a3b8"
                text _("• Pisos: Usa los botones de piso arriba o inspecciona el Ascensor para cambiar de nivel") substitute False:
                    size 11
                    color "#38bdf8"

            # BOTÓN DE CONTINUAR LA HISTORIA
            if can_continue:
                button:
                    action Return()
                    background Solid(theme_tint)
                    hover_background Solid("#10b981")
                    padding (22, 12, 22, 12)
                    text "CONTINUAR HISTORIA ▶":
                        size 13
                        bold True
                        color "#ffffff"
            else:
                frame:
                    background Solid("#1e293b")
                    padding (16, 12, 16, 12)
                    text ("Reúne al menos 2 expedientes (" + str(progress_count) + "/2)"):
                        size 11
                        bold True
                        color "#64748b"

    # --- MODAL FLOTANTE DE DETALLE CON DECISIONES Y COMBATE/FORCEJEO ---
    if hospital_modal_clue:
        $ clue_c = hospital_modal_clue.get("color", theme_tint)

        button:
            xfill True
            yfill True
            background Solid("#000000cb")
            action Function(close_hospital_modal)

        frame:
            xalign 0.5
            yalign 0.5
            xsize 980
            background Frame(Solid("#0a1020fa"), 12, 12)
            padding (36, 28, 36, 28)

            vbox:
                spacing 14
                xfill True

                # Cabecera
                hbox:
                    xfill True
                    yalign 0.5

                    hbox:
                        spacing 14
                        text hospital_modal_clue.get("icon", "✦"):
                            size 32
                        vbox:
                            spacing 2
                            text hospital_modal_clue.get("name", ""):
                                size 12
                                bold True
                                color clue_c
                            text hospital_modal_clue.get("title", ""):
                                size 20
                                bold True
                                color "#ffffff"

                    frame:
                        background Solid("#1e293b")
                        padding (10, 4, 10, 4)
                        text ("PISO " + str(hospital_current_floor)):
                            size 11
                            bold True
                            color "#e2e8f0"

                frame:
                    xfill True
                    ysize 2
                    background Solid(clue_c)

                # Descripción visceral y detallada
                text hospital_modal_clue.get("text", ""):
                    size 14
                    color "#cbd5e1"
                    line_spacing 5

                null height 6

                # Botones de Acción / Decisión Interactiva
                hbox:
                    spacing 12
                    xalign 0.5

                    button:
                        action Function(trigger_clue_event, hospital_modal_clue.get("id", "") + "_vision")
                        background Solid("#7f1d1d")
                        hover_background Solid("#b91c1c")
                        padding (14, 8, 14, 8)
                        text "🩸 OJO DEL DESTINO (PREMONICIÓN)":
                            size 11
                            bold True
                            color "#fecaca"

                    button:
                        action Function(trigger_clue_event, hospital_modal_clue.get("id", "") + "_struggle")
                        background Solid("#1e3a8a")
                        hover_background Solid("#2563eb")
                        padding (14, 8, 14, 8)
                        text ("⚡ " + hospital_modal_clue.get("action_choice", "Intervenir con determinación")):
                            size 11
                            bold True
                            color "#dbeafe"

                    button:
                        action Function(close_hospital_modal)
                        background Solid("#1e293b")
                        padding (16, 8, 16, 8)
                        text "✕ SEGUIR EXPLORANDO [[ESC]]" substitute False:
                            size 11
                            bold True
                            color "#ffffff"
