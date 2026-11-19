


horloge = pygame.time.Clock()
en_cours = True

while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # On vérifie si le clic est dans la zone de saisie de texte
            if rect_saisie.collidepoint(event.pos):
                zone_saisie_active = True
            else:
                zone_saisie_active = False

            # On vérifie si le clic est sur l'un des bits
            for i in range(8):
                if rects_bits[i].collidepoint(event.pos):
                    bits[i] = 1 - bits[i]  

            # On vérifie quel bouton de conversion a été cliqué pour appeler la bonne fonction
            if rect_int_to_bin.collidepoint(event.pos):
                resultat_binaire = convertir(texte_saisie)

            if rect_txt_to_hexa.collidepoint(event.pos):
                resultat_binaire = texte_vers_hexa(texte_saisie)

            if rect_txt_to_binaire.collidepoint(event.pos):
                resultat_binaire = texte_vers_binaire(texte_saisie)

            if rect_int_to_hex.collidepoint(event.pos):
                resultat_binaire = entier_to_hex(texte_saisie)

            if rect_hex_to_int.collidepoint(event.pos):
                resultat_binaire = hex_to_int(texte_saisie)

            if rect_bin_to_int.collidepoint(event.pos):
                resultat_binaire = bin_to_int(texte_saisie)

            if rect_complement_a_deux.collidepoint(event.pos):
                resultat_binaire = complement_a_deux(texte_saisie)

            if rect_iee.collidepoint(event.pos):
                resultat_binaire = iee(texte_saisie)
                             
        if event.type == pygame.KEYDOWN and zone_saisie_active:
            if event.key == pygame.K_BACKSPACE:
                texte_saisie = texte_saisie[:-1]
            else:
                if len(event.unicode) > 0:
                    texte_saisie += event.unicode


    fenetre.fill(BLANC)
    

    couleur_bordure = BLEU if zone_saisie_active else GRIS
    pygame.draw.rect(fenetre, GRIS, rect_saisie)
    pygame.draw.rect(fenetre, couleur_bordure, rect_saisie, 2)
    
    # Affichage du texte saisi pour chaque fonction
    img_saisie = police.render(texte_saisie, True, NOIR)
    fenetre.blit(img_saisie, (rect_saisie.x + 10, rect_saisie.y + 8))
    
    pygame.draw.rect(fenetre, BLEU, rect_int_to_bin)
    img_bouton = police.render("Entier -> Binaire", True, BLANC)
    fenetre.blit(img_bouton, (rect_int_to_bin.x + 30, rect_int_to_bin.y + 8))

    pygame.draw.rect(fenetre, BLEU, rect_txt_to_hexa)
    img_bouton = police.render("Texte -> Hexadecimal", True, BLANC)
    fenetre.blit(img_bouton, (rect_txt_to_hexa.x + 30, rect_txt_to_hexa.y + 8))
    
    pygame.draw.rect(fenetre, BLEU, rect_txt_to_binaire)
    img_bouton = police.render("Texte -> Binaire", True, BLANC)
    fenetre.blit(img_bouton, (rect_txt_to_binaire.x + 30, rect_txt_to_binaire.y + 8))
    
    pygame.draw.rect(fenetre, BLEU, rect_int_to_hex)
    img_bouton = police.render("Entier -> Hexadecimal", True, BLANC)
    fenetre.blit(img_bouton, (rect_int_to_hex.x + 30, rect_int_to_hex.y + 8))

    pygame.draw.rect(fenetre, BLEU, rect_hex_to_int)
    img_bouton = police.render("Hexadecimal -> Entier", True, BLANC)
    fenetre.blit(img_bouton, (rect_hex_to_int.x + 30, rect_hex_to_int.y + 8))
    
    pygame.draw.rect(fenetre, BLEU, rect_bin_to_int)
    img_bouton = police.render("Binaire -> Entier", True, BLANC)
    fenetre.blit(img_bouton, (rect_bin_to_int.x + 30, rect_bin_to_int.y + 8))
    
    pygame.draw.rect(fenetre, BLEU, rect_complement_a_deux)
    img_bouton = police.render("Complement à Deux", True, BLANC)
    fenetre.blit(img_bouton, (rect_complement_a_deux.x + 30, rect_complement_a_deux.y + 8))

    pygame.draw.rect(fenetre, BLEU, rect_iee)
    img_bouton = police.render("IEE 754", True, BLANC)
    fenetre.blit(img_bouton, (rect_iee.x + 30, rect_iee.y + 8))
    
    img_resultat = police1.render(resultat_binaire, True, NOIR)
    fenetre.blit(img_resultat, (50, 100)) 

    #On initialise la valeur à 0
    valeur = 0
    for i in range(8):
        # On calcule la valeur décimale totale
        if bits[i] == 1:
            valeur += 2**(7-i)
        texto = police1.render(str(bits[i]), True, NOIR)
        fenetre.blit(texto, rects_bits[i])

    #On affiche la valeur
    fenetre.blit(police.render(f"= {valeur}", True, NOIR), (650, 610))

    pygame.display.flip()
    horloge.tick(30)

pygame.quit()
sys.exit()

if __name__ == "__main__":
    main()