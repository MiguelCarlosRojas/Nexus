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
            "role": "Protagonista Principal (Perspectiva Carmesí)",
            "thumb": "images/silueta_ren.png",
            "images": [
                "images/silueta_ren.png",
                "images/nexus_destino_mano_sangre.png"
            ],
            "synopsis": "Joven de Nagano que sobrevive milagrosamente a un choque mortal. Al despertar del coma en el Hospital General de Chūbu, sus ojos adquieren el aterrador don de presenciar la muerte exacta de las personas antes de que suceda.",
            "routes": [
                {"title": "Decisión Janken con Aoi", "desc": "Elegir entre confiar en su instinto fraternal o usar la incandescente visión carmesí para anticipar la jugada."},
                {"title": "La Encrucijada de Kenji (18:00)", "desc": "1. Advertir directamente a Kenji (Rechazo y tragedia asfixiante).\n2. Guardar silencio por miedo a ser recluido como demente.\n3. Arrancarse las vías y alertar a los doctores jefes."}
            ]
        },
        {
            "id": "aoi_hermana",
            "name": "Aoi Kazama",
            "kanji": "風間 葵",
            "role": "Hermana Menor de Shinshu",
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
            "synopsis": "Hermana menor devota que visita a Shinshu todos los días durante su coma. Trae consigo esperanza, recuerdos y una partida de Piedra, Papel o Tijera para comprobar si su hermano sigue siendo el mismo de siempre.",
            "routes": [
                {"title": "Ruta de la Promesa Fraternal", "desc": "Jugar limpiamente fortalece el vínculo familiar frente a la tragedia que se avecina."},
                {"title": "Ruta del Ojo Premonitorio", "desc": "Usar la visión anticipa sus dedos pero despierta el terror sobre el verdadero origen del don."}
            ]
        },
        {
            "id": "kenji_ogata",
            "name": "Dr. Kenji Ogata",
            "kanji": "尾形 健二",
            "role": "Compañero de Habitación del Hospital",
            "thumb": "images/silueta_kenji.png",
            "images": [
                "images/silueta_kenji.png"
            ],
            "synopsis": "Paciente afable internado junto a Shinshu. Convencido de que su recuperación es inminente, ignora que una ampolla letal con toxina letal está programada para ser inyectada en su vía a las 18:00.",
            "routes": [
                {"title": "Ruta Destino Trágico", "desc": "Kenji desestima la advertencia como una pesadilla de sedantes y fallece agónicamente por shock respiratorio."},
                {"title": "Ruta de Salvación Rápida", "desc": "Intervención de emergencia con el Dr. Moriyama para detener la dosis fatal."}
            ]
        },
        {
            "id": "moriyama",
            "name": "Dr. Moriyama",
            "kanji": "森山 医師",
            "role": "Médico Jefe de Urgencias",
            "thumb": "images/silueta_doctor.png",
            "images": [
                "images/silueta_doctor.png"
            ],
            "synopsis": "Especialista riguroso a cargo del pabellón. Su escepticismo inicial choca con las advertencias febriles de Shinshu.",
            "routes": [
                {"title": "Ruta de Auditoría Médica", "desc": "Revisa los frascos de infusión a tiempo y confirma la presencia de sustancias tóxicas."}
            ]
        },
        {
            "id": "sato",
            "name": "Enfermera Sato",
            "kanji": "佐藤 看護師",
            "role": "Enfermera de Turno",
            "thumb": "images/silueta_enfermera.png",
            "images": [
                "images/silueta_enfermera.png"
            ],
            "synopsis": "Personal de enfermería asignado a administrar la medicación vespertina en la planta de traumatología.",
            "routes": [
                {"title": "Ruta de las 18:00", "desc": "Portadora involuntaria de la bandeja con la jeringa contaminada."}
            ]
        },
        {
            "id": "madre_kazama",
            "name": "Madre de Shinshu",
            "kanji": "風間 母親",
            "role": "Madre Protectora",
            "thumb": "images/silueta_madre.png",
            "images": [
                "images/silueta_madre.png"
            ],
            "synopsis": "Madre abatida por el accidente que busca desesperadamente proteger la estabilidad emocional de sus dos hijos.",
            "routes": [
                {"title": "Vigilia en Sala de Espera", "desc": "Acompaña a Aoi y ruega por la sanación de Shinshu."}
            ]
        }
    ]

    # Ruta Mujer (Perspectiva Aoi Kazama)
    CHARACTERS_MUJER = [
        {
            "id": "aoi_protagonista",
            "name": "Aoi Kazama",
            "kanji": "風間 葵",
            "role": "Protagonista Principal (Perspectiva Amatista)",
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
            "synopsis": "Despierta tras casi medio año (seis meses) de coma tras el accidente y se entera de la muerte de su hermano Shinshu ocurrida un mes antes. Consumida por la desolación y retenida en el hospital, descubre en el espejo del lavabo que puede ver la muerte antes de que ocurra.",
            "routes": [
                {"title": "Rama 1: Advertir a Yuna", "desc": "Le suplica a Yuna evitar la discusión con su padre; no le cree por su trauma y Yuna muere en el forcejeo."},
                {"title": "Rama 2: Retirar el Objeto Punzante", "desc": "Espera a la noche, retira el objeto letal bajo la cama; Yuna se salva pero Aoi es sedada y aislada."},
                {"title": "Rama 3: No Intervenir", "desc": "Cree que es solo un delirio; el destino se cumple de forma despiadada."}
            ]
        },
        {
            "id": "shinshu_eco",
            "name": "Shinshu Kazama",
            "kanji": "風間 信州",
            "role": "Hermano Mayor (Eco del Pasado)",
            "thumb": "images/silueta_ren.png",
            "images": [
                "images/silueta_ren.png"
            ],
            "synopsis": "El hermano mayor cuya culpa insoportable y rechazo tras el accidente lo llevaron a arrojarse desde la azotea un mes antes de que Aoi despertara, marcando su destino para siempre.",
            "routes": [
                {"title": "El Salto del Ángel Caído", "desc": "Tragedia ocurrida un mes antes del despertar de Aoi tras cinco meses de vigilia."}
            ]
        },
        {
            "id": "yuna_tachibana",
            "name": "Yuna Tachibana",
            "kanji": "立花 由菜",
            "role": "Compañera de Habitación de Aoi",
            "thumb": "images/silueta_enfermera.png",
            "images": [
                "images/silueta_enfermera.png"
            ],
            "synopsis": "Joven paciente cuya tensa relación con su padre desencadena un forcejeo mortal presenciado en premonición por Aoi.",
            "routes": [
                {"title": "El Reflejo del Lavabo", "desc": "Aoi presencia cómo cae mortalmente sobre un objeto cortante durante una discusión paterna."}
            ]
        },
        {
            "id": "padre_yuna_char",
            "name": "Sr. Tachibana",
            "kanji": "立花 父親",
            "role": "Padre de Yuna",
            "thumb": "images/silueta_doctor.png",
            "images": [
                "images/silueta_doctor.png"
            ],
            "synopsis": "Hombre severo y distante cuya violenta recriminación en el cuarto del hospital precipita la catástrofe.",
            "routes": [
                {"title": "Visita Fatal de la Tarde", "desc": "Llega a exigir explicaciones sin saber que su empujón terminará en tragedia."}
            ]
        },
        {
            "id": "madre_aoi",
            "name": "Madre de Aoi",
            "kanji": "風間 母親",
            "role": "Madre Desconsolada",
            "thumb": "images/silueta_madre.png",
            "images": [
                "images/silueta_madre.png"
            ],
            "synopsis": "Madre devastada que debe comunicarle a Aoi el destino de su hermano al despertar del coma.",
            "routes": [
                {"title": "La Revelación en la Cama", "desc": "Sostiene las manos de Aoi mientras le confiesa entre lágrimas la verdad."}
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
        if not persistent.gallery_selected_char:
            persistent.gallery_selected_char = chars[0]["id"]
        for c in chars:
            if c["id"] == persistent.gallery_selected_char:
                return c
        return chars[0]

    def select_gallery_char(char_id):
        persistent.gallery_selected_char = char_id
        persistent.gallery_selected_img_idx = 0
        renpy.restart_interaction()

    def set_gallery_img_idx(idx):
        persistent.gallery_selected_img_idx = idx
        renpy.restart_interaction()

## Pantalla de Galería de Personajes y Expedientes
screen character_gallery():

    tag menu

    use game_menu(_("Galería de Personajes"), scroll=None):

        $ current_chars = get_gallery_characters()
        $ cur_char = get_current_gallery_char()

        vbox:
            spacing 16
            xsize 1160

            # --- CABECERA DE PERSPECTIVA ACTIVA ---
            frame:
                xfill True
                background Frame(Solid("#0d121fe8"), 8, 8)
                padding (20, 12, 20, 12)
                hbox:
                    xfill True
                    yalign 0.5
                    hbox:
                        spacing 12
                        yalign 0.5
                        text ("♀" if persistent.selected_gender == "mujer" else "♂"):
                            size 24
                            bold True
                            color (persistent.theme_border or "#e63946")
                            yalign 0.5
                        vbox:
                            spacing 2
                            text ("EXPEDIENTES • RUTA DE LA MUJER (AOI KAZAMA)" if persistent.selected_gender == "mujer" else "EXPEDIENTES • RUTA DEL HOMBRE (SHINSHU KAZAMA)"):
                                font gui.interface_text_font
                                size 13
                                bold True
                                color "#f8fafc"
                            text ("Personajes interactivos y ramificaciones del Capítulo 1"):
                                font gui.interface_text_font
                                size 10
                                color "#94a3b8"

                    # Selector rápido de perspectiva para explorar la otra historia
                    hbox:
                        spacing 10
                        yalign 0.5
                        text "Filtrar por:":
                            font gui.interface_text_font
                            size 11
                            color "#64748b"
                            yalign 0.5
                        textbutton "Hombre":
                            action [Function(set_protagonist_gender, "hombre"), Function(select_gallery_char, "shinshu")]
                            selected (persistent.selected_gender != "mujer")
                            style "pref_tab_btn"
                        textbutton "Mujer":
                            action [Function(set_protagonist_gender, "mujer"), Function(select_gallery_char, "aoi_protagonista")]
                            selected (persistent.selected_gender == "mujer")
                            style "pref_tab_btn"

            # --- SELECTOR HORIZONTAL DE PERSONAJES ---
            frame:
                xfill True
                background Frame(Solid("#0a0e1af0"), 8, 8)
                padding (16, 12, 16, 12)

                hbox:
                    spacing 14
                    xalign 0.0

                    for c in current_chars:
                        $ is_selected = (cur_char and cur_char["id"] == c["id"])
                        button:
                            action Function(select_gallery_char, c["id"])
                            xsize 175
                            ysize 90
                            padding (8, 6, 8, 6)
                            background Frame(Solid(persistent.theme_color if is_selected else "#141a29b0"), 6, 6)
                            hover_background Frame(Solid(persistent.theme_hover or "#3b1319f0"), 6, 6)

                            hbox:
                                spacing 10
                                yalign 0.5
                                add c["thumb"]:
                                    ysize 74
                                    xsize 56
                                    fit "contain"
                                    yalign 0.5
                                vbox:
                                    yalign 0.5
                                    spacing 2
                                    text c["name"].split()[0]:
                                        size 13
                                        bold True
                                        color ("#ffffff" if is_selected else "#e2e8f0")
                                    text c["kanji"]:
                                        size 10
                                        color ("#ffffffcc" if is_selected else "#94a3b8")

            # --- CUERPO PRINCIPAL DIVIDIDO: IZQUIERDA (IMÁGENES) / DERECHA (SINOPSIS Y RUTAS) ---
            if cur_char:
                $ total_imgs = len(cur_char["images"])
                $ cur_idx = min(persistent.gallery_selected_img_idx, total_imgs - 1)
                $ current_display_img = cur_char["images"][cur_idx]

                hbox:
                    xfill True
                    spacing 20

                    # 1. PANEL IZQUIERDO: VISOR DE IMÁGENES / SPRITES DEL PERSONAJE
                    frame:
                        xsize 480
                        ysize 570
                        background Frame(Solid("#080c16f2"), 8, 8)
                        padding (16, 16, 16, 16)

                        vbox:
                            xfill True
                            yfill True
                            spacing 10

                            # Marco de la imagen actual
                            frame:
                                xfill True
                                ysize 460
                                background Frame(Solid("#04060bf0"), 6, 6)
                                padding (10, 10, 10, 10)

                                add current_display_img:
                                    xalign 0.5
                                    yalign 0.5
                                    fit "contain"
                                    xsize 440
                                    ysize 440

                            # Miniaturas inferiores si el personaje tiene múltiples imágenes
                            if total_imgs > 1:
                                hbox:
                                    xalign 0.5
                                    spacing 8
                                    for idx, img_path in enumerate(cur_char["images"]):
                                        $ is_img_sel = (idx == cur_idx)
                                        button:
                                            action Function(set_gallery_img_idx, idx)
                                            xsize 32
                                            ysize 32
                                            background Frame(Solid(persistent.theme_color if is_img_sel else "#1e293b"), 4, 4)
                                            text str(idx + 1):
                                                size 12
                                                bold True
                                                color ("#ffffff" if is_img_sel else "#94a3b8")
                                                xalign 0.5
                                                yalign 0.5
                            else:
                                text "Ilustración oficial del personaje":
                                    font gui.interface_text_font
                                    size 11
                                    color "#64748b"
                                    xalign 0.5

                    # 2. PANEL DERECHO: NOMBRE, SINOPSIS Y RUTAS POR DECISIONES
                    frame:
                        xsize 660
                        ysize 570
                        background Frame(Solid("#080c16f2"), 8, 8)
                        padding (26, 22, 26, 22)

                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            draggable True

                            vbox:
                                spacing 16
                                xsize 600

                                # Cabecera de nombre
                                vbox:
                                    spacing 2
                                    text cur_char["name"]:
                                        font gui.name_text_font
                                        size 26
                                        bold True
                                        color (persistent.theme_border or "#f87171")
                                    hbox:
                                        spacing 10
                                        text cur_char["kanji"]:
                                            size 14
                                            color "#94a3b8"
                                        text "•":
                                            size 14
                                            color "#475569"
                                        text cur_char["role"]:
                                            size 12
                                            color "#cbd5e1"
                                            bold True

                                frame:
                                    xfill True
                                    ysize 1
                                    background "#1e293b"

                                # Sección 1: Sinopsis del personaje
                                vbox:
                                    spacing 6
                                    text "SINOPSIS DEL PERSONAJE":
                                        font gui.interface_text_font
                                        size 12
                                        bold True
                                        color "#94a3b8"
                                        kerning 2

                                    frame:
                                        xfill True
                                        background Frame(Solid("#0d121ff0"), 6, 6)
                                        padding (16, 14, 16, 14)
                                        text cur_char["synopsis"]:
                                            size 14
                                            color "#e2e8f0"
                                            line_spacing 5

                                # Sección 2: Rutas y Decisiones del Usuario
                                vbox:
                                    spacing 10
                                    text "RUTAS Y ENCRUCIJADAS TOMADAS":
                                        font gui.interface_text_font
                                        size 12
                                        bold True
                                        color (persistent.theme_border or "#c084fc")
                                        kerning 2

                                    for r in cur_char["routes"]:
                                        frame:
                                            xfill True
                                            background Frame(Solid("#0f172ae8"), 6, 6)
                                            padding (16, 12, 16, 12)
                                            vbox:
                                                spacing 4
                                                text "◆ " + r["title"]:
                                                    size 13
                                                    bold True
                                                    color "#f8fafc"
                                                text r["desc"]:
                                                    size 12
                                                    color "#94a3b8"
                                                    line_spacing 4
