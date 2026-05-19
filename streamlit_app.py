import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Kalkulator Termodinamika",
    page_icon="⚗️",
    layout="wide"
)

# =========================
# CSS (RED + BLUE THEME + ANIMASI)
# =========================
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
}

/* Title */
.title {
    text-align: center;
    font-size: 45px;
    font-weight: 800;
    background: linear-gradient(90deg, #ff3b3b, #3b82f6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: fadeIn 1s ease-in-out;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 30px;
}

/* Card menu */
.card {
    padding: 20px;
    border-radius: 20px;
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
    text-align: center;
    transition: 0.3s;
    cursor: pointer;
    color: white;
    font-weight: bold;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 0px 20px rgba(59,130,246,0.6);
}

/* Button */
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #ff3b3b, #3b82f6);
    color: white;
    border-radius: 12px;
    padding: 10px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    transform: scale(1.03);
}

/* Result box */
.result {
    background: rgba(255,255,255,0.1);
    padding: 15px;
    border-radius: 15px;
    color: white;
    border-left: 5px solid #3b82f6;
}

/* Animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(-10px);}
    to {opacity: 1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)


# =========================
# SESSION STATE
# =========================
if "page" not in st.session_state:
    st.session_state.page = "home"

if "menu" not in st.session_state:
    st.session_state.menu = None


def go_home():
    st.session_state.page = "home"
    st.session_state.menu = None


# =========================
# HOME
# =========================
if st.session_state.page == "home":

    st.markdown('<div class="title">⚗️ ThermoCalc Pro</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Kalkulator Termodinamika Interaktif + Langkah Penyelesaian</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    menu_list = [
        "Hukum 1 Termodinamika",
        "Usaha",
        "Kalor",
        "Entalpi",
        "Hukum Hess",
        "ΔH Reaksi",
        "Energi Gibbs",
        "Entropi",
        "Gas Ideal",
        "Gas Nyata"
    ]

    cols = st.columns(2)

    for i, m in enumerate(menu_list):
        with cols[i % 2]:
            if st.button(f"⚡ {m}"):
                st.session_state.menu = m
                st.session_state.page = "calc"


# =========================
# CALC PAGE
# =========================
elif st.session_state.page == "calc":

    st.button("⬅️ Kembali", on_click=go_home)

    menu = st.session_state.menu
    st.markdown(f"## ⚗️ {menu}")

    st.markdown("---")


    # =========================
    # HUKUM 1 TERMODINAMIKA
    # =========================
    if menu == "Hukum 1 Termodinamika":

        st.latex(r"\Delta U = Q - W")

        opsi = st.selectbox("Cari:", ["ΔU", "Q", "W"])

        Q = st.number_input("Q (kJ)", value=0.0)
        W = st.number_input("W (kJ)", value=0.0)

        if st.button("Hitung"):

            if opsi == "ΔU":
                hasil = Q - W
                st.markdown(f"""
                <div class="result">
                <b>Langkah:</b><br>
                ΔU = Q - W <br>
                ΔU = {Q} - {W} <br><br>
                <b>Hasil:</b> ΔU = {hasil:.3f} kJ
                </div>
                """, unsafe_allow_html=True)

            elif opsi == "Q":
                dU = st.number_input("ΔU (kJ)", value=0.0)
                hasil = dU + W
                st.markdown(f"""
                <div class="result">
                Q = ΔU + W <br>
                Q = {dU} + {W} <br><br>
                Q = {hasil:.3f} kJ
                </div>
                """, unsafe_allow_html=True)

            else:
                dU = st.number_input("ΔU (kJ)", value=0.0)
                hasil = Q - dU
                st.markdown(f"""
                <div class="result">
                W = Q - ΔU <br>
                W = {Q} - {dU} <br><br>
                W = {hasil:.3f} kJ
                </div>
                """, unsafe_allow_html=True)


    # =========================
    # USAHA
    # =========================
    elif menu == "Usaha":

        st.latex(r"W = P \cdot \Delta V")

        P = st.number_input("P (Pa)", 0.0)
        dV = st.number_input("ΔV (m³)", 0.0)

        if st.button("Hitung"):
            st.markdown(f"""
            <div class="result">
            W = P × ΔV <br>
            W = {P} × {dV} <br><br>
            W = {(P*dV):.3f} J
            </div>
            """, unsafe_allow_html=True)


    # =========================
    # KALOR
    # =========================
    elif menu == "Kalor":

        st.latex(r"Q = m c \Delta T")

        m = st.number_input("massa (g)", 0.0)
        c = st.number_input("c (J/gK)", 0.0)
        dT = st.number_input("ΔT (K)", 0.0)

        if st.button("Hitung"):
            hasil = m*c*dT
            st.markdown(f"""
            <div class="result">
            Q = m × c × ΔT <br>
            Q = {m} × {c} × {dT} <br><br>
            Q = {hasil:.3f} J
            </div>
            """, unsafe_allow_html=True)


    # =========================
    # ENTALPI
    # =========================
    elif menu == "Entalpi":

        st.latex(r"\Delta H = \Delta U + \Delta nRT")

        dU = st.number_input("ΔU", 0.0)
        dn = st.number_input("Δn", 0.0)
        T = st.number_input("T", 0.0)

        R = 0.008314

        if st.button("Hitung"):
            hasil = dU + (dn*R*T)
            st.markdown(f"""
            <div class="result">
            ΔH = ΔU + ΔnRT <br>
            ΔH = {dU} + ({dn}×{R}×{T}) <br><br>
            ΔH = {hasil:.3f} kJ
            </div>
            """, unsafe_allow_html=True)


    # =========================
    # HESS
    # =========================
    elif menu == "Hukum Hess":

        st.latex(r"\Delta H = \sum \Delta H")

        data = st.text_input("ΔH (pisahkan koma)", "10,-20,30")

        if st.button("Hitung"):
            arr = [float(x) for x in data.split(",")]
            st.markdown(f"""
            <div class="result">
            Data: {arr} <br><br>
            ΣΔH = {sum(arr):.3f} kJ
            </div>
            """, unsafe_allow_html=True)


    # =========================
    # ΔH REAKSI
    # =========================
    elif menu == "ΔH Reaksi":

        st.latex(r"\Delta H = \sum Hf_{produk} - \sum Hf_{reaktan}")

        p = st.text_input("Produk")
        r = st.text_input("Reaktan")

        if st.button("Hitung") and p and r:
            p = [float(x) for x in p.split(",")]
            r = [float(x) for x in r.split(",")]

            hasil = sum(p) - sum(r)

            st.markdown(f"""
            <div class="result">
            ΣProduk = {sum(p)} <br>
            ΣReaktan = {sum(r)} <br><br>
            ΔH = {hasil:.3f} kJ/mol
            </div>
            """, unsafe_allow_html=True)


    # =========================
    # GIBBS
    # =========================
    elif menu == "Energi Gibbs":

        st.latex(r"\Delta G = \Delta H - T\Delta S")

        dH = st.number_input("ΔH", 0.0)
        T = st.number_input("T", 0.0)
        dS = st.number_input("ΔS", 0.0)

        if st.button("Hitung"):
            hasil = dH - (T*dS)

            st.markdown(f"""
            <div class="result">
            ΔG = ΔH - TΔS <br>
            ΔG = {dH} - ({T}×{dS}) <br><br>
            ΔG = {hasil:.3f} kJ
            </div>
            """, unsafe_allow_html=True)


    # =========================
    # ENTROPI
    # =========================
    elif menu == "Entropi":

        st.latex(r"\Delta S = Q/T")

        Q = st.number_input("Q", 0.0)
        T = st.number_input("T", 0.0)

        if st.button("Hitung"):
            if T == 0:
                st.error("T tidak boleh 0")
            else:
                hasil = Q/T
                st.markdown(f"""
                <div class="result">
                ΔS = Q/T <br>
                ΔS = {Q}/{T} <br><br>
                ΔS = {hasil:.3f} kJ/K
                </div>
                """, unsafe_allow_html=True)


    # =========================
    # GAS IDEAL
    # =========================
    elif menu == "Gas Ideal":

        st.latex(r"PV = nRT")

        n = st.number_input("n", 0.0)
        T = st.number_input("T", 0.0)
        V = st.number_input("V", 0.0)

        R = 0.0821

        if st.button("Hitung"):
            P = (n*R*T)/V if V != 0 else 0

            st.markdown(f"""
            <div class="result">
            P = nRT/V <br>
            P = {(n*R*T):.3f}/{V} <br><br>
            P = {P:.3f} atm
            </div>
            """, unsafe_allow_html=True)


    # =========================
    # GAS NYATA
    # =========================
    elif menu == "Gas Nyata":

        st.latex(r"(P+\frac{an^2}{V^2})(V-nb)=nRT")

        n = st.number_input("n", 0.0)
        T = st.number_input("T", 0.0)
        V = st.number_input("V", 0.0)
        a = st.number_input("a", 0.0)
        b = st.number_input("b", 0.0)

        if st.button("Hitung"):
            R = 0.0821
            P = ((n*R*T)/(V-n*b)) - ((a*n**2)/(V**2))

            st.markdown(f"""
            <div class="result">
            Van der Waals <br>
            P = {P:.3f} atm
            </div>
            """, unsafe_allow_html=True)
