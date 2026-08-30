
import streamlit as st
import pandas as pd
import uuid
from datetime import datetime


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="IBeX | Campus Marketplace",
    page_icon="🟣",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* ==========================================================
   GLOBAL
   ========================================================== */

.stApp {
    background:
        radial-gradient(circle at top left, #F4EEFF 0%, transparent 28%),
        linear-gradient(180deg, #F8FAFC 0%, #FFFFFF 100%);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                 Roboto, Helvetica, Arial, sans-serif;
    color: #172033;
}

.block-container {
    max-width: 1450px;
    padding-top: 1.1rem;
    padding-bottom: 3rem;
}

/* Hide Streamlit sidebar completely */
[data-testid="stSidebar"] {
    display: none;
}

/* Reduce Streamlit top whitespace */
header[data-testid="stHeader"] {
    background: transparent;
}


/* ==========================================================
   BRAND / HEADER
   ========================================================== */

.ibex-brand-wrap {
    display: flex;
    align-items: center;
    gap: 10px;
}

.ibex-logo-box {
    width: 47px;
    height: 47px;
    border-radius: 14px;
    background: linear-gradient(135deg, #5B2C83, #8E5BB7);
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 6px 18px rgba(91, 44, 131, 0.20);
}

.ibex-brand-name {
    font-size: 1.85rem;
    font-weight: 850;
    color: #54268A;
    line-height: 1;
    letter-spacing: -0.8px;
}

.ibex-brand-tagline {
    font-size: 0.72rem;
    color: #64748B;
    margin-top: 4px;
    letter-spacing: 0.03em;
}

.header-divider {
    height: 1px;
    background: #E2E8F0;
    margin-top: 10px;
    margin-bottom: 26px;
}


/* ==========================================================
   BUTTONS
   ========================================================== */

div.stButton > button {
    border-radius: 11px;
    border: 1px solid #E2E8F0;
    background: rgba(255,255,255,0.92);
    color: #334155;
    font-weight: 650;
    min-height: 43px;
    transition: all 0.2s ease;
    box-shadow: 0 3px 10px rgba(15,23,42,0.025);
}

div.stButton > button:hover {
    border-color: #7C3FB3;
    color: #5B2C83;
    background: #FAF7FF;
    transform: translateY(-1px);
}


/* ==========================================================
   HERO / GLASSMORPHISM
   ========================================================== */

.hero-glass {
    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.93),
            rgba(247,242,255,0.88)
        );
    border: 1px solid rgba(226,232,240,0.95);
    border-radius: 25px;
    padding: 42px 44px;
    margin-bottom: 20px;
    box-shadow:
        0px 18px 50px rgba(91,44,131,0.08);
    backdrop-filter: blur(16px);
}

.hero-kicker {
    display: inline-block;
    background: #F1E8FA;
    color: #6A359C;
    border-radius: 999px;
    padding: 6px 11px;
    font-weight: 700;
    font-size: 0.76rem;
    margin-bottom: 17px;
}

.hero-title {
    font-size: 3.15rem;
    font-weight: 850;
    color: #172033;
    line-height: 1.08;
    letter-spacing: -1.8px;
}

.hero-highlight {
    color: #6A359C;
}

.hero-text {
    font-size: 1.04rem;
    color: #64748B;
    max-width: 780px;
    line-height: 1.72;
    margin-top: 15px;
}


/* ==========================================================
   TRUST BADGES
   ========================================================== */

.trust-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 23px;
}

.trust-pill {
    background: rgba(255,255,255,0.92);
    border: 1px solid #E2E8F0;
    border-radius: 999px;
    padding: 8px 14px;
    font-size: 0.80rem;
    color: #475569;
    font-weight: 650;
    box-shadow: 0 3px 10px rgba(15,23,42,0.025);
}


/* ==========================================================
   LIVE METRIC PILLS
   ========================================================== */

.metric-pill {
    background: rgba(255,255,255,0.90);
    border: 1px solid #E2E8F0;
    border-radius: 15px;
    padding: 15px 12px;
    text-align: center;
    box-shadow: 0 5px 18px rgba(15,23,42,0.035);
}

.metric-value {
    font-size: 1.48rem;
    font-weight: 850;
    color: #5B2C83;
}

.metric-label {
    font-size: 0.75rem;
    color: #64748B;
    margin-top: 3px;
}


/* ==========================================================
   SECTION HEADINGS
   ========================================================== */

.section-title {
    font-size: 1.65rem;
    font-weight: 800;
    color: #172033;
    margin-top: 30px;
    margin-bottom: 4px;
}

.section-subtitle {
    color: #64748B;
    font-size: 0.91rem;
    margin-bottom: 18px;
}


/* ==========================================================
   PRODUCT CARDS
   ========================================================== */

.product-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 17px;
    padding: 17px;
    min-height: 325px;
    box-shadow: 0 5px 18px rgba(15,23,42,0.04);
    transition: transform 0.22s ease, box-shadow 0.22s ease;
    margin-bottom: 9px;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(15,23,42,0.09);
}

.product-image {
    height: 118px;
    border-radius: 13px;
    background:
        linear-gradient(135deg, #F4EDFA, #FAFAFD);
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 3.5rem;
    margin-bottom: 14px;
}

.product-name {
    font-size: 1.03rem;
    font-weight: 780;
    color: #172033;
    margin-top: 10px;
    margin-bottom: 5px;
}

.product-price {
    font-size: 1.33rem;
    font-weight: 850;
    color: #54268A;
    margin-top: 10px;
    margin-bottom: 6px;
}

.product-meta {
    font-size: 0.76rem;
    color: #64748B;
    line-height: 1.65;
}

.verified-text {
    color: #16803C;
    font-size: 0.76rem;
    font-weight: 700;
    margin-top: 8px;
}


/* ==========================================================
   BADGES
   ========================================================== */

.badge-rent {
    display: inline-block;
    background: #E0F2FE;
    color: #0369A1;
    padding: 5px 9px;
    border-radius: 7px;
    font-size: 0.68rem;
    font-weight: 800;
    letter-spacing: 0.03em;
}

.badge-sale {
    display: inline-block;
    background: #DCFCE7;
    color: #15803D;
    padding: 5px 9px;
    border-radius: 7px;
    font-size: 0.68rem;
    font-weight: 800;
    letter-spacing: 0.03em;
}

.badge-help {
    display: inline-block;
    background: #FEE2E2;
    color: #B91C1C;
    padding: 5px 9px;
    border-radius: 7px;
    font-size: 0.68rem;
    font-weight: 800;
    letter-spacing: 0.03em;
}


/* ==========================================================
   HOW IT WORKS
   ========================================================== */

.step-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 22px;
    min-height: 190px;
    box-shadow: 0 4px 15px rgba(15,23,42,0.03);
}

.step-number {
    width: 35px;
    height: 35px;
    border-radius: 50%;
    background: linear-gradient(135deg, #5B2C83, #8E5BB7);
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 800;
    margin-bottom: 14px;
}

.step-title {
    font-size: 1rem;
    font-weight: 780;
    color: #172033;
    margin-bottom: 7px;
}

.step-text {
    font-size: 0.82rem;
    line-height: 1.6;
    color: #64748B;
}


/* ==========================================================
   GENERIC CARDS
   ========================================================== */

.info-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 17px;
    padding: 22px;
    box-shadow: 0 5px 18px rgba(15,23,42,0.035);
    margin-bottom: 15px;
}

.secure-box {
    background: #F0FDF4;
    border: 1px solid #BBF7D0;
    border-radius: 12px;
    padding: 14px;
    color: #166534;
    line-height: 1.55;
}

.reward-box {
    background: #FFF7E6;
    border: 1px solid #FCD9A7;
    border-radius: 12px;
    padding: 15px;
}

.warning-box {
    background: #FFF7ED;
    border: 1px solid #FED7AA;
    border-radius: 12px;
    padding: 15px;
    color: #9A3412;
}


/* ==========================================================
   PROFILE
   ========================================================== */

.profile-avatar {
    width: 70px;
    height: 70px;
    background: #EFE5F8;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2rem;
}


/* ==========================================================
   FOOTER
   ========================================================== */

.footer {
    text-align: center;
    color: #94A3B8;
    font-size: 0.78rem;
    padding-top: 28px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

if "selected_item" not in st.session_state:
    st.session_state.selected_item = None

if "orders" not in st.session_state:
    st.session_state.orders = []

if "points" not in st.session_state:
    st.session_state.points = 245

if "custom_listings" not in st.session_state:
    st.session_state.custom_listings = []

if "help_requests" not in st.session_state:
    st.session_state.help_requests = []


# ============================================================
# HELPER FUNCTION
# ============================================================

def navigate(page):
    st.session_state.current_page = page


# ============================================================
# HOSTEL BLOCKS
# ============================================================

HOSTEL_BLOCKS = [
    "ABCD Block",
    "QRS Block",
    "U-Block",
    "T-Block",
    "G-Block",
    "H-Block",
    "B1-Block",
    "B2-Block",
    "D1-Block",
    "D2-Block",
    "S1-Block",
    "S2-Block"
]


# ============================================================
# CATEGORY ICONS
# ============================================================

CATEGORY_ICONS = {
    "Academic": "📚",
    "Fashion": "👗",
    "Personal Care": "✨",
    "Hostel Utility": "🏠",
    "Electronics": "🔌",
    "Sports": "🏸",
    "Bags": "🎒",
    "Event / Function": "🎉",
    "Essential Help": "🆘",
    "Other": "📦"
}


# ============================================================
# SAMPLE MARKETPLACE DATA
# ============================================================

marketplace_data = [

    {
        "id": "L001",
        "item": "Scientific Calculator",
        "category": "Academic",
        "type": "Buy",
        "price": 500,
        "deposit": 0,
        "condition": "Excellent",
        "rating": 4.8,
        "seller": "IBX Student 104",
        "location": "ABCD Block",
        "transactions": 18
    },

    {
        "id": "L002",
        "item": "Black Formal Heels",
        "category": "Fashion",
        "type": "Rent",
        "price": 50,
        "deposit": 300,
        "condition": "Good",
        "rating": 4.7,
        "seller": "IBX Student 218",
        "location": "QRS Block",
        "transactions": 12
    },

    {
        "id": "L003",
        "item": "Hair Dryer",
        "category": "Personal Care",
        "type": "Rent",
        "price": 30,
        "deposit": 200,
        "condition": "Excellent",
        "rating": 4.9,
        "seller": "IBX Student 302",
        "location": "U-Block",
        "transactions": 24
    },

    {
        "id": "L004",
        "item": "Electric Iron",
        "category": "Hostel Utility",
        "type": "Rent",
        "price": 20,
        "deposit": 150,
        "condition": "Good",
        "rating": 4.6,
        "seller": "IBX Student 187",
        "location": "T-Block",
        "transactions": 10
    },

    {
        "id": "L005",
        "item": "Ethnic Kurta Set",
        "category": "Fashion",
        "type": "Rent",
        "price": 100,
        "deposit": 500,
        "condition": "Excellent",
        "rating": 4.9,
        "seller": "IBX Student 411",
        "location": "G-Block",
        "transactions": 20
    },

    {
        "id": "L006",
        "item": "Extension Board",
        "category": "Electronics",
        "type": "Buy",
        "price": 300,
        "deposit": 0,
        "condition": "Good",
        "rating": 4.5,
        "seller": "IBX Student 096",
        "location": "H-Block",
        "transactions": 8
    },

    {
        "id": "L007",
        "item": "Sports Shoes",
        "category": "Sports",
        "type": "Buy",
        "price": 800,
        "deposit": 0,
        "condition": "Good",
        "rating": 4.8,
        "seller": "IBX Student 355",
        "location": "B1-Block",
        "transactions": 15
    },

    {
        "id": "L008",
        "item": "Tripod",
        "category": "Electronics",
        "type": "Rent",
        "price": 40,
        "deposit": 300,
        "condition": "Good",
        "rating": 4.7,
        "seller": "IBX Student 274",
        "location": "D1-Block",
        "transactions": 16
    }

]

marketplace_data.extend(st.session_state.custom_listings)


# ============================================================
# TOP HEADER NAVIGATION
# ============================================================

header = st.columns(
    [2.2, 0.8, 1.05, 0.85, 0.95, 1.05, 1.05, 1.05]
)


# Brand logo
with header[0]:

    st.markdown("""
    <div class="ibex-brand-wrap">

        <div class="ibex-logo-box">

            <svg width="28" height="28" viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="42"
                        fill="none"
                        stroke="white"
                        stroke-width="9"/>
                <path d="M30 50 L45 65 L72 34"
                      fill="none"
                      stroke="white"
                      stroke-width="9"
                      stroke-linecap="round"
                      stroke-linejoin="round"/>
            </svg>

        </div>

        <div>
            <div class="ibex-brand-name">IBeX</div>
            <div class="ibex-brand-tagline">
                Campus Marketplace
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)


with header[1]:

    st.button(
        "Home",
        use_container_width=True,
        on_click=navigate,
        args=("Home",),
        key="nav_home"
    )


with header[2]:

    st.button(
        "Marketplace",
        use_container_width=True,
        on_click=navigate,
        args=("Marketplace",),
        key="nav_market"
    )


with header[3]:

    st.button(
        "Services",
        use_container_width=True,
        on_click=navigate,
        args=("Services",),
        key="nav_services"
    )


with header[4]:

    st.button(
        "Community",
        use_container_width=True,
        on_click=navigate,
        args=("Community",),
        key="nav_community"
    )


with header[5]:

    st.button(
        "＋ List Item",
        use_container_width=True,
        on_click=navigate,
        args=("List Item",),
        key="nav_list"
    )


with header[6]:

    st.button(
        f"🛒 Cart ({len(st.session_state.orders)})",
        use_container_width=True,
        on_click=navigate,
        args=("Orders",),
        key="nav_orders"
    )


with header[7]:

    st.button(
        f"👤 {st.session_state.points} Pts",
        use_container_width=True,
        on_click=navigate,
        args=("Profile",),
        key="nav_profile"
    )


st.markdown(
    '<div class="header-divider"></div>',
    unsafe_allow_html=True
)


# ============================================================
# HOME
# ============================================================

if st.session_state.current_page == "Home":

    # --------------------------------------------------------
    # HERO
    # --------------------------------------------------------

    st.markdown("""
    <div class="hero-glass">

        <div class="hero-kicker">
            IBS-ONLY VERIFIED COMMUNITY
        </div>

        <div class="hero-title">
            Campus life made
            <span class="hero-highlight">simpler.</span>
        </div>

        <div class="hero-text">
            Rent what you need, buy second-hand, earn from unused
            products, request campus assistance and reward students
            who make the community work — all within IBeX.
        </div>

        <div class="trust-row">

            <div class="trust-pill">
                🔒 IBS Verified
            </div>

            <div class="trust-pill">
                ⚡ Instant Campus Pickup
            </div>

            <div class="trust-pill">
                🌱 Zero-Waste Mindset
            </div>

            <div class="trust-pill">
                ⭐ Rewards for Helping
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)


    # --------------------------------------------------------
    # LIVE IMPACT METRICS
    # --------------------------------------------------------

    metric1, metric2, metric3, metric4 = st.columns(4)


    with metric1:

        st.markdown(
            f"""
            <div class="metric-pill">

                <div class="metric-value">
                    {len(marketplace_data)}
                </div>

                <div class="metric-label">
                    Active Listings
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with metric2:

        st.markdown(
            f"""
            <div class="metric-pill">

                <div class="metric-value">
                    {st.session_state.points}
                </div>

                <div class="metric-label">
                    IBeX Points
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with metric3:

        st.markdown("""
        <div class="metric-pill">

            <div class="metric-value">
                100%
            </div>

            <div class="metric-label">
                Student Verified
            </div>

        </div>
        """, unsafe_allow_html=True)


    with metric4:

        st.markdown(
            f"""
            <div class="metric-pill">

                <div class="metric-value">
                    {len(st.session_state.orders)}
                </div>

                <div class="metric-label">
                    Your Orders
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # --------------------------------------------------------
    # FEATURED PRODUCTS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Featured Marketplace</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Useful items currently available around campus.'
        '</div>',
        unsafe_allow_html=True
    )


    featured = marketplace_data[:4]

    featured_cols = st.columns(4)


    for index, item in enumerate(featured):

        with featured_cols[index]:

            icon = CATEGORY_ICONS.get(
                item["category"],
                "📦"
            )


            if item["type"] == "Rent":

                badge_class = "badge-rent"
                badge_text = "FOR RENT"
                price_text = f"₹{item['price']}/day"

            else:

                badge_class = "badge-sale"
                badge_text = "FOR SALE"
                price_text = f"₹{item['price']}"


            st.markdown(
                f"""
                <div class="product-card">

                    <div class="product-image">
                        {icon}
                    </div>

                    <span class="{badge_class}">
                        {badge_text}
                    </span>

                    <div class="product-name">
                        {item['item']}
                    </div>

                    <div class="product-price">
                        {price_text}
                    </div>

                    <div class="product-meta">
                        Condition: {item['condition']}
                        <br>
                        📍 {item['location']}
                    </div>

                    <div class="verified-text">
                        ✓ IBS Verified
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


            action_text = (
                "Quick Rent"
                if item["type"] == "Rent"
                else "View Item"
            )


            if st.button(
                action_text,
                key=f"featured_{item['id']}",
                use_container_width=True
            ):

                st.session_state.selected_item = item

                st.session_state.current_page = "Checkout"

                st.rerun()


    # --------------------------------------------------------
    # HOW IT WORKS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">How IBeX Works</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'A simple four-step campus transaction flow.'
        '</div>',
        unsafe_allow_html=True
    )


    step1, step2, step3, step4 = st.columns(4)


    with step1:

        st.markdown("""
        <div class="step-card">

            <div class="step-number">
                1
            </div>

            <div class="step-title">
                Browse & Select
            </div>

            <div class="step-text">
                Search the marketplace and choose whether you
                want to buy, rent or request campus assistance.
            </div>

        </div>
        """, unsafe_allow_html=True)


    with step2:

        st.markdown("""
        <div class="step-card">

            <div class="step-number">
                2
            </div>

            <div class="step-title">
                Connect & Verify
            </div>

            <div class="step-text">
                Interact within an IBS-only verified community
                supported by ratings and trust mechanisms.
            </div>

        </div>
        """, unsafe_allow_html=True)


    with step3:

        st.markdown("""
        <div class="step-card">

            <div class="step-number">
                3
            </div>

            <div class="step-title">
                Campus Pickup / Delivery
            </div>

            <div class="step-text">
                Pick up the item yourself or choose convenient
                campus delivery for an additional fee.
            </div>

        </div>
        """, unsafe_allow_html=True)


    with step4:

        st.markdown("""
        <div class="step-card">

            <div class="step-number">
                4
            </div>

            <div class="step-title">
                Earn Reward Points
            </div>

            <div class="step-text">
                Complete transactions, help other students and
                earn IBeX points for future benefits.
            </div>

        </div>
        """, unsafe_allow_html=True)


    # --------------------------------------------------------
    # VALUE PROPOSITION
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Why IBeX?</div>',
        unsafe_allow_html=True
    )


    value1, value2, value3 = st.columns(3)


    with value1:

        st.markdown("""
        <div class="info-card">

            <h3>💸 Affordable Access</h3>

            <p>
                Avoid purchasing products at full price when
                you only need them temporarily.
            </p>

        </div>
        """, unsafe_allow_html=True)


    with value2:

        st.markdown("""
        <div class="info-card">

            <h3>♻️ Reuse & Extract Value</h3>

            <p>
                Turn unused products into value while helping
                other students reduce unnecessary purchases.
            </p>

        </div>
        """, unsafe_allow_html=True)


    with value3:

        st.markdown("""
        <div class="info-card">

            <h3>🤝 Community Convenience</h3>

            <p>
                Request deliveries or small campus assistance
                from other verified students.
            </p>

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# MARKETPLACE
# ============================================================

elif st.session_state.current_page == "Marketplace":

    st.markdown(
        '<div class="section-title">Marketplace</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Buy second-hand or rent what you only need temporarily.'
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # FILTERS
    # --------------------------------------------------------

    search_col, category_col, type_col = st.columns(
        [2.1, 1.3, 1.2]
    )


    with search_col:

        search = st.text_input(
            "Search",
            placeholder="Search calculator, heels, iron, tripod..."
        )


    categories = sorted(
        list(
            set(
                item["category"]
                for item in marketplace_data
            )
        )
    )


    with category_col:

        category_filter = st.selectbox(
            "Category",
            ["All"] + categories
        )


    with type_col:

        type_filter = st.selectbox(
            "Listing Type",
            [
                "All",
                "Buy",
                "Rent"
            ]
        )


    filtered = marketplace_data.copy()


    if search:

        filtered = [
            item
            for item in filtered
            if search.lower()
            in item["item"].lower()
        ]


    if category_filter != "All":

        filtered = [
            item
            for item in filtered
            if item["category"] == category_filter
        ]


    if type_filter != "All":

        filtered = [
            item
            for item in filtered
            if item["type"] == type_filter
        ]


    st.caption(
        f"{len(filtered)} listing(s) found"
    )


    # --------------------------------------------------------
    # PRODUCT GRID
    # --------------------------------------------------------

    if len(filtered) == 0:

        st.info(
            "No matching items found."
        )


    else:

        for start in range(
            0,
            len(filtered),
            4
        ):

            cols = st.columns(4)

            row_items = filtered[
                start:start + 4
            ]


            for index, item in enumerate(
                row_items
            ):

                with cols[index]:

                    icon = CATEGORY_ICONS.get(
                        item["category"],
                        "📦"
                    )


                    if item["type"] == "Rent":

                        badge_class = "badge-rent"
                        badge_text = "FOR RENT"

                        price_display = (
                            f"₹{item['price']}/day"
                        )

                        extra_text = (
                            f"Deposit: ₹{item['deposit']}"
                        )

                    else:

                        badge_class = "badge-sale"
                        badge_text = "FOR SALE"

                        price_display = (
                            f"₹{item['price']}"
                        )

                        extra_text = (
                            "Second-hand purchase"
                        )


                    st.markdown(
                        f"""
                        <div class="product-card">

                            <div class="product-image">
                                {icon}
                            </div>

                            <span class="{badge_class}">
                                {badge_text}
                            </span>

                            <div class="product-name">
                                {item['item']}
                            </div>

                            <div class="product-price">
                                {price_display}
                            </div>

                            <div class="product-meta">

                                {extra_text}
                                <br>

                                Condition:
                                {item['condition']}
                                <br>

                                📍 {item['location']}
                                <br>

                                ⭐ {item['rating']} •
                                {item['transactions']}
                                transactions

                            </div>

                            <div class="verified-text">
                                ✓ Verified IBS Student
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                    button_text = (
                        "Quick Rent"
                        if item["type"] == "Rent"
                        else "View Item"
                    )


                    if st.button(
                        button_text,
                        key=f"product_{item['id']}",
                        use_container_width=True
                    ):

                        st.session_state.selected_item = item

                        st.session_state.current_page = "Checkout"

                        st.rerun()


    st.caption(
        "Prototype listings are illustrative demo records."
    )


# ============================================================
# LIST ITEM
# ============================================================

elif st.session_state.current_page == "List Item":

    st.markdown(
        '<div class="section-title">＋ List an Item</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Sell something you no longer use or earn by lending it.'
        '</div>',
        unsafe_allow_html=True
    )


    st.info(
        "🎁 First 5 listings are free. "
        "After the free allowance, additional listing benefits "
        "can be unlocked through IBeX subscription plans."
    )


    form_left, form_right = st.columns(2)


    with form_left:

        item_name = st.text_input(
            "Item Name",
            placeholder="Example: Black formal dress"
        )


        category = st.selectbox(
            "Category",
            [
                "Academic",
                "Fashion",
                "Electronics",
                "Hostel Utility",
                "Personal Care",
                "Sports",
                "Bags",
                "Event / Function",
                "Other"
            ]
        )


        listing_type = st.radio(
            "I want to",
            [
                "Sell",
                "Lend / Rent"
            ]
        )


        condition = st.selectbox(
            "Condition",
            [
                "Excellent",
                "Good",
                "Fair"
            ]
        )


    with form_right:

        price = st.number_input(
            "Selling Price / Rental Fee per Day (₹)",
            min_value=0,
            value=50
        )


        deposit = 0


        if listing_type == "Lend / Rent":

            deposit = st.number_input(
                "Refundable Security Deposit (₹)",
                min_value=0,
                value=200
            )


        location_option = st.selectbox(
            "Hostel Block",
            HOSTEL_BLOCKS
            + [
                "Other / Enter Manually"
            ]
        )


        if (
            location_option
            == "Other / Enter Manually"
        ):

            location = st.text_input(
                "Enter Hostel / Block"
            )

        else:

            location = location_option


    description = st.text_area(
        "Description",
        placeholder=(
            "Add size, condition, accessories, "
            "usage details or other useful information."
        )
    )


    if st.button(
        "Publish Listing",
        type="primary"
    ):

        if not item_name.strip():

            st.warning(
                "Please enter an item name."
            )


        elif not location.strip():

            st.warning(
                "Please enter a valid location."
            )


        else:

            new_listing = {

                "id":
                    "L"
                    + str(
                        1000
                        + len(
                            st.session_state.custom_listings
                        )
                    ),

                "item":
                    item_name,

                "category":
                    category,

                "type":
                    (
                        "Rent"
                        if listing_type
                        == "Lend / Rent"
                        else "Buy"
                    ),

                "price":
                    price,

                "deposit":
                    deposit,

                "condition":
                    condition,

                "rating":
                    5.0,

                "seller":
                    "You",

                "location":
                    location,

                "transactions":
                    0
            }


            st.session_state.custom_listings.append(
                new_listing
            )


            st.success(
                f"✅ {item_name} has been listed successfully!"
            )

            st.balloons()


# ============================================================
# CHECKOUT
# ============================================================

elif st.session_state.current_page == "Checkout":

    st.markdown(
        '<div class="section-title">Secure Checkout</div>',
        unsafe_allow_html=True
    )


    item = st.session_state.selected_item


    if item is None:

        st.info(
            "Select an item from Marketplace first."
        )


        if st.button(
            "Go to Marketplace"
        ):

            st.session_state.current_page = "Marketplace"

            st.rerun()


    else:

        item_col, payment_col = st.columns(
            [1.05, 1.5]
        )


        # ----------------------------------------------------
        # SELECTED ITEM
        # ----------------------------------------------------

        with item_col:

            icon = CATEGORY_ICONS.get(
                item["category"],
                "📦"
            )


            st.markdown(
                f"""
                <div class="product-card">

                    <div class="product-image">
                        {icon}
                    </div>

                    <div class="product-name">
                        {item['item']}
                    </div>

                    <div class="product-meta">

                        Condition:
                        {item['condition']}
                        <br>

                        📍 {item['location']}
                        <br>

                        ⭐ {item['rating']}
                        rating

                    </div>

                    <div class="verified-text">
                        ✓ Verified IBS Seller
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        # ----------------------------------------------------
        # PAYMENT / ORDER
        # ----------------------------------------------------

        with payment_col:

            if item["type"] == "Rent":

                days = st.number_input(
                    "Rental Duration (Days)",
                    min_value=1,
                    max_value=30,
                    value=1
                )


                base_price = (
                    item["price"]
                    * days
                )


                deposit = item["deposit"]


            else:

                days = 0

                base_price = item["price"]

                deposit = 0


            delivery_option = st.radio(
                "Delivery Option",
                [
                    "Self Pickup — FREE",
                    "IBeX Campus Delivery — ₹20"
                ]
            )


            delivery_fee = (
                20
                if "₹20"
                in delivery_option
                else 0
            )


            total = (
                base_price
                + deposit
                + delivery_fee
            )


            # -----------------------------------------------
            # SUMMARY
            # -----------------------------------------------

            st.markdown(
                "### Order Summary"
            )


            if item["type"] == "Rent":

                st.write(
                    f"Rental ({days} day(s)): "
                    f"**₹{base_price}**"
                )


                st.write(
                    "Refundable Security Deposit: "
                    f"**₹{deposit}**"
                )


            else:

                st.write(
                    f"Product Price: "
                    f"**₹{base_price}**"
                )


            st.write(
                f"Delivery: "
                f"**₹{delivery_fee}**"
            )


            st.divider()


            st.markdown(
                f"## Total Payable: ₹{total}"
            )


            if item["type"] == "Rent":

                st.success(
                    f"₹{deposit} is refundable after "
                    "successful return of the item."
                )


            # -----------------------------------------------
            # PAYMENT METHOD
            # -----------------------------------------------

            st.markdown(
                "### Payment Method"
            )


            payment_method = st.radio(
                "Choose payment method",
                [
                    "📱 UPI / GPay / PhonePe",
                    "💳 Card",
                    "💵 Cash on Delivery"
                ]
            )


            if "UPI" in payment_method:

                st.markdown("""
                <div class="secure-box">

                    🔐 <b>Secure UPI Payment</b>
                    <br><br>

                    In a live implementation, payment would be
                    processed through an authorised payment gateway.

                    <br><br>

                    Payment information is never displayed
                    to another IBeX user.

                </div>
                """, unsafe_allow_html=True)


                st.text_input(
                    "Prototype UPI ID",
                    placeholder="example@upi",
                    type="password"
                )


                st.caption(
                    "Prototype mode — no real payment is deducted."
                )


            elif "Card" in payment_method:

                st.markdown("""
                <div class="secure-box">

                    🔐 <b>Secure Card Payment</b>
                    <br><br>

                    A live version would send card processing
                    directly through the payment gateway.

                    <br><br>

                    Card information is not shared with sellers.

                </div>
                """, unsafe_allow_html=True)


                st.text_input(
                    "Card Number",
                    placeholder="•••• •••• •••• ••••",
                    type="password"
                )


                card_col1, card_col2 = st.columns(2)


                with card_col1:

                    st.text_input(
                        "Expiry",
                        placeholder="MM/YY"
                    )


                with card_col2:

                    st.text_input(
                        "CVV",
                        type="password"
                    )


                st.caption(
                    "Prototype mode — card details are "
                    "not processed or stored."
                )


            else:

                st.markdown("""
                <div class="secure-box">

                    💵 <b>Cash on Delivery / Handover</b>
                    <br><br>

                    Pay when the item is delivered or handed over.

                </div>
                """, unsafe_allow_html=True)


            st.write("")


            button_text = (
                f"Confirm COD — ₹{total}"
                if "Cash"
                in payment_method
                else f"Secure Test Payment — ₹{total}"
            )


            if st.button(
                button_text,
                type="primary",
                use_container_width=True
            ):

                order_id = (
                    "IBX-"
                    + datetime.now().strftime(
                        "%y%m%d"
                    )
                    + "-"
                    + str(
                        uuid.uuid4()
                    )[:6].upper()
                )


                payment_status = (
                    "Cash on Delivery"
                    if "Cash"
                    in payment_method
                    else "Test Payment Successful"
                )


                order = {

                    "Order ID":
                        order_id,

                    "Item":
                        item["item"],

                    "Type":
                        item["type"],

                    "Amount":
                        total,

                    "Payment":
                        payment_status,

                    "Delivery":
                        delivery_option,

                    "Status":
                        "Confirmed"
                }


                st.session_state.orders.append(
                    order
                )


                st.session_state.points += 10


                st.success(
                    "✅ Order Confirmed!"
                )


                st.balloons()


                st.markdown(
                    f"**Order ID:** `{order_id}`"
                )


                st.write(
                    f"Payment: "
                    f"**{payment_status}**"
                )


                st.write(
                    f"Total: "
                    f"**₹{total}**"
                )


                st.info(
                    "⭐ You earned 10 IBeX Points."
                )


                st.caption(
                    "Prototype transaction — "
                    "no real payment has been processed."
                )


# ============================================================
# ORDERS / CART
# ============================================================

elif st.session_state.current_page == "Orders":

    st.markdown(
        '<div class="section-title">🛒 My Orders</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Your confirmed rentals and purchases.'
        '</div>',
        unsafe_allow_html=True
    )


    if len(st.session_state.orders) == 0:

        st.info(
            "You haven't placed an order yet."
        )


        if st.button(
            "Browse Marketplace"
        ):

            st.session_state.current_page = "Marketplace"

            st.rerun()


    else:

        for order in reversed(
            st.session_state.orders
        ):

            st.markdown(
                f"""
                <div class="info-card">

                    <h3>{order['Item']}</h3>

                    <b>Order ID:</b>
                    {order['Order ID']}
                    <br><br>

                    <b>Amount:</b>
                    ₹{order['Amount']}
                    <br>

                    <b>Payment:</b>
                    {order['Payment']}
                    <br>

                    <b>Delivery:</b>
                    {order['Delivery']}
                    <br>

                    <b>Status:</b>
                    {order['Status']}

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# SERVICES
# ============================================================

elif st.session_state.current_page == "Services":

    st.markdown(
        '<div class="section-title">Campus Services</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Request convenience or earn by helping another student.'
        '</div>',
        unsafe_allow_html=True
    )


    service_tab1, service_tab2, service_tab3 = st.tabs(
        [
            "🚚 Delivery & Pickup",
            "🤝 Help Someone",
            "🏥 Essential Assistance"
        ]
    )


    # --------------------------------------------------------
    # DELIVERY
    # --------------------------------------------------------

    with service_tab1:

        request_type = st.selectbox(
            "Service Type",
            [
                "Parcel Pickup",
                "Item Pickup",
                "Document Delivery",
                "Food / Snack Pickup",
                "Other Assistance"
            ]
        )


        pickup = st.text_input(
            "Pickup Location",
            placeholder="Example: IBS Main Gate"
        )


        drop_option = st.selectbox(
            "Delivery Location",
            HOSTEL_BLOCKS
            + [
                "Other / Enter Manually"
            ]
        )


        if (
            drop_option
            == "Other / Enter Manually"
        ):

            drop = st.text_input(
                "Enter Delivery Location"
            )

        else:

            drop = drop_option


        helper_fee = st.number_input(
            "Helper Reward (₹)",
            min_value=10,
            max_value=200,
            value=20
        )


        if st.button(
            "Post Delivery Request"
        ):

            if not pickup.strip():

                st.warning(
                    "Enter the pickup location."
                )


            elif not drop.strip():

                st.warning(
                    "Enter the delivery location."
                )


            else:

                request = {

                    "Task":
                        request_type,

                    "Pickup":
                        pickup,

                    "Drop":
                        drop,

                    "Reward":
                        helper_fee,

                    "Status":
                        "Open"
                }


                st.session_state.help_requests.append(
                    request
                )


                st.success(
                    "✅ Your request is now visible "
                    "to verified IBeX helpers."
                )


    # --------------------------------------------------------
    # HELP SOMEONE
    # --------------------------------------------------------

    with service_tab2:

        sample_tasks = [

            {
                "Task":
                    "Parcel Pickup",

                "Pickup":
                    "IBS Main Gate",

                "Drop":
                    "ABCD Block",

                "Reward":
                    20
            },

            {
                "Task":
                    "Snack Pickup",

                "Pickup":
                    "Campus Store",

                "Drop":
                    "QRS Block",

                "Reward":
                    15
            }

        ]


        all_tasks = (
            sample_tasks
            + st.session_state.help_requests
        )


        for index, task in enumerate(
            all_tasks
        ):

            st.markdown(
                f"""
                <div class="info-card">

                    <span class="badge-help">
                        ESSENTIAL HELP
                    </span>

                    <br><br>

                    <h3>
                        {task['Task']}
                    </h3>

                    📍
                    {task['Pickup']}
                    →
                    {task['Drop']}

                    <br><br>

                    💰 Reward:
                    <b>₹{task['Reward']}</b>

                </div>
                """,
                unsafe_allow_html=True
            )


            if st.button(
                "Accept Task",
                key=f"accept_task_{index}"
            ):

                st.session_state.points += 30


                st.success(
                    "✅ Task accepted!"
                )


                st.info(
                    "⭐ 30 IBeX Points added "
                    "in prototype mode."
                )


    # --------------------------------------------------------
    # ESSENTIAL ASSISTANCE
    # --------------------------------------------------------

    with service_tab3:

        st.markdown("""
        <div class="warning-box">

            IBeX supports basic campus assistance.
            Prescription medicines and regulated medical
            products would require appropriate institutional
            and legal controls in a live implementation.

        </div>
        """, unsafe_allow_html=True)


        st.write("")


        essential_need = st.selectbox(
            "What do you need?",
            [
                "Sanitary products",
                "ORS / hydration supplies",
                "Bandage / basic first aid",
                "Thermometer",
                "Basic essential item",
                "Help reaching campus medical support"
            ]
        )


        urgency = st.radio(
            "Urgency",
            [
                "Normal",
                "Urgent"
            ]
        )


        essential_reward = st.number_input(
            "Helper Reward (₹)",
            min_value=0,
            max_value=200,
            value=20
        )


        if st.button(
            "Request Essential Assistance"
        ):

            st.success(
                f"✅ Request posted for "
                f"{essential_need}."
            )


            st.info(
                "Only verified IBS users can respond."
            )


# ============================================================
# COMMUNITY
# ============================================================

elif st.session_state.current_page == "Community":

    st.markdown(
        '<div class="section-title">IBeX Community</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Trust, rewards and accountability make the platform work.'
        '</div>',
        unsafe_allow_html=True
    )


    community1, community2, community3 = st.columns(3)


    with community1:

        st.markdown(
            f"""
            <div class="metric-pill">

                <div class="metric-value">
                    {st.session_state.points}
                </div>

                <div class="metric-label">
                    Your IBeX Points
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    with community2:

        st.markdown("""
        <div class="metric-pill">

            <div class="metric-value">
                4.8 ⭐
            </div>

            <div class="metric-label">
                User Rating
            </div>

        </div>
        """, unsafe_allow_html=True)


    with community3:

        st.markdown("""
        <div class="metric-pill">

            <div class="metric-value">
                Trusted
            </div>

            <div class="metric-label">
                Community Status
            </div>

        </div>
        """, unsafe_allow_html=True)


    # --------------------------------------------------------
    # POINT SYSTEM
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Earn IBeX Points</div>',
        unsafe_allow_html=True
    )


    rewards_df = pd.DataFrame(
        {

            "Activity": [

                "Successful Purchase / Rental",

                "Complete Parcel Pickup",

                "Help with Essential Request",

                "Successful Lending",

                "Return Rental On Time",

                "Positive Review"
            ],

            "Points": [

                "+10",

                "+30",

                "+40",

                "+20",

                "+30",

                "+10"
            ]

        }
    )


    st.dataframe(
        rewards_df,
        use_container_width=True,
        hide_index=True
    )


    st.markdown(
        '<div class="section-title">Redeem Rewards</div>',
        unsafe_allow_html=True
    )


    reward_choice = st.selectbox(
        "Choose a Reward",
        [
            "₹20 Delivery Discount — 500 Points",
            "1 Free Listing — 750 Points",
            "Priority Listing — 1000 Points"
        ]
    )


    if st.button(
        "Redeem Reward"
    ):

        st.info(
            "Prototype demonstration: "
            "the reward would be applied "
            "to the user's account."
        )


    # --------------------------------------------------------
    # TRUST
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Built Around Trust</div>',
        unsafe_allow_html=True
    )


    trust1, trust2, trust3 = st.columns(3)


    with trust1:

        st.markdown("""
        <div class="info-card">

            <h3>🔒 IBS Verification</h3>

            Every account is designed to belong
            to the verified IBS community.

        </div>
        """, unsafe_allow_html=True)


    with trust2:

        st.markdown("""
        <div class="info-card">

            <h3>⭐ Ratings & Reviews</h3>

            Transaction history and feedback help
            students identify reliable users.

        </div>
        """, unsafe_allow_html=True)


    with trust3:

        st.markdown("""
        <div class="info-card">

            <h3>🔐 Secure Transactions</h3>

            Deposits, OTP handovers and secure
            payments improve accountability.

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# PROFILE
# ============================================================

elif st.session_state.current_page == "Profile":

    st.markdown(
        '<div class="section-title">My IBeX Profile</div>',
        unsafe_allow_html=True
    )


    profile_left, profile_right = st.columns(
        [1, 1.6]
    )


    with profile_left:

        st.markdown("""
        <div class="info-card">

            <div class="profile-avatar">
                👤
            </div>

            <br>

            <h2>
                IBX Student 001
            </h2>

            <div class="verified-text">
                ✓ IBS Verified Profile
            </div>

            <br>

            ⭐ 4.8 Rating
            <br>

            🔄 16 Successful Transactions
            <br>

            🏆 Trusted Community Member

        </div>
        """, unsafe_allow_html=True)


        st.metric(
            "IBeX Points",
            st.session_state.points
        )


    with profile_right:

        st.markdown(
            "### Trust & Privacy"
        )


        st.write(
            "✅ IBS-only verified access"
        )

        st.write(
            "✅ Masked user identity before transaction"
        )

        st.write(
            "✅ Ratings and reviews"
        )

        st.write(
            "✅ OTP-based handover verification"
        )

        st.write(
            "✅ Refundable rental security deposit"
        )

        st.write(
            "✅ Secure payment processing"
        )

        st.write(
            "✅ Payment information hidden from other users"
        )

        st.write(
            "✅ Community accountability"
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    <b>IBeX — Campus Marketplace</b>

    <br>

    Secure • Sustainable • Community Driven

    <br><br>

    Prototype developed for Managing Platform Business

</div>
""", unsafe_allow_html=True)
