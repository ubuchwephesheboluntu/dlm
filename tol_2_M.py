import random
import time

import streamlit as st


# Amagama esiZulu ahlelwe ngobude obukhulayo.
AMAGAMA = [
    # Amafushane
    "dinsi", "ubude", "ala", "bhuqe", "inja", "vuka", "azi", "ubaba", "bala", "beka",
    "cela", "uju", "dala", "dela", "duma", "fana", "fika", "gula", "hamba",
    "hlela", "gula", "lala", "ucu", "lima", "loba", "lula", "eluka", "qhina",
    "misa", "inono", "neka", "unina", "noma", "nuka", "phaka", "phela", "phika",
    "qala", "qeda", "qina", "sala", "suza", "siza", "suka", "shipha", "vela",
    "vula", "wena", "yena", "woza", "zala",

    # Amafushane kuya kwaphakathi
    "amanzi", "amanga", "amandla", "amasimu", "amashumi", "isandla", "isango",
    "isikole", "isinkwa", "isitulo", "ithanga", "izandla", "izinkomo",
    "umfundi", "ubisi", "uboya", "ukudla", "ukufa", "ukufika", "ukulala",
    "ukuma", "ukubona", "ukubhala", "ukuhamba", "ukufunda", "ukusebenza",
    "inxele", "umfana", "umfula", "umgodi", "umhlaba", "umoya", "umuntu",
    "umuthi", "umuzi", "uzalo", "inyoni", "imali", "indoda", "ingane",
    "indlu", "izulu", "ilanga", "inyanga", "izinkuni", "umngane", "umndeni",
    "umsebenzi", "ukudlala", "ukucula", "ukusiza", "ukubuza", "ukuphila",
    "uthando", "iqabunga", "ukuphuza", "ukuthenga", "ukuthengisa", "ukufika",
    "ukuhamba", "ubuchopho", "ukuvuka", "ukulala", "umkhuhlane", "ukugeza",
    "ukupheka", "ukushanela", "ukubala", "ukufundisa", "ukufunda",
    "ukukhuluma", "ukulalela", "ukucabanga", "ilifu", "ukukhohlwa",
    "emmome", "ukuvala", "ukubamba", "ukulahla", "umhlahlandlela", "ukufuna",
    "ukuthanda", "ukwesaba", "ukujabula", "ukukhala", "mamatheka", "ukugijima",
    "ukuhleka", "amathe", "ukusebenza", "ukudansa", "ukudweba", "immbila",

    # Amagama aphakathi
    "abafundi", "uluntu", "abazali", "amanzi", "isizwe", "izibazi",
    "amakhaya", "amakhanda", "amakhasi", "amakhono", "intuthwane",
    "amapensela", "amafasitela", "amapulazi", "amabhodlela", "isibhakabhaka",
    "abantwana", "izikole", "izincwadi", "izihlalo", "izicathulo", "izimbali",
    "izinkanyezi", "izintaba", "izihlahla", "izilwane", "izinyawo",
    "izandla", "izinkinga", "izimpendulo", "izifundo", "izindaba",
    "izithombe", "emkhathini", "izindlela", "izethulo", "izithelo", "isibindi",
    "izinsuku", "izinyanga", "izimpahla", "izibuko", "isigidi", "ikhulu",
    "inkulungwane", "shumayela", "shayela", "umshayeli", "umculi", "umlimi",
    "umakhi", "umthengisi", "umakhelwane", "umngane", "umzali", "umntwana",
    "umntwana", "umndeni", "umfula", "umkhumbi", "umgwaqo", "shanyela",
    "umdlalo", "umculo", "umlando", "cabanga", "umthetho", "umhlangano",
    "umkhosi", "gcagcelwa", "umoya", "umzimba", "umlenze", "umunwe",
    "umkhono", "umhlane", "ikhanda", "ikhaya", "bhodla", "ihhashi", "ihubo",
    "inqola", "ihhovisi", "emlilweni", "isikhathi", "yenda", "isithelo",
    "isihluthulelo", "isithombe", "isibonelo", "isigubhu", "isivumelwano",
    "isiketi", "isikhwama", "isibhedlela", "ukwetshisa", "isitimela",
    "izikhukhula", "isikhova", "isicathulo", "isiphuzo", "isidlo",
    "isixazululo", "ukuphumelela", "ukubambisana", "ukuzimisela",
    "ukuzivocavoca", "ukuxoxisana", "uzamcolo", "ukulungisa",
    "ukuhlela", "inkululeko", "umthandazo", "ukuthuthuka",
    "ukuziphatha", "ukuzilolonga", "ukuzibophezela", "bingelela",
    "ukubonga", "ukuxolisa", "ukuphendula", "ukuchaza", "ukubonisa",
    "ukuhlola", "fundisa", "cwayiza", "ukwakha", "umkhondo",
    "ukuguqula", "ukuhlanganisa", "ukuhlukanisa", "ukulinganisa",
    "ukubala", "ukubhala", "ukudweba", "ukucula", "imikhonto", "ukugijima",
    "ukubhukuda", "ukukhwela", "ukushayela", "ukuthunga", "amadolo",

    # Amade
    "ubungane", "ubumnandi", "hlakanipha", "ubuhle", "ububele",
    "ubuqotho", "ubuthongo", "ubuhlungu", "ubungcweti", "ubulungiswa",
    "inhliziyo", "ubumnene", "ubumqoka", "ubunzima", "ubukhulu",
    "ubuningi", "umkhomazi", "ubude", "ububanzi", "ubunono", "umlotha",
    "ukuzithoba", "ukuzimisela", "ukuzibophezela", "imisebe",
    "ukuzimela", "emathunjini", "ukubekezela", "ukubambisana",
    "umgede", "ukuthuthuka", "isiziba", "juluka",
    "ukuzilungiselela", "inhlabathi", "ukuziphendulela", "ukuhlakanipha",
    "ukukhuthazeka", "thumba", "ntshontshwa", "umkhulungwane",
    "ukubambisana", "ukuxhumana", "ukuxoxisana", "ukuxazulula",
    "ukuhlalisana", "ukuhlukumezeka", "ezombusazwe", "ukucabangisisa",
    "ukuzindla", "ezokuthutha", "umengameli", "umshumayeli",
    "ukuhleleka", "ukulungiselela", "minya", "minza",
    "ukubabuthakathaka", "isehlukaniso", "indandatho", "isicoco",
    "indondo", "isihluthu", "intshebe", "ukubambisana",
    "phaphatha", "ukuthakazelelana", "qhwanda", "ukwazisana",
    "izingqungqulu", "impatha", "iziko", "ukuthandana",
    "ukuthandeka", "ukuthandazela", "intombazane", "kitazeka",
    "imizwilili", "igidangoma", "isifundiswa", "xilongeka",
    "izipopolo", "ezimbonini", "izithandani", "ukwenziwa",
    "umabhalane", "incwadi", "ichweba", "emhosheni",
    "umshumayeli", "ukuhlwa", "ikwindla", "ihlobo",
    "imvuselelo", "intwasahlobo", "emndenini", "ukusizana",
    "umkhomo", "ukubuyisana", "ukubuyekeza", "isikhungo",
    "ukuphakamisana", "umkhakha", "ukwehlukanisa", "ukwehluleka",
    "ukuphazamiseka", "ukuphazamisana", "isikhukhukazi",
    "ukufuya", "ukuzikhumbuza", "ukuzifundisa", "izinwele",
    "ukuzilawula", "ilala", "inkonkoni", "ubucwebe",
    "ukuzibandakanya", "intshontsho", "izihlabathi",
    "emsamo", "izitshalo", "ubhontshisi",
    "lulama", "ubhejane", "uchungechunge",
    "uxhaxha", "utshwala", "ukuthwala",
    "indlondlo", "isiqhwaga", "isibhakela",
    "itshitshi", "indlulamithi", "amanxusa",
    "umdlavuza", "umthombo", "isiphongo",
    "ihwanqa", "izelamani", "impumalanga",
    "isicathulo", "cathula", "amalahle",
    "ndindizela", "didizela",
]


def lungisa_amazinga():
    """Susa izikhala eziphindaphindiwe, bese uhlela amagama ngobude."""
    amagama = {
        igama.strip().lower()
        for igama in AMAGAMA
        if igama.strip() and " " not in igama.strip()
    }
    return sorted(amagama, key=lambda igama: (len(igama), igama))


def qala_umdlalo():
    amagama = lungisa_amazinga()
    random.shuffle(amagama)

    st.session_state.amagama_asele = amagama
    st.session_state.amaphuzu = 0
    st.session_state.amazinga = 1
    st.session_state.izimpendulo_ezilungile = 0
    st.session_state.isikhathi_sokuphela = time.time() + 45
    st.session_state.isimo = "dlala"
    st.session_state.igama_eliyimfihlo = ""
    st.session_state.igama_elixutshiwe = ""
    khetha_igama_elilandelayo()


def khetha_igama_elilandelayo():
    asele = st.session_state.amagama_asele

    if not asele:
        st.session_state.isimo = "win"
        return

    # Khulisa ubude obuvunyelwe njalo ngemva kwezimpendulo ezinhlanu ezilungile.
    ubude_bokuqala = min(map(len, lungisa_amazinga()))
    umkhawulo = ubude_bokuqala + st.session_state.amazinga - 1
    abakhethiwe = [igama for igama in asele if len(igama) <= umkhawulo]
    if not abakhethiwe:
        st.session_state.amazinga += 1
        return khetha_igama_elilandelayo()
    igama = random.choice(abakhethiwe)
    asele.remove(igama)

    st.session_state.igama_eliyimfihlo = igama

    izinhlamvu = list(igama)
    elixutshiwe = igama
    for _ in range(30):
        random.shuffle(izinhlamvu)
        elixutshiwe = "".join(izinhlamvu)
        if elixutshiwe != igama:
            break

    st.session_state.igama_elixutshiwe = elixutshiwe


def qinisekisa_impendulo():
    impendulo = st.session_state.get("impendulo", "").strip().lower()
    igama = st.session_state.igama_eliyimfihlo

    if impendulo == igama:
        st.session_state.amaphuzu += len(igama)
        st.session_state.izimpendulo_ezilungile += 1
        if st.session_state.izimpendulo_ezilungile % 5 == 0:
            st.session_state.amazinga += 1
        st.session_state.isikhathi_sokuphela += 12
        khetha_igama_elilandelayo()
        st.session_state.impendulo_engalungile = False
    else:
        st.session_state.impendulo_engalungile = True


@st.dialog("Umdlalo Usuphelile")
def bonisa_umhumela():
    if st.session_state.isimo == "win":
        st.success("Halala! Uwatholile Amagama!")
    else:
        st.error("Isikhathi Sesiphelile.")
        st.write(
            f"Igama obekufanele ulithole, yileli: "
            f"**{st.session_state.igama_eliyimfihlo}**"
        )

    st.write(f"Amaphuzu akho: **{st.session_state.amaphuzu}**")

    if st.button("Dlala futhi", type="primary", use_container_width=True):
        qala_umdlalo()
        st.rerun()


st.set_page_config(page_title="Umdlalozinhlamvumagama", page_icon="🔤", layout="centered")

st.markdown(
    """
    <style>
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #000000;
    }
    [data-testid="stMarkdownContainer"], label, p, h1, h2, h3 {
        color: #ffffff !important;
    }
    div.stButton > button,
    div[data-testid="stFormSubmitButton"] > button {
        width: 100%;
        min-height: 2.8rem;
        border-radius: 0.7rem;
        font-size: 1rem;
    }
    @media (max-width: 600px) {
        .block-container { padding: 1rem 0.8rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "isimo" not in st.session_state:
    qala_umdlalo()

st.title("🔬 Uhlelo Lomdlalo Wezinhlamvu Zamagama esiZulu")
st.markdown("### Uhlelo Lokufunda Ngokwakheka Kwamagama esiZulu")
st.markdown("---")

with st.sidebar:
    st.markdown("### 👥 Umsunguli wohlelo")
    st.info(
        "**Lolu hlelo lusungulwe ngu:**\n\n"
        "🎓 **Mthuli Buthelezi**\n\n"
        "🎓 **Isikhungo Sezobuchwepheshe Boluntu™**\n\n"
        "**ubuchwephesheboluntu@gmail.com**"
    )
st.write("Hlanganisa izinhlamvu ukuze uthole igama elifihliwe.")
st.caption("Uma uqagela kahle, uthola imizuzwana engu-12 eyengeziwe.")


@st.fragment(run_every="1s")
def bonisa_iwashi():
    if st.session_state.isimo != "dlala":
        return

    okusele = max(
        0,
        int(st.session_state.isikhathi_sokuphela - time.time() + 0.999),
    )
    st.metric("Isikhathi esisele", f"{okusele} imizuzwana")

    if okusele <= 0:
        st.session_state.isimo = "lose"
        st.rerun()


bonisa_iwashi()

if st.session_state.isimo == "dlala":
    st.metric("Amaphuzu", st.session_state.amaphuzu)
    st.caption(f"Isigaba {st.session_state.amazinga}")
    st.write(f"**Izinhlamvu ezixutshiwe:** `{st.session_state.igama_elixutshiwe}`")

    with st.form("ifomu_lokuqagela", clear_on_submit=True):
        st.text_input(
            "Bhala igama elilungile",
            key="impendulo",
            placeholder="Faka impendulo yakho",
        )
        st.form_submit_button(
            "Qinisekisa impendulo",
            on_click=qinisekisa_impendulo,
            use_container_width=True,
        )

    if st.session_state.get("Lena yimpendulo engalungile", False):
        st.warning("Lempendulo Ayilungile. Zama futhi.")

elif st.session_state.isimo in ("win", "lose"):
    bonisa_umhumela()
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        <p><strong>🔬 Uhlelo LwesiZulu Lokufunda Ngokwakheka Kwamagama</strong></p>
        <p><em>Uhlelo Lwesizindalwazi Lokucwaninga kanye Nokufunda Ulimi LwesiZulu</em></p>
    </div>
    """,
    unsafe_allow_html=True,
)