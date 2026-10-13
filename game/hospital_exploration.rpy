## =============================================================================
## SISTEMA DE EXPLORACIÓN 2D DEL HOSPITAL (CAPÍTULO 1 - HOMBRE Y MUJER)
## =============================================================================
## Permite al jugador recorrer el pabellón hospitalario en 2D en tiempo real
## utilizando las teclas [W, A, S, D], las [Flechas de Dirección], toques directos
## en pantalla o la cruceta táctil virtual para celulares.
## =============================================================================

default hospital_pos_x = 480
default hospital_pos_y = 360
default hospital_player_facing = "down"
default hospital_investigated = set()
default hospital_modal_clue = None

init python:

    # -------------------------------------------------------------------------
    # DEFINICIÓN DE PISTAS Y SALAS: HOSPITAL GENERAL DE SHINSHU (HOMBRE)
    # -------------------------------------------------------------------------
    HOSPITAL_AREAS_SHINSHU = [
        {
            "id": "kenji_bed",
            "name": "Habitación 304 • Camilla de Kenji",
            "x": 440, "y": 270, "radius": 95,
            "icon": "🛏️",
            "tag": "COMPAÑERO",
            "color": "#38bdf8",
            "title": "Kenji Takahashi y el Gotero de las 18:00",
            "text": "Kenji te saluda con una sonrisa cansada pero optimista desde su camilla.\n\n«¡Oye, Ren! A las seis en punto me toca la última dosis de antibiótico. En cuanto me quiten la escayola de la pierna, te invito a un ramen picante en Matsumoto.»\n\nSin embargo, al mirar de cerca el gotero colgado sobre su cabecera, notas una etiqueta manuscrita pegada sobre el envase de suero: «Lote Especial N-4». Un frío helado te recorre la espina dorsal."
        },
        {
            "id": "nursing_station",
            "name": "Estación de Enfermería Central",
            "x": 1020, "y": 260, "radius": 95,
            "icon": "📋",
            "tag": "REGISTRO",
            "color": "#f59e0b",
            "title": "Bandeja de Medicación de Sato",
            "text": "Sobre el mostrador de enfermería reposa la planilla de distribución horaria de la tarde.\n\nUna jeringa precargada y una ampolla de cristal ámbar están apartadas en una cubeta de acero inoxidable, rotuladas para Takahashi (Habitación 304) a las 18:00.\n\nAl lado, una circular interna advierte: «Suministro confidencial autorizado exclusivamente por jefatura quirúrgica del Dr. Moriyama»."
        },
        {
            "id": "pharmacy_depot",
            "name": "Depósito de Farmacia y Toxicología",
            "x": 1200, "y": 550, "radius": 95,
            "icon": "☣️",
            "tag": "ANOMALÍA",
            "color": "#ef4444",
            "title": "Armario de Fármacos de Restricción",
            "text": "El armario metálico de sustancias especiales tiene el precinto de seguridad violentado.\n\nEntre los analgésicos comunes divisas un frasco entreabierto con advertencias de toxicidad: «Tox-NB7: Reactivo bloqueador neuromuscular de parálisis respiratoria fulminante».\n\n¿Por qué hay un paralizante letal en un pabellón traumatológico ordinario? Tu pupila izquierda palpita con un ardor punzante al tocar el frío cristal."
        },
        {
            "id": "hallway_window",
            "name": "Ventanal Panorámico a la Tormenta",
            "x": 720, "y": 420, "radius": 95,
            "icon": "🌧️",
            "tag": "MEMORIA",
            "color": "#94a3b8",
            "title": "La Lluvia de Shinshu y el Pacto",
            "text": "Miras a través del cristal empapado por el temporal. La lluvia cae furiosa sobre las cordilleras alpinas de Shinshu, exactamente igual que aquella tarde en el paso de peatones de Matsumoto donde te arrojaste para salvar a Aoi.\n\nRecuerdas el sonido de neumáticos patinando y aquel susurro glacial en tu mente agonizante.\n\nTu ojo izquierdo no te dio una segunda oportunidad por compasión: te dio una sentencia para contemplar la muerte de cerca."
        },
        {
            "id": "dr_office",
            "name": "Despacho de Jefatura Quirúrgica",
            "x": 860, "y": 640, "radius": 95,
            "icon": "🚪",
            "tag": "JEFATURA",
            "color": "#e63946",
            "title": "La Frialdad del Dr. Moriyama",
            "text": "A través de la puerta entreabierta de caoba, divisas al Dr. Moriyama revisando un informe confidencial bajo una lámpara halógena.\n\nSu voz suena seca y glacial al teléfono: «Los pacientes del pabellón oeste deben mantenerse bajo monitoreo estricto. La administración de las dieciocho horas procederá conforme a la directiva». \n\nSus ojos se clavan un instante en los tuyos a través del pasillo con una frialdad que te hiela la sangre."
        }
    ]

    # -------------------------------------------------------------------------
    # DEFINICIÓN DE PISTAS Y SALAS: HOSPITAL GENERAL DE NAGANO (MUJER)
    # -------------------------------------------------------------------------
    HOSPITAL_AREAS_AOI = [
        {
            "id": "yuna_bed",
            "name": "Habitación 201 • Camilla de Yuna",
            "x": 440, "y": 270, "radius": 95,
            "icon": "🛏️",
            "tag": "COMPAÑERA",
            "color": "#c084fc",
            "title": "Yuna Sasaki y el Temor a la Discusión",
            "text": "Yuna está sentada en su cama, abrazando sus rodillas con la mirada clavada en la puerta.\n\n«Aoi... mi padre vendrá esta tarde. Siempre dice que mis recaídas y mis gastos médicos están destruyendo a la familia. Tengo miedo de que vuelva a gritarme y perder el control...»\n\nSu respiración temblorosa refleja una angustia desgarradora que te recuerda al dolor silencioso que tú misma soportas."
        },
        {
            "id": "bathroom_mirror",
            "name": "Lavabo y Espejo Causal",
            "x": 380, "y": 580, "radius": 95,
            "icon": "🪞",
            "tag": "EVENTO NEXUS",
            "color": "#a855f7",
            "title": "El Reflejo Premonitorio Distorsionado",
            "text": "Te acercas al lavabo del corredor. Al abrir el grifo, el vapor sobre el espejo comienza a ondularse como agua hirviendo con un brillo amatista sobrenatural.\n\nPor un segundo espeluznante, divisas en el reflejo la sombra de Yuna cayendo de espaldas y un reguero espeso de sangre carmesí extendiéndose por las baldosas.\n\nLa premonición es inminente. El destino fatal está a punto de ejecutarse."
        },
        {
            "id": "nursing_chart",
            "name": "Puesto Médico y Expediente Clínico",
            "x": 1020, "y": 260, "radius": 95,
            "icon": "📋",
            "tag": "EXPEDIENTE",
            "color": "#f59e0b",
            "title": "Historial de Aoi: Seis Meses de Coma",
            "text": "Lees disimuladamente tu expediente médico sobre el mostrador:\n\n«Paciente: Aoi Kazama, 17 años. Despertar tras casi medio año de coma postraumático. Estado: Depresión severa y riesgo alto de autolesión tras notificársele el suicidio de su hermano Shinshu Kazama, ocurrido un mes antes de su despertar».\n\nEl pecho te arde de culpa: Shinshu se quitó la vida pensando que tú jamás despertarías."
        },
        {
            "id": "broken_stand",
            "name": "Rincón del Corredor • Soporte Roto",
            "x": 620, "y": 320, "radius": 95,
            "icon": "⚠️",
            "tag": "OBJETO LETAL",
            "color": "#ef4444",
            "title": "La Varilla Metálica Puntiaguda",
            "text": "Junto al rodapié metálico divisas un antiguo soporte de suero desmontado y quebrado.\n\nUna varilla de acero oxidada y afilada sobresale a escasos centímetros del suelo, apuntando hacia arriba como una bayoneta oculta.\n\nSi alguien es empujado con fuerza en esa dirección durante un forcejeo... la caída resultaría mortal en el acto."
        },
        {
            "id": "rooftop_window",
            "name": "Ventanal Sur • Vista a la Azotea",
            "x": 860, "y": 640, "radius": 95,
            "icon": "🌧️",
            "tag": "MEMORIA",
            "color": "#94a3b8",
            "title": "El Salto que Quebró a la Familia",
            "text": "Contemplas la cornisa del edificio este a través de los cristales batidos por la lluvia.\n\nAllí fue donde tu hermano Shinshu pasó sus últimos días sumido en el remordimiento antes de saltar al vacío.\n\nUna lágrima quema tu mejilla, pero en tu corazón nace una determinación de acero: «Shinshu murió por no poder salvarme... Yo no permitiré que nadie más muera ante mis ojos»."
        }
    ]

    def get_hospital_areas(perspective):
        areas = HOSPITAL_AREAS_AOI if perspective == "mujer" else HOSPITAL_AREAS_SHINSHU
        default_color = "#c084fc" if perspective == "mujer" else "#e63946"
        for a in areas:
            if "color" not in a or not a["color"]:
                a["color"] = default_color
            if "icon" not in a:
                a["icon"] = "✦"
            if "name" not in a:
                a["name"] = "Área Hospitalaria"
            if "radius" not in a:
                a["radius"] = 95
            if "tag" not in a:
                a["tag"] = "PISTA"
            if "title" not in a:
                a["title"] = "Expediente"
            if "text" not in a:
                a["text"] = "Sin observaciones adicionales."
        return areas

    def get_nearest_hospital_area(perspective, px, py):
        areas = get_hospital_areas(perspective)
        for a in areas:
            ax = a.get("x", 0)
            ay = a.get("y", 0)
            rad = a.get("radius", 95)
            dist = ((ax - px) ** 2 + (ay - py) ** 2) ** 0.5
            if dist <= rad:
                return a
        return None

    def move_hospital_player(dx, dy, facing, perspective):
        global hospital_pos_x, hospital_pos_y, hospital_player_facing
        hospital_player_facing = facing

        new_x = hospital_pos_x + dx
        new_y = hospital_pos_y + dy

        # Delimitación y colisiones con los muros del pabellón
        min_x, max_x = 360, 1260
        min_y, max_y = 220, 680

        hospital_pos_x = max(min_x, min(max_x, new_x))
        hospital_pos_y = max(min_y, min(max_y, new_y))
        renpy.restart_interaction()

    def teleport_and_inspect_area(area, perspective):
        global hospital_pos_x, hospital_pos_y
        if area:
            hospital_pos_x = area.get("x", hospital_pos_x)
            hospital_pos_y = area.get("y", hospital_pos_y)
            inspect_hospital_area(area)

    def inspect_hospital_area(area):
        global hospital_modal_clue, hospital_investigated
        if area:
            hospital_modal_clue = area
            area_id = area.get("id", "")
            if area_id:
                hospital_investigated.add(area_id)
            tag = area.get("tag", "")
            if "NEXUS" in tag or "ANOMALÍA" in tag or "OBJETO" in tag:
                renpy.play("audio/eye_vision.wav")
            else:
                renpy.play("audio/heartbeat.wav")
            renpy.restart_interaction()

    def close_hospital_modal():
        global hospital_modal_clue
        hospital_modal_clue = None
        renpy.restart_interaction()


## =============================================================================
## PANTALLA PRINCIPAL DE EXPLORACIÓN 2D DEL HOSPITAL
## =============================================================================
screen hospital_2d_exploration(perspective="hombre"):
    modal True
    tag menu

    $ current_areas = get_hospital_areas(perspective)
    $ near_area = get_nearest_hospital_area(perspective, hospital_pos_x, hospital_pos_y)
    $ is_male = (perspective != "mujer")
    $ theme_tint = "#e63946" if is_male else "#c084fc"
    $ progress_count = len([a for a in current_areas if a.get("id") in hospital_investigated])
    $ total_count = len(current_areas)
    $ can_continue = (progress_count >= 2)

    # Controles por Teclado: Arriba, Abajo, Izquierda, Derecha (WASD y Flechas)
    key "K_UP" action Function(move_hospital_player, 0, -32, "up", perspective)
    key "w" action Function(move_hospital_player, 0, -32, "up", perspective)
    key "W" action Function(move_hospital_player, 0, -32, "up", perspective)

    key "K_DOWN" action Function(move_hospital_player, 0, 32, "down", perspective)
    key "s" action Function(move_hospital_player, 0, 32, "down", perspective)
    key "S" action Function(move_hospital_player, 0, 32, "down", perspective)

    key "K_LEFT" action Function(move_hospital_player, -32, 0, "left", perspective)
    key "a" action Function(move_hospital_player, -32, 0, "left", perspective)
    key "A" action Function(move_hospital_player, -32, 0, "left", perspective)

    key "K_RIGHT" action Function(move_hospital_player, 32, 0, "right", perspective)
    key "d" action Function(move_hospital_player, 32, 0, "right", perspective)
    key "D" action Function(move_hospital_player, 32, 0, "right", perspective)

    # Teclas de Interacción / Inspección
    if near_area and not hospital_modal_clue:
        key "K_SPACE" action Function(inspect_hospital_area, near_area)
        key "K_RETURN" action Function(inspect_hospital_area, near_area)
        key "e" action Function(inspect_hospital_area, near_area)
        key "E" action Function(inspect_hospital_area, near_area)

    add "#03060c"

    # --- ENCABEZADO SUPERIOR DEL PABELLÓN ---
    frame:
        xfill True
        ysize 88
        background Solid("#070b16f2")
        padding (32, 14, 32, 14)

        hbox:
            xfill True
            yalign 0.5

            hbox:
                spacing 16
                yalign 0.5
                text ("♂ LÍNEA CARMESÍ" if is_male else "♀ LÍNEA AMATISTA"):
                    font gui.interface_text_font
                    size 14
                    bold True
                    color theme_tint
                    yalign 0.5

                text "•":
                    color "#475569"
                    yalign 0.5

                text ("HOSPITAL GENERAL DE SHINSHU (PABELLÓN OESTE - 17:45)" if is_male else "HOSPITAL GENERAL DE NAGANO (PLANTA SEGUNDA - MEDIANOCHE)"):
                    font gui.name_text_font
                    size 17
                    color "#f8fafc"
                    bold True
                    yalign 0.5

            # Contador de progreso de investigación
            hbox:
                spacing 12
                yalign 0.5
                frame:
                    background Solid("#111827")
                    padding (14, 6, 14, 6)
                    hbox:
                        spacing 8
                        text "EXPEDIENTES DESCUBIERTOS:":
                            font gui.interface_text_font
                            size 11
                            color "#94a3b8"
                            bold True
                        text (str(progress_count) + " / " + str(total_count)):
                            font gui.interface_text_font
                            size 13
                            bold True
                            color theme_tint

    # --- PLANO ARQUITECTÓNICO 2D DEL HOSPITAL (TABLERO DE EXPLORACIÓN) ---
    frame:
        xalign 0.5
        yalign 0.51
        xsize 1380
        ysize 690
        background Frame(Solid("#080d1af0"), 8, 8)
        padding (20, 20, 20, 20)

        fixed:
            xfill True
            yfill True

            # Salas y zonas delimitadas en el mapa 2D
            # Sala 1: Habitación de Internación (Noroeste)
            frame:
                xpos 340
                ypos 190
                xsize 280
                ysize 180
                background Solid("#0e1628d0")
                text ("HABITACIÓN 304" if is_male else "HABITACIÓN 201"):
                    size 11
                    color "#64748b"
                    xalign 0.5
                    ypos 8
                    bold True

            # Sala 2: Pasillo Central y Ventanales (Centro)
            frame:
                xpos 640
                ypos 330
                xsize 220
                ysize 200
                background Solid("#121b30d0")
                text "CORREDOR Y VENTANALES":
                    size 10
                    color "#64748b"
                    xalign 0.5
                    ypos 8
                    bold True

            # Sala 3: Estación de Enfermería (Noreste)
            frame:
                xpos 900
                ypos 190
                xsize 260
                ysize 180
                background Solid("#0f1b2bd0")
                text "ESTACIÓN DE ENFERMERÍA":
                    size 11
                    color "#64748b"
                    xalign 0.5
                    ypos 8
                    bold True

            # Sala 4: Lavabos / Aislamiento (Suroeste)
            frame:
                xpos 340
                ypos 490
                xsize 260
                ysize 180
                background Solid("#11152bd0")
                text ("LAVABOS Y PABELLÓN OESTE" if is_male else "LAVABO Y ESPEJO PREMONITORIO"):
                    size 10
                    color "#64748b"
                    xalign 0.5
                    ypos 8
                    bold True

            # Sala 5: Farmacia / Despacho de Jefatura (Sureste)
            frame:
                xpos 800
                ypos 490
                xsize 360
                ysize 180
                background Solid("#1e131cd0" if is_male else "#1a1024d0")
                text ("JEFATURA MÉDICA Y FARMACIA" if is_male else "DESPACHO Y ARCHIVO"):
                    size 11
                    color "#64748b"
                    xalign 0.5
                    ypos 8
                    bold True

            # RENDER DE CADA PUNTO DE INTERÉS (HOTSPOTS TÁCTILES)
            # Permite hacer clic o tocar con el dedo en celular para caminar directamente a la sala e investigarla
            for area in current_areas:
                $ is_found = (area.get("id") in hospital_investigated)
                $ spot_color = "#10b981" if is_found else area.get("color", theme_tint)
                $ ax = area.get("x", 500)
                $ ay = area.get("y", 300)

                button:
                    xpos (ax - 42)
                    ypos (ay - 42)
                    xsize 84
                    ysize 84
                    background Frame(Solid(spot_color + "30"), 8, 8)
                    hover_background Frame(Solid(spot_color + "80"), 8, 8)
                    # Al tocar en celular o hacer clic, el personaje camina hacia la sala y la investiga
                    action Function(teleport_and_inspect_area, area, perspective)

                    vbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 2
                        text area.get("icon", "✦"):
                            size 26
                            xalign 0.5
                        text ("✔" if is_found else "✦"):
                            size 12
                            color spot_color
                            bold True
                            xalign 0.5

                # Etiqueta de la sala
                text area.get("name", "Sala"):
                    xpos ax
                    ypos (ay + 46)
                    xanchor 0.5
                    font gui.interface_text_font
                    size 10
                    color ("#a7f3d0" if is_found else "#cbd5e1")
                    bold True

            # RENDER DEL AVATAR DEL JUGADOR EN 2D
            frame:
                xpos (hospital_pos_x - 30)
                ypos (hospital_pos_y - 30)
                xsize 60
                ysize 60
                background Frame(Solid(theme_tint + "40"), 30, 30)

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 1

                    text ("▲" if hospital_player_facing == "up" else ("▼" if hospital_player_facing == "down" else ("◀" if hospital_player_facing == "left" else "▶"))):
                        size 12
                        color "#ffffff"
                        bold True
                        xalign 0.5

                    text ("♂" if is_male else "♀"):
                        size 22
                        bold True
                        color theme_tint
                        xalign 0.5

            # Nombre sobre la cabeza del jugador
            text (("SHINSHU" if is_male else "AOI") + " (TÚ)"):
                xpos hospital_pos_x
                ypos (hospital_pos_y - 48)
                xanchor 0.5
                font gui.interface_text_font
                size 10
                bold True
                color "#f8fafc"
                outlines [(1, "#000000ee", 0, 0)]

            # Alerta interactiva flotante cuando el jugador está cerca de una pista
            if near_area and not hospital_modal_clue:
                frame:
                    xpos hospital_pos_x
                    ypos (hospital_pos_y + 44)
                    xanchor 0.5
                    background Frame(Solid("#111827fa"), 6, 6)
                    padding (12, 6, 12, 6)

                    textbutton _("[[ E / ESPACIO ]] INVESTIGAR") substitute False:
                        action Function(inspect_hospital_area, near_area)
                        text_font gui.interface_text_font
                        text_size 11
                        text_bold True
                        text_color theme_tint

    # --- BARRA INFERIOR DE CONTROLES ADAPTADA A CELULARES Y PC ---
    frame:
        xfill True
        ysize 115
        yalign 1.0
        background Solid("#050811f6")
        padding (30, 10, 30, 10)

        hbox:
            xfill True
            yalign 0.5

            # CRUCETA TÁCTIL VIRTUAL PARA CELULARES Y MOUSE
            hbox:
                spacing 6
                yalign 0.5

                text "MÓVIL / TÁCTIL:":
                    font gui.interface_text_font
                    size 11
                    color "#64748b"
                    bold True
                    yalign 0.5

                button:
                    action Function(move_hospital_player, -32, 0, "left", perspective)
                    background Solid("#1e293b")
                    hover_background Solid("#334155")
                    padding (14, 10, 14, 10)
                    text "◀ A":
                        size 13
                        color "#e2e8f0"
                        bold True

                button:
                    action Function(move_hospital_player, 0, -32, "up", perspective)
                    background Solid("#1e293b")
                    hover_background Solid("#334155")
                    padding (14, 10, 14, 10)
                    text "▲ W":
                        size 13
                        color "#e2e8f0"
                        bold True

                button:
                    action Function(move_hospital_player, 0, 32, "down", perspective)
                    background Solid("#1e293b")
                    hover_background Solid("#334155")
                    padding (14, 10, 14, 10)
                    text "▼ S":
                        size 13
                        color "#e2e8f0"
                        bold True

                button:
                    action Function(move_hospital_player, 32, 0, "right", perspective)
                    background Solid("#1e293b")
                    hover_background Solid("#334155")
                    padding (14, 10, 14, 10)
                    text "▶ D":
                        size 13
                        color "#e2e8f0"
                        bold True

                # Botón de Acción Táctil en Celular
                if near_area:
                    button:
                        action Function(inspect_hospital_area, near_area)
                        background Solid(theme_tint)
                        hover_background Solid("#10b981")
                        padding (16, 10, 16, 10)
                        text "🔍 INVESTIGAR":
                            size 13
                            color "#ffffff"
                            bold True

            # Guía de juego en pantalla
            vbox:
                yalign 0.5
                xalign 0.5
                spacing 2
                text _("• Teclado: [[W, A, S, D]] o [[Flechas]] para caminar • [[Espacio / E]] para investigar") substitute False:
                    font gui.interface_text_font
                    size 11
                    color "#94a3b8"
                text _("• Celular: Toca la cruceta táctil o toca directamente cualquier sala en el plano") substitute False:
                    font gui.interface_text_font
                    size 11
                    color "#38bdf8"

            # Botón de Continuar la Historia (se activa al encontrar 2 o más pistas)
            hbox:
                spacing 14
                yalign 0.5

                if can_continue:
                    textbutton _("CONTINUAR HISTORIA ▶"):
                        action Return()
                        text_font gui.interface_text_font
                        text_size 13
                        text_bold True
                        text_color "#ffffff"
                        background Solid(theme_tint)
                        hover_background Solid("#10b981")
                        padding (22, 12, 22, 12)
                else:
                    frame:
                        background Solid("#1e293b")
                        padding (16, 12, 16, 12)
                        text ("Investiga al menos 2 pistas (" + str(progress_count) + "/2)"):
                            font gui.interface_text_font
                            size 11
                            color "#64748b"
                            bold True


    # --- MODAL FLOTANTE DE DETALLE DE LA PISTA INVESTIGADA ---
    if hospital_modal_clue:
        $ clue_color = hospital_modal_clue.get("color", theme_tint)

        # Fondo translúcido que permite cerrar al tocar fuera
        button:
            xfill True
            yfill True
            background Solid("#000000ba")
            action Function(close_hospital_modal)

        frame:
            xalign 0.5
            yalign 0.5
            xsize 920
            background Frame(Solid("#0d1322fa"), 12, 12)
            padding (36, 30, 36, 30)

            vbox:
                spacing 16
                xfill True

                # Cabecera de la pista
                hbox:
                    xfill True
                    yalign 0.5

                    hbox:
                        spacing 12
                        yalign 0.5
                        text hospital_modal_clue.get("icon", "✦"):
                            size 28
                            yalign 0.5
                        vbox:
                            spacing 2
                            text hospital_modal_clue.get("name", "Área de Investigación"):
                                font gui.interface_text_font
                                size 12
                                bold True
                                color clue_color
                            text hospital_modal_clue.get("title", "Expediente"):
                                font gui.name_text_font
                                size 20
                                bold True
                                color "#f8fafc"

                    frame:
                        background Solid("#1e293b")
                        padding (10, 4, 10, 4)
                        yalign 0.5
                        text hospital_modal_clue.get("tag", "PISTA"):
                            font gui.interface_text_font
                            size 11
                            color "#e2e8f0"
                            bold True

                # Línea divisoria de acento
                frame:
                    xfill True
                    ysize 2
                    background Solid(clue_color)

                # Texto de la pista / diálogo
                text hospital_modal_clue.get("text", ""):
                    font gui.interface_text_font
                    size 14
                    color "#cbd5e1"
                    line_spacing 6

                null height 8

                # Botón de cierre del modal
                button:
                    action Function(close_hospital_modal)
                    xalign 1.0
                    background Solid(clue_color)
                    hover_background Solid("#334155")
                    padding (24, 10, 24, 10)
                    text "✕ SEGUIR EXPLORANDO [[ESC / TOCAR]]" substitute False:
                        font gui.interface_text_font
                        size 12
                        bold True
                        color "#ffffff"
