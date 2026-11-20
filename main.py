#!/usr/bin/env python3
"""Conway's Game of Life - Terminal Edition.

An interactive cellular automaton simulation executed in the console.
"""

from __future__ import annotations

import argparse
import random
import sys
import time
from typing import Dict, Tuple

Coordinate = Tuple[int, int]
Grid = Dict[Coordinate, bool]


class GameOfLife:
    """Manages the state and rules for Conway's Game of Life."""

    def __init__(
        self,
        width: int = 70,
        height: int = 20,
        alive_char: str = "O",
        dead_char: str = " ",
        density: float = 0.3,
    ) -> None:
        self.width = width
        self.height = height
        self.alive_char = alive_char
        self.dead_char = dead_char
        self.density = density
        self.generation = 0
        self.grid: Grid = self._initialize_random_grid()

    def _initialize_random_grid(self) -> Grid:
        """Generates an initial grid with randomized cell states."""
        return {
            (x, y): random.random() < self.density
            for x in range(self.width)
            for y in range(self.height)
        }

    def count_living_neighbors(self, x: int, y: int) -> int:
        """Counts alive neighbors surrounding (x, y) with toroidal wrap-around."""
        count = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx = (x + dx) % self.width
                ny = (y + dy) % self.height
                if self.grid.get((nx, ny), False):
                    count += 1
        return count

    def step(self) -> None:
        """Advances the simulation by one generation according to Conway's rules."""
        next_grid: Grid = {}

        for x in range(self.width):
            for y in range(self.height):
                alive = self.grid.get((x, y), False)
                neighbors = self.count_living_neighbors(x, y)

                # Conway's Rules:
                # 1. Any live cell with 2 or 3 live neighbors survives.
                # 2. Any dead cell with exactly 3 live neighbors becomes a live cell.
                # 3. All other live cells die (underpopulation/overpopulation).
                if alive and neighbors in (2, 3):
                    next_grid[(x, y)] = True
                elif not alive and neighbors == 3:
                    next_grid[(x, y)] = True
                else:
                    next_grid[(x, y)] = False

        self.grid = next_grid
        self.generation += 1

    def render(self) -> str:
        """Builds a string representation of the current grid state."""
        lines = []
        for y in range(self.height):
            line = "".join(
                self.alive_char if self.grid.get((x, y), False) else self.dead_char
                for x in range(self.width)
            )
            lines.append(line)
        return "\n".join(lines)


def parse_arguments() -> argparse.Namespace:
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Run Conway's Game of Life in your terminal."
    )
    parser.add_argument(
        "-W", "--width", type=int, default=70, help="Grid width (default: 70)"
    )
    parser.add_argument(
        "-H", "--height", type=int, default=20, help="Grid height (default: 20)"
    )
    parser.add_argument(
        "-s",
        "--speed",
        type=float,
        default=0.15,
        help="Delay in seconds between generations (default: 0.15)",
    )
    parser.add_argument(
        "-d",
        "--density",
        type=float,
        default=0.3,
        help="Initial live cell probability between 0 and 1 (default: 0.3)",
    )
    parser.add_argument(
        "--alive",
        type=str,
        default="O",
        help="Character to display for live cells (default: 'O')",
    )
    parser.add_argument(
        "--dead",
        type=str,
        default=" ",
        help="Character to display for dead cells (default: ' ')",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    game = GameOfLife(
        width=args.width,
        height=args.height,
        alive_char=args.alive,
        dead_char=args.dead,
        density=args.density,
    )

    # Clear terminal screen once at start
    sys.stdout.write("\033[2J")

    try:
        while True:
            # Move cursor to home position and print state
            sys.stdout.write("\033[H")
            sys.stdout.write(
                f"Conway's Game of Life | Gen: {game.generation} | Grid: {game.width}x{game.height}\n"
            )
            sys.stdout.write("-" * game.width + "\n")
            sys.stdout.write(game.render() + "\n")
            sys.stdout.write("-" * game.width + "\n")
            sys.stdout.write("Press Ctrl+C to exit.\n")
            sys.stdout.flush()

            game.step()
            time.sleep(args.speed)
    except KeyboardInterrupt:
        print("\n\nSimulation halted by user. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
