name_age_dict = {
    "Abdel": 36,
    "Shana": 37,
    "Soraya": 18,
    "Younes": 13,
    "Redouane": 12,
    "Inaya": 8,
}

def guess_age(name):
    # Zoek de naam in de dictionary
    age = name_age_dict.get(name)
    if age:
        return f"Op basis van de naam '{name}' schat ik dat je ongeveer {age} jaar oud bent."
    else:
        return f"Sorry, ik heb geen informatie over de naam '{name}'."

# Voorbeeld van gebruik
name_input = input("Voer een naam in: ")
print(guess_age(name_input))