# Asteroids Architecture

This document provides a high-level overview of the architectural structure of the Asteroids project.

## Class Diagram

The project is built using Python and Pygame, following an object-oriented approach. Below is a Mermaid class diagram illustrating the relationships between the main classes:

```mermaid
classDiagram
    class Sprite {
        <<pygame.sprite.Sprite>>
    }

    class CircleShape {
        +Vector2 position
        +Vector2 velocity
        +float radius
        +__init__(x, y, radius)
        +draw(screen)*
        +update(dt)*
        +collides_with(other) bool
    }

    class Player {
        +float rotation
        +float cooldown
        +__init__(x, y)
        +triangle() list~Vector2~
        +draw(screen)
        +rotate(dt)
        +update(dt)
        +move(dt)
        +shoot()
    }

    class Asteroid {
        +__init__(x, y, radius)
        +update(dt)
        +draw(screen)
        +split(asteroid)
    }

    class Shot {
        +__init__(x, y)
        +update(dt)
        +draw(screen)
    }

    class AsteroidField {
        +list edges
        +float spawn_timer
        +__init__()
        +spawn(radius, position, velocity)
        +update(dt)
    }

    Sprite <|-- CircleShape
    Sprite <|-- AsteroidField
    CircleShape <|-- Player
    CircleShape <|-- Asteroid
    CircleShape <|-- Shot
```

## System Overview

1. **Game Loop (`main.py`)**: 
   - Handles the initialization of Pygame.
   - Manages Pygame sprite groups (`updatable`, `drawable`, `asteroids`, `shots`) for efficient updating and rendering of game objects.
   - Contains the main loop which processes events, updates positions (via `dt`), detects collisions, and draws the frame.

2. **Base Shape (`circleshape.py`)**:
   - `CircleShape` extends `pygame.sprite.Sprite` and acts as a base class for all collidable physical objects in the game.
   - It provides `position`, `velocity`, `radius`, and a base `collides_with` method for circle-based collision detection.

3. **Game Entities**:
   - **`Player` (`player.py`)**: Extends `CircleShape`. Manages player inputs, rotation, movement, and shooting. It contains a cooldown timer to limit shooting frequency.
   - **`Asteroid` (`asteroid.py`)**: Extends `CircleShape`. Represents asteroids of various sizes. Handles moving and splitting into two smaller asteroids upon being hit.
   - **`Shot` (`shot.py`)**: Extends `CircleShape`. Represents projectiles fired by the player.

4. **Managers**:
   - **`AsteroidField` (`asteroidfield.py`)**: Extends `pygame.sprite.Sprite`. Manages the timed spawning of asteroids at the edges of the screen, launching them inwards at random angles and speeds.

5. **Utilities**:
   - **`constants.py`**: Holds game configuration constants like screen dimensions, speeds, and sizes.
   - **`logger.py`**: Handles event and state logging.
