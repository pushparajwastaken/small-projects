#!/usr/bin/env python3
"""
Neon Nightfall — Full-branch version
- 12 rounds, 3 choices each -> 3^12 = 531,441 unique endings
- Every distinct choice-path produces a distinct ending generated procedurally
- World: cyborgs, vampires, ghosts, wizards, draculas and futuristic elements
"""

import sys

ROUNDS = 12
CHOICES_PER_ROUND = 3

INTRO = f"""
Welcome to 'Neon Nightfall — Multiverse Edition'.
This is a sprawling branching adventure: {ROUNDS} rounds, {CHOICES_PER_ROUND} choices each.
There are {CHOICES_PER_ROUND ** ROUNDS:,} possible unique endings — each distinct choice path yields a different result.
Type the number of your chosen option and press Enter. Type 'q' to quit at any time.
"""

ROUND_PROMPTS = [
    ("You stand at the chrome bazaar's glowing entrance.", [
        "Barter with a chrome-eyed cyborg merchant.",
        "Slip down a side alley into vapor-thick stalls.",
        "Stick your hand into a humming arc-receptacle."
    ]),
    ("A shadow subway rumbles beneath the city.", [
        "Ride an unlicensed phantom train car.",
        "Climb into the maintenance ducts to sneak forward.",
        "Call out to the whisper-ghosts in the tracks."
    ]),
    ("The Ivory Tower of the Arcane Collective beckons.", [
        "Ask a junior wizard for a simple charm.",
        "Peek into a forbidden grimoire left ajar.",
        "Offer your neural signature in exchange for knowledge."
    ]),
    ("Rooftop gardens hum with bioluminescent vines.", [
        "Steal a glowing seedling guarded by drones.",
        "Meditate with a vampire botanist under moon-sails.",
        "Listen to the ghost of the gardener; it hums coordinates."
    ]),
    ("An abandoned biotech lab hides under tape and rust.", [
        "Break a vial with no label and keep the residue.",
        "Wake the incubated occupant tucked behind glass.",
        "Scan the file server for archived identity records."
    ]),
    ("A cathedral of machines echoes mechanical prayers.", [
        "Tune a servo choir to sing your real name.",
        "Sabotage the low-priority maintenance bots.",
        "Request a blessing from the cyborg-abbot."
    ]),
    ("You find a vampire conclave dining in neon.", [
        "Challenge the eldest to a game of memory.",
        "Trade a favor for a single, precise tooth.",
        "Convince a junior vamp to teach you their shadow-step."
    ]),
    ("A ghost-net node flickers with half-remembered lives.", [
        "Plug in your wrist-hub and share a childhood image.",
        "Download a mournful archive and listen to its heartbeat.",
        "Leave a breadcrumb for other wanderers to find."
    ]),
    ("A wandering wizard offers a peculiar contract.", [
        "Sign the contract in steam-ink with your left hand.",
        "Negotiate for a spell that rewrites one regret.",
        "Refuse; instead barter a secret about the city."
    ]),
    ("An ancient Dracula lounges under LED chandeliers.", [
        "Kiss a drop of lunar wine from his glass.",
        "Ask him about the city before neon — pay in song.",
        "Steal a ribbon of his cloak when he's distracted."
    ]),
    ("A cyborg broker shows you an illicit neural mod.", [
        "Buy the mod and implant it immediately.",
        "Distrust the broker and attempt to replicate it yourself.",
        "Swap the broker's ledger for a forged entry and run."
    ]),
    ("The city's central AI hums like an old friend.", [
        "Send it a poem and wait for an answer.",
        "Try to override a small neighborhood subroutine.",
        "Ask it to reveal one hidden place in New Aurora."
    ]),
]

FLAVOR_LINES = [
    "A titanium heart hums an old lullaby as neon rains begin.",
    "A vampire scholar traces circuits with runes and small smiles.",
    "A translucent ghost-network offers coordinates to a parallel street.",
    "A wizard rewrites a line of your childhood; something fissures.",
    "A Dracula, weary and elegant, drinks moonlight like old champagne.",
    "Tiny drones applaud; their tiny lights spell your name in Morse.",
    "The city's AI bookmarked you as 'interesting' and keeps logs.",
    "A secretive guild chips a mark into your left palm, glowing faintly.",
    "Memory echoes return—parts that do not belong to you.",
    "You awaken with a new sense: you can hear metallic whispers."
]

CONSEQUENCE_LINES = [
    "Your neural map is augmented — you see potential timelines flicker.",
    "You trade a memory for a secret; the trade tastes of iron.",
    "A spectral tag follows you; sometimes it whispers solutions.",
    "Your voice now echoes with a hidden command; doors obey.",
    "You are marked: predators and protectors will both find you.",
    "An invention is left in your pocket you do not recall making.",
    "The city's rumors call you a myth; children fear and admire you.",
    "A lost lover finds you across spans of altered probability.",
    "You gain data that can topple a corporation or save a life.",
    "Something small in the world rearranges to your advantage."
]

ENDING_TAGS = [
    "You walk away powerful — and indebted to the city.",
    "You vanish from ordinary history; your tale becomes an urban myth.",
    "You become celebrated in secret circles for centuries.",
    "You fix one tiny thing, and a universe tilts because of it.",
    "You are hunted and protected in equal measure until the end.",
    "The night keeps you as one of its many good stories.",
    "You hold a key others would kill to touch.",
    "You return to the bazaar with pockets full of impossible things.",
    "Your name is turned into a neon graffiti that never fades.",
    "You finally sleep, and the city sighs with relief."
]

def input_choice(prompt, options):
    """Prompt user for a numeric choice among options. Returns index 0..len-1."""
    print(prompt)
    for idx, opt in enumerate(options, 1):
        print(f"  {idx}. {opt}")
    while True:
        choice = input("\nChoose (number, or 'q' to quit): ").strip()
        if not choice:
            print("Please enter a number.")
            continue
        if choice.lower() in ('q', 'quit', 'exit'):
            print("Exiting. Farewell.")
            sys.exit(0)
      
        if all(ch.isdigit() for ch in choice):
            try:
                num = int(choice)
            except Exception:
                print("Couldn't parse that number; try again.")
                continue
            if 1 <= num <= len(options):
                return num - 1
            else:
                print(f"Please enter a number between 1 and {len(options)}.")
        else:
            print("Invalid input. Type the numeric choice (e.g., 1).")

def path_to_index(path):
    """
    Convert a list of base-3 digits (each 0..2) into a unique integer index between 0 and 3^ROUNDS - 1.
    We compute digit-by-digit to be safe.
    """
    idx = 0
    for digit in path:
      
        idx = idx * CHOICES_PER_ROUND + digit
    return idx

def make_ending_from_path(path):
    """
    Build a unique ending string deterministically from the path (list of ints length ROUNDS).
    Because path-to-index is injective, each unique path will produce a unique ending text.
    """
    # Unique numeric id
    eid = path_to_index(path)  # 0-based
    ending_number = eid + 1  # 1-based for human-friendly display

    # Build scene: combine the chosen short snippets (keeps endings unique)
    chosen_snippets = []
    for round_idx, choice_idx in enumerate(path):
        prompt_text, options = ROUND_PROMPTS[round_idx]
        snippet = options[choice_idx]
        chosen_snippets.append(snippet)

    # Join the snippets into a flowing paragraph (varied punctuation)
    scene = " → ".join(chosen_snippets)

    # Deterministically pick flavor/consequence/tag using modular arithmetic on eid
    flavor = FLAVOR_LINES[eid % len(FLAVOR_LINES)]
    consequence = CONSEQUENCE_LINES[(eid // len(FLAVOR_LINES)) % len(CONSEQUENCE_LINES)]
    tag = ENDING_TAGS[(eid // (len(FLAVOR_LINES) * len(CONSEQUENCE_LINES))) % len(ENDING_TAGS)]

    # Short meta to help players share/reload the exact path
    path_code = ''.join(str(d) for d in path)  # base-3 digits as string

    ending_text = (
        f"=== ENDING #{ending_number:,}  (path code: {path_code}) ===\n\n"
        f"{scene}\n\n"
        f"{flavor}\n"
        f"{consequence}\n\n"
        f"{tag}\n"
        f"{'='*50}\n"
    )
    return ending_text

def play():
    print(INTRO)
    input("Press Enter to begin your neon multiverse journey...")

    path = []
    for r in range(ROUNDS):
        prompt_text, options = ROUND_PROMPTS[r]
        header = f"\nRound {r+1}/{ROUNDS}: {prompt_text}"
        choice = input_choice(header, options)
        path.append(choice)
        print(f"> You chose: {options[choice]}\n")

    # After all rounds, produce unique ending
    ending = make_ending_from_path(path)
    print("\n" + ending)

    # Offer to show route / replay / export
    while True:
        print("Options:")
        print("  1. Play again (random reset)")
        print("  2. Replay same path (re-run ending)")
        print("  3. Print path code for sharing")
        print("  4. Exit")
        c = input("\nChoose (1-4): ").strip()
        if c == '1':
            print("\nRestarting new game...\n")
            return play()
        elif c == '2':
            print("\nReplaying same path ending:\n")
            print(make_ending_from_path(path))
        elif c == '3':
            print(f"\nPath code (base-3 digits): {''.join(str(d) for d in path)}")
            print("Share this code; the same code regenerates the same ending.")
        elif c in ('4', 'q', 'quit', 'exit'):
            print("Goodbye — the neon remembers you.")
            sys.exit(0)
        else:
            print("Invalid choice. Pick 1-4.")

if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        print("\nInterrupted. Farewell.\n")

