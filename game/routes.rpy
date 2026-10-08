## =============================================================================
## SISTEMA DE LÍNEAS ALTERNAS Y EFECTO MARIPOSA - NEXUS
## =============================================================================

default persistent.routes_view_tab = "shinshu"

init python:
    # Definición de las Líneas Temporales del Capítulo 1
    ROUTES_SHINSHU = [
        {
            "id": "nexus_1_shinshu",
            "title": "EVENTO NEXUS: EL DESPERTAR Y LA MIRADA CARMESÍ",
            "type": "NEXUS EVENT",
            "unlocked": "despertar" in persistent.unlocked_achievements,
            "desc": "Tras un mes en coma profundo por el choque, Shinshu Kazama despierta con la capacidad ocular de prever las muertes inminentes.",
            "unlocked_details": "Despertar confirmado en el Hospital General de Chūbu. La pupila derecha percibe coágulos de causalidad.",
            "locked_details": "Línea temporal no explorada aún. Juega la perspectiva de Shinshu para desbloquearla."
        },
        {
            "id": "mariposa_janken",
            "title": "EFECTO MARIPOSA 1: EL JANKEN FRATERNAL",
            "type": "DECISIÓN INICIAL",
            "unlocked": ("janken_jugar" in persistent.unlocked_achievements or "ojo_premonicion" in persistent.unlocked_achievements),
            "desc": "Aoi desafía a Shinshu a Piedra, Papel o Tijera para medir su lucidez.",
            "branches": [
                {
                    "name": "Ruta Confianza / Vínculo Fraternal",
                    "status": "janken_jugar" in persistent.unlocked_achievements,
                    "desc": "Jugar de forma limpia sin usar el ojo premonitorio.",
                    "consequence": "Vínculo emocional intacto; sosiego antes de la tempestad."
                },
                {
                    "name": "Ruta Visión Premonitoria Forzada",
                    "status": "ojo_premonicion" in persistent.unlocked_achievements,
                    "desc": "Canalizar la energía carmesí para anticipar la jugada de Aoi.",
                    "consequence": "Victoria asegurada, pero brota la duda sobre la naturaleza del ojo."
                }
            ]
        },
        {
            "id": "nexus_kenji_fatal",
            "title": "EVENTO NEXUS CLAVE: LA AGUJA DE LAS 18:00 (KENJI)",
            "type": "ENCRUCIJADA CAUSAL",
            "unlocked": ("tragedia_kenji" in persistent.unlocked_achievements or "salvar_kenji" in persistent.unlocked_achievements),
            "desc": "Kenji Takahashi recibirá una inyección de antibiótico a las 18:00 que contiene toxina letal.",
            "branches": [
                {
                    "name": "Bifurcación A: Advertir Directamente a Kenji",
                    "status": "tragedia_kenji" in persistent.unlocked_achievements,
                    "desc": "Suplicarle a Kenji que rechace la medicación.",
                    "consequence": "DESTINO TRÁGICO: Kenji cree que son delirios de sedantes y fallece por asfixia tóxica."
                },
                {
                    "name": "Bifurcación B: Guardar Silencio por Miedo",
                    "status": "tragedia_kenji" in persistent.unlocked_achievements,
                    "desc": "Ocultarse bajo las mantas temiendo ser catalogado demente.",
                    "consequence": "DESTINO TRÁGICO: Kenji colapsa en el suelo en silencio; la culpa atormenta a Shinshu."
                },
                {
                    "name": "Bifurcación C: Alertar al Dr. Moriyama",
                    "status": "salvar_kenji" in persistent.unlocked_achievements,
                    "desc": "Arrancarse las vías y salir gritando al pasillo para exigir una auditoría.",
                    "consequence": "HILO ROTO (ESPERANZA): El Dr. Moriyama requisa la ampolla a las 17:59. Kenji sobrevive."
                }
            ]
        }
    ]

    ROUTES_AOI = [
        {
            "id": "nexus_1_aoi",
            "title": "EVENTO NEXUS: EL DESPERTAR Y LA AUSENCIA DE SHINSHU",
            "type": "NEXUS EVENT",
            "unlocked": "despertar_aoi" in persistent.unlocked_achievements,
            "desc": "Aoi despierta del coma en el hospital de Nagano y descubre que Shinshu ya no está en este mundo.",
            "unlocked_details": "Despertar solitario. El dolor abre una percepción oculta ligada a los reflejos cristalinos.",
            "locked_details": "Línea temporal no explorada aún. Juega la perspectiva de Aoi para desbloquearla."
        },
        {
            "id": "mariposa_espejo_aoi",
            "title": "EVENTO NEXUS: EL REFLEJO MORTAL DEL LAVABO",
            "type": "PREMONICIÓN",
            "unlocked": "espejo_premonicion" in persistent.unlocked_achievements,
            "desc": "En el espejo del lavabo, Aoi presencia la discusión entre Yuna Sasaki y su padre a las 17:00, terminando en empujón mortal.",
            "unlocked_details": "Visión completa del punto ciego: una varilla metálica de construcción bajo la cama.",
            "locked_details": "Visión no presenciada todavía."
        },
        {
            "id": "nexus_yuna_fatal",
            "title": "ENCRUCIJADA CAUSAL: LA CAÍDA DE YUNA SASAKI",
            "type": "ENCRUCIJADA CAUSAL",
            "unlocked": ("tragedia_yuna" in persistent.unlocked_achievements or "salvar_yuna" in persistent.unlocked_achievements or "omision_yuna" in persistent.unlocked_achievements),
            "desc": "Tres caminos para responder a la premonición del espejo antes de las cinco de la tarde.",
            "branches": [
                {
                    "name": "Bifurcación A: Advertir Verbalmente a Yuna",
                    "status": "tragedia_yuna" in persistent.unlocked_achievements,
                    "desc": "Contar la visión a Yuna para evitar que discuta con su padre.",
                    "consequence": "DESTINO TRÁGICO: Yuna se enoja, la discusión se intensifica y la caída ocurre sin poder frenarla."
                },
                {
                    "name": "Bifurcación B: Retirar la Varilla de Madrugada",
                    "status": "salvar_yuna" in persistent.unlocked_achievements,
                    "desc": "Arrastrarse bajo la cama y extraer el filo punzante, asumiendo el estigma psiquiátrico.",
                    "consequence": "HILO ROTO (ESPERANZA): Yuna cae al suelo pero no hay filo mortal; Aoi es aislada en psiquiatría pero salva su vida."
                },
                {
                    "name": "Bifurcación C: Omisión por Miedo a la Locura",
                    "status": "omision_yuna" in persistent.unlocked_achievements,
                    "desc": "Quedarse inmóvil creyendo que fue una alucinación post-coma.",
                    "consequence": "DESTINO TRÁGICO: Yuna fallece exactamente como el espejo anticipó; Aoi vive con la culpa."
                }
            ]
        }
    ]


## Pantalla de Líneas Alternas y Efecto Mariposa
screen alternate_routes():
    tag menu

    use game_menu(_("Líneas Alternas y Eventos Causa"), scroll="viewport"):
        vbox:
            spacing 24
            xfill True

            # Barra superior con selector de perspectiva de líneas
            hbox:
                spacing 16
                xalign 0.5

                textbutton _("Línea Carmesí (Shinshu)"):
                    action SetVariable("persistent.routes_view_tab", "shinshu")
                    selected (persistent.routes_view_tab == "shinshu")
                    style "navigation_button"

                textbutton _("Línea Amatista (Aoi)"):
                    action SetVariable("persistent.routes_view_tab", "aoi")
                    selected (persistent.routes_view_tab == "aoi")
                    style "navigation_button"

            # Resumen de estado de exploración causal
            $ current_routes = ROUTES_SHINSHU if persistent.routes_view_tab == "shinshu" else ROUTES_AOI
            $ completed_nodes = sum(1 for r in current_routes if r.get("unlocked", False))
            $ total_nodes = len(current_routes)

            frame:
                background Solid("#080d1a")
                xfill True
                padding (20, 16)

                hbox:
                    spacing 20
                    yalign 0.5

                    text "ÁRBOL CAUSAL DEL CAPÍTULO 1":
                        font gui.interface_text_font
                        size 13
                        bold True
                        color (persistent.theme_border or "#e63946")
                        kerning 3

                    text "•":
                        color "#475569"

                    text ("Nodos Explorados: " + str(completed_nodes) + " / " + str(total_nodes)) substitute False:
                        font gui.interface_text_font
                        size 13
                        color "#38bdf8"

            # Render de cada Nodo del Árbol Causal
            for route in current_routes:
                frame:
                    xfill True
                    background Solid("#050811")
                    padding (22, 18)

                    vbox:
                        spacing 14
                        xfill True

                        hbox:
                            spacing 14
                            yalign 0.5

                            if route.get("unlocked", False):
                                text "●":
                                    size 14
                                    color (persistent.theme_border or "#e63946")
                                text route["title"] substitute False:
                                    font gui.name_text_font
                                    size 16
                                    bold True
                                    color "#ffffff"
                                text "(Desbloqueado)" substitute False:
                                    font gui.interface_text_font
                                    size 11
                                    color "#4ade80"
                                    bold True
                            else:
                                text "○":
                                    size 14
                                    color "#64748b"
                                text route["title"] substitute False:
                                    font gui.name_text_font
                                    size 16
                                    bold True
                                    color "#64748b"
                                text "(No Explorada)" substitute False:
                                    font gui.interface_text_font
                                    size 11
                                    color "#ef4444"
                                    bold True

                        text route["desc"] substitute False:
                            font gui.interface_text_font
                            size 13
                            color "#94a3b8"

                        # Si tiene bifurcaciones o ramas
                        if "branches" in route:
                            frame:
                                background Solid("#0a0f20")
                                padding (16, 14)
                                xfill True

                                vbox:
                                    spacing 12

                                    text "BIFURCACIONES Y EFECTO MARIPOSA:":
                                        font gui.interface_text_font
                                        size 11
                                        bold True
                                        color "#cbd5e1"
                                        kerning 2

                                    for b in route["branches"]:
                                        frame:
                                            background Solid("#03060f")
                                            padding (14, 10)
                                            xfill True

                                            vbox:
                                                spacing 4

                                                hbox:
                                                    spacing 10
                                                    if b.get("status", False):
                                                        text "✓":
                                                            size 13
                                                            color "#4ade80"
                                                            bold True
                                                        text b["name"] substitute False:
                                                            font gui.interface_text_font
                                                            size 13
                                                            bold True
                                                            color "#f8fafc"
                                                        text "(Ruta Experimentada)" substitute False:
                                                            font gui.interface_text_font
                                                            size 10
                                                            color "#4ade80"
                                                    else:
                                                        text "○":
                                                            size 12
                                                            color "#64748b"
                                                        text b["name"] substitute False:
                                                            font gui.interface_text_font
                                                            size 13
                                                            bold True
                                                            color "#64748b"
                                                        text "(No Explorada)" substitute False:
                                                            font gui.interface_text_font
                                                            size 10
                                                            color "#94a3b8"

                                                if b.get("status", False):
                                                    text b["consequence"] substitute False:
                                                        font gui.interface_text_font
                                                        size 12
                                                        color "#e2e8f0"
                                                else:
                                                    text "Consecuencia causal bloqueada. Toma decisiones diferentes en una nueva partida para desbloquear esta línea." substitute False:
                                                        font gui.interface_text_font
                                                        size 11
                                                        color "#475569"
                                                        italic True
                        else:
                            if route.get("unlocked", False):
                                text route.get("unlocked_details", "") substitute False:
                                    font gui.interface_text_font
                                    size 12
                                    color "#38bdf8"
                            else:
                                text route.get("locked_details", "Línea temporal no explorada aún.") substitute False:
                                    font gui.interface_text_font
                                    size 12
                                    color "#64748b"
                                    italic True
