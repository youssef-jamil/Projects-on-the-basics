stringFile = open("String.txt")

outputFile = open("String_line.txt", "w")
phrase = " "
for line in stringFile:
    if line.strip() in {"I", "Almdrasa"}:
        phrase += f" {line.strip()}"
    else:
        phrase += f" {line.strip().lower()}"

print(phrase)
print(phrase, file=outputFile)
