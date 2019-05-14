#
#Moje kamarádka učí soukromě němčinu. Potřebuje pro klienty připravit texty, které se časem naučí nazpaměň (jedná se o právní předpisy). Proto jim připravuje stále stejný text, ve kterém vynechá nejprve každé 5. slovo, později každé 4. slovo atd., až se text naučí zpaměti. Výstupem bude nový soubor. Pracujte se souborem lorem.py.
#Vytvořte pro ni program, jehož vstupem bude textový soubor a informace, kolikátý znak se má zaměnit.
#
#Rozbor 
#1.načíst soubor
#2.splitnout slova podle mezery do seznamu
#3.procházet jednotlivá slova seznamu
#	když se jedná o x-té slovo:
#		procházet písmenka a:
#			písmenko nahradit pomlčkou
#			vynechat interpunkci
#		upravené slovo přidat do seznamu
#	jinak:
#	původní slovo přidat do seznamu
#4.seznam spojit pomocí mezery do řetězce, řetězec uložit do nového souboru
#
#1.rodelit string--seznam
#oddělovač je mezera
#2-budu procházet prvk seznamu: když narazím na 5,10,15,... slovo tak to tahradím za pomlčky když to bude každé tak provede
# slovo upraveno = tam si uloží kolik pomlček má dané slovo, len toho slove, vyhodí to číslici 4
# cyklus prochází znaky toho slovo, a do nějké proměné slovo upraveno si přes += si přidá náhradné znak, += "-"
#vysledek.append(slovoUpr)
#else jinak do toho výsldeku přidej přes append prvek seznamu, prvek který ted kontroluji
#když to máme udělané tak výsledek jouineme do stringu a ten string pak uložíme do souboru
#
#
#3. Proveďte optimalizaci kódu programu "doplnovacka.py" tak, abys problém řešila s využitím vlastní funkce 
#(vstupními parametry bude vložený text či název souboru, který se má načíst, a celé číslo představující, kolikáté slovo textu se má zaměnit za hvězdičky). 
#Tuto optimalizovanou verzi nahraj do existujícího projektu na GitHubu

with open("song.txt") as f:
	text = f.read()
f.closed#print(text)#vypritneme si to abychom videli jestli to pracuje

pocet_hvezdicek = int(input("Zadej kolikáté slovo se má nahradit kvězdičkama. "))

text = text.replace("\n", "# ")

seznam = []
seznam = text.split(" ")
print(seznam)
vysledek = []
interpunkce = ",.!-;\""

for i in range(0, len(seznam)):
	slovo = seznam[i]
	slovoUpraveno = ""
	if ((i + 1) % pocet_hvezdicek ==0):
		for pismeno in slovo:
			if pismeno not in interpunkce:
				slovoUpraveno += "*"
		else:
			slovoUpraveno +=pismeno
		vysledek.append(slovoUpraveno)
	else:
		vysledek.append(slovo)

s = " ".join(vysledek)#spojí všechny prvky do řetězce a dodělovačem bude mezera
s = s.replace("# ", "\n")
print(s)

