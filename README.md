md
# Swimmy: Big Fish Eat Small Fish

## Description

Swimmy is a fun and engaging 2D underwater game built with Python and Pygame.  Players control a fish and navigate through an aquatic world, growing larger by consuming smaller fish while avoiding becoming prey to bigger ones. The game features simple controls, a scoring system, and visually appealing bubble effects.

## Images
<img src="images/picture1.png">
<img src="images/picture2.png">
<img src="images/picture3.png">

## Key Features & Benefits

-   **Engaging Gameplay:** Experience the thrill of survival in a dynamic underwater environment.
-   **Simple Controls:** Easy-to-learn controls using arrow keys for movement.
-   **Scoring System:** Track your progress and strive for a high score.
-   **Visual Appeal:**  Enjoy colorful graphics and bubble animations that enhance the underwater setting.
-   **Educational Potential:** Demonstrates simple game development concepts using Pygame.

## Prerequisites & Dependencies

Before you begin, ensure you have the following installed:

-   **Python:** Version 3.6 or higher.
-   **Pygame:** A Python library for creating games.  Install it using pip:

    ```bash
    pip install pygame
    ```

## Installation & Setup Instructions

Follow these steps to get Swimmy up and running:

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/wenbintan0907/Swimmy.git
    cd Swimmy
    ```

2.  **Install Dependencies:**

    ```bash
    pip install pygame  # If you haven't already
    ```

3.  **Run the Game:**

    ```bash
    python src/main.py
    ```

## Usage Examples & Gameplay

-   **Controls:**
    -   **Up Arrow:** Move up
    -   **Down Arrow:** Move down
    -   **Left Arrow:** Move left
    -   **Right Arrow:** Move right

-   **Objective:**
    -   Eat smaller fish to grow bigger.
    -   Avoid larger fish to survive.
    -   Track your score displayed in the top-left corner.

-   **Gameplay Loop:** Bubbles automatically appear as your fish swims, adding to the visual experience.

## Project Structure

```
Swimmy/
├── .DS_Store         # (Optional) macOS metadata file
├── README.md        # This file!
├── assets/          # Directory containing game assets (images)
│   ├── BtnPlay.png
│   ├── BtnPlayIcon.png
│   ├── BtnRestart.png
│   ├── Bubble.png
│   ├── Fish01_A.png
│   ├── Fish01_B.png
│   ├── Fish01_open.png
│   ├── Fish02_A.png
│   ├── Fish02_B.png
│   ├── Fish02_open.png
│   ├── Fish03_A.png
│   ├── Fish03_B.png
│   ├── Fish03_open.png
│   ├── Fish04_A.png
│   ├── Fish04_B.png
│   ├── Fish04_open.png
│   ├── Fish05_A.png
└── src/
    └── main.py      # Main game script
```

## Configuration Options

Currently, Swimmy does not have external configuration options.  Future versions may include customizable difficulty settings, screen resolution options, and sound volume controls.

## Contributing Guidelines

We welcome contributions to improve Swimmy!  Here's how you can contribute:

1.  **Fork the Repository:** Create your own fork of the Swimmy repository on GitHub.

2.  **Create a Branch:** Create a new branch for your feature or bug fix.

    ```bash
    git checkout -b feature/your-feature-name
    ```

3.  **Make Changes:** Implement your changes, ensuring code quality and proper testing.

4.  **Commit Changes:** Commit your changes with descriptive commit messages.

    ```bash
    git commit -m "Add your descriptive commit message here"
    ```

5.  **Push to Fork:** Push your branch to your forked repository.

    ```bash
    git push origin feature/your-feature-name
    ```

6.  **Create a Pull Request:** Submit a pull request from your branch to the main Swimmy repository.  Describe the changes you've made and any relevant information.

## License Information

This project does not currently have a specified license. All rights are reserved by the owner, wenbintan0907.
Please contact the owner for licensing information.

## Acknowledgments

-   Thanks to the Pygame community for providing a powerful and accessible game development library.
