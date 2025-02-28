#Contrôle des connaissances GCP 

**Création d'un Service Account** :

   - Accéder à **IAM & Admin**, créer un compte de service, attribuer des rôles (ex : Viewer, Editor), et générez une clé JSON si nécessaire pour l'authentification. 
   - **Bonnes pratiques** : Ne jamais exposer les clés, appliquer le principe du moindre privilège, et faire une rotation régulière des clés.

2. **Création d'un Bucket** :
   - Créer un bucket dans **Cloud Storage**, définir un nom unique et choisir **localisation** (région ou multirégion), et configurer des règles de cycle de vie pour la gestion des objets.
   - **Impact** : La localisation affecte la latence et la redondance, tandis que les politiques de conservation aident à optimiser les coûts et la gestion des données.

3. **Gestion des droits (IAM)** :
   - IAM sur GCP permet de gérer les permissions d'accès aux ressources. Chaque utilisateur ou service reçoit des rôles spécifiques.
   - Exemple : Pour un **bucket de données sensibles**, attribuer un rôle **Storage Object Viewer** à un service account pour limiter l'accès à la lecture uniquement.

4. **Configuration de la facturation** :
   - Configurer la facturation dans la **console Google Cloud**, associer un mode de paiement et suiver les rapports de coûts.
   - **Précautions** : Utiliser des alertes de facturation pour éviter les dépassements et analyser régulièrement les rapports pour ajuster les ressources utilisées.

5. **Règles de vie** :
   - À la fin d'un cours ou TP, on remercie l'enseignant pour son enseignement et on pense à bien dire aurevoir.

Url Github : 


https://github.com/alexs-db/ctpGCP


