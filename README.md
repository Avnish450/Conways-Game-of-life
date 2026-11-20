# Conway's Game of Life

A lightweight, zero-dependency terminal simulation of John Conway's famous cellular automaton in Python.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## Overview

**Conway's Game of Life** is a zero-player game devised by mathematician John Horton Conway in 1970. Its evolution is determined solely by its initial configuration:

1. **Survival**: Any live cell with two or three live neighbors survives into the next generation.
2. **Birth**: Any dead cell with exactly three live neighbors becomes a live cell.
3. **Death**: Any live cell with fewer than two neighbors (underpopulation) or more than three neighbors (overpopulation) dies.

This implementation wraps seamlessly on the grid borders (torus topology) and uses ANSI cursor controls for a smooth, flicker-free terminal experience.

---

## Features

- **Zero External Dependencies**: Runs entirely on the Python Standard Library.
- **Customizable Grid**: Adjust width, height, density, and animation speed via command-line arguments.
- **Configurable Visuals**: Choose custom characters for live and dead cells (e.g. `#`, `■`, `*`, `O`).
- **Smooth Animation**: Utilizes ANSI escape codes instead of repeated newline scrolling.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher installed on your system.

### Running the Simulation

Clone the repository and run:

```bash
python3 main.py
```

Press `Ctrl+C` at any time to cleanly stop the simulation.

---

## Configuration & CLI Options

You can customize the simulation parameters directly from the command line:

```bash
python3 main.py --help
```

### Available Options

| Flag | Long Option | Default | Description |
|---|---|---|---|
| `-W` | `--width` | `70` | Grid width (columns) |
| `-H` | `--height` | `20` | Grid height (rows) |
| `-s` | `--speed` | `0.15` | Delay in seconds between generations |
| `-d` | `--density` | `0.3` | Probability (0.0 to 1.0) of initial cells being alive |
| | `--alive` | `'O'` | Display character for living cells |
| | `--dead` | `' '` | Display character for empty cells |

### Examples

**High-density, fast simulation with square block characters:**
```bash
python3 main.py -W 80 -H 30 -d 0.4 -s 0.08 --alive "#"
```

**Spacious, slow visualization:**
```bash
python3 main.py -W 50 -H 15 -s 0.3 --alive "●" --dead "·"
```

---

## Project Structure

```text
conways-game-of-life/
├── main.py          # Core simulation logic and CLI entrypoint
├── README.md        # Project documentation
├── LICENSE          # MIT License
└── .gitignore       # Python Git ignore rules
```

---

## Contributing

Contributions, bug reports, and feature suggestions are welcome! Feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).
