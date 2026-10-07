## =============================================================================
## SISTEMA INTEGRADO DE LOGROS, XP, NIVEL Y RANKING - NEXUS
## =============================================================================

default persistent.unlocked_achievements = []
default persistent.recent_achievements = []
default persistent.player_nickname = "Ren Kasugai"
default persistent.player_in_ranking = False
default persistent.ranking_list = []

init python:

    TOTAL_ACHIEVEMENTS_COUNT = 110

    # Base de datos completa de logros de NEXUS
    # Capítulo 1 (Activos y desbloqueables durante la partida) + Próximos capítulos
    ACHIEVEMENTS_DB = [
        # --- CAPÍTULO 1: EL DESPERTAR Y LA PRIMERA ELECCIÓN ---
        {
            "id": "despertar",
            "name": "El Despertar de Shinshu",
            "desc": "Sobrevive al impacto del camión, supera el coma profundo y despierta en el Hospital General de Chūbu.",
            "xp": 25,
            "chapter": "Capítulo 1",
            "secret": False
        },
        {
            "id": "janken_jugar",
            "name": "Vínculo de Hermandad",
            "desc": "Acepta el reto de Aoi y juega una partida de Piedra, Papel o Tijera en la camilla del hospital.",
            "xp": 15,
            "chapter": "Capítulo 1",
            "secret": False
        },
        {
            "id": "janken_victoria",
            "name": "Reflejos del Destino",
            "desc": "Vence limpiamente a tu hermana menor Aoi en el minijuego de Piedra, Papel o Tijera.",
            "xp": 20,
            "chapter": "Capítulo 1",
            "secret": False
        },
        {
            "id": "ojo_premonicion",
            "name": "Ojo de la Premonición",
            "desc": "Usa la visión de tus pupilas carmesíes para anticipar la jugada de Aoi.",
            "xp": 20,
            "chapter": "Capítulo 1",
            "secret": False
        },
        {
            "id": "mirada_carmesi",
            "name": "La Mirada Carmesí",
            "desc": "Presencia por primera vez la muerte en los ojos del anciano en el pasillo del hospital.",
            "xp": 30,
            "chapter": "Capítulo 1",
            "secret": False
        },
        {
            "id": "encrucijada_kenji",
            "name": "Encrucijada a las 17:52",
            "desc": "Descubre los dos futuros divergentes de Kenji Takahashi antes de las seis de la tarde.",
            "xp": 25,
            "chapter": "Capítulo 1",
            "secret": False
        },
        {
            "id": "salvar_kenji",
            "name": "Hilos Quebrados (Salvación)",
            "desc": "Alerta con valentía al Dr. Moriyama e impide que le administren la inyección letal a Kenji.",
            "xp": 50,
            "chapter": "Capítulo 1",
            "secret": False
        },
        {
            "id": "tragedia_kenji",
            "name": "Veneno en la Sangre (Destino)",
            "desc": "Presencia la aterradora agonía y muerte de Kenji tras administrarse la dosis envenenada.",
            "xp": 40,
            "chapter": "Capítulo 1",
            "secret": False
        },
        {
            "id": "fin_capitulo_1",
            "name": "Fin del Prólogo de Shinshu",
            "desc": "Completa cualquiera de los dos desenlaces del primer capítulo de NEXUS.",
            "xp": 30,
            "chapter": "Capítulo 1",
            "secret": False
        },

        # --- PRÓXIMOS CAPÍTULOS (PRÓXIMOS A DESBLOQUEAR / BLOQUEADOS) ---
        {
            "id": "cap2_alta_medica",
            "name": "Pasos Fuera del Umbral",
            "desc": "Recibe el alta médica del Hospital de Shinshu y regresa a las calles de Matsumoto.",
            "xp": 20,
            "chapter": "Capítulo 2",
            "secret": True
        },
        {
            "id": "cap2_secreto_farmacia",
            "name": "La Fórmula Silenciosa",
            "desc": "Investiga los registros adulterados del almacén farmacéutico regional.",
            "xp": 35,
            "chapter": "Capítulo 2",
            "secret": True
        },
        {
            "id": "cap2_encuentro_sombras",
            "name": "Ojos en la Niebla",
            "desc": "Descubre que no eres el único portador de la mirada carmesí en Nagano.",
            "xp": 45,
            "chapter": "Capítulo 2",
            "secret": True
        },
        {
            "id": "cap2_promesa_aoi",
            "name": "El Té Helado Prometido",
            "desc": "Cumple la promesa de la cafetería con Aoi tras abandonar el hospital.",
            "xp": 15,
            "chapter": "Capítulo 2",
            "secret": True
        },
        {
            "id": "cap3_vision_colectiva",
            "name": "Ecos en el Cruce Peatonal",
            "desc": "Vislumbra el destino simultáneo de más de diez transeúntes a la vez.",
            "xp": 50,
            "chapter": "Capítulo 3",
            "secret": True
        },
        {
            "id": "cap3_cirujano_sospechoso",
            "name": "Bisturí de Dos Filos",
            "desc": "Descubre las verdaderas anotaciones secretas del Dr. Moriyama.",
            "xp": 40,
            "chapter": "Capítulo 3",
            "secret": True
        },
        {
            "id": "cap3_sacrificio_evitado",
            "name": "Desafío a las Parcas",
            "desc": "Altera una tercera muerte predestinada sin perder la cordura en el intento.",
            "xp": 60,
            "chapter": "Capítulo 3",
            "secret": True
        },
        {
            "id": "cap4_memoria_perdida",
            "name": "El Espejo Fragmentado",
            "desc": "Recupera el recuerdo bloqueado del día del choque del camión.",
            "xp": 75,
            "chapter": "Capítulo 4",
            "secret": True
        },
        {
            "id": "cap4_el_origen_ocular",
            "name": "La Pupila del Juicio",
            "desc": "Comprende el pacto oscuro que salvó a tu hermana menor en tu infancia.",
            "xp": 80,
            "chapter": "Capítulo 4",
            "secret": True
        },
        {
            "id": "cap5_nexus_revelado",
            "name": "Sinfonía Carmesí",
            "desc": "Enfrenta la convergencia final de todos los hilos del destino entrelazados.",
            "xp": 100,
            "chapter": "Capítulo 5",
            "secret": True
        },
    ]

    # Generación programática de los logros restantes de la saga hasta completar 110
    _chapter_names = ["Capítulo 2: Niebla en Matsumoto", "Capítulo 3: La Red del Destino", "Capítulo 4: Cenizas del Pasado", "Capítulo 5: El Fin del Juicio"]
    _tier_xp = [20, 25, 30, 35, 40, 50, 60]
    for i in range(len(ACHIEVEMENTS_DB) + 1, TOTAL_ACHIEVEMENTS_COUNT + 1):
        c_name = _chapter_names[(i % len(_chapter_names))]
        xp_val = _tier_xp[(i % len(_tier_xp))]
        ACHIEVEMENTS_DB.append({
            "id": "nex_ach_{}".format(i),
            "name": "Fragmento del Destino #{}".format(i),
            "desc": "Logro avanzado de la saga NEXUS: Desbloqueable al explorar los caminos ocultos de {}.".format(c_name),
            "xp": xp_val,
            "chapter": c_name.split(":")[0],
            "secret": True
        })

    def get_achievement_by_id(ach_id):
        for ach in ACHIEVEMENTS_DB:
            if ach["id"] == ach_id:
                return ach
        return None

    def is_achievement_unlocked(ach_id):
        if persistent.unlocked_achievements is None:
            persistent.unlocked_achievements = []
        return ach_id in persistent.unlocked_achievements

    def grant_achievement(ach_id):
        """Desbloquea un logro, actualiza XP, historial reciente y muestra notificación sonora y visual."""
        if persistent.unlocked_achievements is None:
            persistent.unlocked_achievements = []
        if persistent.recent_achievements is None:
            persistent.recent_achievements = []

        if ach_id not in persistent.unlocked_achievements:
            ach = get_achievement_by_id(ach_id)
            if ach:
                persistent.unlocked_achievements.append(ach_id)
                # Mantener lista de recientes (últimos 10)
                if ach_id in persistent.recent_achievements:
                    persistent.recent_achievements.remove(ach_id)
                persistent.recent_achievements.insert(0, ach_id)
                if len(persistent.recent_achievements) > 10:
                    persistent.recent_achievements = persistent.recent_achievements[:10]

                # Notificación en pantalla
                msg = _("¡LOGRO DESBLOQUEADO!\n{name} (+{xp} XP)").format(
                    name=ach["name"], xp=ach["xp"]
                )
                try:
                    renpy.play("audio/eye_vision.wav", channel="sound")
                except:
                    pass
                renpy.notify(msg)

                # Si está en el ranking, actualizar ranking
                if persistent.player_in_ranking:
                    update_player_in_ranking()

                renpy.restart_interaction()
                return True
        return False

    def get_total_player_xp():
        """Calcula el total acumulado de XP a partir de los logros desbloqueados."""
        if not persistent.unlocked_achievements:
            return 0
        total = 0
        for ach_id in persistent.unlocked_achievements:
            ach = get_achievement_by_id(ach_id)
            if ach:
                total += ach.get("xp", 0)
        return total

    def get_player_level():
        """Nivel dinámico en base al XP del jugador."""
        xp = get_total_player_xp()
        return max(1, 1 + (xp // 50))

    def get_unlocked_count():
        if not persistent.unlocked_achievements:
            return 0
        return len(persistent.unlocked_achievements)

    def get_achievements_percent():
        total = TOTAL_ACHIEVEMENTS_COUNT
        unlocked = get_unlocked_count()
        if total == 0:
            return 0
        return int((unlocked * 100) / total)

    def get_recorrido_count():
        # Representa los nodos de historia y logros descubiertos
        return get_unlocked_count()

    def get_filtered_achievements():
        """Devuelve los logros según la pestaña seleccionada y el texto de búsqueda."""
        f = persistent.achievement_filter or "Todos"
        search = (persistent.achievement_search or "").strip().lower()

        results = []

        if f == "Desbloqueados":
            for ach in ACHIEVEMENTS_DB:
                if is_achievement_unlocked(ach["id"]):
                    results.append(ach)
        elif f == "Bloqueados":
            for ach in ACHIEVEMENTS_DB:
                if not is_achievement_unlocked(ach["id"]):
                    results.append(ach)
        elif f == "Recientes":
            if persistent.recent_achievements:
                for ach_id in persistent.recent_achievements:
                    ach = get_achievement_by_id(ach_id)
                    if ach:
                        results.append(ach)
            else:
                # Si aún no hay recientes, mostrar los desbloqueados
                for ach in ACHIEVEMENTS_DB:
                    if is_achievement_unlocked(ach["id"]):
                        results.append(ach)
        else: # "Todos"
            results = list(ACHIEVEMENTS_DB)

        # Aplicar búsqueda si hay texto
        if search:
            filtered = []
            for ach in results:
                if search in ach["name"].lower() or search in ach["desc"].lower():
                    filtered.append(ach)
            return filtered

        return results

    def update_player_in_ranking():
        """Asegura que el jugador esté registrado en el ranking con sus estadísticas reales."""
        nick = persistent.player_nickname or "Ren Kasugai"
        xp = get_total_player_xp()
        lvl = get_player_level()
        logros = get_unlocked_count()

        if persistent.ranking_list is None:
            persistent.ranking_list = []

        # Buscar si ya existe el jugador
        updated = False
        for entry in persistent.ranking_list:
            if entry.get("is_player"):
                entry["nickname"] = nick
                entry["xp"] = xp
                entry["level"] = lvl
                entry["achievements"] = logros
                updated = True
                break

        if not updated:
            persistent.ranking_list.append({
                "nickname": nick,
                "xp": xp,
                "level": lvl,
                "achievements": logros,
                "is_player": True
            })

        # Ordenar ranking por XP descendente
        persistent.ranking_list.sort(key=lambda x: x["xp"], reverse=True)

    def join_ranking_action():
        persistent.player_in_ranking = True
        update_player_in_ranking()
        renpy.restart_interaction()

    def set_player_nickname(new_name):
        clean = new_name.strip()
        if clean:
            persistent.player_nickname = clean
            if persistent.player_in_ranking:
                update_player_in_ranking()
        renpy.restart_interaction()

    def reset_all_progress():
        """Restablece todo el progreso del jugador, logros, ranking y XP a cero absoluto."""
        persistent.unlocked_achievements = []
        persistent.recent_achievements = []
        persistent.player_nickname = ""
        persistent.player_in_ranking = False
        persistent.ranking_list = []
        persistent.janken_played = 0
        persistent.janken_won = 0
        try:
            renpy.save_persistent()
        except:
            pass
        try:
            renpy.notify(_("Progreso restablecido: 0 Logros, 0 XP (Nivel 1)."))
        except:
            pass
        renpy.restart_interaction()

