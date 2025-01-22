import streamlit as st
import google.generativeai as genai
from api_key import google_gemini_api_key

# Configuration de la page Streamlit (DOIT ÊTRE LA PREMIÈRE COMMANDE)
st.set_page_config(layout="wide", page_title="BlogCraft", page_icon="📝")

# Configuration de l'API Google Gemini
genai.configure(api_key=google_gemini_api_key)

# Configuration du modèle Gemini
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialisation du modèle Gemini
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

# CSS personnalisé
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #cd2222;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
    }
    .stTextInput>div>div>input {
        background-color: #5f2a2a;
        border-radius: 5px;
    }
    .stTitle {
        font-size: 2.5em;
        color: #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Titre et sous-titre
st.title("📝 BlogCraft - Votre Assistant IA pour la Rédaction de Blogs")
st.subheader("🚀 Créez des articles percutants en quelques clics !")

# Sidebar pour les entrées utilisateur
with st.sidebar:
    st.title("📄 Détails du Blog")
    st.markdown("Renseignez les informations nécessaires pour générer votre blog.")

    blog_title = st.text_input("✏️ Titre de votre Blog")
    keywords = st.text_area("🔑 Mots-clés (séparés par des virgules)")
    num_words = st.slider("🔢 Nombre de mots", min_value=250, max_value=1000, step=100)

    submit_button = st.button("✨ Générer le Blog")

# Génération du blog
if submit_button:
    try:
        # Génération du blog avec Gemini
        chat_session = model.start_chat(history=[])
        prompt = f"Générez un article de blog complet et engageant en rapport avec le titre \"{blog_title}\" et les mots-clés \"{keywords}\". Assurez-vous d'incorporer ces mots-clés dans l'article. Le blog doit faire environ {num_words} mots, adapté à un public en ligne. Le contenu doit être original, informatif et maintenir un ton cohérent."
        response = chat_session.send_message(prompt)

        # Affichage du blog généré
        st.header("📄 Blog Généré")
        st.write(response.text)

    except Exception as e:
        st.error(f"Une erreur s'est produite : {e}")

# Pied de page
st.markdown(
    """
    ---
    **BlogCraft** - Propulsé par Gemini AI et Streamlit.  
    © 2023 - Tous droits réservés.
    """,
    unsafe_allow_html=True,
)