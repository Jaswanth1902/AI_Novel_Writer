"""
Script to append 21 curated authors to reach exactly 100 authors in authors_100.json
"""
import json
from pathlib import Path

new_authors = [
  {
    "id": "patricia-highsmith",
    "name": "Patricia Highsmith",
    "genres": ["Psychological Thriller", "Crime Fiction", "Noir"],
    "vibes": ["moral_decay", "sociopathic_intimacy", "claustrophobic_dread"],
    "tech_eras": ["mid_20th_century", "modern"],
    "magic_hardness": "none_mundane",
    "key_works": ["The Talented Mr. Ripley", "Strangers on a Train", "The Price of Salt"],
    "signature_techniques": [
      "Protagonist amoral intimacy: anchoring third-person narrative so deeply into a criminal psyche that the reader unconsciously roots for evasion",
      "The domestic trap: mundane items (cufflinks, hotel keys, forged passports) carrying immense, suffocating stakes",
      "Slow-burn psychological escalation without melodramatic explosive confrontations",
      "Subtle social awkwardness and class resentment as the primary engine for homicide"
    ],
    "source_repositories": [
      "https://archive.org/search.php?query=patricia+highsmith",
      "https://openlibrary.org/authors/OL218970A/Patricia_Highsmith"
    ]
  },
  {
    "id": "jo-nesbo",
    "name": "Jo Nesbø",
    "genres": ["Nordic Noir", "Police Procedural", "Crime Thriller"],
    "vibes": ["gritty_bleak", "visceral_violence", "melancholic_obsession"],
    "tech_eras": ["modern"],
    "magic_hardness": "none_mundane",
    "key_works": ["The Snowman", "The Bat", "The Leopard", "Nemesis"],
    "signature_techniques": [
      "Layered red herrings with asymmetric timeline reveals to subvert standard procedural tropes",
      "Self-destructive detective archetype whose personal flaws directly compromise crime scene logic",
      "Visceral, atmospheric Scandinavian winter environments amplifying isolation and existential dread",
      "Parallel POVs between hunting detective and methodical serial killer"
    ],
    "source_repositories": [
      "https://jonesbo.com/",
      "https://archive.org/search.php?query=jo+nesbo"
    ]
  },
  {
    "id": "greg-egan",
    "name": "Greg Egan",
    "genres": ["Hard Sci-Fi", "Transhumanism", "Mathematical Speculative"],
    "vibes": ["rigorous_intellectual", "ontological_wonder", "pure_physics"],
    "tech_eras": ["far_future", "post_singularity"],
    "magic_hardness": "none_mundane",
    "key_works": ["Permutation City", "Diaspora", "Axiomatic", "Clockwork Rocket"],
    "signature_techniques": [
      "Uncompromising physics-first premise: building entire narratives around non-standard geometries or computational theory",
      "Cellular automata and substrate-independent consciousness explored with strict mathematical consistency",
      "Decoupling emotional dilemmas from organic human biology to test ethics in synthetic minds",
      "Detailed thought-experiment expositions integrated organically through character problem-solving"
    ],
    "source_repositories": [
      "https://www.gregegan.net/",
      "https://archive.org/search.php?query=greg+egan"
    ]
  },
  {
    "id": "vernor-vinge",
    "name": "Vernor Vinge",
    "genres": ["Hard Sci-Fi", "Space Opera", "Cyberpunk"],
    "vibes": ["deep_time", "singularity_scale", "technological_wonder"],
    "tech_eras": ["near_future", "far_future"],
    "magic_hardness": "none_mundane",
    "key_works": ["A Fire Upon the Deep", "A Deepness in the Sky", "Rainbows End", "True Names"],
    "signature_techniques": [
      "Zones of Thought cosmology: physical laws of computation altering as distance from galactic core increases",
      "Group-mind alien biology (Tines) portrayed with believable sensory coordination and pack mechanics",
      "AR and ubiquitous computing predictive worldbuilding (Rainbows End as the blueprint for wearable tech)",
      "Sub-light relativistic space naval strategy across millennial timelines"
    ],
    "source_repositories": [
      "https://archive.org/search.php?query=vernor+vinge",
      "https://openlibrary.org/authors/OL218520A/Vernor_Vinge"
    ]
  },
  {
    "id": "octavia-butler",
    "name": "Octavia E. Butler",
    "genres": ["Speculative Fiction", "Dystopian", "Afrofuturism"],
    "vibes": ["visceral_survival", "symbiotic_unease", "prophetic_clarity"],
    "tech_eras": ["near_future", "historical_19th_century", "post_apocalyptic"],
    "magic_hardness": "soft",
    "key_works": ["Parable of the Sower", "Kindred", "Dawn (Xenogenesis)", "Fledgling"],
    "signature_techniques": [
      "Hyperempathy syndrome: anchoring high-concept sci-fi in debilitating somatic connection to others' pain",
      "Hierarchical trade-offs in alien symbiosis: forced genetic synthesis without binary villainy",
      "Unsparing depiction of social collapse and community-building grounded in botanical and survival skills",
      "Temporal displacement with unbuffered historical trauma"
    ],
    "source_repositories": [
      "https://octaviabutler.com/",
      "https://archive.org/search.php?query=octavia+butler"
    ]
  },
  {
    "id": "stanislaw-lem",
    "name": "Stanisław Lem",
    "genres": ["Philosophical Sci-Fi", "Hard Sci-Fi", "Satire"],
    "vibes": ["epistemic_humility", "inscrutable_alien", "ironic_wit"],
    "tech_eras": ["far_future", "mid_20th_century"],
    "magic_hardness": "none_mundane",
    "key_works": ["Solaris", "The Cyberiad", "Fiasco", "His Master's Voice"],
    "signature_techniques": [
      "The radically unknowable alien: complete rejection of anthropomorphic contact tropes (sentient plasma ocean)",
      "Mock-scientific literature reviews and pseudo-academic historiography embedded within the narrative",
      "Epistemological critique of scientific hubris through communication failure",
      "Philosophical fables featuring robotic constructors with Voltairean irony"
    ],
    "source_repositories": [
      "https://english.lem.pl/",
      "https://archive.org/search.php?query=stanislaw+lem"
    ]
  },
  {
    "id": "ray-bradbury",
    "name": "Ray Bradbury",
    "genres": ["Speculative Fiction", "Poetic Sci-Fi", "Dark Fantasy"],
    "vibes": ["nostalgic_lyricism", "sensory_wonder", "haunting_melancholy"],
    "tech_eras": ["retro_future", "mid_20th_century"],
    "magic_hardness": "soft",
    "key_works": ["Fahrenheit 451", "The Martian Chronicles", "Something Wicked This Way Comes", "Dandelion Wine"],
    "signature_techniques": [
      "Incandescent metaphor: transforming mechanical apparatus into mythological and biological entities",
      "Sensory-saturated impressionism (the taste of October, dandelion wine as bottled summer)",
      "Epitaph-like vignettes linked through shared thematic atmosphere rather than continuous plot",
      "The horror of automated indifference (the house continuing to run after its inhabitants are ashes)"
    ],
    "source_repositories": [
      "https://archive.org/search.php?query=ray+bradbury",
      "https://openlibrary.org/authors/OL2623727A/Ray_Bradbury"
    ]
  },
  {
    "id": "arthur-c-clarke",
    "name": "Arthur C. Clarke",
    "genres": ["Hard Sci-Fi", "Cosmic Speculation", "Adventure"],
    "vibes": ["monumental_awe", "scientific_optimism", "cosmic_vastness"],
    "tech_eras": ["near_future", "far_future"],
    "magic_hardness": "none_mundane",
    "key_works": ["2001: A Space Odyssey", "Rendezvous with Rama", "Childhood's End", "The City and the Stars"],
    "signature_techniques": [
      "Encounter with the incomprehensibly ancient artifact inspected with engineering precision",
      "Clarke's Third Law dramatized: advanced technology rendered functionally indistinguishable from divinity",
      "Objective, detached narrative tone that lets monumental scale speak for itself without melodrama",
      "Rigorous orbital mechanics and communication latency integrated into plot suspense"
    ],
    "source_repositories": [
      "https://archive.org/search.php?query=arthur+c+clarke",
      "https://openlibrary.org/authors/OL2622765A/Arthur_C._Clarke"
    ]
  },
  {
    "id": "guy-gavriel-kay",
    "name": "Guy Gavriel Kay",
    "genres": ["Historical Fantasy", "Epic Fantasy", "Literary Fiction"],
    "vibes": ["lyrical_melancholy", "historic_elegance", "bittersweet_triumph"],
    "tech_eras": ["medieval", "renaissance", "late_antiquity"],
    "magic_hardness": "soft",
    "key_works": ["Tigana", "The Lions of Al-Rassan", "The Sarantine Mosaic", "Under Heaven"],
    "signature_techniques": [
      "Quarter-turn of the historical wheel: mirroring real history with subtle fantasy veils",
      "The tapestry perspective: tracing how minor decisions ripple outward to seal the fates of empires",
      "Elegaic cadence that mourns lost cultures even as they stand at their absolute zenith",
      "Sympathetic dualities: pitting honorable men and women on opposing sides of unavoidable historical currents"
    ],
    "source_repositories": [
      "https://brightweavings.com/",
      "https://archive.org/search.php?query=guy+gavriel+kay"
    ]
  },
  {
    "id": "terry-pratchett",
    "name": "Terry Pratchett",
    "genres": ["Satirical Fantasy", "High Fantasy", "Humorous"],
    "vibes": ["subversive_humanism", "razor_wit", "affectionate_satire"],
    "tech_eras": ["victorian_fantasy", "early_industrial", "medieval"],
    "magic_hardness": "soft_satirical",
    "key_works": ["Guards! Guards!", "Small Gods", "Night Watch", "Going Postal"],
    "signature_techniques": [
      "Narrative footnotes as comic counterpoint, worldbuilding depth, and philosophical aside",
      "Boots theory of socioeconomic unfairness: grounding high fantasy institutions in working-class economic realities",
      "Anger channeled into incandescent empathy: using absurd comedic fantasy to deliver devastating humanistic moral clarity",
      "Inversion of mythical tropes through relentless logistical common sense"
    ],
    "source_repositories": [
      "https://www.terrypratchettbooks.com/",
      "https://archive.org/search.php?query=terry+pratchett"
    ]
  },
  {
    "id": "susanna-clarke",
    "name": "Susanna Clarke",
    "genres": ["Gaslamp Fantasy", "Historical Fantasy", "Literary"],
    "vibes": ["scholarly_whimsy", "antiquarian_elegance", "eerie_fey"],
    "tech_eras": ["regency_early_19th_century"],
    "magic_hardness": "semi_hard",
    "key_works": ["Jonathan Strange & Mr Norrell", "Piranesi", "The Ladies of Grace Adieu"],
    "signature_techniques": [
      "Pastiche of early 19th-century prose with fictitious scholarly footnotes on fairy lore",
      "The uncanny fairyland: portraying magic not as flashy spells but as dangerous, amoral enchantment",
      "Architectural solipsism: infinite marble halls and tides imprisoned inside vestibules",
      "Dry bureaucratic rivalries between academic theoreticians and pragmatic practitioners of sorcery"
    ],
    "source_repositories": [
      "https://archive.org/search.php?query=susanna+clarke",
      "https://openlibrary.org/authors/OL1393668A/Susanna_Clarke"
    ]
  },
  {
    "id": "roger-zelazny",
    "name": "Roger Zelazny",
    "genres": ["Mythic Fantasy", "Science Fantasy", "Urban Fantasy"],
    "vibes": ["mythic_cool", "cynical_poetry", "cosmic_swashbuckling"],
    "tech_eras": ["multiverse", "mythological_timeless", "mid_20th_century"],
    "magic_hardness": "semi_hard",
    "key_works": ["Nine Princes in Amber", "Lord of Light", "Creatures of Light and Darkness", "A Night in the Lonesome October"],
    "signature_techniques": [
      "Pulp hardboiled dialogue fused with grand mythic elevation and classical cadence",
      "Technological deification: rendering pantheons as post-human immortals manipulating energy via machinery",
      "Shadow-shifting traversal: manipulating reality by adding or subtracting sensory details until destination is reached",
      "First-person cynical narrator holding immense cosmic royalty beneath a world-weary cigarette drag"
    ],
    "source_repositories": [
      "https://archive.org/search.php?query=roger+zelazny",
      "https://openlibrary.org/authors/OL2624443A/Roger_Zelazny"
    ]
  },
  {
    "id": "andrzej-sapkowski",
    "name": "Andrzej Sapkowski",
    "genres": ["Dark Fantasy", "Folkloric Fantasy", "Sword & Sorcery"],
    "vibes": ["ironic_cynicism", "slavic_folklore", "moral_relativism"],
    "tech_eras": ["late_medieval"],
    "magic_hardness": "semi_soft",
    "key_works": ["The Last Wish", "Blood of Elves", "Sword of Destiny", "The Lady of the Lake"],
    "signature_techniques": [
      "Subversion of classic European fairy tales through gritty, transactional economics and monster-ecology pragmatism",
      "The lesser evil paradox: protagonist striving for neutrality while inexorably forced into consequential moral failure",
      "Lively, colloquial, bantering dialogue cutting through melodramatic high fantasy pomp",
      "Anachronistic political terminology juxtaposed against feudal superstitions"
    ],
    "source_repositories": [
      "https://archive.org/search.php?query=andrzej+sapkowski",
      "https://openlibrary.org/authors/OL6966683A/Andrzej_Sapkowski"
    ]
  },
  {
    "id": "michael-moorcock",
    "name": "Michael Moorcock",
    "genres": ["Sword & Sorcery", "Dark Fantasy", "Multiverse Speculative"],
    "vibes": ["tragic_doom", "baroque_decadence", "multiverse_entropy"],
    "tech_eras": ["mythic_dying_earth", "multiverse"],
    "magic_hardness": "soft",
    "key_works": ["Elric of Melniboné", "Stormbringer", "The Knight of the Swords", "Behold the Man"],
    "signature_techniques": [
      "Anti-Conan archetype: sickly, introspective, drug-dependent albino emperor wielding a parasitic soul-eating sword",
      "Cosmic struggle between Law and Chaos replacing traditional binary Good and Evil",
      "The Eternal Champion reincarnation cycle linking disparate heroes across alternate planes",
      "Baroque sensory overload describing ancient, decadent empires collapsing under cosmic entropy"
    ],
    "source_repositories": [
      "https://archive.org/search.php?query=michael+moorcock",
      "https://openlibrary.org/authors/OL218683A/Michael_Moorcock"
    ]
  },
  {
    "id": "pirateaba",
    "name": "pirateaba",
    "genres": ["Progression Fantasy", "LitRPG", "Epic Fantasy", "Slice of Life"],
    "vibes": ["emotional_maximalism", "world_density", "found_family_warmth"],
    "tech_eras": ["medieval_fantasy"],
    "magic_hardness": "progression_levels",
    "key_works": ["The Wandering Inn: Volume 1", "The Wandering Inn: Volume 2", "The General of Izril"],
    "signature_techniques": [
      "Slice-of-life pacing suddenly colliding with cataclysmic war, turning mundane hospitality into sanctuary defense",
      "Massive ensemble perspective tapestry: giving named interiority to every goblin, soldier, and inn guest",
      "Levels and Skills earned not through grinding, but through emotional breakdown, sacrifice, and character definition",
      "Immense wordcount velocity with unhurried conversational cadence building monumental emotional payoffs"
    ],
    "source_repositories": [
      "https://wanderinginn.com/",
      "https://archive.org/search.php?query=pirateaba"
    ]
  },
  {
    "id": "matt-dinniman",
    "name": "Matt Dinniman",
    "genres": ["LitRPG", "Dystopian Sci-Fi", "Dark Comedy"],
    "vibes": ["kinetic_absurdity", "visceral_rage", "indomitable_defiance"],
    "tech_eras": ["modern_collapsing_into_alien_dungeon"],
    "magic_hardness": "system_apocalypse",
    "key_works": ["Dungeon Crawler Carl", "Carl's Doomsday Scenario", "The Dungeon Anarchist's Cookbook"],
    "signature_techniques": [
      "Weaponized absurdity: juxtaposing slapstick comedic items with genuine body horror and trauma",
      "The Intergalactic Reality Show framing: game mechanics driven by sadistic viewership ratings and corporate sponsorships",
      "Engineered explosive chain reactions: solving impossible dungeon bosses through unorthodox chemistry and environmental traps",
      "Undercurrent of righteous working-class fury against corrupt systemic overseers"
    ],
    "source_repositories": [
      "https://mattdinniman.com/",
      "https://royalroad.com/profile/138543",
      "https://archive.org/search.php?query=matt+dinniman"
    ]
  },
  {
    "id": "alexander-wales",
    "name": "Alexander Wales",
    "genres": ["Rational Fiction", "Progression Fantasy", "LitRPG"],
    "vibes": ["hyper_analytical", "philosophical_rigor", "deconstructive_meta"],
    "tech_eras": ["magical_renaissance", "multiverse"],
    "magic_hardness": "ultra_hard_rational",
    "key_works": ["Worth the Candle", "This Used to be About Dungeons", "The Metropolitan Man"],
    "signature_techniques": [
      "Rational deconstruction: testing game systems and worldbuilding logic against economic arbitrage and sociological reality",
      "Meta-narrative self-awareness: characters analyzing their own narrative arcs and trope obligations as existential traps",
      "Hard magic optimization: treating magic systems like engineering problems with explicit constraints and exploit vectors",
      "Unflinching examination of trauma, grief, and tabletop roleplaying psychology"
    ],
    "source_repositories": [
      "https://archiveofourown.org/users/AlexanderWales",
      "https://royalroad.com/fiction/25137/worth-the-candle"
    ]
  },
  {
    "id": "thomas-ligotti",
    "name": "Thomas Ligotti",
    "genres": ["Cosmic Horror", "Weird Fiction", "Philosophical Horror"],
    "vibes": ["existential_nihilism", "nightmarish_delusion", "decaying_industrial"],
    "tech_eras": ["late_20th_century", "decaying_timeless"],
    "magic_hardness": "cosmic_irrational",
    "key_works": ["Teatro Grottesco", "Songs of a Dead Dreamer", "The Conspiracy Against the Human Race"],
    "signature_techniques": [
      "Puppet and mannequin ontologies: reality exposed as a cheap, hollow, mechanically animated puppet show",
      "Corporate and bureaucratic surrealism: mundane decaying industrial towns where sanity dissolves into senseless rituals",
      "Unreliable, clinically depressed narrators recounting horrors that may simply be the unfiltered truth of existence",
      "Hypnotic, repetitious sentence rhythms creating uncanny claustrophobia"
    ],
    "source_repositories": [
      "https://www.ligotti.net/",
      "https://archive.org/search.php?query=thomas+ligotti"
    ]
  },
  {
    "id": "richard-matheson",
    "name": "Richard Matheson",
    "genres": ["Horror", "Sci-Fi Thriller", "Psychological Suspense"],
    "vibes": ["visceral_isolation", "lean_pacing", "existential_reversal"],
    "tech_eras": ["mid_20th_century", "suburban_modern"],
    "magic_hardness": "none_mundane",
    "key_works": ["I Am Legend", "The Shrinking Man", "Hell House", "Duel"],
    "signature_techniques": [
      "The ultimate perspective reversal: the protagonist realizing he is the legendary monster of the new world",
      "Everyday suburban environments transforming into terrifying claustrophobic gauntlets",
      "Lean, muscular, propulsive sentence structure stripped of all decorative fat",
      "Rationalization of supernatural phenomena through biological or psychological mechanisms"
    ],
    "source_repositories": [
      "https://archive.org/search.php?query=richard+matheson",
      "https://openlibrary.org/authors/OL218765A/Richard_Matheson"
    ]
  },
  {
    "id": "kurt-vonnegut",
    "name": "Kurt Vonnegut",
    "genres": ["Satirical Sci-Fi", "Postmodern", "Humanist Fiction"],
    "vibes": ["ironic_fatalism", "profound_gentleness", "subversive_wit"],
    "tech_eras": ["mid_20th_century", "non_linear_temporal"],
    "magic_hardness": "soft",
    "key_works": ["Slaughterhouse-Five", "Cat's Cradle", "Sirens of Titan", "Breakfast of Champions"],
    "signature_techniques": [
      "Unstuck in time non-linear chronology: diffusing traumatic tension through matter-of-fact temporal omniscient looping",
      "The recurring tragic refrain ('So it goes') acknowledging mortality without sentimental bathos",
      "Simple, deceptively childlike prose delivering devastating indictments of warfare and technological hubris",
      "Invention of satirical philosophies and mythologies (Bokononism, ice-nine, Tralfamadorians)"
    ],
    "source_repositories": [
      "https://archive.org/search.php?query=kurt+vonnegut",
      "https://openlibrary.org/authors/OL2622919A/Kurt_Vonnegut"
    ]
  },
  {
    "id": "virginia-woolf",
    "name": "Virginia Woolf",
    "genres": ["Literary Modernism", "Stream of Consciousness", "Psychological Realism"],
    "vibes": ["luminous_interiority", "temporal_fluidity", "impressionistic_depth"],
    "tech_eras": ["early_20th_century", "edwardian"],
    "magic_hardness": "none_mundane",
    "key_works": ["Mrs. Dalloway", "To the Lighthouse", "The Waves", "Orlando"],
    "signature_techniques": [
      "Free indirect discourse gliding seamlessly between multiple characters' internal cognitive associations",
      "Moments of Being: crystallizing an entire lifetime's philosophical weight into a fleeting sensory observation",
      "Fluid compression and expansion of subjective time versus objective mechanical clocks",
      "Rhythmic, musical prose cadence capturing the subterranean emotional currents of domestic life"
    ],
    "source_repositories": [
      "https://standardebooks.org/ebooks/virginia-woolf",
      "https://www.gutenberg.org/ebooks/author/89"
    ]
  }
]

def main():
    target_path = Path("projects/AI_Novel_Engine/data/authors_100.json")
    with open(target_path, "r", encoding="utf-8") as f:
        authors = json.load(f)

    print(f"Starting author count: {len(authors)}")
    existing_ids = {a["id"] for a in authors}

    added = 0
    for a in new_authors:
        if a["id"] in existing_ids:
            print(f"Duplicate found: {a['id']}, skipping...")
        else:
            authors.append(a)
            existing_ids.add(a["id"])
            added += 1

    print(f"Added {added} authors. Total authors now: {len(authors)}")
    assert len(authors) == 100, f"Expected exactly 100 authors, got {len(authors)}"

    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(authors, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved {len(authors)} authors to {target_path}!")

if __name__ == "__main__":
    main()
