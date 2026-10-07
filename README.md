# NEXUS: 宿命の瞳 (Los Ojos del Destino)

[![CI/CD Pipeline](https://github.com/MiguelCarlosRojas/Nexus/actions/workflows/ci.yml/badge.svg)](https://github.com/MiguelCarlosRojas/Nexus/actions/workflows/ci.yml)
[![Latest Release](https://img.shields.io/github/v/release/MiguelCarlosRojas/Nexus?color=e63946&label=Release)](https://github.com/MiguelCarlosRojas/Nexus/releases)
[![Ren'Py Version](https://img.shields.io/badge/Ren'Py-8.5+-ff1e44.svg)](https://www.renpy.org/)
[![License](https://img.shields.io/badge/License-Proprietary%20%2F%20Creative-blue.svg)](COPYRIGHT.md)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com/MiguelCarlosRojas/Nexus/releases)

> *"La muerte no se cancela... solo transfiere sus ojos a quien la desafía."*

**NEXUS: 宿命の瞳** es una novela visual de suspenso psicológico, misterio y thriller sobrenatural desarrollada en el motor **Ren'Py**. La historia transcurre en la región montañosa de Chūbu y la ciudad de Matsumoto (Prefectura de Nagano, Japón Central), explorando el dilema moral entre la predestinación y el libre albedrío a través de los ojos de un joven que ha despertado con la facultad de vislumbrar el instante exacto y la causa de la muerte de quienes le rodean.

---

## 📖 Sinopsis del Capítulo 1: El Despertar de Shinshu

Tras un catastrófico impacto en el que salva la vida de su hermana menor Aoi, **Ren Kasugai** despierta de un coma profundo de años en la habitación 304 del Hospital General de Shinshu. Sin embargo, su cuerpo y mente ya no son los mismos: detrás de sus pupilas ha despertado la **Mirada Carmesí**, un don o maldición capaz de proyectar los momentos finales y las bifurcaciones mortales de la gente.

Al interactuar con su compañero de cuarto, el risueño Kenji Takahashi, Ren descubre horrorizado que a las 18:00 horas una enfermera le administrará una dosis envenenada que lo asfixiará en tres minutos. Con los segundos corriendo en su contra, Ren deberá decidir si guardar silencio, advertir a su amigo o desafiar los protocolos del severo Dr. Moriyama para alterar por primera vez los hilos del destino.

---

## ✨ Características Principales

* **Narrativa Ramificada y Consecuencias Reales:** Múltiples desenlaces y rutas en el Capítulo 1 (*Destino Consumado* vs. *El Hilo Roto*).
* **Minijuego Interactivo de Janken (Piedra, Papel o Tijera):**
  * Duelo mental interactivo contra Aoi con cartas estilizadas HD.
  * Habilidad de activar la **Visión Premonitoria Ocular** para ralentizar el tiempo y vislumbrar los tendones y la decisión de tu rival antes de que mueva la mano.
* **Sistema Integral de Logros, XP, Nivel y Ranking Dinámico (`achievements.rpy`):**
  * Catálogo de 110 logros enlazados a los hitos del juego.
  * Experiencia (XP) acumulativa y cálculo de nivel del jugador en vivo.
  * Pestañas con filtros en tiempo real (*Todos*, *Desbloqueados*, *Bloqueados*, *Recientes*, *Ranking*).
  * Buscador instantáneo de logros.
  * **Ranking Top 20 por XP:** Únete con tu apodo personalizado y compite por los puestos más altos de la temporada.
* **Interfaz de Usuario de Alta Gama (Cyberpunk Glassmorphism):**
  * Barra de desplazamiento lateral (*Scrollbar*) ultra fina (10px) con auto-ocultamiento y resplandor carmesí reactivo.
  * Modal Popups de confirmación con animación de profundidad y botones estructurados.
  * Menú rápido flotante translúcido al pie de los diálogos.
  * Sistema de temas de color dinámicos (Carmesí, Azul Noche, Oro Shinshu, Jade Imperial).
  * Control y presets precisos de volumen de sonido e interruptor de silencio (*Mute*).

---

## 🎮 Descarga e Instalación

Puedes descargar las versiones compiladas y los paquetes de assets listos para jugar desde la sección de **[Releases](https://github.com/MiguelCarlosRojas/Nexus/releases)**.

### Para Desarrolladores y Jugadores con Ren'Py:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/MiguelCarlosRojas/Nexus.git
   ```
2. Abre **Ren'Py Launcher** (versión 8.2 o superior).
3. Añade la carpeta del proyecto `Nexus` en la lista de proyectos.
4. Presiona **Lanzar Proyecto (Launch Project)**.

---

## 📂 Arquitectura del Repositorio

```
Nexus/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md          # Plantilla para reporte de errores
│   │   └── feature_request.md     # Plantilla para nuevas sugerencias
│   ├── workflows/
│   │   ├── ci.yml                 # Integración continua (Validación y Linting)
│   │   └── release.yml            # Automatización de empaquetado y releases
│   ├── PULL_REQUEST_TEMPLATE.md   # Estándar de Pull Requests
│   └── copilot-instructions.md    # Guía para agentes de IA y desarrollo guiado
├── game/
│   ├── achievements.rpy       # Motor de logros, XP, nivel y ranking
│   ├── gui.rpy                # Estilos visuales y configuraciones de UI
│   ├── options.rpy            # Opciones de compilación y metadata
│   ├── screens.rpy            # Pantallas del menú, UI moderna y minijuegos
│   ├── script.rpy             # Guion literario y ramificaciones del Capítulo 1
│   ├── audio/                 # Efectos de sonido y temas melancólicos de piano
│   ├── gui/                   # Texturas HD de botones, barras y modales
│   └── images/                # Siluetas, fondos y emblemas
├── CODE_OF_CONDUCT.md         # Normas comunitarias (Contributor Covenant v2.1)
├── COPYRIGHT.md               # Derechos de autor y licencias de assets
├── README.md                  # Documentación central del proyecto
├── errors.txt                 # Registro de diagnóstico de compilación Ren'Py
├── log.txt                    # Log de ejecución del motor
└── .gitignore                 # Exclusión de archivos compilados y temporales
```

---

## 🛠️ Flujo de Trabajo Git (GitFlow)

* `main`: Rama de producción estable. Cada cambio se etiqueta con un **Tag/Release**.
* `develop`: Rama principal de integración y desarrollo continuo.
* `feature/*`: Ramas dedicadas para módulos, capítulos y componentes grandes. Cada cambio se promueve vía **Pull Request** a `develop` y posteriormente a `main`.

---

## 👥 Créditos y Autoría

* **Dirección, Guion y Diseño:** Miguel Carlos Rojas.
* **Motor:** Ren'Py Engine (Python 3.12 / Cython).
* **Contacto y Soporte:** [GitHub Issues](https://github.com/MiguelCarlosRojas/Nexus/issues).
