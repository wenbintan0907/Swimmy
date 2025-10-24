# Swimmy
A fun 2D underwater game where you play as a fish trying to grow bigger by eating smaller fish while avoiding larger ones.

## 🎮 Gameplay
- Control your fish using arrow keys (↑, ↓, ←, →)
- Eat fish smaller than you to grow bigger
- Avoid larger fish - they'll eat you!
- Watch out for your score in the top-left corner
- Bubbles automatically appear as you swim

## 🔧 Requirements
Python 3.x
Pygame library

## 📥 Installation
1. Clone the repository
2. Install the required dependency:
   pip install pygame
3. Run the game:
   python src/main.py

## 🎯 Game Controls
- Arrow Up: Swim up
- Arrow Down: Swim down
- Arrow Left: Swim left
- Arrow Right: Swim right
- ESC: Quit game

## 🎨 Features
- Smooth swimming animations
- Dynamic background effects
- Different types of enemy fish
- Bubble particle effects
- Score tracking
- Size-based eating mechanics
- Menu system with play button
- FPS display

## 📁 Project Structure
Swimmy/
├── src/
│   └── main.py
└── assets/
    ├── Bubble.png
    ├── Fish01_A.png
    ├── Fish01_B.png
    ├── Fish02_A.png
    ├── Fish02_B.png
    ├── Fish03_A.png
    ├── Fish03_B.png
    ├── Fish04_A.png
    ├── Fish04_B.png
    ├── Scene_A.png
    ├── Scene_B.png
    ├── Title.png
    ├── BtnPlayIcon.png
    ├── wenxi.png
    ├── wenxi2.png
    └── wenxi_open.png
    
## 🎯 Game Goal
Grow as big as possible by eating smaller fish while avoiding larger ones. Your score increases based on the size of the fish you eat. The game ends if you collide with a fish larger than yourself.
