palavra = ("Pablo", "Pedro", "Paloma", "Talia")
for c in palavra:
    print(f"Na palavra {c.upper()} temos: ", end="")
    for d in c:
        if d.lower() in "aeiou":
            print(f"{d} ", end="")

    print("")




