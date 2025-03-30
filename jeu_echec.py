# Jeu d'échec

# Librairies
import pygame
import os

# Appel
pygame.init()

# CSS
blanc = pygame.Color('#DDDDDD')
vert = pygame.Color('#66CC66')
noir = pygame.Color('#000000')
            
# Pygame
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
nb_cases_cote = 8

# Taille de l'écran
largeur_ecran, hauteur_ecran = screen.get_size()

# Taille d'une case et du plateau
taille_plateau = 480
taille_case = taille_plateau // nb_cases_cote
largeur_plateau = nb_cases_cote * taille_case
hauteur_plateau = nb_cases_cote * taille_case

# Import des pieces
taille_piece = (taille_case, taille_case)
images_pieces = {}
nom_images = [
    "pion_blanc", "pion_noir", "tour_blanc", "tour_noir", "fou_blanc", "fou_noir", "cavalier_blanc", "cavalier_noir", "reine_blanc", "reine_noir", "roi_blanc", "roi_noir"
]
print(f"Contenu du dossier images/: {os.listdir('images/')}")
for nom in nom_images:
    chemin_images = f"images/{nom}.png" 
    if os.path.exists(chemin_images):
        images_pieces[nom] = pygame.transform.scale(pygame.image.load(chemin_images), taille_piece)
    else:
        print(f"Image manquante : {chemin_images}")


# Mise en place des pièces
piece_select = None
pieces = {
    "pion_noir_1": ("pion_noir", 0, 1),
    "pion_noir_2": ("pion_noir", 1, 1),
    "pion_noir_3": ("pion_noir", 2, 1),
    "pion_noir_4": ("pion_noir", 3, 1),
    "pion_noir_5": ("pion_noir", 4, 1),
    "pion_noir_6": ("pion_noir", 5, 1),
    "pion_noir_7": ("pion_noir", 6, 1),
    "pion_noir_8": ("pion_noir", 7, 1),
    "tour_noir_g": ("tour_noir", 0, 0),
    "tour_noir_d": ("tour_noir", 7, 0),
    "cavalier_noir_g": ("cavalier_noir", 1, 0),
    "cavalier_noir_d": ("cavalier_noir", 6, 0),
    "fou_noir_g": ("fou_noir", 2, 0),
    "fou_noir_d": ("fou_noir", 5, 0),
    "reine_noir": ("reine_noir", 3, 0),
    "roi_noir": ("roi_noir", 4, 0),
    "pion_blanc_1": ("pion_blanc", 0, 6),
    "pion_blanc_2": ("pion_blanc", 1, 6),
    "pion_blanc_3": ("pion_blanc", 2, 6),
    "pion_blanc_4": ("pion_blanc", 3, 6),
    "pion_blanc_5": ("pion_blanc", 4, 6),
    "pion_blanc_6": ("pion_blanc", 5, 6),
    "pion_blanc_7": ("pion_blanc", 6, 6),
    "pion_blanc_8": ("pion_blanc", 7, 6),
    "tour_blanc_g": ("tour_blanc", 0, 7),
    "tour_blanc_d": ("tour_blanc", 7, 7),
    "cavalier_blanc_g": ("cavalier_blanc", 1, 7),
    "cavalier_blanc_d": ("cavalier_blanc", 6, 7),
    "fou_blanc_g": ("fou_blanc", 2, 7),
    "fou_blanc_d": ("fou_blanc", 5, 7),
    "reine_blanc": ("reine_blanc", 3, 7),
    "roi_blanc": ("roi_blanc", 4, 7),
}

# Centrage du plateau
x_offset = (largeur_ecran - largeur_plateau) // 2
y_offset = (hauteur_ecran - hauteur_plateau) // 2


while running:
    screen.fill("white")

    # Event
    for event in pygame.event.get():
        # Croix pour fermer
        if event.type == pygame.QUIT:
            running = False

        # Echap pour fermer
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        # Clic souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_souris, y_souris = event.pos
            clic_colone = (x_souris - x_offset) // taille_case
            clic_ligne = (y_souris - y_offset) // taille_case
            print(f"Clic détecté en : {clic_colone}, {clic_ligne}")

            if 0 <= clic_colone < nb_cases_cote and clic_ligne < nb_cases_cote:
                print(f"Clic sur le plateau ({clic_colone}, {clic_ligne})")
            else:
                print(f"Clic hors du plateau ({clic_colone}, {clic_ligne})")

            # Vérifaction si il y a une piece sur la case
            for piece, (nom_image, col, row) in pieces.items():
                if col == clic_colone and row == clic_ligne:
                    piece_select = piece
                    print(f"Pièce selectionner : {piece} ({nom_image})")
                    break
                #x_piece = x_offset + col * taille_case
                #y_piece = y_offset + row * taille_case

                #if x_piece <= x_souris < x_piece + taille_case and y_piece <= y_souris < y_piece + taille_case:
                    #print(f"Pièce : {piece} ({nom_image} en {col} et  {row})")


    # Plateau
    for x in range(nb_cases_cote):
        for y in range(nb_cases_cote):
            # Contour
            pygame.draw.rect(screen, vert, (x_offset - 2, y_offset - 2, largeur_plateau + 4, hauteur_plateau + 4), 2)
            
            # Damier
            couleur = blanc if (x + y) % 2 == 0 else vert
            pygame.draw.rect(screen, couleur, (x * taille_case + x_offset, y * taille_case + y_offset, taille_case, taille_case))

              
    for piece, (nom_image, col, row) in pieces.items():
        if nom_image in images_pieces:
            screen.blit(images_pieces[nom_image], (x_offset + col * taille_case, y_offset + row * taille_case))
            #print(f"image : {chemin_images}")
        else:
            print(f" Erreur : L'image '{nom_image}' n'a pas été chargée !")


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 30

pygame.quit()


	
