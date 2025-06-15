<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Asteroids Game 🚀

Ein klassisches Asteroids-Spiel implementiert in Python mit Pygame. Steuere dein Raumschiff durch ein Asteroidenfeld, schieße auf Asteroiden und überlebe so lange wie möglich!

## 🎮 Gameplay

- Steuere ein dreieckiges Raumschiff durch den Weltraum
- Asteroiden spawnen kontinuierlich von den Bildschirmrändern
- Schieße auf Asteroiden, um sie zu zerstören
- Große Asteroiden teilen sich in kleinere, schnellere Asteroiden auf
- Vermeide Kollisionen mit Asteroiden - ein Treffer bedeutet Game Over!


## 🕹️ Steuerung

| Taste | Aktion |
| :-- | :-- |
| **A** | Nach links drehen |
| **D** | Nach rechts drehen |
| **W** | Vorwärts bewegen |
| **S** | Rückwärts bewegen |
| **Leertaste** | Schießen |

## 🛠️ Installation \& Setup

### Voraussetzungen

- Python 3.7 oder höher
- pygame


### Installation

1. Repository klonen:
```bash
git clone https://github.com/yourusername/asteroids-game.git
cd asteroids-game
```

2. Pygame installieren:
```bash
pip install pygame
```

3. Spiel starten:
```bash
python main.py
```


## 📁 Projektstruktur

```
asteroids-game/
├── main.py           # Hauptspiel-Loop und Initialisierung
├── player.py         # Spieler-Raumschiff Klasse
├── asteroid.py       # Asteroid Klasse mit Splitting-Logik
├── asteroidfield.py  # Asteroid-Spawning System
├── shot.py           # Projektil/Schuss Klasse
├── circleshape.py    # Basis-Klasse für alle Spielobjekte
├── constants.py      # Spiel-Konstanten und Einstellungen
└── README.md         # Diese Datei
```


## 🎯 Features

- **Realistische Physik**: Objekte bewegen sich mit konstanter Geschwindigkeit in geraden Linien
- **Kollisionserkennung**: Präzise kreisförmige Kollisionserkennung zwischen allen Objekten
- **Asteroid-Splitting**: Große Asteroiden teilen sich in kleinere, schnellere Asteroiden auf
- **Schuss-Cooldown**: Verhindert Spam-Schießen für ausgewogenes Gameplay
- **Smooth Controls**: Framerate-unabhängige Bewegung und Rotation
- **Automatisches Spawning**: Kontinuierliches Spawnen neuer Asteroiden von den Bildschirmrändern


## ⚙️ Konfiguration

Die Spiel-Parameter können in `constants.py` angepasst werden:

```python
# Bildschirm
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Spieler
PLAYER_RADIUS = 20
PLAYER_SPEED = 200
PLAYER_TURN_SPEED = 300
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3

# Asteroiden
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8

# Schüsse
SHOT_RADIUS = 5
```


## 🏗️ Architektur

Das Spiel verwendet eine objektorientierte Architektur mit pygame Groups:

- **CircleShape**: Basis-Klasse für alle Spielobjekte mit Kollisionserkennung
- **Player**: Spieler-Raumschiff mit Bewegung, Rotation und Schießen
- **Asteroid**: Asteroiden mit Splitting-Logik
- **Shot**: Projektile mit geradliniger Bewegung
- **AsteroidField**: Verwaltet das Spawning neuer Asteroiden
- **Groups**: Organisiert Objekte in updatable, drawable, asteroids und shots


## 🎨 Grafik

- Minimalistisches Design mit weißen Linien auf schwarzem Hintergrund
- Raumschiff als Dreieck dargestellt
- Asteroiden und Schüsse als Kreise
- Alle Objekte mit 2-Pixel Linienbreite für klare Sichtbarkeit


## 🚀 Mögliche Erweiterungen

- [ ] Score-System
- [ ] Mehrere Leben
- [ ] Power-Ups
- [ ] Verschiedene Waffentypen
- [ ] Sound-Effekte
- [ ] Partikel-Effekte
- [ ] Highscore-Liste
- [ ] Verschiedene Schwierigkeitsgrade


## 🤝 Beitragen

1. Fork das Repository
2. Erstelle einen Feature-Branch (`git checkout -b feature/AmazingFeature`)
3. Committe deine Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Push zum Branch (`git push origin feature/AmazingFeature`)
5. Öffne einen Pull Request

## 📝 Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe `LICENSE` Datei für Details.

## 🙏 Danksagungen

- Inspiriert vom klassischen Atari Asteroids (1979)
- Entwickelt als Lernprojekt mit Pygame
- Dank an die Pygame-Community für die ausgezeichnete Dokumentation

---

**Viel Spaß beim Spielen! 🎮**

