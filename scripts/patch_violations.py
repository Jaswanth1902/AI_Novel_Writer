import re

def patch_file(path, replacements):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    orig = text
    for p, r in replacements:
        text = re.sub(p, r, text)
    if text != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Patched {path}")

patch_file("output/Chapter_01_The_Awakening_of_the_Honoured_One.md", [
    (r"the words felt like an indictment\.", "the words stood as an indictment.")
])

patch_file("output/Chapter_03_Ice_and_Brotherhood.md", [
    (r"—", ", ")
])

patch_file("output/Chapter_04_Attire_for_the_Darkest_Night.md", [
    (r"suddenly felt burning against his pulse", "suddenly burned cold against his pulse"),
    (r"speaking of it felt like holding flame near dry straw", "speaking of it was holding flame near dry straw"),
    (r"—", ": ")
])

patch_file("output/Chapter_05_The_Unlit_Ridge.md", [
    (r"—", ", ")
])

patch_file("output/Chapter_06_The_Second_Moon_and_the_Redirected_Bolt.md", [
    (r"stale cold coffee and burnt lard", "stale chicory brew and burnt lard")
])

patch_file("output/Chapter_08_The_Hearth_in_the_Storm.md", [
    (r'"It didn\'t feel like something passing," she murmured, her voice dropping into the quiet of the room\. "It felt like something watching\."',
     '"It was not something passing," she murmured, her voice dropping into the quiet of the room. "It was something watching."')
])

patch_file("output/Chapter_09_The_Purge_of_the_Unawakened.md", [
    (r"—", ", ")
])

patch_file("output/Chapter_10_The_Four_Gates_of_Iron_and_Air.md", [
    (r"darkening a circle no wider than a teacup", "darkening a circle no wider than an iron saucer")
])

patch_file("output/Chapter_36_The_Return_of_Warmth.md", [
    (r"that deep, unspoken understanding that bound the four of them together",
     "that deep, silent solidarity that bound the four of them together")
])

print("Patching complete.")
