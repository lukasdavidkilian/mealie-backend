from .food_class import Food

# Nutrition Sets

nutrition_set_all = []
nutrition_set_lukas = []
nutrition_set_daniel = []
nutrition_set_lucas = []
nutrition_set_rico = []
nutrition_set_stefan = []
nutrition_set_schatu = []
nutrition_set_yasar = []
nutrition_set_sebastian = []
nutrition_set_soula = []
nutrition_set_emil = []
nutrition_set_adrian = []
nutrition_set_martin = []
nutrition_set_fabian = []
nutrition_set_celina = []

nutrition_sets = {
    "lukas": nutrition_set_lukas,
    "daniel": nutrition_set_daniel,
    "all": nutrition_set_all,
    "standard": nutrition_set_standard,
    "lucas": nutrition_set_lucas,
    "rico": nutrition_set_rico,
    "stefan": nutrition_set_stefan,
    "schatu": nutrition_set_schatu,
    "yasar": nutrition_set_yasar,
    "sebastian": nutrition_set_sebastian,
    "soula": nutrition_set_soula,
    "emil": nutrition_set_emil,
    "adrian": nutrition_set_adrian,
    "martin": nutrition_set_martin,
    "fabian": nutrition_set_fabian,
    "celina": nutrition_set_celina

}

# PROTEIN

rinderhackfleisch = Food("Rinderhackfleisch", 25, 9, 0, 100, "g", [2.5, 3, 3.5, 4])
rinderhackfleischF = Food("Rinderhackfleisch", 25, 9, 0, 100, "g", [2,2.5,3])
rinderfilet = Food("Rinderfilet", 29.7, 4.3, 0, 100, "g", [2,2.5])
rinderleber = Food("Rinderleber", 19.2, 3.7, 5.3, 100, "g", [2.5])
hähnchenbrust = Food("Hähnchenbrust", 30, 0, 0, 100, "g", [2.5, 3, 3.5, 4])
hähnchenbrustF = Food("Hähnchenbrust", 30, 0, 0, 100, "g", [2.5])
hühnerherzen = Food("Hühnerherzen", 16, 5, 0, 100, "g", [2])
putenbrust = Food("Putenbrust", 30, 1, 0, 100, "g", [2.5, 3, 3.5, 4])
putenbrustF = Food("Putenbrust", 30, 1, 0, 100, "g", [2.5])
bauernschinken = Food("Bauernschinken", 26.3, 6.8, 1.1, 100, "g", [0.75, 1])
bacon = Food("Bacon", 14, 28, 0.5, 100, "g", [0.5, 0.75])
salami = Food("Salami", 19, 33, 3, 100, "g", [0.7])
lachs = Food("Lachs", 20, 13, 0, 100, "g", [1.25, 2.5])
seelachs = Food("Seelachs", 17, 0.6, 0, 100, "g", [2])
garnelen = Food("Garnelen", 18.6, 1.4, 0, 100, "g", [1.25, 2.5])
eier = Food("Eier", 7.5, 6.5, 1, 1, "", [3, 4, 5,])
eierF = Food("Eier", 7.5, 6.5, 1, 1, "", [2, 3])
milch = Food("Milch", 3.3, 4, 4.8, 100, "ml", [2.5, 3, 3.5, 4])
käse = Food("Käse", 30, 23, 0.1, 100, "g", [0.75, 1])
gouda = Food("Gouda", 22, 30.8, 0, 100, "g", [0.75, 1])
feta = Food("Feta", 17, 22, 0.5, 100, "g", [0.5, 1])
joghurt = Food("Naturjoghurt 1,5%", 6, 1.5, 6, 100, "g", [1.5, 2])
parmesan = Food("Parmesan", 32.3, 35, 0, 100, "g", [0.75, 1])
roteLinsen = Food("Rote Linsen", 26.7, 1.5, 57.8, 100, "g", [1, 2, 3])
kichererbsen = Food("Kichererbsen", 20, 7, 45, 100, "g", [1, 2, 3])
kidneybohnen = Food("Kidneybohnen", 21, 1, 36.5, 100, "g", [0.75, 1])

nutrition_set_all.extend([rinderhackfleisch, hähnchenbrust, putenbrust, bauernschinken, lachs, garnelen, eier, milch, käse])
nutrition_set_lukas.extend([rinderhackfleisch, hähnchenbrust, putenbrust, bauernschinken, eier, milch, käse])
nutrition_set_daniel.extend([rinderhackfleisch, hähnchenbrust, putenbrust, bauernschinken, lachs, garnelen])
nutrition_set_lucas.extend([rinderhackfleisch, hähnchenbrust, putenbrust, bauernschinken, lachs, garnelen, eier, käse])
nutrition_set_rico.extend([rinderhackfleisch, hähnchenbrust, putenbrust, bauernschinken, lachs, garnelen, eier, milch, käse])
nutrition_set_stefan.extend([rinderhackfleisch, hähnchenbrust, putenbrust, bauernschinken, lachs, eier, milch, käse])
nutrition_set_schatu.extend([rinderhackfleisch, hähnchenbrust, putenbrust, lachs, garnelen, eier, milch, käse])
nutrition_set_yasar.extend([rinderhackfleisch, hähnchenbrust, putenbrust, garnelen, eier, milch, käse])
nutrition_set_sebastian.extend([rinderhackfleisch, rinderleber, hähnchenbrust, hühnerherzen, bauernschinken,seelachs, garnelen, eier, milch])
nutrition_set_soula.extend([joghurt,rinderhackfleischF, hähnchenbrustF, putenbrustF, bauernschinken, lachs, garnelen, eierF, milch, käse])
nutrition_set_emil.extend([rinderhackfleisch, hähnchenbrust, putenbrust, eier, milch, bacon, rinderfilet])
nutrition_set_adrian.extend([rinderhackfleisch, hähnchenbrust, putenbrust, bauernschinken, lachs, garnelen, eier, milch, käse])
nutrition_set_martin.extend([rinderhackfleisch, hähnchenbrust, putenbrust, bauernschinken, lachs, eier, milch])
nutrition_set_celina.extend([rinderhackfleischF, hähnchenbrustF, putenbrustF, eierF, milch, rinderfilet, bacon, gouda, parmesan])
# CARBS

reis = Food("Basmati Reis", 8.8, 1, 75, 100, "g", [0.75, 1])
reisflocken = Food("Reisflocken", 8.8, 1, 75, 100, "g", [0.5, 0.75, 1])
milchreis = Food("Milchreis ohne Milch", 8.8, 1, 75, 100, "g", [0.75, 1])
pirincreis = Food("Pirinc Reis", 7.9, 1.2, 77.8, 100, "g", [0.75, 1])
kartoffeln = Food("Kartoffeln", 2, 0, 17, 100, "g", [4, 5, 6])
süßkartoffeln = Food("Süßkartoffeln", 1.6, 0.6, 24, 100, "g", [4, 5, 6])
buchweizen = Food("Buchweizen", 10, 2, 70, 100, "g", [0.5, 1])
honig = Food("Honig", 0, 0, 80, 100, "g", [0.2, 0.3, 0.4])
banane = Food("Banane", 1.1, 0.3, 22.8, 100, "g", [1, 2])
apfel = Food("Apfel", 0.3, 0.2, 14, 100, "g", [1.5])
blaubeeren = Food("Blaubeeren", 0.6, 0.6, 7.4, 100, "g", [1, 1.5, 2])
mango = Food("Mango", 2, 0.2, 13, 100, "g", [2, 2.5])
maracuja = Food("Maracuja", 2.2, 0.5, 11.8, 100, "g", [0.8])
reiswaffeln = Food("Reiswaffeln", 8, 3.6, 80.2, 100, "g", [0.15, 0.3, 0.45])
spinat = Food("Spinat", 2.8, 0.3, 0.6, 100, "g", [1, 1.5, 2])
blumenkohl = Food("Blumenkohl", 1.9, 0, 2, 100, "g", [1, 1.5, 2])
paprikarot = Food("Rote Paprika", 1.3, 0.5, 6.4, 100, "g", [1, 2, 3])
paprikagelb = Food("Gelbe Paprika", 1, 0, 5, 100, "g", [1, 2, 3])
paprikagrün = Food("Grüne Paprika", 1, 0, 2, 100, "g", [1, 2, 3])
karotte = Food("Karotte", 1, 0.2, 4.8, 100, "g", [0.8])
tomate = Food("Tomate", 0.7, 3.5, 0.1, 100, "g", [0.5, 1])
gurke = Food("Gurke", 0.6, 0.2, 1.8, 100, "g", [0.5, 1])
beerenmischung = Food("Beerenmischung TK", 1.4, 0.6, 12.1, 100, "g", [0.5, 1, 1.5])
mandarine = Food("Mandarine", 0.7, 0.2, 10, 100, "g", [1, 2, 3])
orange = Food("Orange", 1, 0.2, 8.2, 100, "g", [1.5, 3])
birne = Food("Mandarine", 1, 0.2, 11, 100, "g", [1, 2, 3])
ananas = Food("Ananas", 0.5, 0.2, 12.4, 100, "g", [1, 2, 3])
dattel = Food("Dattel getrocknet", 1.85, 0.5, 65, 100, "g", [0.1, 0.2, 0.3])
ketchup = Food("Ketchup", 2, 0.3, 24, 100, "g", [0.15, 0.3])
sriracha = Food("Sriracha", 1.8, 1.3, 23, 100, "g", [0.15, 0.3])
sojasauce = Food("Sojasauce glutenfrei", 10, 0, 2, 100, "g", [0.2, 0.4])
gehackteTomaten = Food("Tomaten gehackt", 1.1, 0.1, 3, 100, "g", [2, 3, 4])
grüneBohnen = Food("Grüne Bohnen", 2.4, 0, 5, 100, "g", [1, 2])
raeuchertofu = Food("Räuchertofu", 19, 9, 2.8, 100, "g", [1, 2])


nutrition_set_all.extend([reis, kartoffeln, süßkartoffeln, buchweizen, honig, banane, apfel])
nutrition_set_lukas.extend([reis, kartoffeln, süßkartoffeln, honig, banane, apfel])
nutrition_set_daniel.extend([reis, kartoffeln, süßkartoffeln, buchweizen, honig, banane, apfel])
nutrition_set_lucas.extend([reis, kartoffeln, süßkartoffeln, honig, banane, apfel])
nutrition_set_rico.extend([reis, kartoffeln, honig, banane, apfel])
nutrition_set_stefan.extend([reis, kartoffeln, süßkartoffeln, honig, banane, apfel])
nutrition_set_schatu.extend([reis, kartoffeln, süßkartoffeln, buchweizen, honig, banane, apfel])
nutrition_set_yasar.extend([pirincreis, kartoffeln, süßkartoffeln, buchweizen, honig, banane, apfel])
nutrition_set_sebastian.extend([reis, kartoffeln, buchweizen, honig, banane, apfel, tomate, gurke, spinat])
nutrition_set_soula.extend([reis, kartoffeln, süßkartoffeln, honig, banane, apfel])
nutrition_set_emil.extend([reis, kartoffeln, süßkartoffeln, honig, banane, apfel, reisflocken])
nutrition_set_adrian.extend([reis, kartoffeln, buchweizen, honig, banane, paprikarot, mango])
nutrition_set_martin.extend([reis, kartoffeln, süßkartoffeln, buchweizen, honig, banane, apfel])
nutrition_set_celina.extend([honig, banane, apfel,maracuja, orange, mango, blaubeeren])

# FAT

nusskernmischung = Food("Nusskernmischung", 21, 56, 11, 100, "g", [0.3])
walnüsse = Food("Walnüsse", 16, 71, 6, 100, "g", [0.3])
avocado = Food("Avocado", 2, 15, 9, 100, "g", [1.5, 2])
olivenoel = Food("Olivenöl", 0, 100, 0.2, 100, "g", [0.15, 0.3, 0.45])
butterschmalz = Food("Butterschmalz", 0.3, 100, 0, 100, "g", [0.15])
butter = Food("Butter", 0.7, 83.2, 0.7, 100, "g", [0.15])
hummus = Food("Hummus", 7.9, 9.6, 14.3, 100, "g", [0.25, 0.5, 0.75])
mandelmus = Food("Mandelmus", 21, 52, 19, 100, "g", [0.15, 0.3])

nutrition_set_all.extend([nusskernmischung])
nutrition_set_lukas.extend([nusskernmischung])
nutrition_set_daniel.extend([nusskernmischung])
nutrition_set_lucas.extend([nusskernmischung])
nutrition_set_rico.extend([nusskernmischung])
nutrition_set_stefan.extend([nusskernmischung])
nutrition_set_schatu.extend([nusskernmischung])
nutrition_set_yasar.extend([nusskernmischung])
nutrition_set_sebastian.extend([avocado])
nutrition_set_soula.extend([nusskernmischung, avocado, olivenoel, mandelmus])
nutrition_set_emil.extend([nusskernmischung, avocado])
nutrition_set_adrian.extend([nusskernmischung])
nutrition_set_martin.extend([nusskernmischung])
nutrition_set_celina.extend([avocado, butter])

nutrition_set_standard = nutrition_set_all





