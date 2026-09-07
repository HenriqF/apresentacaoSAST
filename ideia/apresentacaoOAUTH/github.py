from flask import Flask, redirect
from authlib.integrations.flask_client import OAuth

GITHUB_CLIENT_ID = "FDSAJFKSAFNSAJFSAFFF"
GITHUB_CLIENT_SECRET = "FDASJHFSADFSADJFNSADJFNSADFJASDFNSADJFFF"

app = Flask(__name__)
app.secret_key = " meu_gato_se_chama_boa_pergunta "

oauth = OAuth(app)
github = oauth.register(
    name="github",
    client_id=GITHUB_CLIENT_ID,
    client_secret=GITHUB_CLIENT_SECRET,
    access_token_url="https://github.com/login/oauth/access_token",
    authorize_url="https://github.com/login/oauth/authorize",
    api_base_url="https://api.github.com/",
    client_kwargs={
        "scope": "read:user repo"
    }
)


@app.route("/ghub")
def access_github():
    return oauth.github.authorize_redirect("http://127.0.0.1:5000/auth")

@app.route("/auth")
def auth_github():
    try:
        n = oauth.github.authorize_access_token()
        print(n)
    except:
        return redirect("/")

    repos = github.get("user/repos", params={"per_page": 100})
    linguas = sort_linguas(repos)
    
    resposta = "Top 5 linguas: <br>"
    for i in range(0, len(linguas)):
        if i == 5:
            break
        resposta += f"#{i+1} {linguas[i][1]} ({linguas[i][0]})repositórios <br>"
    return resposta

@app.route("/")
def main():
    return '<a href="/ghub">USAR GITHUB PARA ANALISE</a><br>'

def sort_linguas(repos):
    linguas = {}
    for rp in repos.json():
        l = rp["language"]
        if l == None:
            continue

        if l not in linguas:
            linguas[l] = 1
        else:
            linguas[l] += 1
    linguas_t = []
    for k,v in linguas.items():
        linguas_t.append((v, k))
    return sorted(linguas_t, key=lambda x : x[0], reverse=True)
app.run()