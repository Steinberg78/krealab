# 🚀 Guide de Déploiement Heroku

## Prérequis
- ✅ Compte Heroku (https://www.heroku.com)
- ✅ Heroku CLI installé (https://devcenter.heroku.com/articles/heroku-cli)
- ✅ Git installé

## Étapes de déploiement

### 1. Initialiser Git (si pas encore fait)
```bash
cd KREALAB
git init
git add .
git commit -m "Initial commit for Heroku deployment"
```

### 2. Se connecter à Heroku
```bash
heroku login
```
Suivez les instructions pour vous authentifier.

### 3. Créer une application Heroku
```bash
heroku create votre-app-name
```
*Remplacez `votre-app-name` par un nom unique (ex: krealab-app, mon-site-2024)*

### 4. Configurer les variables d'environnement
```bash
heroku config:set SECRET_KEY="votre-cle-secrete-ici"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS="votre-app-name.herokuapp.com"
```

### 5. Appliquer les migrations
```bash
heroku run python manage.py migrate
```

### 6. Collecter les fichiers statiques (optionnel - géré par WhiteNoise)
```bash
heroku run python manage.py collectstatic --noinput
```

### 7. Déployer votre code
```bash
git push heroku main
```
*Si votre branche s'appelle `master` : `git push heroku master`*

### 8. Vérifier que tout fonctionne
```bash
heroku open
```
Cela ouvrira votre application dans le navigateur.

### 9. Consulter les logs
```bash
heroku logs --tail
```

## 🔧 Commandes utiles

**Redémarrer l'application**
```bash
heroku restart
```

**Vérifier les variables d'environnement**
```bash
heroku config
```

**Créer un superuser**
```bash
heroku run python manage.py createsuperuser
```

**Accéder à la console Django**
```bash
heroku run python manage.py shell
```

## ⚠️ Astuces importantes

1. **Clé Secrète** : Ne jamais commit votre vraie SECRET_KEY. Utilisez les variables d'environnement.

2. **Base de données** : SQLite ne persiste pas sur Heroku. Vous devriez utiliser PostgreSQL pour la production :
```bash
heroku addons:create heroku-postgresql:mini
```

3. **Fichiers statiques** : WhiteNoise gère automatiquement vos fichiers statiques.

4. **Limite gratuite** : L'application gratuite peut être lente car elle dort après 30 min sans trafic.

## ❌ Troubleshooting

**Erreur 500**
```bash
heroku logs --tail
```
Regardez les logs pour voir l'erreur exacte.

**Les fichiers statiques ne chargent pas**
```bash
heroku run python manage.py collectstatic --noinput
heroku restart
```

**Migrations échouent**
```bash
heroku run python manage.py showmigrations
heroku run python manage.py migrate --fake-initial
```

---

Pour plus d'aide : https://devcenter.heroku.com/articles/deploying-python
