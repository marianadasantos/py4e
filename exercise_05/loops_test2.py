while True:
    line = input("> ")
    # line[0] -> gives you the first character of a string
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done!")