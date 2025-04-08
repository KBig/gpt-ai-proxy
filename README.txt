🔧 DÉPLOIEMENT DU PROXY GPT POUR MT5 (Render.com)

1. Va sur https://dashboard.render.com/
2. Clique sur "New Web Service" > "Deploy from Git or ZIP"
3. Uploade ce dossier .zip
4. Quand Render te demande la variable OPENAI_API_KEY :
   ➜ Ajoute ta clé OpenAI personnelle

5. Une fois en ligne, ton URL publique sera :
   https://<ton-projet>.onrender.com/chat

6. Dans ton EA MT5, change la ligne :
   #define AI_API_URL "https://<ton-projet>.onrender.com/chat"

⚠️ Ce proxy renvoie du texte brut (PlainText), parfait pour MT5.
