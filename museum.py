print("NATIONAL MUSEUM OF HISTORY")
print(f"{'='*40}")
name=input("Artifact name:\n\n ")

origin=(input("Country of origin: \n\n"))

period=input("Historical period:\n\n ")

acquired=int(input("Acquisition year:\n\n "))
print(f"{'='*40}")
print(f"Artifact name: {name}")
print(f"Country of origin: {origin}")
print(f"Historical period: {period}")
print(f"Acquisition year: {acquired}")
print(f"{' '*40}")
print(f"CATALOG NUMBER: {acquired}-{origin}")
print(f"{'='*40}")
print("Location: Museum wing")