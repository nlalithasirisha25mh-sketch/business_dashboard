import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# IBeX - Campus Marketplace Prototype
# Managing Platform Business Project | IFHE Hyderabad
# ============================================================

st.set_page_config(
    page_title="IBeX | Campus Marketplace",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# SESSION STATE
# ============================================================

if "nav" not in st.session_state:
    st.session_state.nav = "Home"

if "cart" not in st.session_state:
    st.session_state.cart = []

if "points" not in st.session_state:
    st.session_state.points = 245

if "orders" not in st.session_state:
    st.session_state.orders = []

if "selected_item" not in st.session_state:
    st.session_state.selected_item = None

if "checkout" not in st.session_state:
    st.session_state.checkout = False

if "listing_submitted" not in st.session_state:
    st.session_state.listing_submitted = False


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background: #F8FAFC;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        color: #1E293B;
    }

    .main .block-container {
        max-width: 1500px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    /* ---------- TOP HEADER ---------- */

    .brand-name {
        font-size: 2.35rem;
        font-weight: 800;
        color: #5630A8;
        line-height: 1;
        margin-bottom: 4px;
    }

    .brand-tagline {
        font-size: 0.88rem;
        color: #64748B;
        font-weight: 500;
        letter-spacing: 0.2px;
    }

    .points-pill {
        background: #F1EAFE;
        border: 1px solid #DDD0FA;
        border-radius: 14px;
        padding: 10px 16px;
        text-align: center;
        color: #5630A8;
        font-weight: 700;
    }

    .header-line {
        border-bottom: 1px solid #E2E8F0;
        margin-top: 16px;
        margin-bottom: 30px;
    }

    /* ---------- BUTTONS ---------- */

    .stButton > button {
        border-radius: 11px;
        border: 1px solid #E2E8F0;
        background: #FFFFFF;
        color: #334155;
        font-weight: 600;
        min-height: 42px;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #8B5CF6;
        color: #5630A8;
        transform: translateY(-1px);
    }

    /* ---------- HERO ---------- */

    .hero {
        background: linear-gradient(135deg, #FFFFFF 0%, #F7F2FF 100%);
        border: 1px solid #E2E8F0;
        border-radius: 24px;
        padding: 42px 46px;
        margin-bottom: 22px;
        box-shadow: 0 10px 35px rgba(86, 48, 168, 0.06);
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        color: #172033;
        line-height: 1.12;
        margin-bottom: 14px;
    }

    .hero-highlight {
        color: #6D3CC8;
    }

    .hero-text {
        font-size: 1.08rem;
        color: #64748B;
        max-width: 800px;
        line-height: 1.7;
        margin-bottom: 20px;
    }

    /* ---------- TRUST PILLS ---------- */

    .trust-row {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        margin-top: 15px;
    }

    .trust-pill {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 999px;
        padding: 8px 14px;
        color: #475569;
        font-size: 0.88rem;
        font-weight: 600;
    }

    /* ---------- IMPACT METRICS ---------- */

    .metric-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 15px;
        padding: 18px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(15, 23, 42, 0.03);
    }

    .metric-number {
        font-size: 1.65rem;
        font-weight: 800;
        color: #5630A8;
    }

    .metric-label {
        font-size: 0.82rem;
        color: #64748B;
        margin-top: 3px;
    }

    /* ---------- SECTION TITLES ---------- */

    .section-title {
        font-size: 1.55rem;
        font-weight: 750;
        color: #172033;
        margin-top: 20px;
        margin-bottom: 5px;
    }

    .section-subtitle {
        color: #64748B;
        margin-bottom: 20px;
    }

    /* ---------- PRODUCT CARDS ---------- */

    .product-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 17px;
        padding: 18px;
        min-height: 285px;
        margin-bottom: 8px;
        box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .product-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 28px rgba(15, 23, 42, 0.08);
    }

    .product-icon {
        background: #F5F3FF;
        border-radius: 13px;
        height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3.3rem;
        margin-bottom: 14px;
    }

    .product-name {
        font-size: 1.08rem;
        font-weight: 750;
        color: #1E293B;
        margin-bottom: 7px;
    }

    .product-detail {
        font-size: 0.82rem;
        color: #64748B;
        margin-bottom: 5px;
    }

    .price {
        font-size: 1.25rem;
        font-weight: 800;
        color: #5630A8;
        margin-top: 10px;
    }

    .badge-rent {
        display: inline-block;
        background: #E0F2FE;
        color: #0369A1;
        padding: 5px 9px;
        border-radius: 7px;
        font-size: 0.72rem;
        font-weight: 750;
    }

    .badge-sale {
        display: inline-block;
        background: #DCFCE7;
        color: #15803D;
        padding: 5px 9px;
        border-radius: 7px;
        font-size: 0.72rem;
        font-weight: 750;
    }

    .badge-help {
        display: inline-block;
        background: #FEE2E2;
        color: #B91C1C;
        padding: 5px 9px;
        border-radius: 7px;
        font-size: 0.72rem;
        font-weight: 750;
    }

    .badge-lend {
        display: inline-block;
        background: #FEF3C7;
        color: #92400E;
        padding: 5px 9px;
        border-radius: 7px;
        font-size: 0.72rem;
        font-weight: 750;
    }

    /* ---------- WORKFLOW ---------- */

    .step-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 15px;
        padding: 22px;
        min-height: 150px;
    }

    .step-number {
        background: #5630A8;
        color: #FFFFFF;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .step-title {
        font-weight: 750;
        color: #1E293B;
        margin-bottom: 6px;
    }

    .step-text {
        color: #64748B;
        font-size: 0.87rem;
        line-height: 1.5;
    }

    /* ---------- SERVICE CARDS ---------- */

    .service-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 17px;
        padding: 24px;
        min-height: 190px;
        box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
    }

    .service-icon {
        font-size: 2rem;
        margin-bottom: 10px;
    }

    .service-title {
        font-size: 1.1rem;
        font-weight: 750;
        color: #1E293B;
        margin-bottom: 7px;
    }

    .service-text {
        color: #64748B;
        font-size: 0.88rem;
        line-height: 1.55;
    }

    /* ---------- COMMUNITY ---------- */

    .community-box {
        background: linear-gradient(135deg, #F7F2FF, #FFFFFF);
        border: 1px solid #DDD0FA;
        border-radius: 20px;
        padding: 30px;
    }

    /* ---------- CHECKOUT ---------- */

    .checkout-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 18px;
        padding: 25px;
        box-shadow: 0 8px 25px rgba(15, 23, 42, 0.05);
    }

    .secure-box {
        background: #F0FDF4;
        border: 1px solid #BBF7D0;
        border-radius: 12px;
        padding: 13px;
        color: #166534;
        font-size: 0.87rem;
        margin-top: 12px;
    }

    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        color: #94A3B8;
        font-size: 0.82rem;
        padding: 30px 0 10px 0;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# DEMO MARKETPLACE DATA
# ============================================================
# These are PROTOTYPE / DEMONSTRATION listings.
# They are NOT real transactions.

items = [
    {
        "id": 1,
        "name": "Wireless Headphones",
        "category": "Electronics",
        "type": "FOR SALE",
        "icon": "🎧",
        "price": 800,
        "unit": "one-time",
        "condition": "Good",
        "block": "ABCD Block",
        "seller": "Verified Student",
        "deposit": 0
    },
    {
        "id": 2,
        "name": "Formal Blazer",
        "category": "Clothing",
        "type": "FOR RENT",
        "icon": "🧥",
        "price": 80,
        "unit": "day",
        "condition": "Very Good",
        "block": "QRS Block",
        "seller": "Verified Student",
        "deposit": 300
    },
    {
        "id": 3,
        "name": "Scientific Calculator",
        "category": "Study Material",
        "type": "FOR RENT",
        "icon": "🧮",
        "price": 30,
        "unit": "day",
        "condition": "Good",
        "block": "U-Block",
        "seller": "Verified Student",
        "deposit": 150
    },
    {
        "id": 4,
        "name": "Party Heels",
        "category": "Footwear",
        "type": "FOR RENT",
        "icon": "👠",
        "price": 50,
        "unit": "day",
        "condition": "Excellent",
        "block": "T-Block",
        "seller": "Verified Student",
        "deposit": 200
    },
    {
        "id": 5,
        "name": "Mini Electric Kettle",
        "category": "Hostel Utility",
        "type": "FOR SALE",
        "icon": "🫖",
        "price": 650,
        "unit": "one-time",
        "condition": "Good",
        "block": "G-Block",
        "seller": "Verified Student",
        "deposit": 0
    },
    {
        "id": 6,
        "name": "Yoga Mat",
        "category": "Sports",
        "type": "FOR RENT",
        "icon": "🧘",
        "price": 20,
        "unit": "day",
        "condition": "Good",
        "block": "H-Block",
        "seller": "Verified Student",
        "deposit": 100
    },
    {
        "id": 7,
        "name": "Event Jewellery Set",
        "category": "Accessories",
        "type": "FOR RENT",
        "icon": "💎",
        "price": 60,
        "unit": "day",
        "condition": "Excellent",
        "block": "B1-Block",
        "seller": "Verified Student",
        "deposit": 250
    },
    {
        "id": 8,
        "name": "Phone Charger",
        "category": "Electronics",
        "type": "FOR SALE",
        "icon": "🔌",
        "price": 250,
        "unit": "one-time",
        "condition": "Good",
        "block": "B2-Block",
        "seller": "Verified Student",
        "deposit": 0
    }
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def go_to(page):
    st.session_state.nav = page
    st.session_state.checkout = False
    st.session_state.selected_item = None


def add_to_cart(item):
    if item["id"] not in [x["id"] for x in st.session_state.cart]:
        st.session_state.cart.append(item)
        st.success(f"Added {item['name']} to your cart.")
    else:
        st.info("This item is already in your cart.")


def badge_class(item_type):
    if item_type == "FOR RENT":
        return "badge-rent"
    elif item_type == "FOR SALE":
        return "badge-sale"
    elif item_type == "ESSENTIAL HELP":
        return "badge-help"
    else:
        return "badge-lend"


# ============================================================
# TOP HEADER
# ============================================================

header_left, header_home, header_market, header_services, header_community, header_list, header_cart, header_points = st.columns(
    [1.55, 0.85, 0.95, 0.9, 1.0, 1.05, 1.15, 1.05]
)

with header_left:
    st.markdown("""
    <div class="brand-name">IBeX</div>
    <div class="brand-tagline">Campus Marketplace</div>
    """, unsafe_allow_html=True)

with header_home:
    if st.button("Home", use_container_width=True, key="nav_home"):
        go_to("Home")
        st.rerun()

with header_market:
    if st.button("Marketplace", use_container_width=True, key="nav_market"):
        go_to("Marketplace")
        st.rerun()

with header_services:
    if st.button("Services", use_container_width=True, key="nav_services"):
        go_to("Services")
        st.rerun()

with header_community:
    if st.button("Community", use_container_width=True, key="nav_community"):
        go_to("Community")
        st.rerun()

with header_list:
    if st.button("＋ List Item", use_container_width=True, key="nav_list"):
        go_to("List Item")
        st.rerun()

with header_cart:
    cart_count = len(st.session_state.cart)

    if st.button(
        f"🛒 Orders ({cart_count})",
        use_container_width=True,
        key="nav_cart"
    ):
        go_to("Checkout")
        st.rerun()

with header_points:
    st.markdown(
        f"""
        <div class="points-pill">
            👤 {st.session_state.points} Pts
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div class="header-line"></div>', unsafe_allow_html=True)


# ============================================================
# CHECKOUT PAGE
# ============================================================

if st.session_state.nav == "Checkout":

    st.markdown('<div class="section-title">🛒 Your Orders</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Review your selected items before checkout.</div>',
        unsafe_allow_html=True
    )

    if len(st.session_state.cart) == 0:

        st.info("Your cart is currently empty. Browse the marketplace to find something you need.")

        if st.button("Browse Marketplace →", key="empty_cart_market"):
            go_to("Marketplace")
            st.rerun()

    else:

        total_item_cost = sum(item["price"] for item in st.session_state.cart)
        total_deposit = sum(item["deposit"] for item in st.session_state.cart)

        col1, col2 = st.columns([1.6, 1])

        with col1:

            for index, item in enumerate(st.session_state.cart):

                st.markdown(
                    f"""
                    <div class="checkout-card">
                        <div style="font-size:2rem;">{item["icon"]}</div>
                        <h3>{item["name"]}</h3>
                        <p style="color:#64748B;">
                            {item["type"]} • {item["condition"]} • {item["block"]}
                        </p>
                        <p style="font-size:1.2rem;font-weight:750;color:#5630A8;">
                            ₹{item["price"]:,} / {item["unit"]}
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    f"Remove {item['name']}",
                    key=f"remove_{item['id']}"
                ):
                    st.session_state.cart.pop(index)
                    st.rerun()

                st.write("")

        with col2:

            st.markdown(
                """
                <div class="checkout-card">
                    <h3>Order Summary</h3>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(f"**Item total:** ₹{total_item_cost:,}")

            if total_deposit > 0:
                st.write(f"**Refundable security deposit:** ₹{total_deposit:,}")

            delivery_required = st.radio(
                "Delivery option",
                [
                    "I'll collect it myself — Free",
                    "Campus delivery — ₹20"
                ],
                key="delivery_option"
            )

            delivery_fee = 20 if "Campus delivery" in delivery_required else 0

            grand_total = total_item_cost + total_deposit + delivery_fee

            st.markdown("---")

            st.markdown(
                f"""
                <div style="font-size:1.25rem;font-weight:800;">
                    Total Payable: ₹{grand_total:,}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div class="secure-box">
                    🔒 <b>Secure Prototype Checkout</b><br>
                    Payment details are not displayed or stored in this prototype.
                    In a live version, a certified payment gateway would process the transaction.
                </div>
                """,
                unsafe_allow_html=True
            )

            payment_method = st.radio(
                "Payment Method",
                [
                    "UPI / Digital Payment",
                    "Cash on Delivery"
                ],
                key="payment_method"
            )

            if payment_method == "UPI / Digital Payment":

                st.text_input(
                    "UPI ID",
                    placeholder="example@upi",
                    help="Prototype field only — no real payment is processed."
                )

                st.caption(
                    "🔐 Your UPI/payment details are not displayed publicly."
                )

            else:

                st.info(
                    "You can pay the amount to the student/helper when the item is handed over."
                )

            if st.button(
                "🔒 Confirm Secure Order",
                use_container_width=True,
                key="confirm_order"
            ):

                new_order = {
                    "items": [item["name"] for item in st.session_state.cart],
                    "amount": grand_total,
                    "payment": payment_method,
                    "delivery": delivery_required
                }

                st.session_state.orders.append(new_order)

                # Demo reward points
                st.session_state.points += 10

                st.session_state.cart = []

                st.success(
                    "Order placed successfully! This is a prototype transaction."
                )

                st.balloons()

                st.session_state.nav = "Home"

                st.info(
                    "⭐ You earned 10 IBeX Points for completing this prototype transaction."
                )

                if st.button("Continue Shopping", key="continue_shopping"):
                    go_to("Marketplace")
                    st.rerun()


# ============================================================
# HOME PAGE
# ============================================================

elif st.session_state.nav == "Home":

    # ---------- HERO ----------

    st.markdown("""
    <div class="hero">

        <div class="hero-title">
            Campus life made
            <span class="hero-highlight">simpler.</span>
        </div>

        <div class="hero-text">
            Rent what you need, buy second-hand, earn from unused products,
            request campus help and reward students who make the community work —
            all within a verified IBS network.
        </div>

        <div class="trust-row">
            <div class="trust-pill">🔒 IBS Verified</div>
            <div class="trust-pill">⚡ Campus Pickup</div>
            <div class="trust-pill">🌱 Reuse & Reduce Waste</div>
            <div class="trust-pill">⭐ Reward-Based Community</div>
        </div>

    </div>
    """, unsafe_allow_html=True)

    # ---------- IMPACT BAR ----------

    metric1, metric2, metric3, metric4 = st.columns(4)

    with metric1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">8</div>
            <div class="metric-label">Active Demo Listings</div>
        </div>
        """, unsafe_allow_html=True)

    with metric2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-number">{st.session_state.points}</div>
            <div class="metric-label">Your IBeX Points</div>
        </div>
        """, unsafe_allow_html=True)

    with metric3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">100%</div>
            <div class="metric-label">IBS Verified Concept</div>
        </div>
        """, unsafe_allow_html=True)

    with metric4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-number">24/7</div>
            <div class="metric-label">Community Requests</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    # ---------- QUICK ACTIONS ----------

    st.markdown(
        '<div class="section-title">What do you need today?</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Choose an IBeX service to get started.</div>',
        unsafe_allow_html=True
    )

    qa1, qa2, qa3, qa4 = st.columns(4)

    with qa1:
        if st.button("🏷️ Browse Marketplace", use_container_width=True):
            go_to("Marketplace")
            st.rerun()

    with qa2:
        if st.button("📦 Request Campus Help", use_container_width=True):
            go_to("Services")
            st.rerun()

    with qa3:
        if st.button("➕ List Something", use_container_width=True):
            go_to("List Item")
            st.rerun()

    with qa4:
        if st.button("⭐ View My Rewards", use_container_width=True):
            go_to("Community")
            st.rerun()

    st.write("")

    # ---------- FEATURED LISTINGS ----------

    st.markdown(
        '<div class="section-title">Featured on IBeX</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Demo listings showing how the marketplace could work.</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(4)

    for index, item in enumerate(items[:4]):

        with cols[index]:

            st.markdown(
                f"""
                <div class="product-card">

                    <div class="product-icon">
                        {item["icon"]}
                    </div>

                    <span class="{badge_class(item["type"])}">
                        {item["type"]}
                    </span>

                    <div class="product-name">
                        {item["name"]}
                    </div>

                    <div class="product-detail">
                        Condition: {item["condition"]}
                    </div>

                    <div class="product-detail">
                        📍 {item["block"]}
                    </div>

                    <div class="price">
                        ₹{item["price"]:,} / {item["unit"]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "View Item",
                key=f"home_view_{item['id']}",
                use_container_width=True
            ):
                st.session_state.selected_item = item
                st.session_state.nav = "Marketplace"
                st.rerun()

    # ---------- HOW IT WORKS ----------

    st.markdown(
        '<div class="section-title">How IBeX Works</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Simple steps. Safe transactions. Stronger campus community.</div>',
        unsafe_allow_html=True
    )

    s1, s2, s3, s4 = st.columns(4)

    steps = [
        (
            "1",
            "Browse & Select",
            "Find an item, service or campus assistance that fits your need."
        ),
        (
            "2",
            "Connect & Verify",
            "Interact only within a verified IBS student community."
        ),
        (
            "3",
            "Pickup / Delivery",
            "Collect the item yourself or request convenient campus delivery."
        ),
        (
            "4",
            "Earn Reward Points",
            "Help other students and earn IBeX Points for future benefits."
        )
    ]

    for column, step in zip([s1, s2, s3, s4], steps):

        with column:

            st.markdown(
                f"""
                <div class="step-card">

                    <div class="step-number">
                        {step[0]}
                    </div>

                    <div class="step-title">
                        {step[1]}
                    </div>

                    <div class="step-text">
                        {step[2]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# MARKETPLACE
# ============================================================

elif st.session_state.nav == "Marketplace":

    st.markdown(
        '<div class="section-title">🛍️ IBeX Marketplace</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Buy, rent or discover useful products within the IBS community.</div>',
        unsafe_allow_html=True
    )

    # ---------- FILTERS ----------

    f1, f2, f3 = st.columns([1, 1, 1])

    with f1:
        selected_type = st.selectbox(
            "Listing Type",
            ["All", "FOR RENT", "FOR SALE"]
        )

    with f2:
        categories = ["All"] + sorted(list(set(item["category"] for item in items)))

        selected_category = st.selectbox(
            "Category",
            categories
        )

    with f3:
        search = st.text_input(
            "🔎 Search",
            placeholder="Search items..."
        )

    filtered_items = items.copy()

    if selected_type != "All":
        filtered_items = [
            item for item in filtered_items
            if item["type"] == selected_type
        ]

    if selected_category != "All":
        filtered_items = [
            item for item in filtered_items
            if item["category"] == selected_category
        ]

    if search:
        filtered_items = [
            item for item in filtered_items
            if search.lower() in item["name"].lower()
            or search.lower() in item["category"].lower()
        ]

    st.markdown("---")

    # ---------- SELECTED ITEM ----------

    if st.session_state.selected_item is not None:

        item = st.session_state.selected_item

        st.markdown(
            f"""
            <div class="checkout-card">

                <div style="font-size:3rem;">
                    {item["icon"]}
                </div>

                <h2>{item["name"]}</h2>

                <p style="color:#64748B;">
                    {item["category"]} • {item["condition"]} • {item["block"]}
                </p>

                <h2 style="color:#5630A8;">
                    ₹{item["price"]:,} / {item["unit"]}
                </h2>

                {
                    f'<p><b>Refundable Security Deposit:</b> ₹{item["deposit"]:,}</p>'
                    if item["deposit"] > 0
                    else ""
                }

                <p>
                    🔒 Verified IBS student listing
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        action1, action2 = st.columns(2)

        with action1:

            if st.button(
                "🛒 Add to Order",
                use_container_width=True,
                key=f"selected_add_{item['id']}"
            ):

                add_to_cart(item)

        with action2:

            if st.button(
                "← Back to Marketplace",
                use_container_width=True,
                key="back_marketplace"
            ):

                st.session_state.selected_item = None
                st.rerun()

        st.markdown("---")

    # ---------- PRODUCT GRID ----------

    if len(filtered_items) == 0:

        st.warning("No listings match your search.")

    else:

        for start in range(0, len(filtered_items), 4):

            row_items = filtered_items[start:start + 4]

            cols = st.columns(4)

            for index, item in enumerate(row_items):

                with cols[index]:

                    st.markdown(
                        f"""
                        <div class="product-card">

                            <div class="product-icon">
                                {item["icon"]}
                            </div>

                            <span class="{badge_class(item["type"])}">
                                {item["type"]}
                            </span>

                            <div class="product-name">
                                {item["name"]}
                            </div>

                            <div class="product-detail">
                                {item["category"]}
                            </div>

                            <div class="product-detail">
                                Condition: {item["condition"]}
                            </div>

                            <div class="product-detail">
                                📍 {item["block"]}
                            </div>

                            <div class="price">
                                ₹{item["price"]:,} / {item["unit"]}
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    if st.button(
                        "Quick Add",
                        key=f"market_add_{item['id']}",
                        use_container_width=True
                    ):

                        add_to_cart(item)

    st.caption(
        "Prototype note: Marketplace listings shown above are demonstration data and do not represent real transactions."
    )


# ============================================================
# SERVICES
# ============================================================

elif st.session_state.nav == "Services":

    st.markdown(
        '<div class="section-title">⚡ Campus Services</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Small problems. Simple campus-to-campus solutions.</div>',
        unsafe_allow_html=True
    )

    service1, service2, service3 = st.columns(3)

    with service1:

        st.markdown("""
        <div class="service-card">

            <div class="service-icon">📦</div>

            <div class="service-title">
                Parcel Pickup
            </div>

            <div class="service-text">
                Ask another verified student to collect your
                Amazon, Flipkart or quick-commerce parcel from
                the IBS main gate.
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.write("")

        if st.button(
            "Request Parcel Pickup",
            use_container_width=True,
            key="parcel_request"
        ):
            st.session_state.nav = "Request Help"
            st.rerun()

    with service2:

        st.markdown("""
        <div class="service-card">

            <div class="service-icon">💊</div>

            <div class="service-title">
                Medical Assistance
            </div>

            <div class="service-text">
                Request basic campus assistance or access to
                essential products listed by students.
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.write("")

        if st.button(
            "Request Medical Help",
            use_container_width=True,
            key="medical_request"
        ):
            st.session_state.nav = "Request Help"
            st.rerun()

    with service3:

        st.markdown("""
        <div class="service-card">

            <div class="service-icon">🤝</div>

            <div class="service-title">
                Student Assistance
            </div>

            <div class="service-text">
                Need something small done on campus?
                Post a request and reward another student
                for helping you.
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.write("")

        if st.button(
            "Request Campus Help",
            use_container_width=True,
            key="help_request"
        ):
            st.session_state.nav = "Request Help"
            st.rerun()

    st.markdown("---")

    # ---------- HELP REQUEST FORM ----------

    st.markdown(
        '<div class="section-title">Post a Help Request</div>',
        unsafe_allow_html=True
    )

    h1, h2 = st.columns(2)

    with h1:

        request_type = st.selectbox(
            "What do you need help with?",
            [
                "Parcel Pickup",
                "Medical / Essential Item",
                "Item Pickup",
                "Food / Snack Assistance",
                "Other Campus Help"
            ]
        )

        description = st.text_area(
            "Describe your request",
            placeholder="Example: Please collect my parcel from the main gate."
        )

    with h2:

        hostel_blocks = [
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
            "S2-Block",
            "Other / Enter Manually"
        ]

        selected_block = st.selectbox(
            "Your Hostel Block",
            hostel_blocks
        )

        if selected_block == "Other / Enter Manually":

            selected_block = st.text_input(
                "Enter your hostel block"
            )

        reward = st.selectbox(
            "Suggested helper reward",
            [
                "10 IBeX Points",
                "20 IBeX Points",
                "30 IBeX Points",
                "₹10",
                "₹20",
                "₹25"
            ]
        )

    if st.button(
        "Post Request",
        use_container_width=True,
        key="post_help"
    ):

        if description.strip() == "":
            st.warning("Please describe your request first.")

        else:

            st.success(
                f"Your {request_type} request has been posted successfully!"
            )

            st.info(
                f"Suggested reward: {reward} • Location: {selected_block}"
            )


# ============================================================
# LIST ITEM
# ============================================================

elif st.session_state.nav == "List Item":

    st.markdown(
        '<div class="section-title">＋ List an Item</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Turn unused products into value for another student.</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="community-box">

        <b>Freemium Listing Model</b><br><br>

        Your first <b>3 listings</b> are free.<br>
        After the free allowance, additional listings can be
        unlocked through the IBeX subscription plan.

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    l1, l2 = st.columns(2)

    with l1:

        item_name = st.text_input(
            "Item Name",
            placeholder="Example: Formal blazer"
        )

        listing_type = st.selectbox(
            "What do you want to do?",
            [
                "Sell",
                "Lend / Rent"
            ]
        )

        category = st.selectbox(
            "Category",
            [
                "Clothing",
                "Shoes",
                "Bags / Accessories",
                "Hostel Utilities",
                "Sports Equipment",
                "Electronics",
                "Books / Study Material",
                "Other"
            ]
        )

        condition = st.selectbox(
            "Condition",
            [
                "New",
                "Excellent",
                "Very Good",
                "Good",
                "Fair"
            ]
        )

    with l2:

        hostel_blocks = [
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
            "S2-Block",
            "Other / Enter Manually"
        ]

        listing_block = st.selectbox(
            "Pickup / Item Location",
            hostel_blocks,
            key="listing_block"
        )

        if listing_block == "Other / Enter Manually":

            listing_block = st.text_input(
                "Enter block/location",
                key="manual_listing_block"
            )

        price = st.number_input(
            "Price (₹)",
            min_value=0,
            max_value=100000,
            value=50,
            step=10
        )

        if listing_type == "Lend / Rent":

            deposit = st.number_input(
                "Refundable Security Deposit (₹)",
                min_value=0,
                max_value=100000,
                value=100,
                step=10
            )

        else:

            deposit = 0

    description = st.text_area(
        "Item Description",
        placeholder="Describe the item, condition and any important details..."
    )

    st.markdown("---")

    if st.button(
        "Publish Listing",
        use_container_width=True,
        key="publish_listing"
    ):

        if item_name.strip() == "":
            st.warning("Please enter an item name.")

        elif listing_block.strip() == "":
            st.warning("Please enter your location.")

        else:

            st.success(
                f"🎉 {item_name} has been listed successfully!"
            )

            st.info(
                "Prototype message: In the live platform, this listing would become visible to verified IBS students."
            )


# ============================================================
# REQUEST HELP PAGE
# ============================================================

elif st.session_state.nav == "Request Help":

    st.markdown(
        '<div class="section-title">🤝 Request Campus Help</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Post a small task and let another student earn from helping you.</div>',
        unsafe_allow_html=True
    )

    request = st.text_input(
        "What do you need?",
        placeholder="Example: Pick up my parcel from the main gate"
    )

    hostel_blocks = [
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
        "S2-Block",
        "Other / Enter Manually"
    ]

    block = st.selectbox(
        "Delivery / Pickup Block",
        hostel_blocks,
        key="request_help_block"
    )

    if block == "Other / Enter Manually":

        block = st.text_input(
            "Enter your block",
            key="manual_help_block"
        )

    reward_type = st.radio(
        "How would you like to reward the helper?",
        [
            "IBeX Points",
            "Cash / Digital Payment"
        ]
    )

    if reward_type == "IBeX Points":

        reward_amount = st.selectbox(
            "Points",
            [
                "10 Points",
                "20 Points",
                "30 Points",
                "50 Points"
            ]
        )

    else:

        reward_amount = st.selectbox(
            "Amount",
            [
                "₹10",
                "₹15",
                "₹20",
                "₹25"
            ]
        )

    if st.button(
        "Post Help Request",
        use_container_width=True,
        key="post_help_request_page"
    ):

        if request.strip() == "":
            st.warning("Please describe what you need.")

        else:

            st.success("Your request is now visible to the IBeX community.")

            st.info(
                f"📍 {block} • Reward: {reward_amount}"
            )


# ============================================================
# COMMUNITY PAGE
# ============================================================

elif st.session_state.nav == "Community":

    st.markdown(
        '<div class="section-title">⭐ IBeX Community</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">The more you contribute, the more you earn.</div>',
        unsafe_allow_html=True
    )

    # ---------- POINTS ----------

    points_col1, points_col2 = st.columns([1, 1])

    with points_col1:

        st.markdown(
            f"""
            <div class="community-box">

                <div style="font-size:0.9rem;color:#64748B;">
                    YOUR CURRENT BALANCE
                </div>

                <div style="font-size:3rem;font-weight:800;color:#5630A8;">
                    ⭐ {st.session_state.points}
                </div>

                <div style="color:#64748B;">
                    IBeX Points
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with points_col2:

        st.markdown("""
        <div class="community-box">

            <b>How can you earn points?</b><br><br>

            🛒 Complete purchases<br>
            🏠 Complete rentals<br>
            📦 Help with parcel pickup<br>
            💊 Assist with essential needs<br>
            ⭐ Receive positive reviews<br>
            🔄 Complete successful returns

        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ---------- REWARD TABLE ----------

    st.markdown(
        '<div class="section-title">Reward System</div>',
        unsafe_allow_html=True
    )

    reward_df = pd.DataFrame({
        "Activity": [
            "Successful Purchase",
            "Successful Rental",
            "Parcel Pickup",
            "Successful Return",
            "Helpful Review"
        ],
        "IBeX Points": [
            "+50",
            "+30",
            "+20",
            "+40",
            "+10"
        ]
    })

    st.dataframe(
        reward_df,
        use_container_width=True,
        hide_index=True
    )

    # ---------- MATPLOTLIB ----------

    st.markdown(
        '<div class="section-title">Prototype Marketplace Mix</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Demonstration chart based on the prototype listings — not real transaction data."
    )

    category_counts = pd.Series(
        [item["category"] for item in items]
    ).value_counts()

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.bar(
        category_counts.index,
        category_counts.values
    )

    ax.set_xlabel("Category")
    ax.set_ylabel("Number of Demo Listings")
    ax.set_title("IBeX Prototype Listing Mix")

    plt.xticks(
        rotation=35,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    <b>IBeX</b> • One Campus. One Platform. Everything You Need.<br>

    Built as a Managing Platform Business prototype |
    IFHE Hyderabad

    <br><br>

    🔒 IBS Verified Community • 🌱 Reuse • ⭐ Rewards

</div>
""", unsafe_allow_html=True)
