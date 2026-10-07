---
name: "Gameplay & UI Agent"
description: "Especialista en interfaces Ren'Py, minijuegos interactivos y sistema dinámico de logros/XP/ranking."
targets:
  - "game/screens.rpy"
  - "game/achievements.rpy"
  - "game/gui.rpy"
rules:
  - "Garantizar diseño glassmorphic moderno, responsivo y sin desbordamientos de botones."
  - "Verificar que cada minijuego registre estadísticas persistentes y otorgue XP a persistent.player_xp."
  - "Mantener la coherencia estética con las texturas en game/gui/custom_btn y game/gui/janken."
---

# NEXUS Gameplay & UI Agent

Este agente opera en la pestaña **Agents** de GitHub para:
1. Crear e integrar nuevos minijuegos temáticos en la historia de Ren'Py.
2. Añadir nuevos logros a la base de datos de 110 logros en `game/achievements.rpy`.
3. Ajustar interfaces gráficas, scrollbars modernas y modales de configuración.
