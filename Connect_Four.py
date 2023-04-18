import math
import time

class Puissance4:
    
    """
    Une classe représentant le jeu du Puissance 4
    
    Attributes
    ---------
    lignes : int
        le nombre de ligne du Puissance 4
    colonnes : int
        le nombre de colonne du Puissance 4
    vide : str
        une case vide du Puissance 4
    plateau : list (str)
        une liste à 2 dimensions représentant le plateau de jeu
        
    Methods
    --------
    vider_plateau ()
        vide le plateau
    est_jouable (colonne)
        indique si un mouvement (colonne) est jouable
    colonne_disponible ()
        retourne une liste des mouvements (colonne) possibles
    position_pion (colonne)
        retourne la position du pion quand on le lache dans une colonne
    placement_pion (colonne)
        place un pion dans le plateau de jeu
    ligne_gagnant(couleur)
        vérifie si 4 pions de même couleur sont alignés sur une ligne
    colonne_gagnant (couleur)
        vérifie si 4 pions de même couleur sont alignés sur une colonne
    diagonal_gagnant (couleur)
        vérifie si 4 pions de même couleurs sont alignés sur une diagonale
    est_gagnant (couleur)
        vérifie si un joueur a gagné
    """
    
    def __init__(self):
        self.lignes = int(6)
        self.colonnes = int(12)
        self.vide = "_"
        self.nb_pion = int(42)
        
        self.plateau = []
        for ligne in range(self.lignes) :
             self.plateau.append(list((int(self.colonnes)) * [self.vide]))
             
    def __str__(self):
        s=""
        for i in range(self.lignes):
            for j in range(self.colonnes):
                s+=self.plateau[i][j] + "  "
            s+= " " + str(i) + "\n\n"
        s+= "  ".join(str(i) for i in range(self.colonnes)) + "\n"
        return s
         
    def vider_plateau(self):
        """
        Vide le plateau

        Returns
        -------
        None.

        """
        for i in range(self.lignes):
            for j in range(self.colonnes):
                self.plateau[i][j] = self.vide
    
    def est_jouable(self, colonne):
        """
        Indique si un mouvement est jouable sur une colonne

        Parameters
        ----------
        colonne : int
            endroit où l'on veut jouer

        Returns
        -------
        boolean
            Vrai si le coup est jouable, faux sinon

        """
        return colonne >= 0 and colonne < self.colonnes and self.plateau[0][colonne]==self.vide
    
    def colonne_disponible(self):
        """
        retourne une liste de colonnes jouable

        Returns
        -------
        list
            une liste de colonnes disponible pour jouer

        """
        return [m for m in range(self.colonnes) if self.est_jouable(m)]
    
    def position_pion(self,colonne):
        """
        retourne la position du pion joué

        Parameters
        ----------
        colonne : int
            l'emplacement où l'on veut jouer

        Returns
        -------
        pos : int
            la position du pion placé dans le plateau

        """
        pos = -1
        if self.est_jouable(colonne):
            for ligne in range(5,-1,-1):
                if self.plateau[ligne][colonne]==self.vide:
                    pos = ligne
                    break
        return pos
        
    def placement_pion(self,colonne,couleur):
        """
        joue un pion en le mettant dans le plateau de jeu

        Parameters
        ----------
        colonne : int
            endroit où l'on veut jouer
        couleur : str
            couleur du pion à jouer

        Returns
        -------
        None.

        """
        self.plateau[self.position_pion(colonne)][colonne] = couleur
        
    def ligne_gagnant(self, couleur):
        """
        vérifie si 4 pions de même couleur sont sur une ligne

        Parameters
        ----------
        couleur : str
            couleur du pion pour la vérification

        Returns
        -------
        res : boolean
            Vrai si 4 pions sont alignés, faux sinon

        """
        res = False
        for i in range(self.lignes):
            for j in range(self.colonnes):
                if j < self.colonnes - 3:
                    if self.plateau[i][j] == self.plateau[i][j+1] == self.plateau[i][j+2] == self.plateau[i][j+3] == couleur:
                        res = True
        return res
    
    def colonne_gagnant(self, couleur):
        """
        vérifie si 4 pions de même couleur sont sur une colonne

        Parameters
        ----------
        couleur : str
            couleur du pion pour la vérification

        Returns
        -------
        res : boolean
            Vrai si 4 pions sont alignés, faux sinon

        """
        res = False
        for i in range(self.lignes):
            for j in range(self.colonnes):
                if i < self.lignes - 3:
                    if self.plateau[i][j] == self.plateau[i+1][j] == self.plateau[i+2][j] == self.plateau[i+3][j] == couleur:
                        res = True
        return res
    
    def diagonal_gagnant(self, couleur):
        """
        vérifie si 4 pions de même couleur sont sur une diagonale

        Parameters
        ----------
        couleur : str
            couleur du pion pour la vérification

        Returns
        -------
        res : boolean
            Vrai si 4 pions sont alignés, faux sinon

        """
        res = False
        for i in range(self.lignes):
            for j in range(self.colonnes):
                if i < self.lignes - 3 and j < self.colonnes - 3:
                    if self.plateau[i][j] == self.plateau[i+1][j+1] == self.plateau[i+2][j+2] == self.plateau[i+3][j+3] == couleur:
                        res = True
                      
        for i in range(self.lignes-1,-1,-1):
            for j in range(self.colonnes):
                if i > 0 + 3 and j < self.colonnes - 3:
                    if self.plateau[i][j] == self.plateau[i-1][j+1] == self.plateau[i-2][j+2] == self.plateau[i-3][j+3] == couleur:
                        res = True
        return res
    
    def est_gagnant(self, couleur):
        """
        vérifie si un joueur à gagné

        Parameters
        ----------
        couleur : str
            couleur du joueur pour la vérification

        Returns
        -------
        boolean
            Vrai si le joueur à gagné, faux sinon

        """
        return self.ligne_gagnant(couleur) or self.colonne_gagnant(couleur) or self.diagonal_gagnant(couleur)        
     
    
def actions(jeu):
    """
    retourne une liste d'actions possibles

    Parameters
    ----------
    jeu : Puissance4
        le jeu du puissance 4 actuel

    Returns
    -------
    list
        liste d'actions possibles

    """
    return jeu.colonne_disponible()

def terminal(jeu):
    """
    Vérifie si le jeu actuel est dans un état terminal

    Parameters
    ----------
    jeu : Puissance4
        le jeu du puissance 4 actuel

    Returns
    -------
    res : int
        un nombre indiquant le résultat de la vérification

    """
    res = -1
    if jeu.est_gagnant("X"):
        res = 0
    elif jeu.est_gagnant("O"):
        res = 1
    return res

def result(jeu, colonne, couleur):
    """
    retourne un nouveau plateau contenant le résultat d'un mouvement

    Parameters
    ----------
    jeu : Puissance4
        le jeu du puissance 4 actuel
    colonne : int
        endroit où l'on veut jouer
    couleur : str
        couleur du joueur qui veut jouer

    Returns
    -------
    newPlateau : Puissance4
        objet puissance 4 contenant un nouveau plateau

    """
    newPlateau = Puissance4()
    
    for i in range(newPlateau.lignes):
            for j in range(newPlateau.colonnes):
                newPlateau.plateau[i][j] = jeu.plateau[i][j]
    newPlateau.placement_pion(colonne, couleur)
    return newPlateau

def utility(jeu):
    """
    Attribue un nombre de point en fonction des alignements de pion

    Parameters
    ----------
    jeu : Puissance4
        le jeu du puissance 4 actuel

    Returns
    -------
    res : int
        le score en fonction des alignements de pion

    """
    res = 0
    
    for i in range(jeu.lignes):
        for j in range(jeu.colonnes):
            if j < jeu.colonnes - 3:
                if jeu.plateau[i][j] == jeu.plateau[i][j+1] == jeu.plateau[i][j+2] == "X":
                    res += 5
                elif jeu.plateau[i][j] == jeu.plateau[i][j+1] == jeu.plateau[i][j+2] == "O":
                    res += -5
    for i in range(jeu.lignes):
        for j in range(jeu.colonnes):
            if i < jeu.lignes - 3:
                if jeu.plateau[i][j] == jeu.plateau[i+1][j] == jeu.plateau[i+2][j] == "X":
                    res += 5
                elif jeu.plateau[i][j] == jeu.plateau[i+1][j] == jeu.plateau[i+2][j] == "O":
                    res += -5
    for i in range(jeu.lignes):
        for j in range(jeu.colonnes):
            if i < jeu.lignes - 3 and j < jeu.colonnes - 3:
                if jeu.plateau[i][j] == jeu.plateau[i+1][j+1] == jeu.plateau[i+2][j+2] == "X":
                    res += 2
                elif jeu.plateau[i][j] == jeu.plateau[i+1][j+1] == jeu.plateau[i+2][j+2] == "O":
                    res += -2
    for i in range(jeu.lignes-1,-1,-1):
        for j in range(jeu.colonnes):
            if i > 0 + 3 and j < jeu.colonnes - 3:
                if jeu.plateau[i][j] == jeu.plateau[i-1][j+1] == jeu.plateau[i-2][j+2] == "X":
                    res += 2
                elif jeu.plateau[i][j] == jeu.plateau[i-1][j+1] == jeu.plateau[i-2][j+2] == "O":
                    res += -2
    return res        
    
def max_value(jeu,alpha,beta,joueur,limite):
    if (terminal(jeu) == 0):
        return math.inf
    elif (terminal(jeu) == 1):
        return -math.inf
    v = -math.inf
    if limite == 5:
        return utility(jeu)
    for a in actions(jeu):
        if joueur == "X":
            v = max(v,min_value(result(jeu,a,joueur),alpha,beta,"O",limite+1))
        else:
            v = max(v,min_value(result(jeu,a,joueur),alpha,beta,"X",limite+1))
        if v >= beta:
            return v
        alpha = max(alpha,v)
    return v
    
def min_value(jeu,alpha,beta,joueur,limite):
    if (terminal(jeu) == 0):
        return math.inf
    elif (terminal(jeu) == 1):
        return -math.inf
    v = math.inf
    if limite == 5:
        return utility(jeu)
    for a in actions(jeu):
        if joueur == "X":
            v = min(v,max_value(result(jeu,a,joueur),alpha,beta,"O",limite+1))
        else:
            v = min(v,max_value(result(jeu,a,joueur),alpha,beta,"X",limite+1))
        if v <= alpha:
            return v
        beta = min(beta,v)
    return v
     
def alpha_beta_search(jeu,joueur):
    alpha = -math.inf
    beta = math.inf
    v = -math.inf
    liste = actions(jeu)
    action = liste[0]
    for a in liste:
        if joueur == "X":
            vTemp = max(v,min_value(result(jeu,a,joueur),alpha,beta,"O",1))
        else:
            vTemp = max(v,min_value(result(jeu,a,joueur),alpha,beta,"X",1))
        if vTemp > v:
            v = vTemp
            action = a
        alpha = max(alpha,v)
    return action
       
def main():
    
    # On créé un jeu Puissance 4
    jeu = Puissance4()
    
    # On définit une liste de coup disponible
    mouvements = jeu.colonne_disponible()
    
    # On affiche le plateau de jeu
    print(jeu)
    
    # On définit la couleur des joueurs
    joueur1 = "X"
    joueur2 = "O"
    
    # On définit le nombre de pion présent sur le plateau à 0
    nombre_pion = 0
    
    # On définit le nombre de tour à 0
    i=0
    
    # On définit le joueur qui commence
    first = int(input("IA joue en premier ? 1 (oui)    0 (non)"))
    
    # Temps de l'IA
    tempsIA = 0
    
    # On redéfinit la couleur en fonction de qui commence
    if not first:
        joueur1 = "O"
        joueur2 = "X"
        
    # Tant que le platzeau n'est pas plein
    # ou que le nombre de pion n'égal pas le nombre limite, on continue de jouer
    while mouvements != [] or nombre_pion!= jeu.nb_pion:
        
        # A chaque tour, on regarde les colonnes disponibles pour jouer
        mouvements = jeu.colonne_disponible()
        
        # modulo => permet de changer de tour
        if i % 2 == 0:
            if first:
                t0 = time.time()
                mouvement = alpha_beta_search(jeu, joueur1)
                t1 = time.time()
                
                # Temps pour une action
                tempsIA += t1 - t0
                
            else:
                print(f"Mouvements possibles : {mouvements}")
                mouvement = int(input("Joueur 1, entrez un numero de colonne : "))
                
            # Joue un pion
            jeu.placement_pion(mouvement, joueur1)
            
            # Si joueur 1 a gagné alors on quitte la boucle while
            if (jeu.est_gagnant(joueur1)):
                print("Joueur 1 gagne !")
                break
            
            # On affiche le plateau avec le nouveau pion joué
            print(jeu)
            
        else:
            if not first:
                t2= time.time()
                mouvement = alpha_beta_search(jeu, joueur2)
                t3= time.time()
                # Temps pour une action
                tempsIA += t3 - t2
                
            else:
                print(f"Mouvements possibles : {mouvements}")
                mouvement = int(input("Joueur 2, entrez un numero de colonne : "))
                
            # Joue un pion
            jeu.placement_pion(mouvement, joueur2)
            
            # Si joueur 2 a gagné alors on quitte la boucle while
            if (jeu.est_gagnant(joueur2)):
                print("Joueur 2 gagne !")
                break
            
            # On affiche le plateau avec le nouveau pion joué
            print(jeu)
            
        # Incrémente le nombre de tour    
        i += 1
        
        # Incrémente le nombre de pion sur le plateau
        nombre_pion += 1
    
    # Temps moyen de l'IA pour chaque mouvement
    tempsIA /= i/2
    print(tempsIA)
    
    # On affiche une derniere fois le plateau contenant le coup gagnant
    print(jeu)        

if __name__=="__main__":
    main()


