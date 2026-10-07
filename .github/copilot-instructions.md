# Instrucciones de Agentes de Desarrollo y Modelos de IA (NEXUS Agent Guidelines)

Este documento define las directrices y normas de diseño para todos los agentes autónomos de GitHub (GitHub Copilot Workspace, Coding Agents, CI Bots y Asistentes de IA) que operen en este repositorio.

---

## 🎯 Directrices de Arquitectura
1. **Motor Ren'Py:** Todo el código principal reside en archivos `.rpy` dentro de `game/`.
2. **Sintaxis Estricta:**
   - La sentencia `menu:` nunca debe llevar `:` al final de los textos descriptivos.
   - Preservar la resolución base de 1920x1080 Full HD.
   - Los bloques de Python deben situarse dentro de `init python:` o funciones modulares.
3. **Persistencia y Logros (`achievements.rpy`):**
   - Siempre invocar `$ grant_achievement("id")` en los puntos clave de la trama.
   - No resetear las variables `persistent` a menos que sea explícitamente requerido.
4. **Diseño Visual (Cyberpunk / Noir Glassmorphism):**
   - Evitar colores chillones o fondos planos; usar esquinas redondeadas, contrastes limpios y acentos del tema actual (`persistent.theme_color`).
   - El scrollbar lateral debe mantener un grosor de 10px con `unscrollable "hide"`.
5. **Flujo de Git:**
   - Todo trabajo autónomo debe crearse en una rama `feature/*` o `fix/*`.
   - Se debe abrir un Pull Request hacia la rama `develop` antes de promover a `main`.
