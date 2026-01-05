# 🏢 Système ERP Odoo - Gestion des Attestations

## 📋 Description du Projet

Ce projet est un système ERP (Enterprise Resource Planning) basé sur **Odoo 17**, développé dans un cadre pédagogique à l'EMSI. Il comprend un module personnalisé de gestion des attestations permettant de créer, gérer et suivre les attestations étudiantes de manière efficace.

Le système est entièrement containerisé avec Docker pour faciliter le déploiement et garantir la portabilité entre différents environnements.

## ✨ Fonctionnalités Principales

### Module Attestations
- ✅ **Création d'attestations** : Génération d'attestations pour les étudiants
- 📝 **Gestion du cycle de vie** : Suivi des attestations avec statuts (Brouillon, Validée, Annulée)
- 📅 **Traçabilité** : Enregistrement automatique des dates de création
- 🔍 **Recherche et filtrage** : Interface intuitive pour gérer les attestations
- 📄 **Informations détaillées** : Nom de l'étudiant, description, et métadonnées

### Champs du Modèle
- **Nom de l'attestation** : Identification unique de l'attestation
- **Nom de l'étudiant** : Bénéficiaire de l'attestation
- **Date de création** : Horodatage automatique
- **Statut** : Workflow de validation (Brouillon → Validée / Annulée)
- **Description** : Détails et notes complémentaires

## 🛠️ Stack Technique

| Composant | Technologie | Version |
|-----------|-------------|---------|
| **ERP Framework** | Odoo | 17.0 |
| **Base de données** | PostgreSQL | 16 |
| **Containerisation** | Docker & Docker Compose | 3.8 |
| **Langage Backend** | Python | 3.x |
| **ORM** | Odoo ORM | - |

## 📁 Structure du Projet

```
odoo/
├── addons/
│   └── attestations/          # Module personnalisé
│       ├── models/            # Modèles de données
│       │   ├── __init__.py
│       │   └── attestation.py # Modèle principal
│       ├── views/             # Vues XML
│       │   └── attestation_views.xml
│       ├── security/          # Droits d'accès
│       │   └── ir.model.access.csv
│       ├── static/            # Ressources statiques
│       ├── report/            # Rapports et impressions
│       ├── __init__.py
│       └── __manifest__.py    # Métadonnées du module
├── config/
│   └── odoo.conf              # Configuration Odoo
├── docker-compose.yml         # Orchestration des conteneurs
└── README.md
```

## 🚀 Installation et Démarrage

### Prérequis
- Docker Desktop installé
- Docker Compose installé
- Au moins 4 GB de RAM disponible
- Ports 8069 (Odoo) et 5432 (PostgreSQL) libres

### Étapes d'Installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/MnbYsf/ERP.git
   cd ERP
   ```

2. **Démarrer les conteneurs**
   ```bash
   docker-compose up -d
   ```

3. **Vérifier le statut des conteneurs**
   ```bash
   docker-compose ps
   ```

4. **Accéder à Odoo**
   - Ouvrir un navigateur et aller sur : `http://localhost:8069`
   - Créer une nouvelle base de données
   - Installer le module **Attestations** depuis le menu Applications

### Arrêter le Système
```bash
docker-compose down
```

### Arrêter et Supprimer les Données
```bash
docker-compose down -v
```

## 🔧 Configuration

### Base de Données PostgreSQL
- **Host** : `db`
- **Port** : `5432`
- **Utilisateur** : `odoo`
- **Mot de passe** : `odoo`
- **Base de données** : `postgres`

### Volumes Docker
- `odoo-web-data` : Données de l'application Odoo
- `odoo-db-data` : Données PostgreSQL persistantes
- `./config` : Fichiers de configuration
- `./addons` : Modules personnalisés

## 📖 Utilisation

### Accéder au Module Attestations

1. Connectez-vous à Odoo (`http://localhost:8069`)
2. Allez dans **Applications**
3. Recherchez "Attestations"
4. Cliquez sur **Installer**
5. Le module apparaîtra dans le menu principal

### Créer une Attestation

1. Ouvrir le menu **Attestations**
2. Cliquer sur **Créer**
3. Remplir les champs :
   - Nom de l'attestation
   - Nom de l'étudiant
   - Date de création
   - Description
4. Sauvegarder et changer le statut selon le workflow

## 👥 Auteur

**EMSI** - École Marocaine des Sciences de l'Ingénieur

## 📄 Licence

Ce projet est développé à des fins pédagogiques.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit vos changements (`git commit -m 'Ajout d'une fonctionnalité'`)
4. Push vers la branche (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

## 📞 Support

Pour toute question ou problème, veuillez ouvrir une issue sur GitHub.

---

**Développé avec ❤️ pour l'apprentissage d'Odoo**