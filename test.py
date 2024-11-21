import re
import time
import tkinter as tk
from tkinter import simpledialog, PhotoImage, LabelFrame,messagebox
from tkinter.ttk import Label


def ouvrir_formulaire():
    def valider_commande():
        nom = entry_nom.get()
        adresse = entry_adresse.get()
        telephone = entry_telephone.get()

        # Vérification avec regex
        nom_prenom_regex = r'^[A-Za-zÀ-ÖØ-öø-ÿ\- ]+$'
        adresse_regex = r'^[\w\s,.-]+$'
        telephone_regex = r'^\+?\d{10,15}$'  # Format pour un numéro international ou national

        if not re.match(nom_prenom_regex, nom):
            messagebox.showerror("Erreur", "Nom invalide")
        elif not re.match(adresse_regex, adresse):
            messagebox.showerror("Erreur", "Adresse invalide")
        elif not re.match(telephone_regex, telephone):
            messagebox.showerror("Erreur", "Numéro de téléphone invalide")
        else:
            messagebox.showinfo("Succès", "Commande validée")
            Formulaire.infos = f"vos informations:\n nom: {nom}\n adresse: {adresse}\n num: {telephone}"
            time.sleep(1)
            Formulaire.destroy()



    Formulaire = tk.Toplevel()
    Formulaire.title("Formulaire de commande")
    Formulaire.geometry("300x400")
    titre = tk.Label(text="Remplire La Formulaire !", font=("Inter Medium", 17, "bold"), foreground="green")
    titre.pack(pady=10)

    # Champs de formulaire
    nom = tk.Label(Formulaire, text="Nom complet:", font=("Inter Medium", 8))
    nom.pack(anchor="w", padx=50)
    entry_nom = tk.Entry(Formulaire, font=("Inter Medium", 13))
    entry_nom.pack()

    adresse = tk.Label(Formulaire, text="Adresse:", font=("Inter Medium", 8))
    adresse.pack(anchor="w", padx=50, )
    entry_adresse = tk.Entry(Formulaire, font=("Inter Medium", 13))
    entry_adresse.pack()

    num = tk.Label(Formulaire, text="Numéro de téléphone:", font=("Inter Medium", 8))
    num.pack(anchor="w", padx=50)
    entry_telephone = tk.Entry(Formulaire, font=("Inter Medium", 13))
    entry_telephone.pack()

    # Bouton de validation
    btn_valider = tk.Button(Formulaire, text="Valider La Commande", font=("Inter Medium", 8), bg="lightgreen",command=valider_commande)
    btn_valider.pack(pady=20)
    Formulaire.infos = None
    Formulaire.wait_window()  # Attendre que la fenêtre soit fermée
    return Formulaire.infos  # Retourne les informations sauvegardées

    # Vous pouvez ensuite traiter les données ou les envoyer à la base de données


def charger_reponses(fichier):
    reponses = []
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            for ligne in f:
                if ':' in ligne:
                    question, reponse = ligne.strip().split(':', 1)
                    reponses.append((re.compile(question, re.IGNORECASE), reponse))
        return reponses
    except FileNotFoundError:
        with open(fichier, 'w', encoding='utf-8') as f:
            f.write("")
        return []


def ajouter_reponse(fichier, question, reponse):
    with open(fichier, 'a', encoding='utf-8') as f:
        f.write(f"{question}:{reponse}\n")
    reponses.append((re.compile(question, re.IGNORECASE), reponse))


def chatbot(reponses, message, fichier):
    formulaire_regex = r".*\b(valider|passer|faire|envoyer|commander|effectuer)\s*(ma|la|une|mon)?\s*(commande|ordre|achat|demande)\b.*"
    if re.match(formulaire_regex,message):
        infos=ouvrir_formulaire()
        return infos

    else:
        for regex, reponse in reponses:
            if regex.search(message):
                return reponse

    nouvelle_reponse = simpledialog.askstring("Enseigner au chatbot","Je n'ai pas compris. Quelle réponse devrais-je donner ?")
    if nouvelle_reponse:
        ajouter_reponse(fichier, message, nouvelle_reponse)
        return "Merci, j'ai appris une nouvelle réponse !"
    else:
        return "D'accord, peut-être une autre fois."


def envoyer_message():
    message = message_entry.get()
    if message.strip():
        # Créer un nouveau frame pour contenir les messages
        message_container = tk.Frame(messages_canvas, bg="#eaeded")
        messages_canvas.create_window((0, current_message_y[0]), window=message_container, anchor="nw", width=330)

        # Fonction pour mettre à jour le défilement
        def defiler():
            messages_canvas.update_idletasks()
            messages_canvas.configure(scrollregion=messages_canvas.bbox("all"))
            messages_canvas.yview_moveto(1.0)

        reponse = chatbot(reponses, message, fichier_reponses)
        def afficher_reponse():
            msg2 = Label(lb2, text=reponse, font=("Bahnschrift", 13), background="white", wraplength=250, justify="left")
            msg2.pack(anchor="w")
            defiler()  # Défilement automatique
        # Animation et réponse
        def afficher_animation(lb2, callback):
            def afficher_points(i=0):
                if i < 3:  # Animation limitée à 3 étapes
                    msg_animation.config(text="." * (i + 1))
                    defiler()  # Défilement automatique
                    lb2.after(500, afficher_points, i + 1)  # Appel récursif
                else:
                    msg_animation.destroy()
                    callback()  # Appeler le callback pour afficher la réponse

            msg_animation = Label(lb2, text="", font=("Bahnschrift SemiBold", 17, "bold"), background="white", wraplength=250, justify="left")
            msg_animation.pack(anchor="w")
            defiler()  # Défilement automatique
            afficher_points()

        # Message de l'utilisateur
        lb1 = LabelFrame(message_container, bg="#3d41ff", padx=5, pady=5, borderwidth=0)
        auteur_label = Label(lb1, text="Vous", font=("Arial", 9, "italic"), foreground="lightblue",
                                 background="#3d41ff")
        auteur_label.pack(anchor="e")
        msg1 = Label(lb1, text=message, font=("Bahnschrift", 13), background="#3d41ff", wraplength=250,
                         foreground="white", borderwidth=0)
        msg1.pack(anchor="e")
        lb1.pack(anchor="e", pady=5)

        # message de bot

        lb2 = LabelFrame(message_container, bg="white", padx=5, pady=5, borderwidth=0)
        auteur_label_bot = Label(lb2, text="Bot", font=("Arial", 9, "italic"), foreground="grey", background="white")
        auteur_label_bot.pack(anchor="w")
        lb2.pack(anchor="w", pady=5)

        afficher_animation(lb2, afficher_reponse)

        # Mettre à jour la position Y pour le prochain message
        message_container.update_idletasks()
        current_message_y[0] += message_container.winfo_height()

        # Configurer la région de défilement
        defiler()

        # Effacer le champ d'entrée
        message_entry.delete(0, tk.END)

# Configuration initiale
fichier_reponses = 'DataBase.txt'
reponses = charger_reponses(fichier_reponses)
current_message_y = [0]  # Variable pour suivre la position Y des messages

# Fenêtre principale
root = tk.Tk()
root.title("AMN Chatbot")
root.configure(bg="#eaeded")
root.geometry("370x545")
root.resizable(False, False)

# En-tête
fr1 = tk.LabelFrame(root,padx=94, bg="white")
fr1.pack()

try:
    logo = PhotoImage(file=r"D:\projet Chat Bot\chat logo trans.png")
    logo_img = Label(fr1, image=logo,background="white")
    logo_img.place(x=-80, y=0)
    logo_img.pack(side=tk.LEFT)
except tk.TclError:
    # Fallback si l'image n'est pas trouvée
    Label(fr1, text="LOGO", font=("Arial", 12), background="white").pack(side=tk.LEFT)

botname = Label(fr1, text="Restau-Bot", font=("Bahnschrift", 17),background="white")
botname.pack(pady=0)

online = Label(fr1, text="online", font=("Arial", 10), foreground="green",background="white")
online.pack(side=tk.LEFT,pady=0)

# Zone de messages avec scrollbar
message_frame = tk.Frame(root, bg="#eaeded")
message_frame.pack(pady=0, padx=5, fill="both", expand=True)

messages_canvas = tk.Canvas(message_frame, bg="#eaeded", width=350, height=400)
scrollbar = tk.Scrollbar(message_frame, orient="vertical",command=messages_canvas.yview)
messages_canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y",anchor="w")
messages_canvas.pack(side="left", fill="both", expand=True)

# Zone de saisie
cadre2 = tk.LabelFrame(root, bg="white",padx=12,pady=5)
cadre2.pack(pady=5)
message_entry = tk.Entry(cadre2, font=("Inter", 15), width=23,borderwidth=0)
message_entry.pack(padx=0, pady=0, side=tk.LEFT,)
message_entry.focus()
message_entry.bind("<Return>", lambda event: envoyer_message())

try:
    icon = PhotoImage(file=r"D:\projet Chat Bot\send trans.png")
    send_button = tk.Button(cadre2, image=icon, command=envoyer_message,borderwidth=0,background="white")
except tk.TclError:
    # Fallback si l'image n'est pas trouvée
    send_button = tk.Button(cadre2, text="Envoyer", command=envoyer_message)
send_button.pack(pady=0, side=tk.LEFT)

# Pied de page
powb = Label(root, text="Powered by AMiNe", font=("arial", 8),background="#eaeded", foreground="grey")
powb.pack(pady=0)

# Création de la fenêtre principale

root.mainloop()