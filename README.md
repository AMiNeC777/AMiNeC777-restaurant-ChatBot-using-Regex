﻿# Amine_chatbot
 Le projet consiste  à créer un chatbot simple en Python . Ce chatbot est un programme informatique qui simule une conversation avec un utilisateur humain en suivant un ensemble de règles prédéfinis.
 
# Objectif du projet :
 
L'objectif principale était de développer un chatbot qui :
- Répond aux questions courantes de l'utilisateur  à partir de données stockées dans un fichier texte.
- Permet  à l'utilisateur de lui enseigner de nouvelles réponses .
- Fournit une interface graphique où les messages sont affichés de manière lisible .
Le chatbot est conçu pour apprendre des interactions en ajoutant de nouvelles réponses dans le fichier  à chaque fois qu'il rencontre une question  à laquelle il ne peut pas répondre .

# 1-fonctionnement globale du programme :
## 1-1.Chargement des réponses :
- Le programme lit chaque ligne du fichier, puis sépare la question et la réponse  à l'aide du caractère" : ".
- Les questions sont transformées en expressions régulaires, ce qui permet au chatbot de répondre de manière flexible  à differentes variations d'une  même question .
## 1-2.Interaction utilisateur :
Lorsqu'un utilisateur envoie un message au chatbot, le programme :
- Recherche si une réponse est  déjà présente pour la question posée dans la base de données de réponses.
- Si une réponse trouvée, elle est affichée à l'écran.
- Si aucune réponse n'est trouvée, le chatbot demande  à l'utilisateur d'enseigner une nouvelle réponse, puis l'ajoute au fichier "reponses.txt" .
## 1-3.Interface graphique :
Le programme utilise Tkinter pour créer une interface graphique . Voivi les composants principaux de l'interface :
- Fenêtre principale : La fenêtre principale contient un en-tête avec le titre "CHAT BOT" , un espace pour afficher les messages échangés, un champ de saisie pour l'utilisateur et un bouton pour envoyer des messages.
- Zone de saisie : L'utilisateur peut taper un message dans un champ de texte et appuyer sur "Entrée" ou cliquer sur le bouton pour envoyer le message.
- Affichage des messages : les messages sont affichés dans un cadre . les messages de l'utilisateur sont alignés  à droite, tandis que les réponses du chatbot sont alignées  à gauche .

![Screenshot 2024-11-17 023450](https://github.com/user-attachments/assets/c30ba130-7491-42e2-a284-f7bd4b151e70) ![Screenshot 2024-11-17 023746](https://github.com/user-attachments/assets/ff8853d9-1d42-4e0e-8f08-7d10d10ebf41) 

# 2-Détails techniques :
## 2-1.Chargement et stockage des réponses :
Le fichier "reponses.txt" contient des paires de question-réponse , le programme charge ces paires et les convertit en une liste d'expressions régulières pour comparer les messages de l'utilisateur.
Si le fichier n'existe pas, le programme affiche un message d'erreur et continue sans charger les réponses.

![Screenshot 2024-11-17 023830](https://github.com/user-attachments/assets/4cc48b26-282b-46d4-9e6c-40b72f79ad22)


2-2.Fonctionnement du Chatbot :
Lorsqu'un message est envoyé, la fontion "chatbot()" est appelée pour rechercher une réponse dans la liste de réponses. Si aucune correspondance n'est trouvée, la fonction demande  à l'utilisateur d'enseigner une nouvelle réponse. Cette réponse est ensuite ajoutée au fichier de réponses et  à la mémoire du programme. Puis La fonction ouvrir_formulaire() , cette fonction a été ajoutée spécifiquement pour ce genre de chatbot, cette dernière permet aux utilisateurs(clients) de démarrer le processus d’une commande de manière simple et interactive. Après l’activation, cette fonctionnalité ouvre un formulaire où les clients peuvent spécifier leurs choix de plats, quantités...Ensuite de saisir les coordonnées pour finaliser leurs commandes. Cette approche facilite et accélère l'expérience de commande en ligne tout en garantissant une meilleure interaction utilisateur


2-3.Affichage et gestion des messages :
L'interface est construite autour de frames et labels pour afficher les messages. Les messages de l'utilisateur et les réponses du chatbot sont affichées dans des cadres (LabelFrame) qui permettent de les organiser de manière lisible.

