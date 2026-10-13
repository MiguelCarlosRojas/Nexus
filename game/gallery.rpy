## =============================================================================
## SISTEMA DE GALERÍA DE PERSONAJES Y EXPEDIENTES DINÁMICOS - NEXUS
## =============================================================================

default persistent.gallery_selected_char = None
default persistent.gallery_selected_img_idx = 0

init python:
    # Base de datos de Personajes según la perspectiva elegida en el Capítulo 1
    # Ruta Hombre (Perspectiva Shinshu Kazama)
    CHARACTERS_HOMBRE = [
        {
            "id": "shinshu",
            "name": "Shinshu Kazama (Ren)",
            "kanji": "風間 信州",
            "role": "Protagonista Principal",
            "role_detail": "Perspectiva Carmesí • Ojos del Destino",
            "status": "Sujeto Causal 01 • Consciencia Despierta",
            "quote": "«Mis ojos arden como brasas... No es un sueño ni un delirio febril: puedo ver el instante exacto en que la muerte los reclama.»",
            "thumb": "images/silueta_ren.png",
            "images": [
                "images/silueta_ren.png",
                "images/nexus_destino_mano_sangre.png"
            ],
            "image_labels": [
                "Silueta del Protagonista (Shinshu)",
                "Premonición Carmesí (Mano de Sangre)"
            ],
            "synopsis": "Joven de Nagano que sobrevive milagrosamente a un choque mortal. Al despertar del coma en el Hospital General de Chūbu, sus ojos adquieren el aterrador don de presenciar la muerte exacta de las personas antes de que suceda.",
            "routes": [
                {"title": "Decisión Janken con Aoi", "desc": "Elegir entre confiar en el instinto fraternal o activar la incandescente visión carmesí para anticipar la jugada."},
                {"title": "La Encrucijada de Kenji (18:00)", "desc": "1. Advertir directamente a Kenji (Rechazo y tragedia asfixiante).\n2. Guardar silencio por miedo a ser recluido como demente.\n3. Arrancarse las vías y alertar a los doctores jefes."}
            ]
        },
        {
            "id": "aoi_hermana",
            "name": "Aoi Kazama",
            "kanji": "風間 葵",
            "role": "Hermana Menor",
            "role_detail": "Familia Directa • Vínculo Emocional",
            "status": "Vigilia Hospitalaria • Compañera Devota",
            "quote": "«Hermano... por favor despierta. Traje nuestras partidas pendientes... prometiste que jugaríamos de nuevo como antes.»",
            "thumb": "images/Aoi.png",
            "images": [
                "images/Aoi.png",
                "images/aoi_de_pie_abrazandose.png",
                "images/aoi_de_pie_correa_bolso.png",
                "images/aoi_sentada_suelo.png",
                "images/aoi_sentada_piernas_desganadas.png",
                "images/aoi_sentada_costado_mano.png",
                "images/aoi_agachada_melancolica.png",
                "images/aoi_abrazando_rodillas.png",
                "images/aoi_arrodillada_desolada.png",
                "images/aoi_acurrucada_llorando_mano.png",
                "images/aoi_llorando_manga.png",
                "images/aoi_caminando_desanimada.png"
            ],
            "image_labels": [
                "Retrato Oficial (Vigilia)",
                "Preocupación Fraternal",
                "Espera en el Pasillo",
                "Desolación Silenciosa",
                "Cansancio Emocional",
                "Nostalgia Incontenible",
                "Tristeza Oculta",
                "Abrazo a la Soledad",
                "Ruego en Penumbra",
                "Lágrimas Contenidas",
                "Llanto en Silencio",
                "Partida Apesadumbrada"
            ],
            "synopsis": "Hermana menor devota que visita a Shinshu todos los días durante su coma. Trae consigo esperanza, recuerdos y una partida de Piedra, Papel o Tijera para comprobar si su hermano sigue siendo el mismo de siempre tras el accidente.",
            "routes": [
                {"title": "Ruta de la Promesa Fraternal", "desc": "Jugar limpiamente fortalece el vínculo familiar frente a la tragedia inminente."},
                {"title": "Ruta del Ojo Premonitorio", "desc": "Usar la visión anticipa sus dedos pero despierta el terror sobre el verdadero origen del don."}
            ]
        },
        {
            "id": "kenji_ogata",
            "name": "Dr. Kenji Ogata",
            "kanji": "尾形 健二",
            "role": "Compañero de Sala",
            "role_detail": "Paciente de Traumatología • Habitación 302",
            "status": "Vulnerable • Evento Crítico 18:00",
            "quote": "«Tranquilo, chico... solo es una ampolla para el dolor a las 18:00. Pronto saldremos de aquí los dos.»",
            "thumb": "images/silueta_kenji.png",
            "images": [
                "images/silueta_kenji.png"
            ],
            "image_labels": [
                "Registro Clínico de Kenji Ogata"
            ],
            "synopsis": "Paciente afable internado junto a Shinshu. Convencido de que su recuperación es inminente, ignora que una ampolla con toxina letal está programada para ser inyectada en su vía intravenosa exactamente a las 18:00.",
            "routes": [
                {"title": "Ruta Destino Trágico", "desc": "Kenji desestima la advertencia como una pesadilla de sedantes y fallece agónicamente por shock respiratorio."},
                {"title": "Ruta de Salvación Rápida", "desc": "Intervención de emergencia con el Dr. Moriyama para detener la dosis fatal antes de su administración."}
            ]
        },
        {
            "id": "moriyama",
            "name": "Dr. Moriyama",
            "kanji": "森山 医師",
            "role": "Médico Jefe",
            "role_detail": "Especialista en Traumatología y Urgencias",
            "status": "Personal Médico • En Turno de Guardia",
            "quote": "«En este hospital nos regimos por la ciencia médica, no por alucinaciones. Pero ningún médico puede ignorar una anomalía fatal confirmada.»",
            "thumb": "images/silueta_doctor.png",
            "images": [
                "images/silueta_doctor.png"
            ],
            "image_labels": [
                "Ficha Médica del Dr. Moriyama"
            ],
            "synopsis": "Especialista riguroso a cargo del pabellón. Su escepticismo inicial choca con las advertencias febriles de Shinshu, pero su deber profesional lo obliga a investigar cuando las pruebas se vuelven irrefutables.",
            "routes": [
                {"title": "Ruta de Auditoría Médica", "desc": "Revisa los frascos de infusión a tiempo y confirma la presencia de sustancias tóxicas en el sistema."}
            ]
        },
        {
            "id": "sato",
            "name": "Enfermera Sato",
            "kanji": "佐藤 看護師",
            "role": "Enfermera de Turno",
            "role_detail": "Pabellón 3 • Administración de Medicación",
            "status": "Involuntaria Portadora de Medicación",
            "quote": "«Es la ronda rutinaria de la tarde... Todo el instrumental y la medicación están preparados en la bandeja según la ficha.»",
            "thumb": "images/silueta_enfermera.png",
            "images": [
                "images/silueta_enfermera.png"
            ],
            "image_labels": [
                "Registro de Turno Vespertino"
            ],
            "synopsis": "Personal de enfermería asignado a administrar la medicación vespertina en la planta de traumatología. Cumple sus órdenes sin sospechar el peligro latente en la ampolla.",
            "routes": [
                {"title": "Ruta de las 18:00", "desc": "Portadora involuntaria de la bandeja con la jeringa contaminada programada para Kenji."}
            ]
        },
        {
            "id": "madre_kazama",
            "name": "Madre de Shinshu",
            "kanji": "風間 母親",
            "role": "Madre Protectora",
            "role_detail": "Familia Kazama • Soporte Vital",
            "status": "Vigilia Constante • En Sala de Espera",
            "quote": "«Dios mío, no me quites a mis hijos... Ya hemos sufrido bastante desde aquella noche en la carretera.»",
            "thumb": "images/silueta_madre.png",
            "images": [
                "images/silueta_madre.png"
            ],
            "image_labels": [
                "Fotografía Familiar en Guardia"
            ],
            "synopsis": "Madre abatida por el choque vehicular que busca desesperadamente proteger la estabilidad emocional y física de sus dos hijos en medio del dolor.",
            "routes": [
                {"title": "Vigilia en Sala de Espera", "desc": "Acompaña a Aoi y ruega incansablemente por la sanación de Shinshu tras el despertar."}
            ]
        }
    ]

    # Ruta Mujer (Perspectiva Aoi Kazama)
    CHARACTERS_MUJER = [
        {
            "id": "aoi_protagonista",
            "name": "Aoi Kazama",
            "kanji": "風間 葵",
            "role": "Protagonista Principal",
            "role_detail": "Perspectiva Amatista • Visión Premonitoria",
            "status": "Sujeto Causal 02 • Despertar tras 6 Meses",
            "quote": "«Seis meses de oscuridad... y al abrir los ojos, descubro que mi hermano ya no está. Y ahora el espejo me muestra la muerte antes de que ocurra.»",
            "thumb": "images/Aoi.png",
            "images": [
                "images/Aoi.png",
                "images/aoi_de_pie_abrazandose.png",
                "images/aoi_de_pie_correa_bolso.png",
                "images/aoi_sentada_suelo.png",
                "images/aoi_sentada_piernas_desganadas.png",
                "images/aoi_sentada_costado_mano.png",
                "images/aoi_agachada_melancolica.png",
                "images/aoi_abrazando_rodillas.png",
                "images/aoi_arrodillada_desolada.png",
                "images/aoi_acurrucada_llorando_mano.png",
                "images/aoi_llorando_manga.png",
                "images/aoi_caminando_desanimada.png",
                "images/nexus_destino_mariposa_rosa.png"
            ],
            "image_labels": [
                "Despertar tras Medio Año de Coma",
                "Shock Emocional y Trauma",
                "Búsqueda Desesperada de Respuestas",
                "Desesperación al Límite",
                "Postración en el Suelo",
                "Reflexión en Penumbras",
                "El Peso Devastador de la Culpa",
                "Aislamiento Traumatológico",
                "Angustia por Shinshu",
                "Lágrimas de Duelo",
                "Llanto Desgarrador",
                "Vagando por el Hospital",
                "Efecto Mariposa (El Destino)"
            ],
            "synopsis": "Despierta tras casi medio año (seis meses) de coma tras el accidente y se entera de la muerte de su hermano Shinshu ocurrida un mes antes. Consumida por la desolación y retenida en el hospital, descubre en el espejo del lavabo que puede ver la muerte antes de que ocurra.",
            "routes": [
                {"title": "Rama 1: Advertir a Yuna", "desc": "Le suplica a Yuna evitar la discusión con su padre; no le cree por su trauma y Yuna muere en el forcejeo."},
                {"title": "Rama 2: Retirar el Objeto Punzante", "desc": "Espera a la noche, retira el objeto letal bajo la cama; Yuna se salva pero Aoi es sedada y aislada."},
                {"title": "Rama 3: No Intervenir", "desc": "Cree que es solo un delirio febril; el destino se cumple de forma despiadada."}
            ]
        },
        {
            "id": "shinshu_eco",
            "name": "Shinshu Kazama",
            "kanji": "風間 信州",
            "role": "Hermano Mayor",
            "role_detail": "Eco del Pasado • Destino Trágico",
            "status": "Fallecido un mes antes del despertar de Aoi",
            "quote": "«La culpa me consume... no puedo seguir viviendo sabiendo lo que te ocurrió por mi culpa en aquel cruce.»",
            "thumb": "images/silueta_ren.png",
            "images": [
                "images/silueta_ren.png"
            ],
            "image_labels": [
                "Silueta Memorial de Shinshu Kazama"
            ],
            "synopsis": "El hermano mayor cuya culpa insoportable y rechazo tras el accidente lo llevaron a arrojarse desde la azotea del hospital un mes antes de que Aoi despertara, marcando su destino para siempre.",
            "routes": [
                {"title": "El Salto del Ángel Caído", "desc": "Tragedia ocurrida un mes antes del despertar de Aoi tras cinco meses de vigilia constante."}
            ]
        },
        {
            "id": "yuna_tachibana",
            "name": "Yuna Tachibana",
            "kanji": "立花 由菜",
            "role": "Compañera de Habitación",
            "role_detail": "Paciente de Recuperación • Habitación 305",
            "status": "En Peligro Causal Inminente",
            "quote": "«Papá nunca me escucha... cree que todo esto es una excusa para desobedecer a la familia. No entiende nada.»",
            "thumb": "images/silueta_enfermera.png",
            "images": [
                "images/silueta_enfermera.png"
            ],
            "image_labels": [
                "Expediente de Ingreso de Yuna Tachibana"
            ],
            "synopsis": "Joven paciente cuya tensa relación con su padre desencadena un forcejeo mortal presenciado en premonición en el espejo por Aoi.",
            "routes": [
                {"title": "El Reflejo del Lavabo", "desc": "Aoi presencia cómo cae mortalmente sobre un objeto cortante durante una discusión paterna."}
            ]
        },
        {
            "id": "padre_yuna_char",
            "name": "Sr. Tachibana",
            "kanji": "立花 父親",
            "role": "Padre de Yuna",
            "role_detail": "Familiar Responsable • Visita Conflictiva",
            "status": "Catalizador de la Tragedia",
            "quote": "«¡Ya basta de rebeldías, Yuna! Vas a firmar el alta médica y regresar a casa de inmediato.»",
            "thumb": "images/silueta_doctor.png",
            "images": [
                "images/silueta_doctor.png"
            ],
            "image_labels": [
                "Identificación de Visitante Autorizado"
            ],
            "synopsis": "Hombre severo y distante cuya violenta recriminación en el cuarto del hospital precipita la catástrofe contra el objeto punzante.",
            "routes": [
                {"title": "Visita Fatal de la Tarde", "desc": "Llega a exigir explicaciones sin saber que su empujón terminará en tragedia irreversible."}
            ]
        },
        {
            "id": "madre_aoi",
            "name": "Madre de Aoi",
            "kanji": "風間 母親",
            "role": "Madre Desconsolada",
            "role_detail": "Familia Kazama • Dolor en Silencio",
            "status": "Portadora de la Verdad",
            "quote": "«Aoi... perdóname por ocultártelo estos días... Shinshu... tu hermano ya no está con nosotros...»",
            "thumb": "images/silueta_madre.png",
            "images": [
                "images/silueta_madre.png"
            ],
            "image_labels": [
                "Ficha de Visita de Madre de Aoi"
            ],
            "synopsis": "Madre devastada que debe comunicarle a Aoi el destino trágico de su hermano al despertar tras seis meses de coma profundo.",
            "routes": [
                {"title": "La Revelación en la Cama", "desc": "Sostiene las manos de Aoi mientras le confiesa entre lágrimas la muerte de Shinshu."}
            ]
        }
    ]

    def get_gallery_characters():
        if persistent.selected_gender == "mujer":
            return CHARACTERS_MUJER
        else:
            return CHARACTERS_HOMBRE

    def get_current_gallery_char():
        chars = get_gallery_characters()
        if not chars:
            return None
        for c in chars:
            if c["id"] == persistent.gallery_selected_char:
                return c
        persistent.gallery_selected_char = chars[0]["id"]
        persistent.gallery_selected_img_idx = 0
        return chars[0]

    def select_gallery_char(char_id):
        persistent.gallery_selected_char = char_id
        persistent.gallery_selected_img_idx = 0
        renpy.restart_interaction()

    def set_gallery_img_idx(idx):
        persistent.gallery_selected_img_idx = idx
        renpy.restart_interaction()

    def prev_gallery_img():
        cur = get_current_gallery_char()
        if cur and cur.get("images"):
            total = len(cur["images"])
            if total > 1:
                persistent.gallery_selected_img_idx = (persistent.gallery_selected_img_idx - 1) % total
                renpy.restart_interaction()

    def next_gallery_img():
        cur = get_current_gallery_char()
        if cur and cur.get("images"):
            total = len(cur["images"])
            if total > 1:
                persistent.gallery_selected_img_idx = (persistent.gallery_selected_img_idx + 1) % total
                renpy.restart_interaction()


## =============================================================================
## PANTALLA DE GALERÍA DE PERSONAJES Y EXPEDIENTES (REDISEÑO PREMIUM)
## =============================================================================

screen character_gallery():

    tag menu

    use game_menu(_("Galería de Personajes"), scroll=None):

        $ is_mujer = (persistent.selected_gender == "mujer")
        $ theme_accent = "#c084fc" if is_mujer else "#fb7185"
        $ theme_border = persistent.theme_border or ("#a855f7" if is_mujer else "#f43f5e")
        $ theme_bg = persistent.theme_color or ("#3b0764" if is_mujer else "#4c0519")
        $ current_chars = get_gallery_characters()
        $ cur_char = get_current_gallery_char()

        vbox:
            spacing 14
            xfill True

            # -----------------------------------------------------------------
            # 1. CABECERA EXPANDIDA: EXPEDIENTE NEXUS Y ESTADO CAUSAL
            # -----------------------------------------------------------------
            frame:
                xfill True
                background Frame(Solid("#090e1cf5"), 8, 8)
                padding (22, 12, 22, 12)

                hbox:
                    xfill True
                    yalign 0.5

                    hbox:
                        spacing 14
                        yalign 0.5

                        # Insignia de Género / Perspectiva
                        frame:
                            background Frame(Solid(theme_bg), 6, 6)
                            padding (10, 4, 10, 4)
                            yalign 0.5
                            text ("♀ LÍNEA AMATISTA" if is_mujer else "♂ LÍNEA CARMESÍ"):
                                font gui.interface_text_font
                                size 12
                                bold True
                                color "#ffffff"

                        vbox:
                            spacing 2
                            text ("ARCHIVOS CLÍNICOS • PERSPECTIVA DE AOI KAZAMA" if is_mujer else "ARCHIVOS CLÍNICOS • PERSPECTIVA DE SHINSHU KAZAMA"):
                                font gui.interface_text_font
                                size 14
                                bold True
                                color "#f8fafc"
                                kerning 1

                            text ("Expedientes de personajes interactivos y destinos causales del Capítulo 1"):
                                font gui.interface_text_font
                                size 11
                                color "#94a3b8"

                    # Estado de desbloqueo a la derecha
                    hbox:
                        spacing 16
                        yalign 0.5

                        frame:
                            background Frame(Solid("#0f172a"), 4, 4)
                            padding (12, 5, 12, 5)
                            text ("PERSONAJES REGISTRADOS: " + str(len(current_chars))):
                                font gui.interface_text_font
                                size 11
                                bold True
                                color "#38bdf8"

                        frame:
                            background Frame(Solid("#0f172a"), 4, 4)
                            padding (12, 5, 12, 5)
                            text "CAPÍTULO 1 • SINCRONIZADO":
                                font gui.interface_text_font
                                size 11
                                bold True
                                color "#10b981"

            # -----------------------------------------------------------------
            # 2. SELECTOR HORIZONTAL DE PERSONAJES (TARJETAS ESTILIZADAS)
            # -----------------------------------------------------------------
            frame:
                xfill True
                background Frame(Solid("#070b16f8"), 8, 8)
                padding (12, 10, 12, 10)

                hbox:
                    spacing 12
                    xalign 0.0

                    for c in current_chars:
                        $ is_selected = (cur_char and cur_char["id"] == c["id"])

                        button:
                            action Function(select_gallery_char, c["id"])
                            xsize 215
                            ysize 84
                            padding (10, 6, 10, 6)
                            background Frame(Solid(theme_bg if is_selected else "#0f172acc"), 6, 6)
                            hover_background Frame(Solid("#1e293bcc"), 6, 6)

                            hbox:
                                spacing 10
                                yalign 0.5

                                # Avatar con marco reactivo
                                frame:
                                    background Frame(Solid("#050811"), 4, 4)
                                    padding (3, 3, 3, 3)
                                    xsize 48
                                    ysize 68
                                    yalign 0.5

                                    add c["thumb"]:
                                        fit "contain"
                                        xsize 42
                                        ysize 62
                                        xalign 0.5
                                        yalign 0.5

                                vbox:
                                    spacing 2
                                    yalign 0.5
                                    xsize 135

                                    text c["name"].split()[0]:
                                        font gui.interface_text_font
                                        size 14
                                        bold True
                                        color ("#ffffff" if is_selected else "#e2e8f0")

                                    text c["kanji"]:
                                        font gui.interface_text_font
                                        size 10
                                        color (theme_accent if is_selected else "#94a3b8")

                                    text c.get("role", "Personaje"):
                                        font gui.interface_text_font
                                        size 9
                                        color ("#cbd5e1" if is_selected else "#64748b")

            # -----------------------------------------------------------------
            # 3. CUERPO PRINCIPAL DIVIDIDO: VISOR DE FOTOS + EXPEDIENTE Y RUTAS
            # -----------------------------------------------------------------
            if cur_char:
                $ total_imgs = len(cur_char["images"])
                $ cur_idx = min(persistent.gallery_selected_img_idx, total_imgs - 1)
                $ current_display_img = cur_char["images"][cur_idx]
                $ current_img_label = cur_char["image_labels"][cur_idx] if ("image_labels" in cur_char and cur_idx < len(cur_char["image_labels"])) else ("Registro " + str(cur_idx + 1))

                hbox:
                    xfill True
                    spacing 18

                    # ---------------------------------------------------------
                    # PANEL IZQUIERDO: VISOR DE IMÁGENES / SPRITES PREMIUM
                    # ---------------------------------------------------------
                    frame:
                        xsize 510
                        ysize 630
                        background Frame(Solid("#080c18f8"), 8, 8)
                        padding (16, 14, 16, 14)

                        vbox:
                            xfill True
                            yfill True
                            spacing 8

                            # Encabezado del visor
                            hbox:
                                xfill True
                                yalign 0.5
                                text "VISOR DE RETRATO":
                                    font gui.interface_text_font
                                    size 11
                                    bold True
                                    color "#94a3b8"
                                    kerning 2

                                text ("ARCHIVO " + str(cur_idx + 1).zfill(2) + " / " + str(total_imgs).zfill(2)):
                                    font gui.interface_text_font
                                    size 11
                                    bold True
                                    color theme_accent

                            # Marco central de la ilustración
                            frame:
                                xfill True
                                ysize 470
                                background Frame(Solid("#03050dfc"), 6, 6)
                                padding (10, 10, 10, 10)

                                add current_display_img:
                                    xalign 0.5
                                    yalign 0.5
                                    fit "contain"
                                    xsize 470
                                    ysize 450

                            # Etiqueta descriptiva del retrato actual
                            frame:
                                xfill True
                                background Frame(Solid("#0c1220ee"), 4, 4)
                                padding (8, 5, 8, 5)

                                text ("◈ " + current_img_label):
                                    font gui.interface_text_font
                                    size 11
                                    bold True
                                    color theme_accent
                                    xalign 0.5

                            # Controles inferiores si tiene más de 1 imagen
                            if total_imgs > 1:
                                hbox:
                                    xalign 0.5
                                    spacing 8
                                    yalign 0.5

                                    # Botón Anterior
                                    button:
                                        action Function(prev_gallery_img)
                                        xsize 80
                                        ysize 30
                                        background Frame(Solid("#1e293b"), 4, 4)
                                        hover_background Frame(Solid(theme_bg), 4, 4)
                                        text "◀ Anterior":
                                            size 10
                                            bold True
                                            color "#e2e8f0"
                                            xalign 0.5
                                            yalign 0.5

                                    # Mini chips para selección directa rápida
                                    viewport:
                                        xsize 280
                                        ysize 30
                                        scrollbars None
                                        mousewheel True
                                        draggable True
                                        hbox:
                                            spacing 5
                                            yalign 0.5
                                            for idx, img_path in enumerate(cur_char["images"]):
                                                $ is_img_sel = (idx == cur_idx)
                                                button:
                                                    action Function(set_gallery_img_idx, idx)
                                                    xsize 24
                                                    ysize 24
                                                    background Frame(Solid(theme_bg if is_img_sel else "#141c2e"), 3, 3)
                                                    hover_background Frame(Solid(theme_border), 3, 3)
                                                    text str(idx + 1):
                                                        size 10
                                                        bold True
                                                        color ("#ffffff" if is_img_sel else "#94a3b8")
                                                        xalign 0.5
                                                        yalign 0.5

                                    # Botón Siguiente
                                    button:
                                        action Function(next_gallery_img)
                                        xsize 80
                                        ysize 30
                                        background Frame(Solid("#1e293b"), 4, 4)
                                        hover_background Frame(Solid(theme_bg), 4, 4)
                                        text "Siguiente ▶":
                                            size 10
                                            bold True
                                            color "#e2e8f0"
                                            xalign 0.5
                                            yalign 0.5

                            else:
                                text "✦ Ilustración Oficial Única en Archivo ✦":
                                    font gui.interface_text_font
                                    size 10
                                    color "#64748b"
                                    xalign 0.5

                    # ---------------------------------------------------------
                    # PANEL DERECHO: DOSSIER CLÍNICO, SINOPSIS Y RUTAS
                    # ---------------------------------------------------------
                    frame:
                        xsize 840
                        ysize 630
                        background Frame(Solid("#080c18f8"), 8, 8)
                        padding (24, 20, 24, 20)

                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            draggable True

                            vbox:
                                spacing 16
                                xsize 790

                                # Cabecera de Identificación
                                vbox:
                                    spacing 4
                                    hbox:
                                        spacing 12
                                        yalign 0.5

                                        text cur_char["name"]:
                                            font gui.name_text_font
                                            size 26
                                            bold True
                                            color theme_accent

                                        frame:
                                            background Frame(Solid("#1e293b"), 4, 4)
                                            padding (8, 2, 8, 2)
                                            yalign 0.5
                                            text cur_char["kanji"]:
                                                size 12
                                                color "#cbd5e1"

                                    hbox:
                                        spacing 10
                                        yalign 0.5

                                        text cur_char.get("role_detail", cur_char.get("role", "")):
                                            font gui.interface_text_font
                                            size 12
                                            color "#94a3b8"
                                            bold True

                                        text "•":
                                            size 12
                                            color "#475569"

                                        text cur_char.get("status", "Registrado"):
                                            font gui.interface_text_font
                                            size 11
                                            color "#38bdf8"

                                # Cita / Reflexión del personaje
                                if "quote" in cur_char and cur_char["quote"]:
                                    frame:
                                        xfill True
                                        background Frame(Solid("#0b1222b0"), 6, 6)
                                        padding (14, 10, 14, 10)
                                        text cur_char["quote"]:
                                            font gui.interface_text_font
                                            size 12
                                            italic True
                                            color "#cbd5e1"
                                            line_spacing 4

                                # Separador
                                frame:
                                    xfill True
                                    ysize 1
                                    background "#1e293b"

                                # SECCIÓN 1: BIOGRAFÍA Y SINOPSIS
                                vbox:
                                    spacing 6

                                    hbox:
                                        spacing 8
                                        yalign 0.5
                                        text "📁":
                                            size 12
                                        text "EXPEDIENTE BIOGRÁFICO Y CLÍNICO":
                                            font gui.interface_text_font
                                            size 12
                                            bold True
                                            color "#cbd5e1"
                                            kerning 2

                                    frame:
                                        xfill True
                                        background Frame(Solid("#0d1424f0"), 6, 6)
                                        padding (16, 14, 16, 14)
                                        text cur_char["synopsis"]:
                                            size 13
                                            color "#e2e8f0"
                                            line_spacing 6

                                # SECCIÓN 2: ENCRUCIJADAS Y DESTINOS DEL JUGADOR
                                vbox:
                                    spacing 8

                                    hbox:
                                        spacing 8
                                        yalign 0.5
                                        text "🦋":
                                            size 12
                                        text "RAMIFICACIONES Y DESTINOS (EFECTO MARIPOSA)":
                                            font gui.interface_text_font
                                            size 12
                                            bold True
                                            color theme_accent
                                            kerning 2

                                    text "Decisiones que determinan la vida o muerte de este personaje en el Capítulo 1:":
                                        font gui.interface_text_font
                                        size 11
                                        color "#64748b"

                                    for r in cur_char["routes"]:
                                        frame:
                                            xfill True
                                            background Frame(Solid("#0f172ae8"), 6, 6)
                                            padding (14, 10, 14, 10)

                                            vbox:
                                                spacing 4
                                                hbox:
                                                    spacing 6
                                                    yalign 0.5
                                                    text "◈":
                                                        size 12
                                                        color theme_accent
                                                    text r["title"]:
                                                        size 13
                                                        bold True
                                                        color "#f8fafc"

                                                text r["desc"]:
                                                    size 12
                                                    color "#94a3b8"
                                                    line_spacing 4

                                # NOTA INFORMATIVA FINAL DEL SISTEMA NEXUS
                                frame:
                                    xfill True
                                    background Frame(Solid("#050811e0"), 4, 4)
                                    padding (12, 8, 12, 8)
                                    text "Archivo Causal Nexus sincronizado con el registro de decisiones del jugador en el Hospital General de Chūbu.":
                                        font gui.interface_text_font
                                        size 10
                                        italic True
                                        color "#64748b"
                                        xalign 0.5
