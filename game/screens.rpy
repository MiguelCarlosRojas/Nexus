################################################################################
## Inicialización
################################################################################

init offset = -1


################################################################################
## Estilos
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize 10
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", Borders(0, 8, 0, 8), tile=False)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", Borders(0, 8, 0, 8), tile=False)
    unscrollable gui.unscrollable

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Pantallas internas del juego
################################################################################


## Pantalla de diálogo #########################################################
##
## La pantalla de diálogo muestra el diálogo al jugador. Acepta dos parámetros,
## 'who' y 'what', es decir, el nombre del personaje que habla y el texto que ha
## de ser mostrado respectivamente. (El parámetro 'who' puede ser 'None' si no
## se da ningún nombre.)
##
## Esta pantalla debe crear un texto visualizable con id "what" que Ren'Py usa
## para gestionar la visualización del texto. Puede crear también visualizables
## con id "who" y id "window" para aplicar propiedades de estilo.
##
## https://www.renpy.org/doc/html/screen_special.html#say

## Animación de pulso para el indicador de diálogo (CTC)
transform ctc_pulse:
    alpha 0.35
    easein 0.65 alpha 1.0 yoffset 2
    easeout 0.65 alpha 0.35 yoffset 0
    repeat

screen say(who, what):

    window:
        id "window"
        style "say_window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who" style "say_label"

        text what id "what" style "say_dialogue"

        # Indicador de continuación de línea de diálogo (CTC)
        add "gui/ctc.png":
            at ctc_pulse
            xalign 0.965
            yalign 0.82

    ## Si hay una imagen lateral, la muestra encima del texto. No la muestra en
    ## la variante de teléfono - no hay lugar.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Permite que el 'namebox' pueda ser estilizado en el objeto 'Character'.
init python:
    config.character_id_prefixes.append('namebox')

style say_window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style say_window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    font gui.name_text_font
    size gui.name_text_size
    bold True
    color "#f8fafc"
    outlines [(1, "#020617ee", 0, 0), (2, "#0f172a66", 0, 0)]
    xalign 0.0
    yalign 0.5
    xoffset 8

style say_dialogue:
    font gui.text_font
    size gui.text_size
    color gui.text_color
    outlines [(1, "#00000088", 0, 0)]
    line_spacing 6

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

style say_thought:
    italic True
    color "#cbd5e1"

## Pantalla de introducción de texto ###########################################
##
## Pantalla usada para visualizar 'renpy.input'. El parámetro 'prompt' se usa
## para pasar el texto presentado.
##
## Esta pantalla debe crear un displayable 'input' con id "input" para aceptar
## diversos parámetros de entrada.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Pantalla de menú ############################################################
##
## Esta pantallla presenta las opciones internas al juego de la sentencia
## 'menu'. El parámetro único, 'items', es una lista de objetos, cada uno los
## campos 'caption' y 'action'.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    $ timeout_val = get_choice_timeout(items)
    $ is_urgent = (timeout_val <= 2.5)

    # Temporizador de inactividad inteligente: selecciona automáticamente al expirar
    timer timeout_val action Function(auto_select_choice, items)

    vbox:
        xalign 0.5
        yalign 0.42
        spacing 20

        # --- CABECERA DE DECISIÓN Y BARRA DE TIEMPO ELEGANTE ---
        frame:
            xalign 0.5
            xsize 940
            background Frame(Solid("#080c16ea"), 8, 8)
            padding (24, 14, 24, 14)

            vbox:
                spacing 10
                xfill True

                hbox:
                    xfill True
                    yalign 0.5

                    # Título de encrucijada y estado
                    hbox:
                        spacing 12
                        yalign 0.5
                        text ("⚡" if is_urgent else "⏳"):
                            size 16
                            color ("#ef4444" if is_urgent else "#38bdf8")
                            yalign 0.5
                        text ("LÍMITE CRÍTICO DE REACCIÓN" if is_urgent else "DESTINO EN DISPUTA"):
                            font gui.interface_text_font
                            size 13
                            bold True
                            color ("#f87171" if is_urgent else "#e2e8f0")
                            kerning 2
                            yalign 0.5

                    # Contador digital de tiempo restante
                    frame:
                        background Frame(Solid("#111827d0"), 4, 4)
                        padding (12, 4, 12, 4)
                        yalign 0.5
                        hbox:
                            spacing 6
                            yalign 0.5
                            text "TIEMPO:":
                                font gui.interface_text_font
                                size 10
                                color "#94a3b8"
                                bold True
                                yalign 0.5
                            text ("[timeout_val:.0f]s"):
                                font gui.interface_text_font
                                size 12
                                bold True
                                color ("#ef4444" if is_urgent else "#38bdf8")
                                yalign 0.5

                # Marco de la barra de tiempo fluida
                frame:
                    xfill True
                    ysize 10
                    background Frame(Solid("#0f172a"), 5, 5)
                    padding (2, 2, 2, 2)

                    bar:
                        xfill True
                        ysize 6
                        value AnimatedValue(0.0, range=1.0, delay=timeout_val, old_value=1.0)
                        left_bar Frame(Solid("#ef4444" if is_urgent else (persistent.theme_color or "#c084fc")), 3, 3)
                        right_bar Solid("#00000000")
                        thumb None

        # --- OPCIONES DE DECISIÓN ---
        vbox:
            xalign 0.5
            spacing 14

            for i in items:
                textbutton i.caption:
                    action i.action
                    style "nexus_choice_btn"


style nexus_choice_btn is gui_button:
    xsize 940
    padding (36, 16, 36, 16)
    xalign 0.5
    background Frame("gui/button/choice_idle_background.png", 8, 8)
    hover_background Frame("gui/button/choice_hover_background.png", 8, 8)

style nexus_choice_btn_text is gui_button_text:
    size 17
    bold True
    color "#e2e8f0"
    hover_color "#ffffff"
    xalign 0.5
    yalign 0.5


## Pantalla de menú rápido #####################################################
##
## El menú rápido se presenta en el juego para ofrecer fácil acceso a los menus
## externos al juego.

screen quick_menu():

    ## Pantalla de menú rápido deshabilitada conforme a la preferencia visual del usuario
    zorder 100
    pass


## Este código asegura que la pantalla 'quick_menu' se muestra en el juego,
## mientras el jugador no haya escondido explícitamente la interfaz.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style nexus_quick_bar_frame:
    xalign 0.5
    yalign 0.985
    padding (14, 5, 14, 5)
    background Frame(Solid("#0a0e19c0"), 6, 6)

style nexus_quick_btn is gui_button:
    padding (12, 4, 12, 4)
    background Frame("gui/custom_btn/pill_idle.png", 4, 4)
    hover_background Frame("gui/custom_btn/pill_hover.png", 4, 4)
    selected_background Frame("gui/custom_btn/pill_selected.png", 4, 4)

style nexus_quick_btn_text is gui_button_text:
    size 12
    bold True
    color "#94a3b8"
    hover_color "#ffffff"
    selected_color (persistent.theme_color or "#e63946")


################################################################################
## Personalización Dinámica de Tema y Barra de Navegación Lateral
################################################################################

default persistent.janken_wins = 0
default persistent.janken_losses = 0
default persistent.janken_draws = 0

default persistent.selected_gender = None
default persistent.theme_name = "Carmesí"
default persistent.theme_color = "#b82626"
default persistent.theme_hover = "#501217ee"
default persistent.theme_border = "#9e1b1b"
default persistent.text_size_choice = 33
default persistent.font_choice = "DejaVuSans.ttf"
default persistent.font_choice_name = "Estándar"
default persistent.screen_shake = True
default persistent.flash_effects = True
default persistent.ambient_particles = True
default persistent.auto_save_choices = True
default persistent.textbox_alpha = 0.90
default persistent.achievement_filter = "Todos"
default persistent.achievement_search = ""

init python:
    def set_theme(name):
        persistent.theme_name = name
        if name == "Carmesí":
            persistent.theme_color = "#b82626"
            persistent.theme_hover = "#501217ee"
            persistent.theme_border = "#9e1b1b"
            gui.accent_color = "#b82626"
            gui.hover_color = "#e63946"
        elif name == "Amatista Sakura":
            persistent.theme_color = "#9333ea"
            persistent.theme_hover = "#581c87ee"
            persistent.theme_border = "#c084fc"
            gui.accent_color = "#9333ea"
            gui.hover_color = "#f472b6"
        elif name == "Azul Noche":
            persistent.theme_color = "#1d4ed8"
            persistent.theme_hover = "#14254dee"
            persistent.theme_border = "#2563eb"
            gui.accent_color = "#2563eb"
            gui.hover_color = "#60a5fa"
        elif name == "Oro Shinshu":
            persistent.theme_color = "#b45309"
            persistent.theme_hover = "#42280dee"
            persistent.theme_border = "#d97706"
            gui.accent_color = "#d97706"
            gui.hover_color = "#fbbf24"
        elif name == "Jade Imperial":
            persistent.theme_color = "#047857"
            persistent.theme_hover = "#0d3625ee"
            persistent.theme_border = "#059669"
            gui.accent_color = "#059669"
            gui.hover_color = "#34d399"
        renpy.restart_interaction()

    def set_protagonist_gender(gender):
        persistent.selected_gender = gender
        if gender == "mujer":
            set_theme("Amatista Sakura")
            if not persistent.player_nickname or persistent.player_nickname == "Shinshu Kazama":
                persistent.player_nickname = "Aoi Kazama"
        else:
            set_theme("Carmesí")
            if not persistent.player_nickname or persistent.player_nickname == "Aoi Kazama":
                persistent.player_nickname = "Shinshu Kazama"
        renpy.restart_interaction()

    def auto_select_protagonist():
        import random
        if persistent.selected_gender is None:
            count_h = len([aid for aid in (persistent.unlocked_achievements or []) if get_achievement_by_id(aid) and get_achievement_by_id(aid).get("gender") == "hombre"])
            count_m = len([aid for aid in (persistent.unlocked_achievements or []) if get_achievement_by_id(aid) and get_achievement_by_id(aid).get("gender") == "mujer"])
            if count_m > count_h:
                chosen = "mujer"
            elif count_h > count_m:
                chosen = "hombre"
            else:
                chosen = random.choice(["hombre", "mujer"])
            set_protagonist_gender(chosen)
        renpy.return_statement()

    def get_choice_timeout(items):
        """Calcula el tiempo del temporizador: 2.0s si es decisión rápida/urgente, 4.0s si es reflexiva."""
        if not items:
            return 4.0
        # Palabras clave de urgencia/reflejos inmediatos
        urgent_keywords = ["limpiamente", "concentrarte", "reflejos", "rápido", "rapido", "instinto", "intuitivo", "janken", "puño", "puno", "reaccionar"]
        for it in items:
            cap = (getattr(it, "caption", "") or "").lower()
            if any(k in cap for k in urgent_keywords):
                return 2.0
        return 4.0

    def auto_select_choice(items):
        """Selecciona automáticamente una opción tras expirar el temporizador de inactividad,
        basándose en logros, nivel de experiencia y selección pseudoaleatoria balanceada."""
        import random
        if not items:
            return

        unlocked = set(persistent.unlocked_achievements or [])
        user_xp = get_total_player_xp()

        # Ponderación dinámica basada en la afinidad del jugador
        scored_items = []
        for it in items:
            cap = (getattr(it, "caption", "") or "").lower()
            weight = 10.0

            # 1. Influencia por logros previos desbloqueados
            # Si el jugador ha demostrado valentía o premonición en logros anteriores
            if "ojo_premonicion" in unlocked or "espejo_premonicion" in unlocked:
                if any(w in cap for w in ["concentrarte", "visión", "vision", "ojo", "retirar", "advertir", "filo"]):
                    weight += 15.0
            if "janken_victoria" in unlocked or "salvar_kenji" in unlocked:
                if any(w in cap for w in ["limpiamente", "advertir", "alertar", "retirar"]):
                    weight += 12.0
            if "tragedia_kenji" in unlocked:
                if any(w in cap for w in ["silencio", "ignorar", "callar"]):
                    weight += 5.0

            # 2. Experiencia acumulada (los jugadores de mayor nivel tienden a tomar acción directa)
            if user_xp >= 50:
                if any(w in cap for w in ["advertir", "retirar", "concentrarte", "alertar"]):
                    weight += 8.0

            # 3. Variabilidad pseudoaleatoria balanceada
            weight += random.uniform(1.0, 6.0)
            scored_items.append((weight, it))

        # Ordenar por puntaje ponderado descendente
        scored_items.sort(key=lambda x: x[0], reverse=True)
        chosen_item = scored_items[0][1]

        if hasattr(chosen_item, "action") and chosen_item.action:
            renpy.run(chosen_item.action)

    def set_dialogue_size(size):
        persistent.text_size_choice = size
        gui.text_size = size
        renpy.restart_interaction()

    def set_font_choice(font_name, display_name):
        persistent.font_choice = font_name
        persistent.font_choice_name = display_name
        gui.text_font = font_name
        renpy.restart_interaction()

    def toggle_screen_shake():
        persistent.screen_shake = not persistent.screen_shake
        renpy.restart_interaction()

    def toggle_flash_effects():
        persistent.flash_effects = not persistent.flash_effects
        renpy.restart_interaction()

    def toggle_ambient_particles():
        persistent.ambient_particles = not persistent.ambient_particles
        renpy.restart_interaction()

    def toggle_auto_save_choices():
        persistent.auto_save_choices = not persistent.auto_save_choices
        renpy.restart_interaction()

    def set_textbox_opacity(opacity):
        persistent.textbox_alpha = opacity
        renpy.restart_interaction()

    def set_music_volume_level(val):
        _preferences.set_volume('music', val)
        renpy.restart_interaction()

    def set_sfx_volume_level(val):
        _preferences.set_volume('sfx', val)
        renpy.restart_interaction()

    def set_achieve_filter(filter_name):
        persistent.achievement_filter = filter_name
        renpy.restart_interaction()

    def join_ranking():
        join_ranking_action()


## Pantalla de navegación ######################################################
screen navigation():

    # Panel lateral profesional de diseño japonés (450px x 1080px)
    frame:
        style "sidebar_navigation_panel"

        # Contenedor central vertical equilibrado
        vbox:
            xalign 0.5
            yalign 0.5
            xsize 400
            spacing 16

            # --- CABECERA DE LA BARRA LATERAL ---
            vbox:
                xalign 0.5
                spacing 6

                add "images/nexus_logo.png":
                    xalign 0.5
                    ysize 92
                    fit "contain"

                text "CHŪBU CENTRAL • SHINSHU REGION":
                    font gui.interface_text_font
                    size 10
                    color "#757f93"
                    xalign 0.5
                    kerning 3

            # Separador estético sutil
            null height 2

            # --- BOTONES DE ACCIÓN (CON ICONOS MÁS GRANDES: 24px) ---
            vbox:
                spacing 8
                xalign 0.5

                if main_menu:
                    button:
                        action Start()
                        style "nav_icon_button"
                        hbox:
                            spacing 18
                            yalign 0.5
                            add "gui/icons/icon_play.png" yalign 0.5 ysize 24 fit "contain"
                            text _("Iniciar Historia") style "nav_icon_text"
                else:
                    button:
                        action ShowMenu("history")
                        style "nav_icon_button"
                        hbox:
                            spacing 18
                            yalign 0.5
                            add "gui/icons/icon_history.png" yalign 0.5 ysize 24 fit "contain"
                            text _("Historial") style "nav_icon_text"

                    button:
                        action ShowMenu("save")
                        style "nav_icon_button"
                        hbox:
                            spacing 18
                            yalign 0.5
                            add "gui/icons/icon_save.png" yalign 0.5 ysize 24 fit "contain"
                            text _("Guardar Partida") style "nav_icon_text"

                button:
                    action ShowMenu("load")
                    style "nav_icon_button"
                    hbox:
                        spacing 18
                        yalign 0.5
                        add "gui/icons/icon_load.png" yalign 0.5 ysize 24 fit "contain"
                        text _("Cargar Partida") style "nav_icon_text"

                button:
                    action ShowMenu("preferences")
                    style "nav_icon_button"
                    hbox:
                        spacing 18
                        yalign 0.5
                        add "gui/icons/icon_settings.png" yalign 0.5 ysize 24 fit "contain"
                        text _("Configuración") style "nav_icon_text"

                button:
                    action ShowMenu("achievements")
                    style "nav_icon_button"
                    hbox:
                        spacing 18
                        yalign 0.5
                        add "gui/icons/icon_achievements.png" yalign 0.5 ysize 24 fit "contain"
                        text _("Logros y Nivel") style "nav_icon_text"

                # Solo se visualizan tras completar el Capítulo 1
                if getattr(persistent, "completed_chapter_1", False):
                    button:
                        action ShowMenu("character_gallery")
                        style "nav_icon_button"
                        hbox:
                            spacing 18
                            yalign 0.5
                            add "gui/icons/icon_gallery.png" yalign 0.5 ysize 24 fit "contain"
                            text _("Galería") style "nav_icon_text"

                    button:
                        action ShowMenu("alternate_routes")
                        style "nav_icon_button"
                        hbox:
                            spacing 18
                            yalign 0.5
                            add "gui/icons/icon_routes.png" yalign 0.5 ysize 24 fit "contain"
                            text _("Líneas Alternas") style "nav_icon_text"

                if _in_replay:
                    button:
                        action EndReplay(confirm=True)
                        style "nav_icon_button"
                        hbox:
                            spacing 18
                            yalign 0.5
                            add "gui/icons/icon_quit.png" yalign 0.5 ysize 24 fit "contain"
                            text _("Fin Repetición") style "nav_icon_text"

                elif not main_menu:
                    button:
                        action MainMenu()
                        style "nav_icon_button"
                        hbox:
                            spacing 18
                            yalign 0.5
                            add "gui/icons/icon_return.png" yalign 0.5 ysize 24 fit "contain"
                            text _("Menú Principal") style "nav_icon_text"

                button:
                    action ShowMenu("about")
                    style "nav_icon_button"
                    hbox:
                        spacing 18
                        yalign 0.5
                        add "gui/icons/icon_about.png" yalign 0.5 ysize 24 fit "contain"
                        text _("Acerca de") style "nav_icon_text"

                if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                    button:
                        action ShowMenu("help")
                        style "nav_icon_button"
                        hbox:
                            spacing 18
                            yalign 0.5
                            add "gui/icons/icon_help.png" yalign 0.5 ysize 24 fit "contain"
                            text _("Ayuda") style "nav_icon_text"

                if renpy.variant("pc"):
                    button:
                        action Quit(confirm=not main_menu)
                        style "nav_icon_button"
                        hbox:
                            spacing 18
                            yalign 0.5
                            add "gui/icons/icon_quit.png" yalign 0.5 ysize 24 fit "contain"
                            text _("Salir del Juego") style "nav_icon_text"

            # Espaciado suave inferior
            null height 2

            # --- PIE DE PÁGINA ---
            if not main_menu:
                button:
                    action Return()
                    style "nav_return_friendly"
                    hbox:
                        spacing 14
                        xalign 0.5
                        yalign 0.5
                        add "gui/icons/icon_return.png" yalign 0.5 ysize 24 fit "contain"
                        text _("Volver a la Historia") style "nav_return_friendly_text"
            else:
                vbox:
                    xalign 0.5
                    spacing 3
                    text "HOSPITAL GENERAL DE SHINSHU":
                        size 10
                        color "#646d7e"
                        xalign 0.5
                        kerning 1.5
                    text "TEMA ACTIVO: [persistent.theme_name]":
                        size 9
                        color (persistent.theme_border or "#9e1b1b")
                        xalign 0.5
                        kerning 1


style sidebar_navigation_panel:
    xpos 0
    ypos 0
    xsize 450
    ysize 1080
    background Frame(Solid("#090b10f5"), 0, 0)
    padding (25, 25, 25, 25)

style nav_icon_button is gui_button:
    xsize 380
    ysize 48
    xalign 0.5
    padding (20, 8, 20, 8)
    background Frame(Solid("#131622b8"), 6, 6)
    hover_background Frame(Solid(persistent.theme_hover or "#3b1319f0"), 6, 6)
    selected_background Frame(Solid(persistent.theme_color or "#8b1818"), 6, 6)

style nav_icon_text is gui_button_text:
    font gui.interface_text_font
    size 16
    color "#cad0dc"
    hover_color "#ffffff"
    selected_color "#ffffff"
    yalign 0.5

style nav_return_friendly is gui_button:
    xsize 380
    ysize 48
    xalign 0.5
    padding (20, 8, 20, 8)
    background Frame(Solid("#261118f0"), 6, 6)
    hover_background Frame(Solid("#4a141ffa"), 6, 6)

style nav_return_friendly_text is gui_button_text:
    font gui.interface_text_font
    size 16
    color "#ff9e9e"
    hover_color "#ffffff"
    bold True
    yalign 0.5


## Pantalla de Selección de Protagonista (Hombre / Mujer) ########################
## Pantalla de Selección de Protagonista (Hombre / Mujer) ########################
screen protagonist_selection():
    modal True
    tag menu

    # Temporizador inteligente (4 segundos): Si no selecciona, el sistema elige automáticamente
    timer 4.0 action Function(auto_select_protagonist)

    add "#06080d"

    # Marco ambiental
    frame:
        xfill True
        yfill True
        background Frame(Solid("#02030698"), 0, 0)

    vbox:
        xalign 0.5
        yalign 0.14
        spacing 10

        text "NEXUS • SELECCIÓN DE PERSPECTIVA":
            font gui.interface_text_font
            size 14
            color "#94a3b8"
            kerning 6
            xalign 0.5

        text "ELIGE TU DESTINO":
            font gui.name_text_font
            size 40
            color "#f8fafc"
            bold True
            xalign 0.5

        text "Una vez confirmada la elección, la realidad quedará sellada.":
            font gui.interface_text_font
            size 15
            color "#64748b"
            xalign 0.5

        # Barra de tiempo estilizada del temporizador de selección
        frame:
            xalign 0.5
            xsize 560
            background Frame(Solid("#080c16ea"), 6, 6)
            padding (16, 10, 16, 10)

            vbox:
                spacing 6
                xfill True

                hbox:
                    xfill True
                    text "⏳ DECISIÓN TEMPORAL":
                        font gui.interface_text_font
                        size 11
                        bold True
                        color "#94a3b8"
                        kerning 2
                    text "Límite: 4s":
                        font gui.interface_text_font
                        size 11
                        bold True
                        color "#e63946"
                        xalign 1.0

                frame:
                    xfill True
                    ysize 8
                    background Frame(Solid("#0f172a"), 4, 4)
                    padding (2, 2, 2, 2)

                    bar:
                        xfill True
                        ysize 4
                        value AnimatedValue(0.0, range=1.0, delay=4.0, old_value=1.0)
                        left_bar Frame(Solid("#e63946"), 2, 2)
                        right_bar Solid("#00000000")
                        thumb None

    # Contenedor de selección dual sobrio (sin siluetas ni detalles de trama)
    hbox:
        xalign 0.5
        yalign 0.56
        spacing 60

        # --- OPCIÓN 1: HOMBRE ---
        button:
            xsize 420
            ysize 320
            action [
                Function(set_protagonist_gender, "hombre"),
                Return()
            ]
            background Frame(Solid("#0d111bf2"), 12, 12)
            hover_background Frame(Solid("#1a0f16f8"), 12, 12)
            padding (36, 36, 36, 36)

            vbox:
                spacing 22
                xfill True
                yalign 0.5

                text "♂":
                    size 48
                    color "#e63946"
                    bold True
                    xalign 0.5

                text "HOMBRE":
                    size 28
                    color "#f8fafc"
                    bold True
                    xalign 0.5
                    kerning 4

                null height 8

                frame:
                    xfill True
                    ysize 46
                    background Solid("#e63946")
                    text "SELECCIONAR":
                        size 13
                        color "#ffffff"
                        bold True
                        xalign 0.5
                        yalign 0.5

        # --- OPCIÓN 2: MUJER ---
        button:
            xsize 420
            ysize 320
            action [
                Function(set_protagonist_gender, "mujer"),
                Return()
            ]
            background Frame(Solid("#120d1cf2"), 12, 12)
            hover_background Frame(Solid("#201032f8"), 12, 12)
            padding (36, 36, 36, 36)

            vbox:
                spacing 22
                xfill True
                yalign 0.5

                text "♀":
                    size 48
                    color "#c084fc"
                    bold True
                    xalign 0.5

                text "MUJER":
                    size 28
                    color "#f8fafc"
                    bold True
                    xalign 0.5
                    kerning 4

                null height 8

                frame:
                    xfill True
                    ysize 46
                    background Solid("#9333ea")
                    text "SELECCIONAR":
                        size 13
                        color "#ffffff"
                        bold True
                        xalign 0.5
                        yalign 0.5

    # Indicador de selección automática por inactividad
    text "Decisión automática en 4 segundos si no seleccionas...":
        xalign 0.5
        yalign 0.88
        font gui.interface_text_font
        size 13
        color "#475569"


## Pantallas Cinemáticas en Pantalla Completa: Prólogo Conceptual #################
## (Visualización en pantalla pura con diseño cinematográfico, sin caja de diálogo)

screen cinematic_prologue_epigraph():
    modal True
    zorder 150

    add "#040508"

    # Permite continuar haciendo clic en cualquier parte de la pantalla o con barra espaciadora
    key "dismiss" action Return()
    button:
        xfill True
        yfill True
        action Return()
        background None

    vbox:
        xalign 0.5
        yalign 0.48
        xsize 1100
        spacing 26

        text "« EL DESTINO Y LA CAUSALIDAD »":
            font gui.interface_text_font
            size 14
            color "#64748b"
            kerning 8
            xalign 0.5

        text "«El aleteo de una sola mariposa en el corazón de Japón\nes capaz de desatar un tifón al otro confín del océano.»":
            font gui.name_text_font
            size 30
            color "#f1f5f9"
            italic True
            text_align 0.5
            xalign 0.5
            line_spacing 14

        null height 10

        text "— Proverbio del Caos y la Predeterminación —":
            font gui.interface_text_font
            size 13
            color "#475569"
            kerning 4
            xalign 0.5

    text "Haz clic o pulsa una tecla para continuar...":
        xalign 0.5
        yalign 0.92
        font gui.interface_text_font
        size 12
        color "#334155"


screen cinematic_butterfly_effect():
    modal True
    zorder 150

    add "#030407"

    key "dismiss" action Return()
    button:
        xfill True
        yfill True
        action Return()
        background None

    vbox:
        xalign 0.5
        yalign 0.46
        xsize 1050
        spacing 28

        text "LEY UNIVERSAL • NEXUS CAUSAL":
            font gui.interface_text_font
            size 13
            color "#ef4444"
            bold True
            kerning 6
            xalign 0.5

        text "EL EFECTO MARIPOSA":
            font gui.name_text_font
            size 44
            bold True
            color "#ffffff"
            kerning 5
            xalign 0.5

        # Línea divisoria de energía carmesí
        frame:
            xalign 0.5
            xsize 220
            ysize 2
            background Solid("#dc2626")

        text "Una ley matemática y cósmica irrevocable:\nuna variación infinitesimal, una pisada apresurada en un paso de peatones\no un segundo de retraso... desvía la causalidad universal hacia un abismo completamente nuevo.":
            font gui.interface_text_font
            size 20
            color "#cbd5e1"
            text_align 0.5
            xalign 0.5
            line_spacing 12

    text "Haz clic o pulsa una tecla para continuar...":
        xalign 0.5
        yalign 0.92
        font gui.interface_text_font
        size 12
        color "#334155"


screen cinematic_nexus_event():
    modal True
    zorder 150

    add "#04030a"

    key "dismiss" action Return()
    button:
        xfill True
        yfill True
        action Return()
        background None

    vbox:
        xalign 0.5
        yalign 0.46
        xsize 1050
        spacing 28

        text "COLISIÓN CUÁNTICA DE DESTINOS":
            font gui.interface_text_font
            size 13
            color "#c084fc"
            bold True
            kerning 6
            xalign 0.5

        text "EL EVENTO NEXUS":
            font gui.name_text_font
            size 44
            bold True
            color "#ffffff"
            kerning 5
            xalign 0.5

        # Línea divisoria de energía amatista
        frame:
            xalign 0.5
            xsize 220
            ysize 2
            background Solid("#a855f7")

        text "Una rasgadura en el tejido del espacio-tiempo.\nUna bifurcación cuántica donde dos destinos colisionan:\nla realidad de quien corrió para salvar... y la realidad de quien cayó en la sombra del impacto.":
            font gui.interface_text_font
            size 20
            color "#cbd5e1"
            text_align 0.5
            xalign 0.5
            line_spacing 12

    text "Haz clic o pulsa una tecla para continuar...":
        xalign 0.5
        yalign 0.92
        font gui.interface_text_font
        size 12
        color "#334155"


## Pantalla Cinemática en Pantalla Completa: Título del Capítulo 1
screen cinematic_chapter_title(cap_num="CAPÍTULO 1", cap_title="El Despertar y la Aguja del Destino", cap_subtitle="Hospital General de Chūbu • Nagano"):
    modal True
    zorder 150

    add "#030407"

    key "dismiss" action Return()
    button:
        xfill True
        yfill True
        action Return()
        background None

    vbox:
        xalign 0.5
        yalign 0.48
        xsize 1100
        spacing 22

        text "NEXUS: 宿命の瞳":
            font gui.interface_text_font
            size 14
            color (persistent.theme_border or "#e63946")
            bold True
            kerning 8
            xalign 0.5

        text "[cap_num]":
            font gui.name_text_font
            size 48
            bold True
            color "#ffffff"
            kerning 6
            xalign 0.5

        # Línea divisoria
        frame:
            xalign 0.5
            xsize 280
            ysize 2
            background Solid(persistent.theme_border or "#e63946")

        text "[cap_title]":
            font gui.name_text_font
            size 28
            color "#f8fafc"
            bold True
            text_align 0.5
            xalign 0.5

        text "[cap_subtitle]":
            font gui.interface_text_font
            size 15
            color "#94a3b8"
            xalign 0.5
            kerning 2

    text "Haz clic o pulsa una tecla para comenzar...":
        xalign 0.5
        yalign 0.92
        font gui.interface_text_font
        size 12
        color "#334155"


## Pantalla Cinemática en Pantalla Completa: Fin del Capítulo 1 con Resumen de Rutas
screen cinematic_chapter_end(route_summary="DESTINO CONSUMADO", choices_taken=[]):
    modal True
    zorder 150

    add "#020306"

    key "dismiss" action Return()
    button:
        xfill True
        yfill True
        action Return()
        background None

    vbox:
        xalign 0.5
        yalign 0.45
        xsize 1100
        spacing 20

        text "NEXUS • INFORME CAUSAL DE LA LÍNEA TEMPORAL":
            font gui.interface_text_font
            size 13
            color (persistent.theme_border or "#e63946")
            bold True
            kerning 6
            xalign 0.5

        text "FIN DEL CAPÍTULO 1":
            font gui.name_text_font
            size 44
            bold True
            color "#ffffff"
            kerning 6
            xalign 0.5

        text "[route_summary]":
            font gui.interface_text_font
            size 18
            bold True
            color (persistent.theme_border or "#c084fc")
            xalign 0.5
            kerning 3

        # Línea divisoria
        frame:
            xalign 0.5
            xsize 340
            ysize 2
            background Solid(persistent.theme_border or "#e63946")

        # Tarjeta de elecciones, efectos mariposa y eventos nexus experimentados
        frame:
            xalign 0.5
            xsize 880
            background Frame(Solid("#080c16f0"), 8, 8)
            padding (24, 20, 24, 20)

            vbox:
                spacing 12
                xfill True

                text "REGISTRO DE DECISIONES Y EFECTO MARIPOSA:":
                    font gui.interface_text_font
                    size 12
                    bold True
                    color "#94a3b8"
                    kerning 2

                for ch in choices_taken:
                    hbox:
                        spacing 12
                        text "◆":
                            size 12
                            color (persistent.theme_border or "#e63946")
                        text ch:
                            size 14
                            color "#e2e8f0"
                            line_spacing 4

    text "Haz clic o pulsa una tecla para continuar...":
        xalign 0.5
        yalign 0.92
        font gui.interface_text_font
        size 12
        color "#475569"


## Pantalla Cinemática en Pantalla Completa: Próximamente Capítulo 2
screen cinematic_chapter2_coming_soon():
    modal True
    zorder 150

    add "#020306"

    key "dismiss" action Return()
    button:
        xfill True
        yfill True
        action Return()
        background None

    vbox:
        xalign 0.5
        yalign 0.46
        xsize 1000
        spacing 24

        text "NEXUS: 宿命の瞳":
            font gui.interface_text_font
            size 14
            color (persistent.theme_border or "#e63946")
            bold True
            kerning 8
            xalign 0.5

        text "CAPÍTULO 2":
            font gui.name_text_font
            size 52
            bold True
            color "#ffffff"
            kerning 8
            xalign 0.5

        frame:
            xalign 0.5
            xsize 260
            ysize 2
            background Solid(persistent.theme_border or "#e63946")

        text "PROXIMAMENTE EN PRODUCCIÓN":
            font gui.interface_text_font
            size 20
            bold True
            color "#38bdf8"
            kerning 6
            xalign 0.5

        text "Nuevos personajes, consecuencias del Efecto Mariposa y bifurcaciones irreversibles de la realidad.":
            font gui.interface_text_font
            size 15
            color "#94a3b8"
            xalign 0.5
            text_align 0.5

    text "Haz clic o pulsa una tecla para volver al menú principal...":
        xalign 0.5
        yalign 0.92
        font gui.interface_text_font
        size 12
        color "#475569"


## Pantalla del menú principal #################################################
screen main_menu():

    tag menu

    add gui.main_menu_background

    # Fondo cinematográfico animado con alternancia continua entre los dos destinos
    frame:
        xpos 450
        ypos 0
        xsize 1470
        ysize 1080
        background None

        # Fondo dinámico animado sin siluetas invasivas
        add "main_menu_animated_bg":
            fit "cover"
            xsize 1470
            ysize 1080

        # Capa de oscurecimiento suave central para máxima legibilidad del logo (sin siluetas de personajes)
        frame:
            xalign 0.35
            yalign 0.5
            xsize 850
            ysize 520
            background Frame(Solid("#090b12a8"), 10, 10)
            padding (40, 35, 40, 35)

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 22

                add "images/nexus_logo.png":
                    xalign 0.5
                    ysize 175
                    fit "contain"

                if persistent.selected_gender == "mujer":
                    text "「 運 命 の 瞳 、 輪 廻 の 淵 」":
                        size 22
                        color (persistent.theme_border or "#c084fc")
                        xalign 0.5
                        bold True
                        kerning 4

                    text "Despertaste tras seis meses de coma y la muerte de tu hermano un mes atrás.\nUn reflejo en el espejo del hospital revela la muerte antes de que ocurra.":
                        size 16
                        color "#d8b4fe"
                        xalign 0.5
                        text_align 0.5
                        line_spacing 6
                elif persistent.selected_gender == "hombre":
                    text "「 瞳 の 奥 に 、 死 が 映 る 」":
                        size 22
                        color (persistent.theme_border or "#e63946")
                        xalign 0.5
                        bold True
                        kerning 4

                    text "En el corazón de Nagano, la muerte aguarda en cada mirada.\nUn don que nació de una herida. Una elección que decide quién respira mañana.":
                        size 16
                        color "#a4adbe"
                        xalign 0.5
                        text_align 0.5
                        line_spacing 6
                else:
                    text "「 宿 命 の 瞳 、 二 つ の 運 命 」":
                        size 22
                        color "#e63946"
                        xalign 0.5
                        bold True
                        kerning 4

                    text "Dos almas entrelazadas en el epicentro de Nagano.\nElige tu perspectiva al comenzar la historia y desafía las leyes del destino.":
                        size 16
                        color "#cbd5e1"
                        xalign 0.5
                        text_align 0.5
                        line_spacing 6

    use navigation

    if gui.show_name:
        vbox:
            xalign 0.98
            yalign 0.96
            spacing 4
            text "[config.name!t]":
                size 14
                color "#525968"
                bold True
            text "v[config.version]":
                size 12
                color "#3c414d"


## Pantalla del menú del juego #################################################
screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":
                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True
                    vbox:
                        spacing spacing
                        transclude

            elif scroll == "vpgrid":
                vpgrid:
                    cols 1
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True
                    spacing spacing
                    transclude

            else:
                transclude

    use navigation

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame:
    xpos 450
    ypos 0
    xsize 1470
    ysize 1080
    top_padding 115
    bottom_padding 35
    left_padding 50
    right_padding 50
    background "#0c0e15f2"

style game_menu_content_frame is empty

style game_menu_viewport:
    xsize 1370

style game_menu_vscrollbar:
    xsize 10
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", Borders(0, 8, 0, 8), tile=False)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", Borders(0, 8, 0, 8), tile=False)
    unscrollable "hide"

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 500
    ypos 32
    ysize 65

style game_menu_label_text:
    size 38
    color (persistent.theme_border or "#e63946")
    yalign 0.5
    bold True
    kerning 2
    outlines [(2, "#0a0c12", 0, 0)]


## Pantalla 'acerca de' ########################################################
##
## Esta pantalla da información sobre los créditos y el copyright del juego y de
## Ren'Py.
##
## No hay nada especial en esta pantalla y por tanto sirve también como ejemplo
## de cómo hacer una pantalla personalizada.

screen about():

    tag menu

    ## Esta sentencia 'use' incluye la pantalla 'game_menu' dentro de esta. El
    ## elemento 'vbox' se incluye entonces dentro del 'viewport' al interno de
    ## la pantalla 'game_menu'.
    use game_menu(_("Acerca de"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Versión [config.version!t]\n")

            ## 'gui.about' se ajusta habitualmente en 'options.rpy'.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Hecho con {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size 18
    bold True
    color "#f1f5f9"

style about_text:
    size 15
    color "#cbd5e1"
    line_spacing 4


## Pantallas de carga y grabación ##############################################
##
## Estas pantallas permiten al jugador grabar el juego y cargarlo de nuevo. Como
## comparten casi todos los elementos, ambas están implementadas en una tercera
## pantalla: 'file_slots'.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Guardar"))


screen load():

    tag menu

    use file_slots(_("Cargar"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Página {}"), auto=_("Grabación automática"), quick=_("Grabación rápida"))

    use game_menu(title):

        fixed:

            ## Esto asegura que 'input' recibe el evento 'enter' antes que otros
            ## botones.
            order_reverse True

            ## El nombre de la pagina, se puede editar haciendo clic en el
            ## botón.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## La cuadrícula de huecos de guardado.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %d de %B %Y, %H:%M"), empty=_("vacío")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Botones de acceso a otras páginas
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}R") action FilePage("quick")

                    ## range(1, 10) da los números del 1 al 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Subir Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Descargar Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style slot_time_text:
    size 13
    color "#94a3b8"

style slot_name_text:
    size 15
    bold True
    color "#f1f5f9"

style page_button_text:
    size 15
    bold True
    color "#94a3b8"
    hover_color "#ffffff"
    selected_color (persistent.theme_color or "#e63946")

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Pantalla de preferencias ####################################################
##
## La pantalla de preferencias permite al jugador configurar el juego a su
## gusto.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Configuración"), scroll="viewport"):

        # Ecosistema completo y enriquecido con gran variedad de opciones
        vbox:
            spacing 26
            xalign 0.5
            xsize 1160

            # =================================================================
            # SECCIÓN 1: PANTALLA Y VISUALIZACIÓN
            # =================================================================
            vbox:
                spacing 14

                hbox:
                    spacing 10
                    yalign 0.5
                    text "PANTALLA Y MODO DE VENTANA" style "pref_group_title"

                hbox:
                    style "pref_row_box"
                    label _("Modo de Pantalla") style "pref_row_label"
                    hbox:
                        spacing 14
                        yalign 0.5
                        textbutton _("Ventana"):
                            action Preference("display", "window")
                            selected (preferences.fullscreen == False)
                            style "pref_tab_btn"
                        textbutton _("Pantalla Completa"):
                            action Preference("display", "fullscreen")
                            selected (preferences.fullscreen == True)
                            style "pref_tab_btn"

                hbox:
                    style "pref_row_box"
                    label _("Modo de Salto de Diálogo") style "pref_row_label"
                    hbox:
                        spacing 14
                        yalign 0.5
                        textbutton _("Texto No Visto"):
                            action Preference("skip", "toggle")
                            style "pref_tab_btn"
                        textbutton _("Tras Elecciones"):
                            action Preference("after choices", "toggle")
                            style "pref_tab_btn"
                        textbutton _("Transiciones"):
                            action InvertSelected(Preference("transitions", "toggle"))
                            style "pref_tab_btn"

            # =================================================================
            # SECCIÓN 2: PERSONALIZACIÓN VISUAL Y TEMA JAPONÉS
            # =================================================================
            vbox:
                spacing 14

                hbox:
                    spacing 10
                    yalign 0.5
                    text "PERSONALIZACIÓN VISUAL Y ESTILO" style "pref_group_title"

                hbox:
                    style "pref_row_box"
                    label _("Tema de la Barra Lateral") style "pref_row_label"
                    hbox:
                        spacing 12
                        yalign 0.5
                        textbutton _("Carmesí Japón"):
                            action Function(set_theme, "Carmesí")
                            selected (persistent.theme_name == "Carmesí")
                            style "pref_tab_btn"
                        textbutton _("Amatista Sakura"):
                            action Function(set_theme, "Amatista Sakura")
                            selected (persistent.theme_name == "Amatista Sakura")
                            style "pref_tab_btn"
                        textbutton _("Azul Noche"):
                            action Function(set_theme, "Azul Noche")
                            selected (persistent.theme_name == "Azul Noche")
                            style "pref_tab_btn"
                        textbutton _("Oro Shinshu"):
                            action Function(set_theme, "Oro Shinshu")
                            selected (persistent.theme_name == "Oro Shinshu")
                            style "pref_tab_btn"
                        textbutton _("Jade Imperial"):
                            action Function(set_theme, "Jade Imperial")
                            selected (persistent.theme_name == "Jade Imperial")
                            style "pref_tab_btn"

                hbox:
                    style "pref_row_box"
                    label _("Tamaño del Texto de Diálogo") style "pref_row_label"
                    hbox:
                        spacing 12
                        yalign 0.5
                        textbutton _("Normal (30px)"):
                            action Function(set_dialogue_size, 30)
                            selected (persistent.text_size_choice == 30)
                            style "pref_tab_btn"
                        textbutton _("Grande (34px)"):
                            action Function(set_dialogue_size, 34)
                            selected (persistent.text_size_choice == 34)
                            style "pref_tab_btn"
                        textbutton _("Extra (38px)"):
                            action Function(set_dialogue_size, 38)
                            selected (persistent.text_size_choice == 38)
                            style "pref_tab_btn"

                hbox:
                    style "pref_row_box"
                    label _("Opacidad de la Caja de Diálogo") style "pref_row_label"
                    hbox:
                        spacing 12
                        yalign 0.5
                        textbutton _("Translúcida (70%)"):
                            action Function(set_textbox_opacity, 0.70)
                            selected (persistent.textbox_alpha == 0.70)
                            style "pref_tab_btn"
                        textbutton _("Equilibrada (85%)"):
                            action Function(set_textbox_opacity, 0.85)
                            selected (persistent.textbox_alpha == 0.85)
                            style "pref_tab_btn"
                        textbutton _("Sólida (100%)"):
                            action Function(set_textbox_opacity, 1.0)
                            selected (persistent.textbox_alpha == 1.0)
                            style "pref_tab_btn"

            # =================================================================
            # SECCIÓN 3: EFECTOS CINEMATOGRÁFICOS Y ACCESIBILIDAD
            # =================================================================
            vbox:
                spacing 14

                hbox:
                    spacing 10
                    yalign 0.5
                    text "EFECTOS VISUALES Y ACCESIBILIDAD" style "pref_group_title"

                hbox:
                    style "pref_row_box"
                    label _("Sacudidas de Pantalla (Vibración)") style "pref_row_label"
                    hbox:
                        spacing 14
                        yalign 0.5
                        textbutton _("Activado"):
                            action Function(toggle_screen_shake)
                            selected (persistent.screen_shake == True)
                            style "pref_tab_btn"
                        textbutton _("Desactivado"):
                            action Function(toggle_screen_shake)
                            selected (persistent.screen_shake == False)
                            style "pref_tab_btn"

                hbox:
                    style "pref_row_box"
                    label _("Destellos de Ojos / Visiones de Muerte") style "pref_row_label"
                    hbox:
                        spacing 14
                        yalign 0.5
                        textbutton _("Completos"):
                            action Function(toggle_flash_effects)
                            selected (persistent.flash_effects == True)
                            style "pref_tab_btn"
                        textbutton _("Suavizados"):
                            action Function(toggle_flash_effects)
                            selected (persistent.flash_effects == False)
                            style "pref_tab_btn"

                hbox:
                    style "pref_row_box"
                    label _("Guardado Automático en Decisiones") style "pref_row_label"
                    hbox:
                        spacing 14
                        yalign 0.5
                        textbutton _("Habilitado"):
                            action Function(toggle_auto_save_choices)
                            selected (persistent.auto_save_choices == True)
                            style "pref_tab_btn"
                        textbutton _("Deshabilitado"):
                            action Function(toggle_auto_save_choices)
                            selected (persistent.auto_save_choices == False)
                            style "pref_tab_btn"

            # =================================================================
            # SECCIÓN 4: AUDIO Y BANDA SONORA (SOLO PIANO TRISTE)
            # =================================================================
            vbox:
                spacing 16

                hbox:
                    spacing 10
                    yalign 0.5
                    text "AUDIO Y BANDA SONORA" style "pref_group_title"

                # Control de Música de Piano (Selector de Niveles + Control Fino + Escucha)
                if config.has_music:
                    frame:
                        style "pref_audio_card"
                        vbox:
                            spacing 12
                            xfill True

                            hbox:
                                xfill True
                                yalign 0.5
                                label _("Música de Piano (BGM)") style "pref_audio_header_label"
                                text "[int(preferences.get_volume('music') * 100)]%":
                                    style "pref_volume_percent_text"

                            # Barra de niveles directos (0% Silencio, 25% Suave, 50% Medio, 75% Alto, 100% Máximo)
                            hbox:
                                spacing 8
                                xfill True
                                yalign 0.5
                                textbutton _("Mute (0%)"):
                                    action Function(set_music_volume_level, 0.0)
                                    selected (preferences.get_volume('music') == 0.0)
                                    style "audio_preset_btn"
                                textbutton _("Suave (25%)"):
                                    action Function(set_music_volume_level, 0.25)
                                    selected (abs(preferences.get_volume('music') - 0.25) < 0.04)
                                    style "audio_preset_btn"
                                textbutton _("Medio (50%)"):
                                    action Function(set_music_volume_level, 0.50)
                                    selected (abs(preferences.get_volume('music') - 0.50) < 0.04)
                                    style "audio_preset_btn"
                                textbutton _("Alto (75%)"):
                                    action Function(set_music_volume_level, 0.75)
                                    selected (abs(preferences.get_volume('music') - 0.75) < 0.04)
                                    style "audio_preset_btn"
                                textbutton _("Máximo (100%)"):
                                    action Function(set_music_volume_level, 1.0)
                                    selected (preferences.get_volume('music') >= 0.96)
                                    style "audio_preset_btn"

                            # Fila de ajuste analógico fino + botón de prueba
                            hbox:
                                spacing 16
                                yalign 0.5
                                xfill True

                                hbox:
                                    spacing 10
                                    yalign 0.5
                                    text _("Ajuste Preciso:") style "pref_fine_label"
                                    bar value Preference("music volume") style "audio_modern_bar"

                                textbutton _("Escuchar Tema"):
                                    action Play("music", "audio/piano_sad_theme.wav")
                                    style "audio_listen_btn"

                # Control de Efectos de Sonido SFX
                if config.has_sound:
                    frame:
                        style "pref_audio_card"
                        vbox:
                            spacing 12
                            xfill True

                            hbox:
                                xfill True
                                yalign 0.5
                                label _("Efectos de Sonido (SFX)") style "pref_audio_header_label"
                                text "[int(preferences.get_volume('sfx') * 100)]%":
                                    style "pref_volume_percent_text"

                            # Barra de niveles directos
                            hbox:
                                spacing 8
                                xfill True
                                yalign 0.5
                                textbutton _("Mute (0%)"):
                                    action Function(set_sfx_volume_level, 0.0)
                                    selected (preferences.get_volume('sfx') == 0.0)
                                    style "audio_preset_btn"
                                textbutton _("Suave (25%)"):
                                    action Function(set_sfx_volume_level, 0.25)
                                    selected (abs(preferences.get_volume('sfx') - 0.25) < 0.04)
                                    style "audio_preset_btn"
                                textbutton _("Medio (50%)"):
                                    action Function(set_sfx_volume_level, 0.50)
                                    selected (abs(preferences.get_volume('sfx') - 0.50) < 0.04)
                                    style "audio_preset_btn"
                                textbutton _("Alto (75%)"):
                                    action Function(set_sfx_volume_level, 0.75)
                                    selected (abs(preferences.get_volume('sfx') - 0.75) < 0.04)
                                    style "audio_preset_btn"
                                textbutton _("Máximo (100%)"):
                                    action Function(set_sfx_volume_level, 1.0)
                                    selected (preferences.get_volume('sfx') >= 0.96)
                                    style "audio_preset_btn"

                            # Fila de ajuste analógico fino + botón de prueba
                            hbox:
                                spacing 16
                                yalign 0.5
                                xfill True

                                hbox:
                                    spacing 10
                                    yalign 0.5
                                    text _("Ajuste Preciso:") style "pref_fine_label"
                                    bar value Preference("sound volume") style "audio_modern_bar"

                                textbutton _("Probar Sonido"):
                                    action Play("sound", "audio/eye_vision.wav")
                                    style "audio_listen_btn"

                # Interruptor de Silencio Global
                if config.has_music or config.has_sound:
                    frame:
                        style "pref_audio_mute_card"
                        hbox:
                            xfill True
                            yalign 0.5
                            vbox:
                                spacing 2
                                label _("Modo Silencioso Global") style "pref_audio_header_label"
                                text _("Silencia o reanuda toda la música y efectos de sonido con un clic."):
                                    size 12
                                    color "#788294"
                            hbox:
                                xalign 1.0
                                yalign 0.5
                                textbutton (_("Mudo") if (_preferences.get_mute('music') and _preferences.get_mute('sfx')) else _("Silenciar")):
                                    action Preference("all mute", "toggle")
                                    style "audio_master_mute_btn"

            # =================================================================
            # SECCIÓN 5: VELOCIDAD Y TIEMPOS DE LECTURA
            # =================================================================
            vbox:
                spacing 14

                hbox:
                    spacing 10
                    yalign 0.5
                    text "VELOCIDAD Y TIEMPOS DE AVANCE" style "pref_group_title"

                hbox:
                    style "pref_row_box"
                    label _("Velocidad de Aparición del Texto") style "pref_row_label"
                    hbox:
                        yalign 0.5
                        bar value Preference("text speed") style "pref_ecosystem_bar_wide"

                hbox:
                    style "pref_row_box"
                    label _("Tiempo de Autoavance de Diálogo") style "pref_row_label"
                    hbox:
                        yalign 0.5
                        bar value Preference("auto-forward time") style "pref_ecosystem_bar_wide"

            # =================================================================
            # SECCIÓN 6: GESTIÓN DE DATOS Y PERFIL (NUEVO USUARIO)
            # =================================================================
            vbox:
                spacing 14

                hbox:
                    spacing 10
                    yalign 0.5
                    text "GESTIÓN DE PERFIL Y PROGRESO" style "pref_group_title"

                frame:
                    style "pref_audio_card"
                    hbox:
                        xfill True
                        yalign 0.5
                        vbox:
                            spacing 3
                            label _("Restablecer Progreso a Cero") style "pref_audio_header_label"
                            text _("Reinicia todos los logros, puntos de XP y estadísticas para comenzar desde cero como un nuevo usuario."):
                                size 12
                                color "#8c96a8"
                        textbutton _("Restablecer a Cero"):
                            action Confirm(_("¿Deseas restablecer todo el progreso, logros y XP a cero absoluto como un nuevo usuario?"), Function(reset_all_progress))
                            style "pref_act_button"
                            xalign 1.0


style pref_audio_card:
    xfill True
    padding (22, 18, 22, 18)
    background Frame("gui/custom_btn/btn_idle.png", 8, 8)

style pref_audio_mute_card:
    xfill True
    padding (22, 16, 22, 16)
    background Frame("gui/custom_btn/btn_idle.png", 8, 8)

style pref_audio_header_label is gui_label
style pref_audio_header_label_text:
    size 16
    bold True
    color "#f1f5f9"

style pref_volume_percent_text is gui_text:
    size 15
    bold True
    color (persistent.theme_color or "#b82626")
    xalign 1.0

style pref_fine_label is gui_text:
    size 13
    color "#94a3b8"
    yalign 0.5

style audio_preset_btn is gui_button:
    padding (12, 9, 12, 9)
    xfill True
    background Frame("gui/custom_btn/pill_idle.png", 6, 6)
    hover_background Frame("gui/custom_btn/pill_hover.png", 6, 6)
    selected_background Frame("gui/custom_btn/pill_selected.png", 6, 6)

style audio_preset_btn_text is gui_button_text:
    size 13
    bold True
    color "#94a3b8"
    hover_color "#ffffff"
    selected_color "#ffffff"
    xalign 0.5
    yalign 0.5

style audio_modern_bar is gui_slider:
    ysize 18
    xsize 620
    yalign 0.5

style audio_listen_btn is gui_button:
    padding (16, 9, 16, 9)
    xsize 165
    yalign 0.5
    background Frame("gui/custom_btn/act_idle.png", 6, 6)
    hover_background Frame("gui/custom_btn/act_hover.png", 6, 6)

style audio_listen_btn_text is gui_button_text:
    size 13
    bold True
    color "#e2e8f0"
    hover_color "#ffffff"
    xalign 0.5
    yalign 0.5

style audio_master_mute_btn is gui_button:
    padding (10, 5, 10, 5)
    xsize 90
    ysize 32
    xfill False
    xalign 1.0
    yalign 0.5
    background Frame("gui/custom_btn/mute_idle.png", 6, 6)
    hover_background Frame("gui/custom_btn/mute_hover.png", 6, 6)
    selected_background Frame("gui/custom_btn/mute_selected.png", 6, 6)

style audio_master_mute_btn_text is gui_button_text:
    size 12
    bold True
    color "#f87171"
    hover_color "#ffffff"
    selected_color "#ffffff"
    xalign 0.5
    yalign 0.5


style pref_group_title:
    size 14
    bold True
    color (persistent.theme_color or "#b82626")
    kerning 2

style pref_row_box:
    xfill True
    spacing 25
    yalign 0.5
    padding (18, 12, 18, 12)
    background Frame(Solid("#0f121bb8"), 6, 6)

style pref_row_label is gui_label:
    xsize 360
    right_padding 20
    yalign 0.5

style pref_row_label_text is gui_label_text:
    size 15
    color "#cbd5e1"
    bold True
    yalign 0.5
    textalign 0.0

style pref_tab_btn is gui_button:
    padding (20, 9, 20, 9)
    background Frame("gui/custom_btn/btn_idle.png", 6, 6)
    hover_background Frame("gui/custom_btn/btn_hover.png", 6, 6)
    selected_background Frame("gui/custom_btn/btn_selected.png", 6, 6)

style pref_tab_btn_text is gui_button_text:
    size 14
    bold True
    color "#94a3b8"
    hover_color "#ffffff"
    selected_color "#ffffff"
    yalign 0.5

style pref_ecosystem_bar is gui_slider:
    ysize 24
    xsize 460
    yalign 0.5

style pref_ecosystem_bar_wide is gui_slider:
    ysize 24
    xsize 600
    yalign 0.5

style pref_action_test_btn is gui_button:
    padding (16, 9, 16, 9)
    xsize 130
    yalign 0.5
    background Frame("gui/custom_btn/act_idle.png", 6, 6)
    hover_background Frame("gui/custom_btn/act_hover.png", 6, 6)

style pref_action_test_btn_text is gui_button_text:
    size 13
    bold True
    color "#e2e8f0"
    hover_color "#ffffff"
    xalign 0.5


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## Pantalla de historial #######################################################
##
## Esta pantalla presenta el historial de diálogo al jugador, almacenado en
## '_history_list'.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Evita la predicción de esta pantalla, que podría ser demasiado grande.
    predict False

    use game_menu(_("Historial"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Esto distribuye los elementos apropiadamente si
                ## 'history_height' es 'None'.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Toma el color del texto 'who' de 'Character', si ha
                        ## sido establecido.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("El historial está vacío.")


## Esto determina qué etiquetas se permiten en la pantalla de historial.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Pantalla de ayuda ###########################################################
##
## Una pantalla que da información sobre el uso del teclado y el ratón. Usa
## otras pantallas con el contenido de la ayuda ('keyboard_help', 'mouse_help',
## y 'gamepad_help').

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Ayuda"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Teclado") action SetScreenVariable("device", "keyboard")
                textbutton _("Ratón") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Mando") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Intro")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Espacio")
        text _("Avanza el diálogo sin seleccionar opciones.")

    hbox:
        label _("Teclas de flecha")
        text _("Navega la interfaz.")

    hbox:
        label _("Escape")
        text _("Accede al menú del juego.")

    hbox:
        label _("Ctrl")
        text _("Salta el diálogo mientras se presiona.")

    hbox:
        label _("Tabulador")
        text _("Activa/desactiva el salto de diálogo.")

    hbox:
        label _("Av. pág.")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Re. pág.")
        text _("Avanza hacia el diálogo siguiente.")

    hbox:
        label "H"
        text _("Oculta la interfaz.")

    hbox:
        label "S"
        text _("Captura la pantalla.")

    hbox:
        label "V"
        text _("Activa/desactiva la asistencia por {a=https://www.renpy.org/l/voicing}voz-automática{/a}.")

    hbox:
        label "Shift+A"
        text _("Abre el menú de accesibilidad.")


screen mouse_help():

    hbox:
        label _("Clic izquierdo")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Clic medio")
        text _("Oculta la interfaz.")

    hbox:
        label _("Clic derecho")
        text _("Accede al menú del juego.")

    hbox:
        label _("Rueda del ratón arriba")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Rueda del ratón abajo")
        text _("Avanza hacia el diálogo siguiente.")


screen gamepad_help():

    hbox:
        label _("Gatillo derecho\nA/Botón inferior")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Gatillo izquierdo\nBotón sup. frontal izq.")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Botón sup. frontal der.")
        text _("Avanza hacia el diálogo siguiente.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navega la interfaz.")

    hbox:
        label _("Inicio, Guía, B/Botón Derecho")
        text _("Accede al menú del juego.")

    hbox:
        label _("Y/Botón superior")
        text _("Oculta la interfaz.")

    textbutton _("Calibrar") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    padding (16, 8, 16, 8)
    background Frame("gui/custom_btn/btn_idle.png", 6, 6)
    hover_background Frame("gui/custom_btn/btn_hover.png", 6, 6)
    selected_background Frame("gui/custom_btn/btn_selected.png", 6, 6)
    xmargin 8

style help_button_text:
    size 14
    bold True
    color "#94a3b8"
    hover_color "#ffffff"
    selected_color "#ffffff"

style help_label:
    xsize 320
    right_padding 24

style help_label_text:
    size 15
    bold True
    color (persistent.theme_color or "#e63946")
    xalign 1.0
    textalign 1.0

style help_text:
    size 15
    color "#cbd5e1"
    yalign 0.5



################################################################################
## Pantallas adicionales
################################################################################


## Pantalla de confirmación ####################################################
##
## Ren'Py llama la pantalla de confirmación para presentar al jugador preguntas
## de sí o no.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

transform modal_popup_anim:
    on show:
        alpha 0.0 zoom 0.94
        easein 0.16 alpha 1.0 zoom 1.0
    on hide:
        easeout 0.12 alpha 0.0 zoom 0.96

screen confirm(message, yes_action, no_action):

    modal True
    zorder 300

    # Fondo oscurecido con profundidad
    add Solid("#04060dd0")

    frame at modal_popup_anim:
        style "nexus_modal_frame"

        vbox:
            spacing 18
            xfill True

            # Barra superior de la ventana modal
            hbox:
                xfill True
                yalign 0.5
                spacing 10
                add "gui/icons/icon_settings.png" ysize 18 fit "contain" yalign 0.5
                text _("AVISO DEL SISTEMA"):
                    size 13
                    bold True
                    kerning 2
                    color (persistent.theme_color or "#e63946")
                    yalign 0.5

            # Divisor carmesí
            frame:
                xfill True
                ysize 2
                background Solid(persistent.theme_color or "#e63946")

            # Cuerpo del mensaje
            null height 6
            text _(message):
                size 16
                color "#f1f5f9"
                xalign 0.5
                textalign 0.5
                line_spacing 4

            null height 10

            # Botones de acción modal
            hbox:
                xalign 0.5
                spacing 20

                textbutton _("Confirmar"):
                    action yes_action
                    style "nexus_modal_yes_btn"

                textbutton _("Cancelar"):
                    action no_action
                    style "nexus_modal_no_btn"

    key "game_menu" action no_action


style nexus_modal_frame:
    xsize 560
    xalign 0.5
    yalign 0.5
    padding (32, 24, 32, 26)
    background Frame("gui/frame.png", 8, 8)

style nexus_modal_yes_btn is gui_button:
    padding (34, 11, 34, 11)
    xsize 180
    background Frame("gui/custom_btn/btn_selected.png", 6, 6)
    hover_background Frame("gui/custom_btn/btn_hover.png", 6, 6)

style nexus_modal_yes_btn_text is gui_button_text:
    size 14
    bold True
    color "#ffffff"
    xalign 0.5
    yalign 0.5

style nexus_modal_no_btn is gui_button:
    padding (34, 11, 34, 11)
    xsize 180
    background Frame("gui/custom_btn/btn_idle.png", 6, 6)
    hover_background Frame("gui/custom_btn/act_hover.png", 6, 6)

style nexus_modal_no_btn_text is gui_button_text:
    size 14
    bold True
    color "#94a3b8"
    hover_color "#ffffff"
    xalign 0.5
    yalign 0.5


## Pantalla del indicador de salto #############################################
##
## La pantalla de indicador de salto se muestra para indicar que se está
## realizando el salto.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Saltando")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Esta transformación provoca el parpadeo de las flechas una tras otra.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Es necesario usar un tipo de letra que contenga el glifo BLACK RIGHT-
    ## POINTING SMALL TRIANGLE.
    font "DejaVuSans.ttf"


## Pantalla de notificación ####################################################
##
## La pantalla de notificación muestra al jugador un mensaje. (Por ejemplo, con
## un guardado rápido o una captura de pantalla.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 250
    style_prefix "notify"

    frame at notify_appear:
        style "nexus_notify_frame"
        hbox:
            spacing 14
            yalign 0.5
            add "gui/icons/icon_achievements.png" ysize 22 fit "contain" yalign 0.5
            text "[message!tq]":
                size 14
                bold True
                color "#f1f5f9"
                yalign 0.5

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0.0 xoffset 40
        easein 0.22 alpha 1.0 xoffset 0
    on hide:
        easeout 0.25 alpha 0.0 xoffset 40


style nexus_notify_frame:
    xalign 0.985
    ypos 28
    padding (20, 12, 24, 12)
    background Frame("gui/notify.png", Borders(14, 8, 14, 8))

style notify_text:
    properties gui.text_properties("notify")


## Pantalla NVL ################################################################
##
## Esta pantalla se usa para el diálogo y los menús en modo NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Presenta el diálogo en una 'vpgrid' o una 'vbox'.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Presenta el menú, si lo hay. El menú puede ser presentado
        ## incorrectamente si 'config.narrator_menu' está ajustado a 'True'.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Esto controla el número máximo de entradas en modo NVL que pueden ser
## mostradas de una vez.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Pantalla de globos ##########################################################
##
## La pantalla de burbujas se utiliza para mostrar el diálogo al jugador cuando
## se utilizan burbujas de diálogo. La pantalla de burbujas toma los mismos
## parámetros que la pantalla "say", debe crear un visualizable con el id de
## "what", y puede crear visualizables con los ids "namebox", "who", y "window".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Variantes móviles
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Ya que puede carecer de ratón, se reempleza el menú rápido con una versión
## con menos botones y más grandes, más fáciles de tocar.
screen quick_menu():
    variant "touch"
    zorder 100
    pass


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900



## Pantalla de Logros y Nivel (Ranking y Progreso) #############################
screen achievements():

    tag menu

    use game_menu(_("Logros y Nivel"), scroll="viewport"):

        vbox:
            spacing 26
            xsize 1160

            # -----------------------------------------------------------------
            # CABECERA DE ESTADÍSTICAS Y NIVEL DEL JUGADOR
            # -----------------------------------------------------------------
            frame:
                style "achieve_hero_card"
                hbox:
                    xfill True
                    yalign 0.5
                    spacing 20

                    # Stat 1: Logros desbloqueados
                    vbox:
                        spacing 2
                        xalign 0.5
                        text "[get_unlocked_count()]/[get_total_gender_achievements_count()]":
                            size 28
                            bold True
                            color "#ffffff"
                            xalign 0.5
                        text _("logros"):
                            size 13
                            color "#8c96a8"
                            xalign 0.5

                    # Divisor vertical tenue
                    frame:
                        ysize 45
                        xsize 1
                        background "#262d40"
                        yalign 0.5

                    # Stat 2: Experiencia XP
                    vbox:
                        spacing 2
                        xalign 0.5
                        text "[get_total_player_xp()]":
                            size 28
                            bold True
                            color (persistent.theme_color or "#e63946")
                            xalign 0.5
                        text _("XP"):
                            size 13
                            bold True
                            color "#8c96a8"
                            xalign 0.5

                    # Divisor vertical tenue
                    frame:
                        ysize 45
                        xsize 1
                        background "#262d40"
                        yalign 0.5

                    # Stat 3: Porcentaje y Barra de Progreso
                    vbox:
                        spacing 4
                        xsize 420
                        yalign 0.5
                        hbox:
                            xfill True
                            text "[get_achievements_percent()]%":
                                size 20
                                bold True
                                color "#ffffff"
                            text _("completo"):
                                size 13
                                color "#8c96a8"
                                xalign 1.0
                        # Barra de progreso
                        bar:
                            value get_achievements_percent()
                            range 100
                            ysize 10
                            xsize 420
                            left_bar Frame(Solid(persistent.theme_color or "#e63946"), 2, 2)
                            right_bar Frame(Solid("#1c2233"), 2, 2)

                    # Divisor vertical tenue
                    frame:
                        ysize 45
                        xsize 1
                        background "#262d40"
                        yalign 0.5

                    # Stat 4: Recorrido
                    vbox:
                        spacing 2
                        xalign 0.5
                        text "[get_recorrido_count()]/[get_total_gender_achievements_count()]":
                            size 24
                            bold True
                            color "#ffffff"
                            xalign 0.5
                        text _("Recorrido"):
                            size 13
                            color "#8c96a8"
                            xalign 0.5

            # -----------------------------------------------------------------
            # BARRA DE PESTAÑAS Y BÚSQUEDA
            # -----------------------------------------------------------------
            vbox:
                spacing 14

                hbox:
                    xfill True
                    yalign 0.5

                    # Pestañas de filtrado
                    hbox:
                        spacing 10
                        yalign 0.5

                        textbutton _("Todos"):
                            action Function(set_achieve_filter, "Todos")
                            selected (persistent.achievement_filter == "Todos")
                            style "pref_tab_btn"

                        textbutton _("Desbloqueados"):
                            action Function(set_achieve_filter, "Desbloqueados")
                            selected (persistent.achievement_filter == "Desbloqueados")
                            style "pref_tab_btn"

                        textbutton _("Bloqueados"):
                            action Function(set_achieve_filter, "Bloqueados")
                            selected (persistent.achievement_filter == "Bloqueados")
                            style "pref_tab_btn"

                        textbutton _("Recientes"):
                            action Function(set_achieve_filter, "Recientes")
                            selected (persistent.achievement_filter == "Recientes")
                            style "pref_tab_btn"

                        textbutton _("Ranking"):
                            action Function(set_achieve_filter, "Ranking")
                            selected (persistent.achievement_filter == "Ranking")
                            style "pref_tab_btn"

                    # Cuadro interactivo de búsqueda
                    frame:
                        xsize 250
                        ysize 42
                        padding (12, 8, 12, 8)
                        background Frame(Solid("#141926"), 4, 4)
                        yalign 0.5
                        xalign 1.0
                        input:
                            value FieldInputValue(persistent, "achievement_search")
                            default ""
                            size 13
                            color "#94a3b8"
                            yalign 0.5

            # -----------------------------------------------------------------
            # VISTA DE CONTENIDO SEGÚN FILTRO
            # -----------------------------------------------------------------
            if persistent.achievement_filter == "Ranking":

                # --- VISTA DE RANKING XP ---
                frame:
                    style "achieve_card_panel"
                    vbox:
                        spacing 18
                        xfill True

                        hbox:
                            xfill True
                            yalign 0.5
                            text "TOP 20 POR XP" style "achieve_section_header"
                            if persistent.player_in_ranking:
                                text "TEMPORADA 1 • EN VIVO" size 12 color "#4ade80" xalign 1.0
                            else:
                                text "TEMPORADA 1" size 12 color "#64748b" xalign 1.0

                        if not persistent.player_in_ranking:
                            # Mensaje de ranking vacío (solicitado textualmente)
                            frame:
                                xfill True
                                padding (24, 28, 24, 28)
                                background Frame(Solid("#0d1017"), 6, 6)
                                vbox:
                                    spacing 8
                                    xalign 0.5
                                    text "Todavía no hay nadie. ¡Sé el primero!":
                                        size 16
                                        bold True
                                        color "#ffffff"
                                        xalign 0.5
                                    text "Elegí un apodo. Solo se publica el apodo, tu nivel, tu XP y cuántos logros tenés.":
                                        size 14
                                        color "#94a3b8"
                                        xalign 0.5

                            # Botón para unirse al ranking
                            hbox:
                                xalign 0.5
                                spacing 15
                                textbutton _("Sumarme al ranking"):
                                    action Function(join_ranking_action)
                                    style "achieve_join_btn"

                        else:
                            # Ranking activo mostrando la posición del jugador
                            vbox:
                                spacing 10
                                xfill True

                                frame:
                                    style "achieve_row_frame"
                                    hbox:
                                        xfill True
                                        yalign 0.5
                                        spacing 18

                                        text "#1":
                                            size 20
                                            bold True
                                            color (persistent.theme_color or "#e63946")
                                            yalign 0.5
                                            xsize 40

                                        vbox:
                                            spacing 3
                                            hbox:
                                                spacing 10
                                                yalign 0.5
                                                text "[persistent.player_nickname]":
                                                    size 16
                                                    bold True
                                                    color "#ffffff"
                                                frame:
                                                    padding (6, 2, 6, 2)
                                                    background Frame(Solid(persistent.theme_color or "#e63946"), 3, 3)
                                                    text _("TÚ"):
                                                        size 10
                                                        bold True
                                                        color "#ffffff"
                                            text _("Nivel [get_player_level()] • [get_unlocked_count()] logros completados"):
                                                size 12
                                                color "#94a3b8"

                                        vbox:
                                            xalign 1.0
                                            spacing 2
                                            text "[get_total_player_xp()] XP":
                                                size 16
                                                bold True
                                                color (persistent.theme_color or "#e63946")
                                                xalign 1.0
                                            text _("Rango Shinshu"):
                                                size 11
                                                color "#64748b"
                                                xalign 1.0

                                hbox:
                                    xalign 0.5
                                    spacing 20
                                    text _("✓ Publicado en el ranking con el apodo: [persistent.player_nickname]"):
                                        size 13
                                        color "#4ade80"
                                        yalign 0.5

            else:

                # --- VISTA DE LOGROS DINÁMICOS SEGÚN FILTRO ---
                $ current_list = get_filtered_achievements()

                vbox:
                    spacing 14
                    xfill True

                    hbox:
                        spacing 10
                        if persistent.achievement_filter == "Desbloqueados":
                            text "LOGROS DESBLOQUEADOS" style "achieve_section_header"
                        elif persistent.achievement_filter == "Bloqueados":
                            text "PRÓXIMOS A DESBLOQUEAR" style "achieve_section_header"
                        elif persistent.achievement_filter == "Recientes":
                            text "LOGROS OBTENIDOS RECIENTEMENTE" style "achieve_section_header"
                        else:
                            text "PRÓXIMOS A DESBLOQUEAR" style "achieve_section_header"

                    if not current_list:
                        frame:
                            style "achieve_row_frame"
                            text _("No se encontraron logros en esta categoría o filtro de búsqueda."):
                                size 14
                                color "#94a3b8"
                                xalign 0.5
                    else:
                        for ach in current_list[:15]:
                            $ is_unlocked = is_achievement_unlocked(ach["id"])
                            frame:
                                style "achieve_row_frame"
                                hbox:
                                    spacing 18
                                    yalign 0.5
                                    xfill True
                                    if is_unlocked:
                                        add "gui/icons/icon_achievements.png" ysize 36 fit "contain" yalign 0.5
                                    else:
                                        add "gui/icons/icon_achievements.png" ysize 36 fit "contain" yalign 0.5 alpha 0.45

                                    vbox:
                                        spacing 2
                                        hbox:
                                            spacing 8
                                            yalign 0.5
                                            text ach["name"]:
                                                size 16
                                                bold True
                                                if is_unlocked:
                                                    color "#ffffff"
                                                else:
                                                    color "#cbd5e1"
                                            if ach.get("chapter"):
                                                text ("(" + ach["chapter"] + ")"):
                                                    size 12
                                                    color "#64748b"
                                                    yalign 0.5

                                        if is_unlocked:
                                            text ach["desc"]:
                                                size 13
                                                color "#94a3b8"
                                        else:
                                            if ach.get("secret", False):
                                                text _("Logro secreto del destino. Continúa avanzando en la historia para revelarlo."):
                                                    size 13
                                                    color "#64748b"
                                            else:
                                                text ach["desc"]:
                                                    size 13
                                                    color "#64748b"

                                    vbox:
                                        xalign 1.0
                                        spacing 2
                                        text ("+" + str(ach["xp"]) + " XP"):
                                            size 14
                                            bold True
                                            if is_unlocked:
                                                color (persistent.theme_color or "#e63946")
                                            else:
                                                color "#64748b"
                                            xalign 1.0

                                        if is_unlocked:
                                            text _("Desbloqueado"):
                                                size 12
                                                color "#4ade80"
                                                xalign 1.0
                                        else:
                                            text _("Pendiente"):
                                                size 12
                                                color "#f59e0b"
                                                xalign 1.0


style achieve_hero_card:
    xfill True
    padding (24, 20, 24, 20)
    background Frame("gui/custom_btn/btn_idle.png", 8, 8)

style achieve_card_panel:
    xfill True
    padding (24, 22, 24, 22)
    background Frame(Solid("#11131ef0"), 6, 6)

style achieve_row_frame:
    xfill True
    padding (18, 14, 18, 14)
    background Frame("gui/custom_btn/btn_idle.png", 6, 6)

style achieve_section_header:
    size 15
    bold True
    color (persistent.theme_color or "#b82626")
    kerning 1.8

style achieve_join_btn is gui_button:
    padding (24, 12, 24, 12)
    background Frame("gui/custom_btn/btn_selected.png", 6, 6)
    hover_background Frame("gui/custom_btn/btn_hover.png", 6, 6)

style achieve_join_btn_text is gui_button_text:
    size 15
    bold True
    color "#ffffff"
    xalign 0.5
    yalign 0.5




## =============================================================================
## MINIJUEGO: PIEDRA, PAPEL O TIJERA (JANKEN) - INTERFAZ DEL DESTINO
## =============================================================================

screen janken_minigame(aoi_choice, foresight_active=False):

    modal True

    # Marco a Pantalla Completa Total 1920x1080 (Sin cajas de dialogo visibles)
    frame:
        xpos 0
        ypos 0
        xsize 1920
        ysize 1080
        background Frame(Solid("#070a13fa"), 0, 0)
        padding (70, 40, 70, 35)

        vbox:
            xfill True
            yfill True
            spacing 20

            # --- 1. CABECERA EXPANDIDA FULLSCREEN ---
            hbox:
                xfill True
                yalign 0.5

                vbox:
                    spacing 4
                    text "じゃんけん • DUELO DEL DESTINO: PIEDRA, PAPEL O TIJERA":
                        size 26
                        bold True
                        color (persistent.theme_color or "#e63946")
                        kerning 3
                    text "Desafío fraternal en la habitación 304 del Hospital de Matsumoto":
                        size 14
                        color "#94a3b8"

                # Marcador extendido
                hbox:
                    spacing 16
                    yalign 0.5
                    xalign 1.0
                    frame:
                        padding (16, 8, 16, 8)
                        background Frame(Solid("#111827"), 6, 6)
                        text "Victorias: [persistent.janken_wins]":
                            size 14
                            bold True
                            color "#4ade80"
                    frame:
                        padding (16, 8, 16, 8)
                        background Frame(Solid("#111827"), 6, 6)
                        text "Empates: [persistent.janken_draws]":
                            size 14
                            bold True
                            color "#38bdf8"
                    frame:
                        padding (16, 8, 16, 8)
                        background Frame(Solid("#111827"), 6, 6)
                        text "Derrotas: [persistent.janken_losses]":
                            size 14
                            bold True
                            color "#f87171"

            # Línea decorativa horizontal
            frame:
                xfill True
                ysize 2
                background Frame(Solid("#1e293b"), 0, 0)

            # --- 2. ZONA DEL RIVAL (AOI) DE ANCHO COMPLETO ---
            frame:
                style "janken_rival_card"
                hbox:
                    xfill True
                    yalign 0.5
                    spacing 28

                    # Retrato / Silueta de Aoi ampliada
                    add "images/silueta_aoi.png":
                        ysize 140
                        fit "contain"
                        yalign 0.5

                    vbox:
                        spacing 6
                        yalign 0.5
                        text "Aoi Kazama (妹 • Hermana Menor)":
                            size 22
                            bold True
                            color "#ffffff"
                        text "«¡Te toca elegir, hermanito! ¡Esta vez no pienso perder contra ti!»":
                            size 16
                            color "#e2e8f0"
                            italic True

                    # Habilidad del Ojo Carmesí: Predicción del Futuro
                    if foresight_active:
                        frame:
                            style "janken_foresight_badge"
                            hbox:
                                spacing 16
                                yalign 0.5
                                add "gui/janken/eye_foresight.png" ysize 44 fit "contain" yalign 0.5
                                vbox:
                                    spacing 2
                                    text "VISIÓN DEL DESTINO ACTIVA":
                                        size 12
                                        bold True
                                        color "#ff3355"
                                        kerning 2
                                    if aoi_choice == "piedra":
                                        text "PREMONICIÓN: Aoi sacará PIEDRA":
                                            size 15
                                            bold True
                                            color "#ffffff"
                                    elif aoi_choice == "papel":
                                        text "PREMONICIÓN: Aoi sacará PAPEL":
                                            size 15
                                            bold True
                                            color "#ffffff"
                                    else:
                                        text "PREMONICIÓN: Aoi sacará TIJERA":
                                            size 15
                                            bold True
                                            color "#ffffff"

            # --- 3. ZONA CENTRAL: CARTAS DE ACCIÓN A PANTALLA COMPLETA ---
            vbox:
                spacing 16
                xfill True
                yalign 0.5

                text "SELECCIONA TU JUGADA PARA ALTERAR LA LÍNEA TEMPORAL":
                    size 15
                    bold True
                    color "#94a3b8"
                    kerning 3
                    xalign 0.5

                hbox:
                    spacing 45
                    xalign 0.5

                    # Opción 1: PIEDRA (Guu)
                    button:
                        action Return("piedra")
                        style "janken_card_btn"
                        vbox:
                            spacing 14
                            xalign 0.5
                            yalign 0.5
                            add "gui/janken/hand_rock.png" ysize 170 fit "contain" xalign 0.5
                            text "PIEDRA (グー)":
                                size 22
                                bold True
                                color "#ffffff"
                                xalign 0.5
                            text "Vence a Tijera":
                                size 14
                                color "#94a3b8"
                                xalign 0.5

                    # Opción 2: PAPEL (Paa)
                    button:
                        action Return("papel")
                        style "janken_card_btn"
                        vbox:
                            spacing 14
                            xalign 0.5
                            yalign 0.5
                            add "gui/janken/hand_paper.png" ysize 170 fit "contain" xalign 0.5
                            text "PAPEL (パー)":
                                size 22
                                bold True
                                color "#ffffff"
                                xalign 0.5
                            text "Vence a Piedra":
                                size 14
                                color "#94a3b8"
                                xalign 0.5

                    # Opción 3: TIJERA (Choki)
                    button:
                        action Return("tijera")
                        style "janken_card_btn"
                        vbox:
                            spacing 14
                            xalign 0.5
                            yalign 0.5
                            add "gui/janken/hand_scissors.png" ysize 170 fit "contain" xalign 0.5
                            text "TIJERA (チョキ)":
                                size 22
                                bold True
                                color "#ffffff"
                                xalign 0.5
                            text "Vence a Papel":
                                size 14
                                color "#94a3b8"
                                xalign 0.5

            # --- 4. PIE DE PÁGINA ---
            text "«El destino puede ser alterado con una sola decisión...»":
                size 13
                color "#64748b"
                italic True
                xalign 0.5
                yalign 1.0


style janken_rival_card:
    xfill True
    ysize 170
    padding (32, 14, 32, 14)
    background Frame(Solid("#0d121ff2"), 8, 8)

style janken_foresight_badge:
    padding (20, 12, 20, 12)
    background Frame(Solid("#3b0d1af6"), 8, 8)
    xalign 1.0
    yalign 0.5

style janken_card_btn is gui_button:
    xsize 380
    ysize 360
    padding (24, 24, 24, 24)
    background Frame("gui/custom_btn/btn_idle.png", 10, 10)
    hover_background Frame("gui/custom_btn/btn_hover.png", 10, 10)
