
import streamlit as st
import pandas as pd
import uuid
from datetime import datetime


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="IBeX | Campus Marketplace",
    page_icon="🔄",
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
    background-color: #F8FAFC;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.block-container {
    padding-top: 1.2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

header[data-testid="stHeader"] {
    background: transparent;
}

section[data-testid="stSidebar"] {
    display: none;
}


/* ==========================================================
   BRAND
   ========================================================== */

.brand-logo {
    font-size: 2.15rem;
    font-weight: 850;
    color: #5B2C83;
    line-height: 1;
    margin-bottom: 3px;
}

.brand-tagline {
    font-size: 0.78rem;
    color: #64748B;
    letter-spacing: 0.04em;
    font-weight: 500;
}


/* ==========================================================
   HERO
   ========================================================== */

.hero-glass {
    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.95),
            rgba(248,245,255,0.88)
        );
    border: 1px solid #E2E8F0;
    border-radius: 24px;
    padding: 3rem 3.2rem;
    margin-top: 1.2rem;
    margin-bottom: 1.3rem;
    box-shadow: 0px 15px 45px rgba(91, 44, 131, 0.08);
}

.hero-title {
    font-size: 3.25rem;
    font-weight: 850;
    color: #111827;
    line-height: 1.08;
    margin-bottom: 0.8rem;
}

.hero-highlight {
    color: #6A359C;
}

.hero-text {
    font-size: 1.08rem;
    color: #64748B;
    max-width: 760px;
    line-height: 1.7;
}


/* ==========================================================
   TRUST PILLS
   ========================================================== */

.trust-row {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    margin-top: 1.4rem;
}

.trust-pill {
    display: inline-block;
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 100px;
    padding: 8px 14px;
    font-size: 0.85rem;
    font-weight: 650;
    color: #334155;
}


/* ==========================================================
   METRIC PILLS
   ========================================================== */

.metric-pill {
    background: rgba(255,255,255,0.92);
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 16px;
    text-align: center;
    box-shadow: 0px 5px 18px rgba(15,23,42,0.04);
}

.metric-number {
    font-size: 1.55rem;
    font-weight: 800;
    color: #5B2C83;
}

.metric-label {
    font-size: 0.80rem;
    color: #64748B;
    margin-top: 2px;
}


/* ==========================================================
   SECTION TITLES
   ========================================================== */

.section-title {
    font-size: 1.7rem;
    font-weight: 800;
    color: #111827;
    margin-top: 1.7rem;
    margin-bottom: 0.3rem;
}

.section-subtitle {
    font-size: 0.95rem;
    color: #64748B;
    margin-bottom: 1.2rem;
}


/* ==========================================================
   PRODUCT CARDS
   ========================================================== */

.product-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 1.15rem;
    min-height: 300px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    box-shadow: 0 4px 12px rgba(15,23,42,0.025);
}

.product-card:hover {
    transform: translateY(-4px);
    box-shadow: 0px 12px 28px rgba(15,23,42,0.08);
}

.product-image {
    background: linear-gradient(135deg,#F3E8FF,#F8FAFC);
    height: 115px;
    border-radius: 12px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 3.4rem;
    margin-bottom: 1rem;
}

.product-name {
    color: #111827;
    font-size: 1.05rem;
    font-weight: 750;
    margin-top: 8px;
    margin-bottom: 5px;
}

.product-price {
    color: #111827;
    font-size: 1.35rem;
    font-weight: 850;
    margin-top: 8px;
}

.product-meta {
    color: #64748B;
    font-size: 0.78rem;
    line-height: 1.6;
}

.verified {
    color: #15803D;
    font-size: 0.78rem;
    font-weight: 700;
}


/* ==========================================================
   BADGES
   ========================================================== */

.badge-rent {
    background-color: #E0F2FE;
    color: #0369A1;
    font-weight: 700;
    padding: 5px 9px;
    border-radius: 6px;
    font-size: 0.70rem;
}

.badge-sale {
    background-color: #DCFCE7;
    color: #166534;
    font-weight: 700;
    padding: 5px 9px;
    border-radius: 6px;
    font-size: 0.70rem;
}

.badge-help {
    background-color: #FEE2E2;
    color: #B91C1C;
    font-weight: 700;
    padding: 5px 9px;
    border-radius: 6px;
    font-size: 0.70rem;
}


/* ==========================================================
   STEP CARDS
   ========================================================== */

.step-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 1.35rem;
    min-height: 185px;
}

.step-number {
    width: 34px;
    height: 34px;
    border-radius: 50%;
    background: #6A359C;
    color: white;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 12px;
}

.step-title {
    color: #111827;
    font-size: 1rem;
    font-weight: 750;
}

.step-text {
    color: #64748B;
    font-size: 0.85rem;
    line-height: 1.6;
}


/* ==========================================================
   GENERIC CARDS
   ========================================================== */

.info-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 1.3rem;
    box-shadow: 0 4px 12px rgba(15,23,42,0.03);
}

.secure-box {
    background: #F0FDF4;
    border: 1px solid #BBF7D0;
    border-radius: 12px;
    padding: 1rem;
    color: #166534;
}

.warning-box {
    background: #FFF7ED;
    border: 1px solid #FED7AA;
    border-radius: 12px;
    padding: 1rem;
    color: #9A3412;
}


/* ==========================================================
   BUTTONS
   ========================================================== */

div.stButton > button {
    border-radius: 10px;
    border: 1px solid #E2E8F0;
    font-weight: 650;
    transition: 0.2s;
}

div.stButton > button:hover {
    border-color: #6A359C;
    color: #6A359C;
}


/* ==========================================================
   INPUTS
   ========================================================== */

div[data-baseweb="select"] > div {
    border-radius: 10px;
}

div[data-testid="stTextInput"] input {
    border-radius: 10px;
}


/* ==========================================================
   FOOTER
   ========================================================== */

.footer {
    text-align: center;
    color: #94A3B8;
    font-size: 0.8rem;
    padding-top: 2rem;
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
# NAVIGATION FUNCTION
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
# PRODUCT EMOJIS
# ============================================================

CATEGORY_EMOJIS = {
    "Academic": "📚",
    "Fashion": "👗",
    "Personal Care": "✨",
    "Hostel Utility": "🏠",
    "Electronics": "🔌",
    "Sports": "🏸",
    "Bags": "🎒",
    "Event / Function": "🎉",
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
# TOP HEADER
# ============================================================

header = st.columns([2.2, 1, 1, 1, 1, 1.25, 1.25, 1.3])


with header[0]:

    st.markdown("""
    <div>
        <div class="brand-logo">IBeX</div>
        <div class="brand-tagline">Campus Marketplace</div>
    </div>
    """, unsafe_allow_html=True)


with header[1]:

    st.button(
        "Home",
        use_container_width=True,
        on_click=navigate,
        args=("Home",)
    )


with header[2]:

    st.button(
        "Marketplace",
        use_container_width=True,
        on_click=navigate,
        args=("Marketplace",)
    )


with header[3]:

    st.button(
        "Services",
        use_container_width=True,
        on_click=navigate,
        args=("Services",)
    )


with header[4]:

    st.button(
        "Community",
        use_container_width=True,
        on_click=navigate,
        args=("Community",)
    )


with header[5]:

    st.button(
        "＋ List Item",
        use_container_width=True,
        on_click=navigate,
        args=("List Item",)
    )


with header[6]:

    st.button(
        f"🛒 Orders ({len(st.session_state.orders)})",
        use_container_width=True,
        on_click=navigate,
        args=("Orders",)
    )


with header[7]:

    st.button(
        f"👤 {st.session_state.points} Pts",
        use_container_width=True,
        on_click=navigate,
        args=("Profile",)
    )


st.divider()


# ============================================================
# HOME PAGE
# ============================================================

if st.session_state.current_page == "Home":

    # HERO

    st.markdown("""
    <div class="hero-glass">

        <div class="hero-title">
            Campus life made
            <span class="hero-highlight">simpler.</span>
        </div>

        <div class="hero-text">
            Rent what you need, buy second-hand, earn from unused
            products, request campus help and reward students who
            make the community work — all within a verified IBS network.
        </div>

        <div class="trust-row">
            <div class="trust-pill">🔒 IBS Verified</div>
            <div class="trust-pill">⚡ Campus Pickup</div>
            <div class="trust-pill">🌱 Reuse & Reduce Waste</div>
            <div class="trust-pill">⭐ Reward-Based Community</div>
        </div>

    </div>
    """, unsafe_allow_html=True)


    # ========================================================
    # LIVE IMPACT METRICS
    # ========================================================

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.markdown(
            f"""
            <div class="metric-pill">
                <div class="metric-number">
                    {len(marketplace_data)}
                </div>
                <div class="metric-label">
                    Active Listings
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with m2:
        st.markdown(
            f"""
            <div class="metric-pill">
                <div class="metric-number">
                    {st.session_state.points}
                </div>
                <div class="metric-label">
                    Your IBeX Points
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with m3:
        st.markdown(
            """
            <div class="metric-pill">
                <div class="metric-number">
                    100%
                </div>
                <div class="metric-label">
                    Student Verified
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with m4:
        st.markdown(
            f"""
            <div class="metric-pill">
                <div class="metric-number">
                    {len(st.session_state.orders)}
                </div>
                <div class="metric-label">
                    Your Orders
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # FEATURED ITEMS
    # ========================================================

    st.markdown(
        '<div class="section-title">Featured on IBeX</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Explore useful items currently available within the community.'
        '</div>',
        unsafe_allow_html=True
    )


    featured_items = marketplace_data[:4]

    product_cols = st.columns(4)


    for i, item in enumerate(featured_items):

        with product_cols[i]:

            emoji = CATEGORY_EMOJIS.get(
                item["category"],
                "📦"
            )

            badge_class = (
                "badge-rent"
                if item["type"] == "Rent"
                else "badge-sale"
            )

            badge_text = (
                "FOR RENT"
                if item["type"] == "Rent"
                else "FOR SALE"
            )

            if item["type"] == "Rent":

                price_display = (
                    f"₹{item['price']}/day"
                )

            else:

                price_display = (
                    f"₹{item['price']}"
                )


            st.markdown(
                f"""
                <div class="product-card">

                    <div class="product-image">
                        {emoji}
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
                        {item['condition']} condition
                        <br>
                        📍 {item['location']}
                    </div>

                    <br>

                    <div class="verified">
                        ✓ IBS Verified
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


            if st.button(
                "View Item",
                key=f"featured_{item['id']}",
                use_container_width=True
            ):

                st.session_state.selected_item = item
                st.session_state.current_page = "Checkout"
                st.rerun()


    # ========================================================
    # HOW IT WORKS
    # ========================================================

    st.markdown(
        '<div class="section-title">How IBeX Works</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'A simple trusted workflow designed specifically for campus.'
        '</div>',
        unsafe_allow_html=True
    )


    step1, step2, step3, step4 = st.columns(4)


    with step1:

        st.markdown("""
        <div class="step-card">

            <div class="step-number">1</div>

            <div class="step-title">
                Browse & Select
            </div>

            <div class="step-text">
                Search products, compare rental or sale options
                and choose what you need.
            </div>

        </div>
        """, unsafe_allow_html=True)


    with step2:

        st.markdown("""
        <div class="step-card">

            <div class="step-number">2</div>

            <div class="step-title">
                Connect & Verify
            </div>

            <div class="step-text">
                Interact only with verified IBS students and
                review trust ratings.
            </div>

        </div>
        """, unsafe_allow_html=True)


    with step3:

        st.markdown("""
        <div class="step-card">

            <div class="step-number">3</div>

            <div class="step-title">
                Pickup / Delivery
            </div>

            <div class="step-text">
                Collect the item yourself or request convenient
                campus delivery.
            </div>

        </div>
        """, unsafe_allow_html=True)


    with step4:

        st.markdown("""
        <div class="step-card">

            <div class="step-number">4</div>

            <div class="step-title">
                Earn Rewards
            </div>

            <div class="step-text">
                Complete transactions and help students to earn
                IBeX reward points.
            </div>

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


    search_col, cat_col, type_col = st.columns(
        [2.2, 1.3, 1.3]
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


    with cat_col:

        category_filter = st.selectbox(
            "Category",
            ["All"] + categories
        )


    with type_col:

        type_filter = st.selectbox(
            "Listing Type",
            ["All", "Buy", "Rent"]
        )


    filtered = marketplace_data.copy()


    if search:

        filtered = [
            item
            for item in filtered
            if search.lower() in item["item"].lower()
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


    st.write(
        f"**{len(filtered)} listings found**"
    )


    if len(filtered) == 0:

        st.info(
            "No items match your current filters."
        )

    else:

        # Product grid: 3 columns

        for start in range(0, len(filtered), 3):

            cols = st.columns(3)

            row_items = filtered[
                start:start + 3
            ]

            for index, item in enumerate(row_items):

                with cols[index]:

                    emoji = CATEGORY_EMOJIS.get(
                        item["category"],
                        "📦"
                    )

                    badge_class = (
                        "badge-rent"
                        if item["type"] == "Rent"
                        else "badge-sale"
                    )

                    badge_text = (
                        "FOR RENT"
                        if item["type"] == "Rent"
                        else "FOR SALE"
                    )


                    if item["type"] == "Rent":

                        price_display = (
                            f"₹{item['price']}/day"
                        )

                        secondary_price = (
                            f"₹{item['deposit']} refundable deposit"
                        )

                    else:

                        price_display = (
                            f"₹{item['price']}"
                        )

                        secondary_price = (
                            "Second-hand purchase"
                        )


                    st.markdown(
                        f"""
                        <div class="product-card">

                            <div class="product-image">
                                {emoji}
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
                                {secondary_price}
                                <br>
                                Condition: {item['condition']}
                                <br>
                                📍 {item['location']}
                                <br>
                                ⭐ {item['rating']} •
                                {item['transactions']} transactions
                            </div>

                            <br>

                            <div class="verified">
                                ✓ Verified IBS Student
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                    action_text = (
                        "Quick Rent"
                        if item["type"] == "Rent"
                        else "Buy Now"
                    )


                    if st.button(
                        action_text,
                        key=f"product_{item['id']}",
                        use_container_width=True
                    ):

                        st.session_state.selected_item = item

                        st.session_state.current_page = "Checkout"

                        st.rerun()


# ============================================================
# LIST ITEM
# ============================================================

elif st.session_state.current_page == "List Item":

    st.markdown(
        '<div class="section-title">List an Item</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Sell something you no longer use or earn by lending it.'
        '</div>',
        unsafe_allow_html=True
    )


    st.info(
        "IBeX Freemium: initial listings are free. "
        "Higher-volume sellers can later upgrade to listing plans."
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
            "Listing Type",
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
            + ["Other / Enter Manually"]
        )


        if location_option == "Other / Enter Manually":

            location = st.text_input(
                "Enter Location",
                placeholder="Enter hostel / block"
            )

        else:

            location = location_option


    description = st.text_area(
        "Description",
        placeholder=(
            "Add size, condition, accessories, "
            "usage details or anything the buyer/renter should know."
        )
    )


    if st.button(
        "Publish Listing",
        type="primary"
    ):

        if not item_name.strip():

            st.warning(
                "Please enter the item name."
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
                        if listing_type == "Lend / Rent"
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
                f"✅ {item_name} is now listed on IBeX!"
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
            "Select an item from the marketplace first."
        )

        st.button(
            "Go to Marketplace",
            on_click=navigate,
            args=("Marketplace",)
        )


    else:

        product_col, checkout_col = st.columns(
            [1.1, 1.5]
        )


        # ====================================================
        # ITEM DETAILS
        # ====================================================

        with product_col:

            emoji = CATEGORY_EMOJIS.get(
                item["category"],
                "📦"
            )


            st.markdown(
                f"""
                <div class="product-card">

                    <div class="product-image">
                        {emoji}
                    </div>

                    <div class="product-name">
                        {item['item']}
                    </div>

                    <div class="product-meta">
                        Condition: {item['condition']}
                        <br>
                        📍 {item['location']}
                        <br>
                        ⭐ {item['rating']} rating
                    </div>

                    <br>

                    <div class="verified">
                        ✓ Verified IBS Seller
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


        # ====================================================
        # CHECKOUT FORM
        # ====================================================

        with checkout_col:

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
                "Delivery",
                [
                    "Self Pickup — FREE",
                    "IBeX Campus Delivery — ₹20"
                ]
            )


            delivery_fee = (
                20
                if "₹20" in delivery_option
                else 0
            )


            total = (
                base_price
                + deposit
                + delivery_fee
            )


            st.markdown("### Order Summary")


            if item["type"] == "Rent":

                st.write(
                    f"Rental ({days} day(s)): "
                    f"**₹{base_price}**"
                )

                st.write(
                    f"Refundable Security Deposit: "
                    f"**₹{deposit}**"
                )

            else:

                st.write(
                    f"Product Price: "
                    f"**₹{base_price}**"
                )


            st.write(
                f"Delivery: **₹{delivery_fee}**"
            )


            st.divider()


            st.markdown(
                f"## Total: ₹{total}"
            )


            if item["type"] == "Rent":

                st.success(
                    f"₹{deposit} is refundable after "
                    "the item is safely returned."
                )


            # =================================================
            # PAYMENT
            # =================================================

            st.markdown("### Payment Method")


            payment_method = st.radio(
                "Select Payment",
                [
                    "📱 UPI / GPay / PhonePe",
                    "💳 Card",
                    "💵 Cash on Delivery"
                ]
            )


            if "UPI" in payment_method:

                st.markdown("""
                <div class="secure-box">
                    🔐 <b>Secure UPI Checkout</b><br><br>
                    In the live platform, payment is processed by
                    an authorised gateway. Payment credentials are
                    never shown to another IBeX user.
                </div>
                """, unsafe_allow_html=True)


                st.text_input(
                    "Prototype UPI ID",
                    placeholder="••••••@upi",
                    type="password"
                )


                st.caption(
                    "Prototype mode — no real money is transferred."
                )


            elif "Card" in payment_method:

                st.markdown("""
                <div class="secure-box">
                    🔐 <b>Secure Card Checkout</b><br><br>
                    In production, card details would be captured
                    and processed directly by the payment gateway.
                </div>
                """, unsafe_allow_html=True)


                st.caption(
                    "No actual card information is required "
                    "for this prototype."
                )


            else:

                st.markdown("""
                <div class="secure-box">
                    💵 <b>Cash on Delivery</b><br><br>
                    Pay when the item is handed over.
                </div>
                """, unsafe_allow_html=True)


            if "Cash" in payment_method:

                payment_button = (
                    f"Confirm COD — ₹{total}"
                )

            else:

                payment_button = (
                    f"Secure Test Payment — ₹{total}"
                )


            if st.button(
                payment_button,
                type="primary",
                use_container_width=True
            ):

                order_id = (
                    "IBX-"
                    + datetime.now().strftime("%y%m%d")
                    + "-"
                    + str(uuid.uuid4())[:6].upper()
                )


                if "Cash" in payment_method:

                    payment_status = "Cash on Delivery"

                else:

                    payment_status = "Test Payment Successful"


                order = {

                    "Order ID": order_id,

                    "Item": item["item"],

                    "Type": item["type"],

                    "Amount": total,

                    "Payment": payment_status,

                    "Delivery": delivery_option,

                    "Status": "Confirmed"
                }


                st.session_state.orders.append(
                    order
                )

                st.session_state.points += 10


                st.success(
                    "✅ Order confirmed!"
                )

                st.balloons()


                st.markdown(
                    f"**Order ID:** `{order_id}`"
                )

                st.write(
                    f"Payment: **{payment_status}**"
                )

                st.write(
                    f"Total: **₹{total}**"
                )

                st.info(
                    "⭐ You earned 10 IBeX Points."
                )

                st.caption(
                    "Prototype transaction. "
                    "No real payment has been processed."
                )


# ============================================================
# ORDERS
# ============================================================

elif st.session_state.current_page == "Orders":

    st.markdown(
        '<div class="section-title">My Orders</div>',
        unsafe_allow_html=True
    )


    if len(st.session_state.orders) == 0:

        st.info(
            "You haven't placed any orders yet."
        )


    else:

        for order in reversed(
            st.session_state.orders
        ):

            st.markdown(
                f"""
                <div class="info-card">

                    <b>{order['Item']}</b>

                    <br><br>

                    🆔 {order['Order ID']}
                    <br>
                    💰 ₹{order['Amount']}
                    <br>
                    💳 {order['Payment']}
                    <br>
                    🚚 {order['Delivery']}
                    <br>
                    ✅ {order['Status']}

                </div>
                <br>
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
        'Request help or earn by assisting another IBS student.'
        '</div>',
        unsafe_allow_html=True
    )


    tab1, tab2, tab3 = st.tabs(
        [
            "🚚 Request Delivery",
            "🤝 Help Someone",
            "🏥 Essential Assistance"
        ]
    )


    # ========================================================
    # DELIVERY REQUEST
    # ========================================================

    with tab1:

        request_type = st.selectbox(
            "Service",
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
            + ["Other / Enter Manually"]
        )


        if drop_option == "Other / Enter Manually":

            drop = st.text_input(
                "Enter Delivery Location"
            )

        else:

            drop = drop_option


        fee = st.number_input(
            "Helper Reward (₹)",
            min_value=10,
            max_value=200,
            value=20
        )


        if st.button(
            "Post Request"
        ):

            if not pickup.strip():

                st.warning(
                    "Please enter the pickup location."
                )


            elif not drop.strip():

                st.warning(
                    "Please enter the delivery location."
                )


            else:

                request = {

                    "Task": request_type,

                    "Pickup": pickup,

                    "Drop": drop,

                    "Reward": fee,

                    "Status": "Open"
                }


                st.session_state.help_requests.append(
                    request
                )


                st.success(
                    "✅ Your request is now visible "
                    "to verified IBeX helpers."
                )


    # ========================================================
    # HELP SOMEONE
    # ========================================================

    with tab2:

        sample_tasks = [

            {
                "Task": "Parcel Pickup",
                "Pickup": "IBS Main Gate",
                "Drop": "ABCD Block",
                "Reward": 20
            },

            {
                "Task": "Snack Pickup",
                "Pickup": "Campus Store",
                "Drop": "QRS Block",
                "Reward": 15
            }

        ]


        all_tasks = (
            sample_tasks
            + st.session_state.help_requests
        )


        for i, task in enumerate(all_tasks):

            st.markdown(
                f"""
                <div class="info-card">

                    <span class="badge-help">
                        OPEN REQUEST
                    </span>

                    <br><br>

                    <b>{task['Task']}</b>

                    <br><br>

                    📍 {task['Pickup']}
                    → {task['Drop']}

                    <br>

                    💰 Reward:
                    <b>₹{task['Reward']}</b>

                </div>
                """,
                unsafe_allow_html=True
            )


            if st.button(
                "Accept Task",
                key=f"service_task_{i}"
            ):

                st.session_state.points += 30

                st.success(
                    "Task accepted!"
                )

                st.info(
                    "⭐ 30 IBeX Points earned "
                    "in prototype mode."
                )


            st.write("")


    # ========================================================
    # ESSENTIAL HELP
    # ========================================================

    with tab3:

        st.markdown("""
        <div class="warning-box">
            IBeX supports basic campus assistance.
            Prescription medicines and regulated products
            would require appropriate institutional and
            legal controls in a live implementation.
        </div>
        """, unsafe_allow_html=True)


        st.write("")


        need = st.selectbox(
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


        helper_reward = st.number_input(
            "Helper Reward (₹)",
            min_value=0,
            max_value=200,
            value=20
        )


        if st.button(
            "Request Assistance"
        ):

            st.success(
                f"✅ Request posted for {need}."
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
        'Help others, build trust and earn rewards.'
        '</div>',
        unsafe_allow_html=True
    )


    c1, c2, c3 = st.columns(3)


    with c1:

        st.markdown(
            f"""
            <div class="metric-pill">
                <div class="metric-number">
                    {st.session_state.points}
                </div>
                <div class="metric-label">
                    Your Points
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with c2:

        st.markdown("""
        <div class="metric-pill">
            <div class="metric-number">
                4.8 ⭐
            </div>
            <div class="metric-label">
                Community Rating
            </div>
        </div>
        """, unsafe_allow_html=True)


    with c3:

        st.markdown("""
        <div class="metric-pill">
            <div class="metric-number">
                Trusted
            </div>
            <div class="metric-label">
                Member Status
            </div>
        </div>
        """, unsafe_allow_html=True)


    st.markdown(
        '<div class="section-title">Earn Points</div>',
        unsafe_allow_html=True
    )


    points_df = pd.DataFrame({

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

    })


    st.dataframe(
        points_df,
        use_container_width=True,
        hide_index=True
    )


    st.markdown(
        '<div class="section-title">Redeem Rewards</div>',
        unsafe_allow_html=True
    )


    reward_choice = st.selectbox(
        "Choose Reward",
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
            "the selected benefit would be "
            "applied to the user's account."
        )


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

            <div style="
                width:75px;
                height:75px;
                background:#EDE9FE;
                border-radius:50%;
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:2rem;
                margin-bottom:15px;
            ">
                👤
            </div>

            <h3>IBX Student 001</h3>

            <div class="verified">
                ✓ IBS Verified
            </div>

            <br>

            ⭐ 4.8 Rating

            <br>

            🔄 16 Successful Transactions

            <br>

            🏆 Trusted Member

        </div>
        """, unsafe_allow_html=True)


    with profile_right:

        st.markdown("### Trust & Privacy")

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
            "✅ Refundable rental security deposits"
        )

        st.write(
            "✅ Secure payment processing"
        )

        st.write(
            "✅ Payment details hidden from other users"
        )

        st.write(
            "✅ Community accountability"
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown("""
<div class="footer">
    IBeX — IBS Exchange • Campus Marketplace Prototype
    <br>
    Secure • Sustainable • Community Driven
</div>
""", unsafe_allow_html=True)
