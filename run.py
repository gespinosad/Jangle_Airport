from app import app
import os

# - podemos crear más files "view" por ejemplo "adm_views", "usuario_views" "userAutorización_view"etc
secret = os.urandom(16)
app.secret_key = secret
app.config['SESSION_TYPE'] = 'filesystem'
if __name__ == "__main__":
    app.run(debug=True)
