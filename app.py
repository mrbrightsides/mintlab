import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="MintLab",
    page_icon="💻",
    layout="wide"
)

with st.sidebar:
    st.sidebar.image(
        "https://i.imgur.com/pwYe3ox.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    **MintLab** adalah platform pembelajaran interaktif yang dirancang untuk mahasiswa mata kuliah Bisnis Kapal Pesiar. Platform ini menggabungkan jalur pembelajaran terstruktur, studi kasus nyata, kuis interaktif, dan pelacakan progres untuk menciptakan pengalaman belajar yang seru dan praktis.

    Dengan Rantai-Cruise, mahasiswa bisa:
    
    - Memahami industri kapal pesiar melalui contoh nyata.
    
    - Melacak perjalanan belajar dan pencapaian secara mudah.
    
    - Membuat catatan dan menandai materi penting.
    
    - Menjelajahi peluang karier di sektor cruise.
    
    Dibuat dengan fokus pada kesederhanaan dan interaktivitas, Rantai-Cruise mengubah konsep bisnis yang kompleks menjadi pembelajaran yang menyenangkan dan mudah dipahami
    
    ---
    #### 🔮 Vision Statement
    
    Visi kami adalah memberdayakan generasi baru profesional bisnis kapal pesiar melalui platform belajar yang interaktif, praktis, dan menyenangkan.

    Kami bertujuan untuk:
    
    - Menjembatani teori di kelas dengan praktik nyata di industri.
    
    - Menginspirasi mahasiswa untuk mengeksplorasi karier di sektor kapal pesiar dan maritim.
    
    - Mendorong pembelajaran seumur hidup dengan alat yang intuitif, mudah diakses, dan menyenangkan.
    
    Rantai-Cruise bukan sekadar alat belajar—ini adalah gerbang menuju dunia peluang bisnis maritim.
   
    ---
    ### 🧩 Apps Showcase
    Lihat disini untuk semua tools yang kami kembangkan:
    [ELPEEF](https://showcase.elpeef.com/)
    
    ---
    #### 🙌 Dukungan & kontributor
    
    - ⭐ **Star / Fork**: [GitHub repo](https://github.com/mrbrightsides/mintlab)
    - Built with 💙 by [Khudri](https://s.id/khudri)
    - Dukung pengembangan proyek ini melalui: 
      [💖 GitHub Sponsors](https://github.com/sponsors/mrbrightsides) • 
      [☕ Ko-fi](https://ko-fi.com/khudri) • 
      [💵 PayPal](https://www.paypal.com/paypalme/akhmadkhudri) • 
      [🍵 Trakteer](https://trakteer.id/akhmad_khudri)

    Versi UI: v1.0 • Streamlit • Theme Dark
    """)

import streamlit.components.v1 as components

def embed_iframe(src, hide_top_px=100, hide_bottom_px=0, height=800):
    components.html(f"""
    <style>
        @media (max-width: 768px) {{
            .hide-on-mobile {{
                display: none !important;
            }}
            .show-on-mobile {{
                display: block !important;
                padding: 24px 12px;
                background: #ffecec;
                color: #d10000;
                font-weight: bold;
                text-align: center;
                border-radius: 12px;
                font-size: 1.2em;
                margin-top: 24px;
                animation: fadeIn 0.6s ease-in-out;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            }}
        }}
        @media (min-width: 769px) {{
            .show-on-mobile {{
                display: none !important;
            }}
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(12px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>

    <!-- Desktop view -->
    <div class="hide-on-mobile" style="height:{height}px; overflow:hidden; position:relative;">
        <iframe src="{src}" 
                style="width:100%; height:calc(100% + {hide_top_px + hide_bottom_px}px); 
                       border:none; position:relative; top:-{hide_top_px}px;">
        </iframe>
    </div>

    <!-- Mobile fallback -->
    <div class="show-on-mobile">
        📱 Tampilan ini tidak tersedia di perangkat seluler.<br>
        Silakan buka lewat laptop atau desktop untuk pengalaman penuh 💻
    </div>
    """, height=height + hide_top_px + hide_bottom_px)

iframe_url = "https://cruise.elpeef.com"

# Panggil fungsi
embed_iframe(iframe_url, hide_top_px=0, hide_bottom_px = -100, height=800)
