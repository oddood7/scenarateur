import warnings
warnings.filterwarnings("ignore")

from transformers import pipeline
import json
import os
from datetime import datetime

class AssistantScenario:
	def __init__(self):
		"""Initialise l'assistant du scenario"""
		self.generator = None
		self.histoires_sauvees = []
		self.dossier_sauvegardees = "histoires"

		if not os.path.exists(self.dossier_sauvegardees):
			os.makedirs(self.dossier_sauvegardees)
			
	def charger_modele(self):
		"""Charger Modele GPT2"""
		if self.generator is None:
			print("Chargement de GPT2 ...")
			self.generator = pipeline('text-generation', model='gpt2')  
			print("Modele charge avec succees\n")
		else:
			print("Modele deja charge\n")

	def afficher_menu(self):
		"""Afficher le menu principal"""
		print("\n" + "="*50)
		print("ASSISTANT DE SCENARIO - MENU")
		print("="*50)
		print("1. Generer une histoire complete")
		print("2. Creer un personnage")
		print("3. Decrire un univers")
		print("4. Generation aleatoire rapide")
		print("5. Voir les histoires sauvegardees")
		print("6. Continuer une histoire existante")
		print("7. Quitter")
		print("-"*50)
	
	def generer_personnage(self):
		"""Genere un personnage avec plusieurs caracteristiques"""
		print("\nCREATION PERSONNAGE")
		print("-"*30)

		nom = input("Nom du personnage: ")
		profession = input("Profession (en anglais): ")
		trait = input("Trait de caractere: ")

		prompt_physique = f"{nom} is a {trait} {profession}. {nom} looks"
		desc_physique = self.generer_texte(prompt_physique, 25) 

		prompt_personnalite = f"{nom} the {profession} is {trait} and"
		desc_personnalite = self.generer_texte(prompt_personnalite, 30)

		prompt_background = f"{nom} became a {profession} because"
		desc_background = self.generer_texte(prompt_background, 35)

		personnage = {
			"nom": nom,
			"profession": profession,
			"trait": trait,
			"description_physique": desc_physique,
			"personnalite": desc_personnalite,
			"background": desc_background,
			"date_creation": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		}

		self.afficher_personnage(personnage)

		if input("Sauvergarder ce personnage ? (o/n): ").lower() == 'o':
			self.sauvegarder_personnage(personnage)
		
		return personnage
	
	def generer_univers_detaille(self):
		"""Generer un univers avec plusieurs aspects"""
		print("\n CREATION D'UNIVERS")
		print("-"*25)

		nom_lieu = input("Nom du lieu: ")
		type_lieu = input("Type de lieu: ")
		ambiance = input("Ambiance du lieu: ")

		prompt_general = f"The {ambiance} {type_lieu} called {nom_lieu} is"
		desc_general = self.generer_texte(prompt_general, 30)

		prompt_habitants = f"The people living in {nom_lieu} are"
		desc_habitants = self.generer_texte(prompt_habitants, 25)

		prompt_mystere = f"The mysterious secrets of {nom_lieu} include"
		desc_mystere = self.generer_texte(prompt_mystere, 30)

		univers = {
			"nom": nom_lieu,
			"type": type_lieu,
			"ambiance": ambiance,
			"description_generale": desc_general,
			"habitants": desc_habitants,
			"mysteres": desc_mystere,
			"date_creation": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		}

		self.afficher_univers(univers)

		if input("Sauvergarder cet univers ? (o/n): ").lower() == 'o':
			self.sauvegarder_univers(univers)
		
		return univers
	
	def generer_histoire_complete(self):
		"""Genere l'histoire complete etape par etape"""
		print("\n GENERATION D'HISTOIRE COMPLETE")
		print("-"*35)

		personnage = input("Nom du personnage principal: ")
		metier = input("Profession du heros: ")
		lieu = input("Lieu principal du scenario: ")
		genre = input("Genre du scenario: ")

		print(f"\n Generation de l'histoire de {personnage} ...\n")

		parties = []

		prompt_intro = f"In a {genre} story, {personnage} the {metier} lived in {lieu}. One day,"
		intro = self.generer_texte(prompt_intro, 40)
		parties.append(("INTRODUCTION", intro))

		prompt_conflit = f"{personnage} discovered a terrible problem:"
		conflit = self.generer_texte(prompt_conflit, 35)
		parties.append(("CONFLIT", conflit))

		prompt_action = f"To solve this, {personnage} decided to"
		action = self.generer_texte(prompt_action, 40)
		parties.append(("ACTION", action))

		prompt_resolution = f"Finally, {personnage} managed to"
		resolution = self.generer_texte(prompt_resolution, 35)
		parties.append(("RESOLUTION", resolution))

		histoire_complete = {
			"personnage": personnage,
			"metier": metier,
			"lieu": lieu,
			"genre": genre,
			"parties": parties,
			"date_creation": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		}

		self.afficher_histoire_complete(histoire_complete)

		if input("Sauvergarder cette histoire ? (o/n): ").lower() == 'o':
			self.sauvegarder_histoire(histoire_complete)
		
		return histoire_complete
	
	def generation_aleatoire(self):
		"""Generation rapide avec des elements aleatoires"""
		print("\n GENERATION ALEATOIRE RAPIDE")
		print("-"*35)

		prompts_aleatoires = [
			"The ancient wizard discovered a hidden",
			"Captain Alex's spaceship crashed on",
			"At the haunted mansion, detective John found",
			"The brave knight stood in front of the dragon and",
			"The mysterious stranger entered the bar and",
			"Deep in the jungle, the explorer heard",
			"The princess escaped the tower by",
			"The robot awakened in the abandoned laboratory and"
		]

		import random
		prompt = random.choice(prompts_aleatoires)

		print(f"Prompt selectionne: {prompt}")
		print("\nHistoire generee:")
		print("-"*25)

		resultat = self.generer_texte(prompt, 50)
		print(resultat)

		if input("\n Continuer cette histoire ? (o/n): ").lower() == 'o':
			self.continuer_histoire(resultat)

	def continuer_histoire(self, debut_histoire):
		"""Continuer une histoire existante"""
		print("\n CONTINUATION DE L'HISTOIRE")
		print("-"*35)

		mots = debut_histoire.split()
		if len(mots) > 15:
			nouveau_prompt = " ".join(mots[-15:])
		else:
			nouveau_prompt = debut_histoire
		
		print(f"Suite de: ...{nouveau_prompt}")
		print("\n Continue: ")
		print("-"*15)

		suite = self.generer_texte(nouveau_prompt, 45)
		print(suite)

		if input("\n Continuer cette histoire ? (o/n): ").lower() == 'o':
			self.continuer_histoire(suite)
	
	def generer_texte(self, prompt, max_tokens=30):
		"""Generer du texte a partir d'un prompt"""
		result = self.generator(
			prompt,
			max_new_tokens=max_tokens,
			temperature=0.7,
			do_sample=True,
			pad_token_id=50256,
			truncation=True
		)
		return result[0]['generated_text']
	
	def afficher_personnage(self, personnage):
		"""Afficher un personnage"""
		print(f"\n{personnage['nom'].upper()}")
		print("="*30)
		print(f"Profession: {personnage['profession']}")
		print(f"Trait: {personnage['trait']}")
		print(f"Apparence: {personnage['description_physique']}")
		print(f"Personnalite: {personnage['personnalite']}")
		print(f"Histoire: {personnage['background']}")
	
	def afficher_univers(self, univers):
		"""Afficher un univers"""
		print(f"\n{univers['nom'].upper()}")
		print("="*30)
		print(f"Type: {univers['type']}")
		print(f"Ambiance: {univers['ambiance']}")
		print(f"\nDescription: {univers['description_generale']}")
		print(f"\nHabitants: {univers['habitants']}")
		print(f"\nMysteres: {univers['mysteres']}")
	
	def afficher_histoire_complete(self, histoire):
		"""Afficher une histoire complete formatee"""
		print(f"\n HISTOIRE DE {histoire['personnage'].upper()}")
		print("="*50)

		for titre, contenu in histoire['parties']:
			print(f"\n{titre}")
			print("-" * len(titre))
			print(contenu)

	def sauvegarder_personnage(self, personnage):
		"""Sauvegarder un personnage"""
		nom_fichier = f"personnage_{personnage['nom']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
		chemin = os.path.join(self.dossier_sauvegardees, nom_fichier)

		with open(chemin, 'w', encoding='utf-8') as f:
			json.dump(personnage, f, indent=2, ensure_ascii=False)
		
		print(f"Personnage sauvegarde: {nom_fichier}")
	
	def sauvegarder_histoire(self, histoire):
		"""Sauvegarder une histoire"""
		nom_fichier = f"histoire_{histoire['personnage']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
		chemin = os.path.join(self.dossier_sauvegardees, nom_fichier)

		with open(chemin, 'w', encoding='utf-8') as f:
			json.dump(histoire, f, indent=2, ensure_ascii=False)
		
		print(f"Histoire sauvegardee: {nom_fichier}")
	
	def sauvegarder_univers(self, univers):
		"""Sauvegarder un univers"""
		nom_fichier = f"univers_{univers['nom']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
		chemin = os.path.join(self.dossier_sauvegardees, nom_fichier)

		with open(chemin, 'w', encoding='utf-8') as f:
			json.dump(univers, f, indent=2, ensure_ascii=False)
		
		print(f"Univers sauvegarde: {nom_fichier}")
	
	def voir_sauvegardes(self):
		"""Afficher les fichiers sauvegardes"""
		print("\nHISTOIRES SAUVEGARDEES")
		print("-"*30)

		fichiers = os.listdir(self.dossier_sauvegardees)
		if not fichiers:
			print("Aucune sauvegarde trouvee.")
			return
		
		for i, fichier in enumerate(fichiers, 1):
			print(f"{i}. {fichier}")
		
		try:
			choix = int(input(f"\nCharger un fichier (1-{len(fichiers)}, 0 pour retour): "))
			if 1 <= choix <= len(fichiers):
				self.charger_sauvegarde(fichiers[choix-1])
		except ValueError:
			print("Choix invalide.")
		
	def charger_sauvegarde(self, nom_fichier):
		"""Charger et affiche une sauvegarde"""
		chemin = os.path.join(self.dossier_sauvegardees, nom_fichier)

		try:
			with open(chemin, 'r', encoding='utf-8') as f:
				data = json.load(f)
			
			if 'parties' in data:
				self.afficher_histoire_complete(data)
			elif 'profession' in data:
				self.afficher_personnage(data)
			elif 'type' in data:
				self.afficher_univers(data)
			
			if 'parties' in data:
				if input("\nContinuer cette histoire ? (o/n): ").lower() == 'o':
					derniere_partie = data['parties'][-1][1]
					self.continuer_histoire(derniere_partie)
		
		except Exception as e:
			print(f"Erreur lors du chargement: {e}")
		
	def run(self):
		"""Lancer l'application"""
		print("Bienvenue dans l'assistant scenario!")
		print("Cet outil utilise l'IA pour vous aider a creer des histoires")

		while True:
			self.afficher_menu()

			try:
				choix = input("Votre choix (1-7): ")

				if choix == "1":
					self.charger_modele()
					self.generer_histoire_complete()

				elif choix == "2":
					self.charger_modele()
					self.generer_personnage()
				
				elif choix == "3":
					self.charger_modele()
					self.generer_univers_detaille()
				
				elif choix == "4":
					self.charger_modele()
					self.generation_aleatoire()

				elif choix == "5":
					self.voir_sauvegardes()
				
				elif choix == "6":
					self.charger_modele()
					print("Chargez d'abord une histoire depuis les sauvegardes...")
					self.voir_sauvegardes()
				
				elif choix == "7":
					print("\nAu revoir ! Merci d'avoir utilise l'Assistant de Scenario!")
					break
				else:
					print("Choix invalide. Veuillez choisir entre 1 et 7.")
				
				input("\nAppuyez sur Entree pour continuer...")
			
			except KeyboardInterrupt:
				print("\n Au revoir !")
				break
			except Exception as e:
				print(f"Une erreur s'est produite: {e}")

if __name__ == "__main__":
	assistant = AssistantScenario()
	assistant.run()