#!/usr/bin/env python3
"""
superheroes.py — A curated list of the coolest superheroes ever.
Run it. You know you want to.
"""

SUPERHEROES = [
    ("Spider-Man",      "Slings webs and wisecracks in equal measure"),
    ("Batman",          "No powers, just pure determination and a great cape"),
    ("Wonder Woman",    "Warrior princess who can out-fight anyone in any universe"),
    ("Black Panther",   "King, scientist, and the most stylish fighter alive"),
    ("Iron Man",        "Genius billionaire who built a suit of armor in a cave"),
    ("Storm",           "Commands the weather — the whole weather"),
    ("Doctor Strange",  "Sorcerer Supreme with the most mind-bending powers around"),
    ("Wolverine",       "Indestructible, grumpy, and absolutely iconic"),
    ("Captain Marvel",  "Flies through space punching things at near-light speed"),
    ("The Flash",       "So fast he can literally run through time itself"),
]

def main():
    width = 52
    print("=" * width)
    print(" THE COOLEST SUPERHEROES OF ALL TIME ".center(width))
    print("=" * width)
    print()

    for rank, (name, tagline) in enumerate(SUPERHEROES, start=1):
        print(f"  {rank:>2}. {name}")
        print(f"       {tagline}")
        print()

    print("-" * width)
    print("  No capes were harmed in the making of this list.")
    print("=" * width)

if __name__ == "__main__":
    main()
