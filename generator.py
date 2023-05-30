import json
import random


names = ["Adel", "Adonis", "Ajaz", "Akos", "Aldo", "Amets", "Amaro", "Aquiles", "Algimantas", "Alpidio", "Amrane", "Anish", "Arián", "Ayun", "Azariel", "Bagrat", "Bencomo", "Bertino", "Candi", "Cesc", "Cirino", "Crisólogo", "Cruz", "Danilo", "Dareck", "Dariel", "Darin", "Delmiro", "Damen", "Dilan", "Dipa", "Doménico", "Drago", "Edivaldo", "Elvis", "Elyan", "Emeric", "Engracio", "Ensa", "Eñaut", "Eleazar", "Eros", "Eufemio", "Feiyang", "Fiorenzo", "Foudil", "Galo", "Gastón", "Giulio", "Gautam", "Gentil", "Gianni", "Gianluca", "Giorgio", "Gourav", "Grober", "Guido", "Guifre", "Guim", "Hermes", "Inge", "Irai", "Iraitz", "Iyad", "Iyán", "Jeremías", "Joao", "Jun", "Khaled", "Leónidas", "Lier", "Lionel", "Lisandro", "Lucián", "Mael", "Misael", "Moad", "Munir", "Nael", "Najim", "Neo", "Neil", "Nikita", "Nilo", "Otto", "Pep", "Policarpo", "Radu", "Ramsés", "Rómulo", "Roy", "Severo", "Sidi", "Simeón", "Taha", "Tao", "Vadim", "Vincenzo", "Zaid", "Zigor", "Zouhair"]

last_name = ["Adel", "Adonis", "Ajaz", "Akos", "Aldo", "Amets", "Amaro", "Aquiles", "Algimantas", "Alpidio", "Amrane", "Anish", "Arián", "Ayun", "Azariel", "Bagrat", "Bencomo", "Bertino", "Candi", "Cesc", "Cirino", "Crisólogo", "Cruz", "Danilo", "Dareck", "Dariel", "Darin", "Delmiro", "Damen", "Dilan", "Dipa", "Doménico", "Drago", "Edivaldo", "Elvis", "Elyan", "Emeric", "Engracio", "Ensa", "Eñaut", "Eleazar", "Eros", "Eufemio", "Feiyang", "Fiorenzo", "Foudil", "Galo", "Gastón", "Giulio", "Gautam", "Gentil", "Gianni", "Gianluca", "Giorgio", "Gourav", "Grober", "Guido", "Guifre", "Guim", "Hermes", "Inge", "Irai", "Iraitz", "Iyad", "Iyán", "Jeremías", "Joao", "Jun", "Khaled", "Leónidas", "Lier", "Lionel", "Lisandro", "Lucián", "Mael", "Misael", "Moad", "Munir", "Nael", "Najim", "Neo", "Neil", "Nikita", "Nilo", "Otto", "Pep", "Policarpo", "Radu", "Ramsés", "Rómulo", "Roy", "Severo", "Sidi", "Simeón", "Taha", "Tao", "Vadim", "Vincenzo", "Zaid", "Zigor", "Zouhair"]

def save_as_json(filename, number):

    with open(filename, "r+") as file:
        data = json.load(file)

    for i in range (number):
        register = {
            "name" : f'{random.choice(names)} {random.choice(last_name)}',
            "experience" : random.randint(0, 100)
        }
        data.append(register)
    
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

save_as_json("data_players.json", 15)