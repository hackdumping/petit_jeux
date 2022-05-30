from  random import*


print("\n\n\t\tLISTE DES JEUX DISPONIBLE : \n\n")
print ("\t1- Chiffre cacher \n")
print ("\t2- simulateur de 02 dés\n")
print ("\t3- pierre-papier-ciseaux\n")
print ("\t4- OFF\n")

choix=int(input("\n\tchoisir votre jeux >> "))
while(choix<1 or choix>4) :
	print ("\n\tvaleur hors plage ! Ressayer ..\n")
	choix=int(input("\n\tchoisir votre jeux >> "))
	
if(choix==1) :
	print ("\n\n\t\tCHERCHER LE CHIFFRE CACHER\n\n")
	dec= 1
	nom=input("\n\tEntrer votre nom : ")
	print ("\n\tBienvenue au jeux",nom)
	print ("\n\tUn chiffre compris entre 0 et 100 a ete cacher . Tenter de trouver ce chiffre en un nombre d'essai inferieur ou egal a 6\n\n")
	score= 0
	while(dec==1):
		rd= randint(0,100)
		nb=int(input("\tEntrer le nombre d'essai : "))
		while(nb<1 or nb>6) :
			print ("\n\tValeur hors plage ! reessayer .. \n")
			nb=int(input("\tEntrer le nombre d'essai : "))
		print ("\n\n\t// Le jeu peux commencer //\n\n")
		for i in range (nb) :
			es=int(input("\n\tQuel est le nombre mystere ? >> "))
			if(es > rd) :
				print ("\n\tLe nombre mystere est plus petit que ce nombre\n")
			elif (es < rd) :
				print ("\n\tLe nombre mystere est plus grand que ce nombre\n")
			else :
				if(i<=3) :
					print (f"\n\tWAOUH ! bravo {nom} vous avez trouver en {i} essais seulemsnt\n")
					score=score+4
					break
				else :
					print ("\n\t BRAVO vous avez trouver le nombre mystere !! ..\n")
					score=score+2
					break
			if((es != rd) and (i== nb-1)) :
				print (f"\n\tDesolé {nom} vous avez PERDU . \n")
				print (f"\n\tLe nombre mystere était {rd}..\n")
		print ("\n\tSCORE = ",score," .\n")
		print ("\n\n\tVoulez vous reessayer ?  \t1- OUI  \t2- NON\n")
		dec= int(input("\t>> "))
		while(dec<1 or dec>2) :
			print("\n\tValeur hors plage !\n")
			print ("\n\n\tVoulez vous reessayer ?  \t1- OUI  \t2- NON\n")
			dec= int(input("\t>> "))
		if(dec==2) :
			print ("\n\n\n\tMerci et a bientot ! ..\n\n")
		if(dec==1) :
			print ("\n\n\tSuper! \n\n")
elif(choix==2) :
	print ("\n\n\t\tDONNER LA FACE SUPERIEUR DE DEUX DÉS\n\n")
	nom= input("\n\tEntrer votre nom : ")
	print(f"\n\tBienvenue au jeu {nom}")
	print("\n\tDeux dés ont été lancé . deviner les faces superieurs de ces 02 dés\n")
	d1=[1,2,3,4,5,6]
	d2=[1,2,3,4,5,6]
	dec=1
	
	while(dec==1) :
		score=0
		nd1=choice(d1)
		nd2=choice(d2)
		print ("\n\n\t// Le jeu peux commencer //\n\n")
		es1=int(input("\n\tQuel est la face superieur du 1er dé >> "))
		if(es1==nd1) :
			print("\n\n\t -- 1er dé TROUVÉ --")
		else :
			print(f"\n\n\t -- 1er dé RATÉ --  \t//La face était {nd1}")
		es2=int(input("\n\n\tQuel est la face superieur du 2eme dé >> "))
		if(es2==nd2) :
			print("\n\n\t -- 2ème dé TROUVÉ --")
		else :
			print(f"\n\n\t -- 2ème dé RATÉ --  \t//La face était {nd2}")
		if(es1==nd1 and es2==nd2) :
			score=score+4
		elif((es1==nd1 and es2!=nd2) or (es1!=nd1 and es2==nd2)) :
			score=score+2
		else :
			score +=0
		print (f"\n\tSCORE = {score} .\n")
		print ("\n\n\tVoulez vous reessayer ?  \t1- OUI  \t2- NON\n")
		dec= int(input("\t>> "))
		while(dec<1 or dec>2) :
			print("\n\tValeur hors plage !\n")
			print ("\n\n\tVoulez vous reessayer ?  \t1- OUI  \t2- NON\n")
			dec= int(input("\t>> "))
		if(dec==2) :
			print ("\n\n\n\tMerci et a bientot ! ..\n\n")
		if(dec==1) :
			print ("\n\n\tSuper! \n")
elif(choix==3) :
	liste=["pierre","papier","ciseaux"]
	print ("\n\n\t\tPIERRE-PAPIER-CISEAUX\n\n")
	nom= input("\n\tEntrer votre nom : ")
	print(f"\n\n\tBienvenue au jeu {nom}\n\n")
	dec=1
	while(dec==1) :
		score_moi=0
		score_mach=0
		nb=int(input("\tEntrer le nombre de tour de jeu  : "))
		while(nb<1) :
			print ("\n\t reessayer .. \n")
			nb=int(input("\tEntrer le nombre de tour de jeu  : "))
		print(f"\n\tVous bénéficiez de {nb} tours de jeu\n")
		print ("\n\n\t// Le jeu peux commencer //\n\n")
		for i in range(nb) :
			ch=choice(liste)
			es=int(input("\n\t1- pierre ; 2- papier ; 3- ciseaux ? >> "))
			while(es<1 or es>3) :
				print("\n\tValeur hors plage ! Ressayer..\n")
				es=int(input("\n\t1- pierre ; 2- papier ; 3- ciseaux ? >> "))
			if((ch== "pierre" and es==1) or (ch== "papier" and es==2) or (ch== "ciseaux" and es==3)) :
				score_moi +=0
				score_mach +=0
			if((ch== "pierre" and es==3) or (ch== "ciseaux" and es==2) or (ch== "papier" and es==1)) :
				score_mach +=1
			if((ch== "pierre" and es==2) or (ch== "ciseaux" and es==1) or (ch== "papier" and es==3)) :
				score_moi +=1
			print(f"\n\n\tVous = {score_moi} \tMachine = {score_mach}\n")
		if(score_moi > score_mach) :
			print("\n\t-- BRAVO ! Vous avez GAGNER la partie --\n")
		elif(score_moi < score_mach) :
			print("\n\t-- DESOLÉ vous avez PERDUE la partie --\n")
		else :
			print("\n\t-- Vous avez fait un MATCH NUL --\n")
		print ("\n\n\tVoulez vous reessayer ?  \t1- OUI  \t2- NON\n")
		dec= int(input("\t>> "))
		while(dec<1 or dec>2) :
			print("\n\tValeur hors plage !\n")
			print ("\n\n\tVoulez vous reessayer ?  \t1- OUI  \t2- NON\n")
			dec= int(input("\t>> "))
		if(dec==2) :
			print ("\n\n\n\tMerci et a bientot ! ..\n\n")
		if(dec==1) :
			print ("\n\n\tSuper! \n\n")
else :
	print ("\n\n\n\tMerci et a bientot ! ..\n\n")
	
	
