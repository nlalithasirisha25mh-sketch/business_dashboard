import streamlit as st
import pandas as pd
import uuid
import secrets
from datetime import datetime, timedelta


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="IBeX | IBS Exchange",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(180deg, #F7F2FF 0%, #FFFFFF 45%);
}

/* Main title */
.main-title {
    font-size: 52px;
    font-weight: 800;
    color: #5B2C83;
    margin-bottom: 0px;
}

.tagline {
    font-size: 20px;
    color: #6B5B7B;
    margin-bottom: 25px;
}

/* Hero section */
.hero {
    background: linear-gradient(135deg, #5B2C83, #8E5BB7);
    padding: 32px;
    border-radius: 22px;
    color: white;
    margin-bottom: 25px;
}

.hero h2 {
    color: white;
}

/* Cards */
.card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 3px 14px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

.listing-image {
    width: 100%;
    height: 210px;
    object-fit: cover;
    border-radius: 14px;
    margin-bottom: 14px;
}

.image-placeholder {
    width: 100%;
    height: 210px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #F3F0F7;
    border-radius: 14px;
    font-size: 60px;
    margin-bottom: 14px;
}

/* Price */
.price {
    font-size: 23px;
    font-weight: 700;
    color: #5B2C83;
}

/* Verified */
.verified {
    color: #1F8A4C;
    font-weight: 600;
}

/* Secure payment */
.secure-box {
    background: #EFFAF3;
    border-left: 5px solid #2E8B57;
    padding: 15px;
    border-radius: 10px;
}

/* Rewards */
.reward-box {
    background: #FFF7E6;
    border-left: 5px solid #E3A008;
    padding: 15px;
    border-radius: 10px;
}

/* Buttons */
div.stButton > button {
    background-color: #6A359C;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: 600;
    padding: 8px 18px;
}

div.stButton > button:hover {
    background-color: #51247A;
    color: white;
}

/* Horizontal Navigation */
.nav-container {
    background: white;
    padding: 12px 10px;
    border-radius: 14px;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.06);
    margin-bottom: 25px;
}

.nav-title {
    font-size: 22px;
    font-weight: 800;
    color: #5B2C83;
    margin-bottom: 5px;
}

.nav-subtitle {
    font-size: 12px;
    color: #777;
}

/* Active navigation button */
div.stButton > button[kind="primary"] {
    background-color: #5B2C83;
    color: white;
}


/* Pastel-pop visual system */
:root { --cream:#FFFDF8; --lilac:#B79CED; --coral:#FF9A8D; --mint:#8EDCC0; --butter:#F8DF7A; --ink:#342F3A; }
.stApp { background: linear-gradient(180deg, #FFFDF8 0%, #F8F5FF 48%, #FFFFFF 100%); color: var(--ink); }
.main-title { color:#5D3C78; letter-spacing:-1px; }
.tagline { color:#766B7D; }
.hero { background: linear-gradient(135deg, #5D3C78 0%, #7E5BA4 48%, #A27BC5 100%); box-shadow:0 12px 32px rgba(93,60,120,.15); }
.card { border:1px solid rgba(93,60,120,.08); box-shadow:0 8px 24px rgba(55,45,65,.07); }
.nav-container { border:1px solid rgba(93,60,120,.08); }
.auth-card { background:rgba(255,255,255,.88); border:1px solid rgba(93,60,120,.10); border-radius:28px; padding:36px; box-shadow:0 16px 45px rgba(55,45,65,.10); }
.auth-badge { display:inline-block; padding:7px 12px; border-radius:999px; background:#EFE8FF; color:#5D3C78; font-weight:700; font-size:13px; }
.pastel-pill { display:inline-block; padding:8px 12px; border-radius:999px; margin:4px 4px 4px 0; font-weight:700; font-size:13px; }
.pastel-lilac { background:#EFE8FF; color:#5D3C78; }
.pastel-mint { background:#E4FAF1; color:#23765A; }
.pastel-coral { background:#FFF0ED; color:#A84D40; }
.pastel-butter { background:#FFF8D9; color:#806915; }


/* Full-screen celebration animations */
.celebration {
    position: fixed;
    inset: 0;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    z-index: 999999;
    pointer-events: none;
    background: transparent;
}
.celebration span {
    position: absolute;
    bottom: -80px;
    font-size: clamp(30px, 3.2vw, 58px);
    animation: fullScreenPop 2.5s cubic-bezier(.18,.75,.28,1) forwards;
    opacity: 0;
    filter: drop-shadow(0 5px 8px rgba(0,0,0,.12));
}
@keyframes fullScreenPop {
    0% {
        transform: translateY(0) scale(.25) rotate(-15deg);
        opacity: 0;
    }
    10% {
        opacity: 1;
    }
    35% {
        transform: translateY(-32vh) scale(1.15) rotate(8deg);
        opacity: 1;
    }
    70% {
        transform: translateY(-68vh) scale(1) rotate(-8deg);
        opacity: .95;
    }
    100% {
        transform: translateY(-112vh) scale(.7) rotate(18deg);
        opacity: 0;
    }
}
.celebration-message {
    position: fixed;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    z-index: 1000000;
    pointer-events: none;
    text-align: center;
    width: min(90vw, 620px);
    text-shadow: 0 2px 14px rgba(255,255,255,.95);
}
.celebration-message h2 {
    font-size: clamp(28px, 4vw, 48px);
    color: #5D3C78;
    margin: 0 0 8px 0;
}
.celebration-message p {
    font-size: clamp(16px, 2vw, 22px);
    color: #342F3A;
    margin: 0;
    font-weight: 600;
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

if "order_chats" not in st.session_state:
    st.session_state.order_chats = {}

if "points" not in st.session_state:
    st.session_state.points = 245

if "custom_listings" not in st.session_state:
    st.session_state.custom_listings = []

if "help_requests" not in st.session_state:
    st.session_state.help_requests = []

if "essential_requests" not in st.session_state:
    st.session_state.essential_requests = []

if "notifications" not in st.session_state:
    st.session_state.notifications = []

if "show_celebration" not in st.session_state:
    st.session_state.show_celebration = None

# Demo profile: authentication/login has been removed for the prototype.
# Edit these values if you want the Profile page to display different details.
if "profile" not in st.session_state:
    st.session_state.profile = {
        "name": "IBS Student",
        "email": "demo@ibsindia.org",
        "department": "MBA",
        "batch": "2026",
        "role": "Student",
    }

if "otp" not in st.session_state:
    st.session_state.otp = None

if "otp_email" not in st.session_state:
    st.session_state.otp_email = None

if "otp_generated_at" not in st.session_state:
    st.session_state.otp_generated_at = None

if "otp_verified" not in st.session_state:
    st.session_state.otp_verified = False

if "onboarding_complete" not in st.session_state:
    st.session_state.onboarding_complete = True


# ============================================================
# PROTOTYPE NOTIFICATIONS & CELEBRATIONS
# ============================================================

def add_notification(title, message, kind="info"):
    st.session_state.notifications.insert(
        0,
        {
            "title": title,
            "message": message,
            "kind": kind,
            "time": datetime.now().strftime("%d %b %Y, %I:%M %p"),
            "read": False
        }
    )


def show_celebration(kind):
    if kind == "stars":
        symbols = ["⭐", "✨", "🌟", "⭐", "✨", "🌟", "⭐", "✨", "🌟", "⭐", "✨", "🌟"]
        title = "Request accepted! ⭐"
        message = "Thank you for helping a fellow IBS student."
    else:
        symbols = ["❤️", "💗", "💕", "❤️", "💗", "💕", "❤️", "💗", "💕", "❤️", "💗", "💕"]
        title = "Help accepted! 💗"
        message = "A student is now helping with this essential request."

    positions = [4, 12, 20, 28, 36, 44, 52, 60, 68, 76, 84, 92]
    delays = [0.0, .12, .24, .36, .48, .60, .72, .84, .96, 1.08, 1.20, 1.32]

    spans = "".join(
        f"<span style='left:{positions[i]}%;animation-delay:{delays[i]}s'>{symbols[i]}</span>"
        for i in range(len(symbols))
    )

    st.markdown(
        f"""
        <div class="celebration">{spans}</div>
        <div class="celebration-message">
            <h2>{title}</h2>
            <p>{message}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


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
# SAMPLE MARKETPLACE DATA
# ============================================================

marketplace_data = [

    {
        "id": "L001",
        "item": "Scientific Calculator",
        "image": "https://images.unsplash.com/photo-1587145820266-a5951ee6f620?auto=format&fit=crop&w=900&q=80",
        "category": "Academic",
        "type": "Buy",
        "price": 500,
        "deposit": 0,
        "condition": "Excellent",
        "rating": 4.8,
        "seller": "IBX Student 104",
        "seller_contact": "@ibex_student_104",
        "location": "ABCD Block",
        "transactions": 18
    },

    {
        "id": "L002",
        "item": "Black Formal Heels",
        "image": "https://images.unsplash.com/photo-1559334417-1adb87b6e97f?auto=format&fit=crop&fm=jpg&q=85&w=1200",
        "category": "Fashion",
        "type": "Rent",
        "price": 50,
        "deposit": 300,
        "condition": "Good",
        "rating": 4.7,
        "seller": "IBX Student 218",
        "seller_contact": "@ibex_student_218",
        "location": "QRS Block",
        "transactions": 12
    },

    {
        "id": "L003",
        "item": "Hair Dryer",
        "image": "https://images.unsplash.com/photo-1522338140262-f46f5913618a?auto=format&fit=crop&fm=jpg&q=85&w=1200",
        "category": "Personal Care",
        "type": "Rent",
        "price": 30,
        "deposit": 200,
        "condition": "Excellent",
        "rating": 4.9,
        "seller": "IBX Student 302",
        "seller_contact": "@ibex_student_302",
        "location": "U-Block",
        "transactions": 24
    },

    {
        "id": "L004",
        "item": "Electric Iron",
        "image": "https://orientelectric.com/cdn/shop/files/fabrismooth-non-stick-dry-iron-white-orient-electric-1.png?v=1696835084&width=1445",
        "category": "Hostel Utility",
        "type": "Rent",
        "price": 20,
        "deposit": 150,
        "condition": "Good",
        "rating": 4.6,
        "seller": "IBX Student 187",
        "seller_contact": "@ibex_student_187",
        "location": "T-Block",
        "transactions": 10
    },

    {
        "id": "L005",
        "item": "Ethnic Kurta Set",
        "image": "https://fashor.com/cdn/shop/files/27266_13.jpg?v=1749480577&width=1080",
        "category": "Fashion",
        "type": "Rent",
        "price": 100,
        "deposit": 500,
        "condition": "Excellent",
        "rating": 4.9,
        "seller": "IBX Student 411",
        "seller_contact": "@ibex_student_411",
        "location": "G-Block",
        "transactions": 20
    },

    {
        "id": "L006",
        "item": "Extension Board",
        "image": "https://zebronics.com/cdn/shop/files/ZEB-PS4200H-pic1.jpg?v=1751979486&width=1200",
        "category": "Electronics",
        "type": "Buy",
        "price": 300,
        "deposit": 0,
        "condition": "Good",
        "rating": 4.5,
        "seller": "IBX Student 096",
        "seller_contact": "@ibex_student_096",
        "location": "H-Block",
        "transactions": 8
    },

    {
        "id": "L007",
        "item": "Sports Shoes",
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=900&q=80",
        "category": "Sports",
        "type": "Buy",
        "price": 800,
        "deposit": 0,
        "condition": "Good",
        "rating": 4.8,
        "seller": "IBX Student 355",
        "seller_contact": "@ibex_student_355",
        "location": "B1-Block",
        "transactions": 15
    },

    {
        "id": "L008",
        "item": "Tripod",
        "image": "https://down-ph.img.susercontent.com/file/cn-11134207-820l4-msmkxh0l3j0kc8",
        "category": "Electronics",
        "type": "Rent",
        "price": 40,
        "deposit": 300,
        "condition": "Good",
        "rating": 4.7,
        "seller": "IBX Student 274",
        "seller_contact": "@ibex_student_274",
        "location": "D1-Block",
        "transactions": 16
    }

]


# Add user-created listings

marketplace_data.extend(
    st.session_state.custom_listings
)


# ============================================================
# TOP BRAND HEADER
# ============================================================

header_left, header_right = st.columns([4, 1])

with header_left:

    st.markdown(
        '<div class="main-title">IBeX</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="nav-subtitle">IBS Exchange • One Campus. One Platform.</div>',
        unsafe_allow_html=True
    )

with header_right:

    st.metric(
        "⭐ IBeX Points",
        st.session_state.points
    )


# ============================================================
# HORIZONTAL NAVIGATION
# ============================================================

st.markdown(
    '<div class="nav-container">',
    unsafe_allow_html=True
)

nav1, nav2, nav3, nav4, nav5 = st.columns(5)

nav6, nav7, nav8, nav9, nav10 = st.columns(5)


with nav1:
    if st.button(
        "🏠 Home",
        use_container_width=True
    ):
        st.session_state.current_page = "Home"
        st.rerun()


with nav2:
    if st.button(
        "🛍️ Marketplace",
        use_container_width=True
    ):
        st.session_state.current_page = "Marketplace"
        st.rerun()


with nav3:
    if st.button(
        "➕ List Item",
        use_container_width=True
    ):
        st.session_state.current_page = "List an Item"
        st.rerun()


with nav4:
    if st.button(
        "🛒 Checkout",
        use_container_width=True
    ):
        st.session_state.current_page = "Checkout"
        st.rerun()


with nav5:
    if st.button(
        "📦 My Orders",
        use_container_width=True
    ):
        st.session_state.current_page = "My Orders"
        st.rerun()


with nav6:
    if st.button(
        "🚚 Delivery & Help",
        use_container_width=True
    ):
        st.session_state.current_page = "Delivery & Help"
        st.rerun()


with nav7:
    if st.button(
        "🏥 Essential Help",
        use_container_width=True
    ):
        st.session_state.current_page = "Essential Assistance"
        st.rerun()


with nav8:
    if st.button(
        "⭐ Rewards",
        use_container_width=True
    ):
        st.session_state.current_page = "Rewards"
        st.rerun()


with nav9:
    if st.button(
        "👤 Profile",
        use_container_width=True
    ):
        st.session_state.current_page = "Profile"
        st.rerun()


with nav10:
    unread_count = sum(
        1 for n in st.session_state.notifications
        if not n.get("read", False)
    )
    notification_label = (
        f"🔔 Notifications ({unread_count})"
        if unread_count
        else "🔔 Notifications"
    )
    if st.button(
        notification_label,
        use_container_width=True
    ):
        st.session_state.current_page = "Notifications"
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# HOME
# ============================================================

if st.session_state.current_page == "Home":

    st.markdown("""
    <div class="hero">
        <h2>Everything you need. Within your campus.</h2>
        <p>
        IBeX is a verified IBS-only community platform where
        students can rent, buy, sell, lend and help each other.
        </p>
    </div>
    """, unsafe_allow_html=True)


    # KPI CARDS

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "🛍️ Available Items",
        len(marketplace_data)
    )

    col2.metric(
        "⭐ Your Points",
        st.session_state.points
    )

    col3.metric(
        "📦 Your Orders",
        len(st.session_state.orders)
    )

    col4.metric(
        "✅ Community",
        "IBS Only"
    )


    st.markdown("---")

    st.subheader("What can you do on IBeX?")


    a, b, c = st.columns(3)

    with a:

        st.markdown("""
        <div class="card">
            <h3>🔄 Rent</h3>
            <p>
            Need something temporarily?
            Rent it from another IBS student.
            </p>
        </div>
        """, unsafe_allow_html=True)


    with b:

        st.markdown("""
        <div class="card">
            <h3>🛍️ Buy</h3>
            <p>
            Find affordable second-hand products
            from verified students.
            </p>
        </div>
        """, unsafe_allow_html=True)


    with c:

        st.markdown("""
        <div class="card">
            <h3>💰 Sell / Lend</h3>
            <p>
            Earn from products you no longer use
            by selling or lending them.
            </p>
        </div>
        """, unsafe_allow_html=True)


    d, e, f = st.columns(3)


    with d:

        st.markdown("""
        <div class="card">
            <h3>🚚 Campus Delivery</h3>
            <p>
            Get your parcels or items picked up
            when you're unavailable.
            </p>
        </div>
        """, unsafe_allow_html=True)


    with e:

        st.markdown("""
        <div class="card">
            <h3>🏥 Essential Help</h3>
            <p>
            Request basic urgent necessities
            from your campus community.
            </p>
        </div>
        """, unsafe_allow_html=True)


    with f:

        st.markdown("""
        <div class="card">
            <h3>⭐ Earn Points</h3>
            <p>
            Help other students and earn IBeX
            points for future benefits.
            </p>
        </div>
        """, unsafe_allow_html=True)


    st.markdown("---")

    st.subheader("Why IBeX?")

    st.write(
        "♻️ **Reuse instead of waste** • "
        "🤝 **Student-to-student community** • "
        "🔐 **Verified users** • "
        "💸 **Affordable access**"
    )


# ============================================================
# MARKETPLACE
# ============================================================

elif st.session_state.current_page == "Marketplace":

    st.title("🛍️ IBeX Marketplace")

    st.caption(
        "Buy or rent products listed by verified IBS students."
    )


    search = st.text_input(
        "🔍 Search for an item",
        placeholder="Try calculator, dress, iron, charger..."
    )


    col1, col2 = st.columns(2)


    categories = sorted(
        list(
            set(
                item["category"]
                for item in marketplace_data
            )
        )
    )


    with col1:

        category_filter = st.selectbox(
            "Category",
            ["All"] + categories
        )


    with col2:

        type_filter = st.selectbox(
            "Looking to",
            ["All", "Buy", "Rent"]
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


    st.markdown("---")


    if len(filtered) == 0:

        st.warning(
            "No matching listings found."
        )


    for item in filtered:

        colA, colB, colC = st.columns(
            [4, 2, 1.5]
        )


        with colA:

            # Listing image
            if item.get("image"):
                st.image(
                    item["image"],
                    use_container_width=True
                )
            else:
                st.markdown(
                    "<div class='image-placeholder'>🛍️</div>",
                    unsafe_allow_html=True
                )

            st.markdown(
                f"### {item['item']}"
            )

            st.markdown(
                f"🟢 **{item['type']}** "
                f"&nbsp; | &nbsp; "
                f"{item['category']}"
            )

            st.write(
                f"Condition: **{item['condition']}**"
            )

            st.write(
                f"📍 {item['location']}"
            )

            st.markdown(
                "<span class='verified'>"
                "✓ Verified IBS Student"
                "</span>",
                unsafe_allow_html=True
            )

            st.caption(
                f"⭐ {item['rating']} rating • "
                f"{item['transactions']} successful transactions"
            )


        with colB:

            if item["type"] == "Rent":

                st.markdown(
                    f"<div class='price'>"
                    f"₹{item['price']}/day"
                    f"</div>",
                    unsafe_allow_html=True
                )

                st.caption(
                    f"Refundable deposit: "
                    f"₹{item['deposit']}"
                )

            else:

                st.markdown(
                    f"<div class='price'>"
                    f"₹{item['price']}"
                    f"</div>",
                    unsafe_allow_html=True
                )


        with colC:

            if item["type"] == "Rent":

                button_text = "Rent Now"

            else:

                button_text = "Buy Now"


            if st.button(
                button_text,
                key=f"select_{item['id']}"
            ):

                st.session_state.selected_item = item

                st.session_state.current_page = "Checkout"

                st.rerun()


        st.markdown("---")


# ============================================================
# LIST AN ITEM
# ============================================================

elif st.session_state.current_page == "List an Item":

    st.title("➕ List an Item")

    st.write(
        "Sell something you no longer need or "
        "lend it to another IBS student."
    )


    st.info(
        "🎁 Your first 3 listings are free. Additional listings require a paid listing plan."
    )


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
            "Others"
        ]
    )

    other_category = ""
    if category == "Others":
        other_category = st.text_input(
            "Specify the item category",
            placeholder="Example: Kitchenware, Stationery, Accessories"
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


    location_options = HOSTEL_BLOCKS + [
        "Other / Enter Manually"
    ]


    location_option = st.selectbox(
        "📍 Hostel Block",
        location_options
    )


    if location_option == "Other / Enter Manually":

        location = st.text_input(
            "Enter your hostel/block name",
            placeholder="Enter hostel/block"
        )

    else:

        location = location_option


    description = st.text_area(
        "Description",
        placeholder=(
            "Describe the item's condition, "
            "size, usage, accessories, etc."
        )
    )

    uploaded_image = st.file_uploader(
        "📷 Upload Item Image",
        type=["jpg", "jpeg", "png", "webp"],
        help="Upload a clear photo of the item you want to list."
    )

    if uploaded_image is not None:
        st.image(
            uploaded_image,
            caption="Listing image preview",
            width=300
        )


    if st.button("📤 Publish Listing"):

        if item_name.strip() == "":

            st.warning(
                "Please enter the item name."
            )

        elif category == "Others" and other_category.strip() == "":

            st.warning(
                "Please specify what type of item you are listing."
            )

        elif location.strip() == "":

            st.warning(
                "Please enter your hostel/block."
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
                    (
                        f"Others • {other_category.strip()}"
                        if category == "Others" and other_category.strip()
                        else category
                    ),

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

                "seller_contact":
                    "@ibex_you",

                "location":
                    location,

                "image":
                    (
                        uploaded_image.getvalue()
                        if uploaded_image is not None
                        else None
                    ),

                "transactions":
                    0
            }


            st.session_state.custom_listings.append(
                new_listing
            )


            st.success(
                f"✅ {item_name} has been listed!"
            )

            st.balloons()


# ============================================================
# CHECKOUT
# ============================================================

elif st.session_state.current_page == "Checkout":

    st.title("🛒 Secure Checkout")


    item = st.session_state.selected_item


    if item is None:

        st.warning(
            "No item has been selected."
        )


        if st.button("← Go to Marketplace"):

            st.session_state.current_page = "Marketplace"

            st.rerun()


    else:

        if item.get("image"):
            st.image(
                item["image"],
                width=350
            )

        st.subheader(
            item["item"]
        )


        st.markdown(
            "<span class='verified'>"
            "✓ Verified IBS Seller"
            "</span>",
            unsafe_allow_html=True
        )


        st.write(
            f"Condition: **{item['condition']}**"
        )

        st.write(
            f"Seller: **{item['seller']}**"
        )

        st.write(
            f"📍 Item location: **{item['location']}**"
        )


        st.markdown("---")


        if item["type"] == "Rent":

            days = st.number_input(
                "Rental Duration",
                min_value=1,
                max_value=30,
                value=1
            )

            st.caption(
                "Rental fee is calculated per day."
            )

            base_price = item["price"] * days

        else:

            days = 0

            base_price = item["price"]


        st.subheader("🚚 Delivery")


        delivery_option = st.radio(
            "Choose your option",
            [
                "Self Pickup — FREE",
                "IBeX Campus Delivery — ₹20"
            ]
        )


        if "₹20" in delivery_option:

            delivery_fee = 20

        else:

            delivery_fee = 0


        if item["type"] == "Rent":

            deposit = item["deposit"]

        else:

            deposit = 0


        total = (
            base_price
            + delivery_fee
            + deposit
        )


        st.markdown("---")

        st.subheader("💰 Order Summary")


        summary_col1, summary_col2 = st.columns(2)


        with summary_col1:

            if item["type"] == "Rent":

                st.write(
                    f"Rental Fee ({days} day(s))"
                )

            else:

                st.write(
                    "Product Price"
                )

            st.write("Delivery")

            if item["type"] == "Rent":

                st.write(
                    "Refundable Security Deposit"
                )


        with summary_col2:

            st.write(
                f"₹{base_price}"
            )

            st.write(
                f"₹{delivery_fee}"
            )

            if item["type"] == "Rent":

                st.write(
                    f"₹{deposit}"
                )


        st.markdown("---")


        st.markdown(
            f"## Total Payable: ₹{total}"
        )


        if item["type"] == "Rent":

            st.success(
                f"🔄 ₹{deposit} is a refundable "
                "security deposit."
            )


        st.markdown("---")

        st.subheader("💳 Payment Method")


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

            In a live version, payment would be processed
            through an authorised payment gateway.

            <br><br>

            <b>Your payment details would not be visible
            to the seller.</b>

            </div>
            """, unsafe_allow_html=True)


            st.text_input(
                "UPI ID",
                placeholder="example@upi",
                type="password"
            )


            st.caption(
                "🧪 Prototype Mode — no real payment "
                "will be deducted."
            )


        elif "Card" in payment_method:

            st.markdown("""
            <div class="secure-box">

            🔐 <b>Secure Card Payment</b>

            <br><br>

            In a live implementation, card information
            would be handled directly by the payment gateway.

            <br><br>

            <b>Card details would not be shared with sellers.</b>

            </div>
            """, unsafe_allow_html=True)


            st.text_input(
                "Card Number",
                placeholder="•••• •••• •••• ••••",
                type="password"
            )


            c1, c2 = st.columns(2)


            with c1:

                st.text_input(
                    "Expiry",
                    placeholder="MM/YY"
                )


            with c2:

                st.text_input(
                    "CVV",
                    type="password"
                )


            st.caption(
                "🧪 Prototype Mode — card information "
                "is not processed or stored."
            )


        else:

            st.markdown("""
            <div class="secure-box">

            💵 <b>Cash on Delivery</b>

            <br><br>

            Pay when the item is handed over to you.

            <br><br>

            Your payment information is not required.

            </div>
            """, unsafe_allow_html=True)


        st.markdown("---")


        if "Cash" in payment_method:

            confirm_text = (
                f"📦 Confirm COD — ₹{total}"
            )

        else:

            confirm_text = (
                f"🔒 Pay ₹{total}"
            )


        if st.button(confirm_text):

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

                "Order ID":
                    order_id,

                "Item":
                    item["item"],

                "Image":
                    item.get("image"),

                "Type":
                    item["type"],

                "Seller":
                    item.get("seller", "IBX Student"),

                "Private Contact":
                    item.get("seller_contact", "Private IBeX Contact"),

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

            add_notification(
                "Order confirmed",
                f"Your {item['item']} order ({order_id}) is confirmed. Your private seller chat is now open.",
                "order"
            )

            # In the prototype, items marked as "You" are listings owned by
            # the currently active demo profile. Notify the seller when one
            # of those listings is purchased.
            if item.get("seller") == "You":
                add_notification(
                    "Someone bought your item 🎉",
                    f"Your listing '{item['item']}' has been purchased. Order {order_id} is confirmed.",
                    "seller"
                )
                st.toast(f"🎉 Someone bought your {item['item']}!", icon="🎉")

            st.toast("📦 Order confirmed — private seller chat is open!", icon="📦")

            st.session_state.order_chats[order_id] = [
                {
                    "sender": "IBeX",
                    "text": "Private chat is now open. You can coordinate the handover with the seller here."
                }
            ]


            st.session_state.points += 10


            st.success(
                "✅ Order Confirmed!"
            )


            st.balloons()


            st.markdown(
                f"### Order ID: `{order_id}`"
            )


            st.write(
                f"**Payment:** {payment_status}"
            )


            st.write(
                f"**Amount:** ₹{total}"
            )


            st.write(
                f"**Delivery:** {delivery_option}"
            )


            st.info(
                "⭐ You earned 10 IBeX points!"
            )


            st.caption(
                "Prototype transaction — "
                "no real money has been transferred."
            )


# ============================================================
# MY ORDERS
# ============================================================

elif st.session_state.current_page == "My Orders":

    st.title("📦 My Orders")

    st.caption(
        "Private seller chat becomes available inside IBeX after a purchase or rental is confirmed."
    )

    if len(st.session_state.orders) == 0:

        st.info(
            "You haven't placed any orders yet."
        )

    else:

        for order in st.session_state.orders:

            st.markdown(
                f"""
                <div class="card">

                <h3>{order['Item']}</h3>

                <p>
                🆔 Order ID:
                <b>{order['Order ID']}</b>
                </p>

                <p>
                👤 Seller:
                <b>{order.get('Seller', 'IBX Student')}</b>
                </p>

                <p>
                💰 Amount:
                <b>₹{order['Amount']}</b>
                </p>

                <p>
                💳 Payment:
                {order['Payment']}
                </p>

                <p>
                🚚 Delivery:
                {order['Delivery']}
                </p>

                <p>
                ✅ Status:
                <b>{order['Status']}</b>
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("### 💬 Private Seller Chat")
            st.caption(
                "Your contact details are not displayed publicly. After confirmation, you can communicate with the seller through this private in-app chat."
            )

            order_id = order["Order ID"]

            chat = st.session_state.order_chats.setdefault(
                order_id,
                [
                    {
                        "sender": "IBeX",
                        "text": "Private chat is now open for this confirmed order."
                    }
                ]
            )

            with st.container(border=True):

                for message in chat:

                    if message["sender"] == "You":

                        with st.chat_message("user"):
                            st.write(message["text"])

                    else:

                        with st.chat_message("assistant"):
                            st.write(message["text"])


                message = st.text_input(
                    "Message seller",
                    placeholder="Example: Hi, when can we meet for the handover?",
                    key=f"chat_input_{order_id}"
                )


                if st.button(
                    "💬 Send Message",
                    key=f"send_chat_{order_id}"
                ):

                    if message.strip():

                        chat.append(
                            {
                                "sender": "You",
                                "text": message.strip()
                            }
                        )

                        add_notification(
                            "Private chat message sent",
                            f"Your message about {order['Item']} was sent through the IBeX chat.",
                            "chat"
                        )

                        st.success(
                            "Message sent privately through IBeX."
                        )

                        st.rerun()

                    else:

                        st.warning(
                            "Please enter a message first."
                        )


            st.markdown("---")


# DELIVERY & HELP
# ============================================================

elif st.session_state.current_page == "Delivery & Help":

    st.title("🚚 Delivery & Campus Help")

    st.write(
        "Need a parcel collected from the main gate "
        "or an item brought to your hostel?"
    )

    tab1, tab2 = st.tabs(
        [
            "📤 Request Help",
            "🤝 Help Someone"
        ]
    )

    with tab1:

        request_type = st.selectbox(
            "What do you need?",
            [
                "Parcel Pickup",
                "Item Pickup",
                "Document Delivery",
                "Food / Snack Pickup",
                "Other Assistance"
            ]
        )

        pickup = st.text_input(
            "📍 Pickup Location",
            placeholder="Example: IBS Main Gate"
        )

        delivery_blocks = HOSTEL_BLOCKS + [
            "Other / Enter Manually"
        ]

        drop_option = st.selectbox(
            "📦 Delivery Location",
            delivery_blocks
        )

        if drop_option == "Other / Enter Manually":

            drop = st.text_input(
                "Enter delivery block",
                placeholder="Enter hostel/block"
            )

        else:

            drop = drop_option

        fee = st.number_input(
            "Helper Reward (₹)",
            min_value=10,
            max_value=200,
            value=20
        )

        if st.button("📤 Post Request"):

            if not pickup or not drop:

                st.warning(
                    "Please enter both pickup and delivery locations."
                )

            else:

                request_id = (
                    "DLV-"
                    + datetime.now().strftime("%y%m%d")
                    + "-"
                    + str(uuid.uuid4())[:5].upper()
                )

                request = {
                    "Request ID": request_id,
                    "Task": request_type,
                    "Pickup": pickup,
                    "Drop": drop,
                    "Reward": fee,
                    "Status": "Open",
                    "Requester": st.session_state.profile.get(
                        "name", "IBS Student"
                    ),
                    "Created": datetime.now().strftime(
                        "%d %b %Y, %I:%M %p"
                    )
                }

                st.session_state.help_requests.append(request)

                add_notification(
                    "Delivery request posted",
                    f"Your {request_type.lower()} request is now visible to campus helpers.",
                    "delivery"
                )

                st.success(
                    "✅ Your request has been posted."
                )

                st.info(
                    "🔔 You'll receive an IBeX notification when someone accepts it."
                )

    with tab2:

        sample_tasks = [
            {
                "Request ID": "DLV-DEMO-01",
                "Task": "Parcel Pickup",
                "Pickup": "IBS Main Gate",
                "Drop": "ABCD Block",
                "Reward": 20,
                "Status": "Open",
                "Requester": "IBX Student 118",
                "Created": "19 Sep 2026, 05:20 PM"
            },
            {
                "Request ID": "DLV-DEMO-02",
                "Task": "Snack Pickup",
                "Pickup": "Campus Store",
                "Drop": "QRS Block",
                "Reward": 15,
                "Status": "Open",
                "Requester": "IBX Student 241",
                "Created": "19 Sep 2026, 05:35 PM"
            }
        ]

        all_tasks = sample_tasks + st.session_state.help_requests

        open_tasks = [
            task for task in all_tasks
            if task.get("Status") == "Open"
        ]

        if not open_tasks:
            st.info("No open campus-help requests right now.")

        for i, task in enumerate(open_tasks):

            st.markdown(
                f"""
                <div class="card">
                    <h3>🚚 {task['Task']}</h3>
                    <p><b>Requested by:</b> {task['Requester']}</p>
                    <p>📍 {task['Pickup']} → {task['Drop']}</p>
                    <p>💰 Student Reward: <b>₹{task['Reward']}</b></p>
                    <small>Posted: {task['Created']}</small>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "🤝 Accept Task",
                key=f"delivery_accept_{task['Request ID']}"
            ):

                task["Status"] = "Accepted"
                task["Accepted By"] = st.session_state.profile.get(
                    "name", "IBS Student"
                )

                st.session_state.points += 30

                add_notification(
                    "Delivery help accepted",
                    f"You accepted {task['Task'].lower()} for {task['Requester']}. +30 IBeX points.",
                    "delivery"
                )

                # Notify the requester too when the accepted request belongs
                # to the current demo profile. In a production backend this
                # would be delivered to the requester's account/device.
                current_name = st.session_state.profile.get("name", "IBS Student")
                if task.get("Requester") == current_name:
                    add_notification(
                        "Someone accepted your delivery request ⭐",
                        f"{task.get('Accepted By', 'A campus helper')} accepted your {task['Task'].lower()} request.",
                        "delivery"
                    )
                    st.toast("⭐ Someone accepted your delivery request!", icon="⭐")

                st.toast("⭐ Delivery help accepted — +30 IBeX points!", icon="⭐")
                st.session_state.show_celebration = "stars"

                st.success(
                    "✅ Task accepted!"
                )

                st.info(
                    "⭐ You earned 30 IBeX points for helping the community."
                )

                show_celebration("stars")

            st.markdown("---")


# ============================================================
# ESSENTIAL ASSISTANCE
# ============================================================

elif st.session_state.current_page == "Essential Assistance":

    st.title("🏥 Essential Assistance")

    st.warning(
        "IBeX is intended for basic campus assistance. "
        "Prescription medicines and regulated medical products "
        "would require appropriate institutional and legal controls."
    )

    tab1, tab2 = st.tabs(
        [
            "🆘 Request Essential Help",
            "🤝 Help Someone"
        ]
    )

    with tab1:

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

        requester_location = st.selectbox(
            "📍 Where should the help reach you?",
            HOSTEL_BLOCKS + ["Other / Enter Manually"]
        )

        if requester_location == "Other / Enter Manually":

            requester_location = st.text_input(
                "Enter hostel/block",
                placeholder="Enter your hostel/block"
            )

        helper_reward = st.number_input(
            "Suggested Helper Reward (₹)",
            min_value=0,
            max_value=200,
            value=20
        )

        additional_details = st.text_area(
            "Additional details",
            placeholder="Example: Need it within the next hour."
        )

        if st.button("🏥 Request Assistance"):

            if not requester_location.strip():

                st.warning(
                    "Please enter where the assistance should reach you."
                )

            else:

                request_id = (
                    "ESS-"
                    + datetime.now().strftime("%y%m%d")
                    + "-"
                    + str(uuid.uuid4())[:5].upper()
                )

                essential_request = {
                    "Request ID": request_id,
                    "Need": need,
                    "Urgency": urgency,
                    "Location": requester_location,
                    "Reward": helper_reward,
                    "Details": additional_details,
                    "Status": "Open",
                    "Requester": st.session_state.profile.get(
                        "name", "IBS Student"
                    ),
                    "Created": datetime.now().strftime(
                        "%d %b %Y, %I:%M %p"
                    )
                }

                st.session_state.essential_requests.append(
                    essential_request
                )

                add_notification(
                    "Essential help requested",
                    f"Your request for {need.lower()} has been posted for verified campus helpers.",
                    "help"
                )

                st.success(
                    f"✅ Request posted for {need}."
                )

                st.info(
                    "🔔 You'll receive an IBeX notification when someone accepts your request."
                )

    with tab2:

        sample_essential_requests = [
            {
                "Request ID": "ESS-DEMO-01",
                "Need": "ORS / hydration supplies",
                "Urgency": "Urgent",
                "Location": "U-Block",
                "Reward": 30,
                "Details": "Needed as soon as possible.",
                "Status": "Open",
                "Requester": "IBX Student 326",
                "Created": "19 Sep 2026, 05:40 PM"
            },
            {
                "Request ID": "ESS-DEMO-02",
                "Need": "Sanitary products",
                "Urgency": "Normal",
                "Location": "G-Block",
                "Reward": 20,
                "Details": "Any standard pack is fine.",
                "Status": "Open",
                "Requester": "IBX Student 174",
                "Created": "19 Sep 2026, 05:45 PM"
            }
        ]

        all_essential = (
            sample_essential_requests
            + st.session_state.essential_requests
        )

        open_requests = [
            request for request in all_essential
            if request.get("Status") == "Open"
        ]

        if not open_requests:

            st.info(
                "No open essential-help requests right now."
            )

        for request in open_requests:

            urgency_label = (
                "🔴 URGENT"
                if request["Urgency"] == "Urgent"
                else "🟢 NORMAL"
            )

            st.markdown(
                f"""
                <div class="card">
                    <h3>🏥 {request['Need']}</h3>
                    <p><b>{urgency_label}</b></p>
                    <p><b>Requested by:</b> {request['Requester']}</p>
                    <p>📍 Delivery / Help Location: <b>{request['Location']}</b></p>
                    <p>💰 Suggested Helper Reward: <b>₹{request['Reward']}</b></p>
                    <p>📝 {request['Details'] or 'No additional details provided.'}</p>
                    <small>Posted: {request['Created']}</small>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "🤝 Accept Essential Help",
                key=f"essential_accept_{request['Request ID']}"
            ):

                request["Status"] = "Accepted"
                request["Accepted By"] = st.session_state.profile.get(
                    "name", "IBS Student"
                )

                st.session_state.points += 40

                add_notification(
                    "Essential help accepted",
                    f"You accepted the {request['Need'].lower()} request for {request['Requester']}. +40 IBeX points.",
                    "help"
                )

                # Notify the student who originally requested the help.
                current_name = st.session_state.profile.get("name", "IBS Student")
                if request.get("Requester") == current_name:
                    add_notification(
                        "Someone accepted your essential-help request 💗",
                        f"{request.get('Accepted By', 'A campus helper')} accepted your {request['Need'].lower()} request.",
                        "help"
                    )
                    st.toast("💗 Someone accepted your essential-help request!", icon="💗")

                st.toast("💗 Essential help accepted — +40 IBeX points!", icon="💗")

                st.success(
                    "💗 Essential help accepted!"
                )

                st.info(
                    "💗 You earned 40 IBeX points for helping a fellow student."
                )

                show_celebration("hearts")

            st.markdown("---")


# REWARDS
# ============================================================

elif st.session_state.current_page == "Rewards":

    st.title("⭐ IBeX Rewards")


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Current Points",
            st.session_state.points
        )


    with col2:

        st.metric(
            "Community Status",
            "Trusted Member"
        )


    st.markdown("""
    <div class="reward-box">

    ⭐ <b>Earn while you help.</b>

    <br><br>

    Complete transactions, help other students,
    return rentals on time and contribute to the
    IBeX community to earn points.

    </div>
    """, unsafe_allow_html=True)


    st.markdown("---")


    rewards = pd.DataFrame({

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


    st.subheader(
        "How points are earned"
    )


    st.dataframe(
        rewards,
        use_container_width=True,
        hide_index=True
    )


    st.markdown("---")


    st.subheader("🎁 Redeem Points")


    reward = st.selectbox(
        "Choose a reward",
        [
            "₹20 Delivery Discount — 500 Points",
            "Priority Support — 1000 Points"
        ]
    )


    if st.button("Redeem Reward"):

        st.info(
            "Prototype demonstration: "
            "the reward would be applied to "
            "the user's IBeX account."
        )


# ============================================================
# NOTIFICATIONS
# ============================================================

elif st.session_state.current_page == "Notifications":

    st.title("🔔 Notifications")

    st.caption(
        "IBeX keeps your important activity updates inside the app. "
        "For the live platform, these can be connected to browser/mobile push notifications."
    )

    if len(st.session_state.notifications) == 0:

        st.info("You're all caught up. No notifications yet.")

    else:

        unread = sum(
            1 for n in st.session_state.notifications
            if not n.get("read", False)
        )

        c1, c2 = st.columns([3, 1])

        with c1:
            st.metric("Unread", unread)

        with c2:
            if st.button("✓ Mark all as read"):
                for n in st.session_state.notifications:
                    n["read"] = True
                st.rerun()

        st.markdown("---")

        for idx, notification in enumerate(st.session_state.notifications):

            icon = {
                "success": "✅",
                "help": "💗",
                "delivery": "⭐",
                "chat": "💬",
                "order": "📦"
            }.get(notification.get("kind"), "🔔")

            background = "#FFF8E8" if not notification.get("read") else "#FFFFFF"

            st.markdown(
                f"""
                <div class="card" style="background:{background};">
                    <h4>{icon} {notification['title']}</h4>
                    <p>{notification['message']}</p>
                    <small>{notification['time']}</small>
                </div>
                """,
                unsafe_allow_html=True
            )

            if not notification.get("read"):
                if st.button(
                    "Mark as read",
                    key=f"read_notification_{idx}"
                ):
                    notification["read"] = True
                    st.rerun()


# ============================================================
# PROFILE — OTP LOGIN
# ============================================================

elif st.session_state.current_page == "Profile":

    st.title("👤 My IBeX Profile")


    # ========================================================
    # NOT LOGGED IN
    # ========================================================

    if not st.session_state.otp_verified:

        st.markdown("""
        <div class="auth-card">

            <span class="auth-badge">
                🔐 IBS Verified Access
            </span>

            <h2 style="margin-top:18px;">
                Login to IBeX
            </h2>

            <p style="color:#766B7D;">
                Enter your email address and we'll send
                you a one-time verification code.
            </p>

        </div>
        """, unsafe_allow_html=True)


        st.markdown("")


        email = st.text_input(
            "📧 Email Address",
            value=(
                st.session_state.otp_email
                or ""
            ),
            placeholder="yourname@ibsindia.org"
        )


        if st.button(
            "📨 Send OTP",
            use_container_width=True
        ):

            email_clean = email.strip().lower()


            if not email_clean:

                st.warning(
                    "Please enter your email address."
                )


            elif "@" not in email_clean:

                st.warning(
                    "Please enter a valid email address."
                )


            else:

                # Generate a secure 6-digit OTP
                otp = str(
                    secrets.randbelow(900000) + 100000
                )


                st.session_state.otp = otp

                st.session_state.otp_email = (
                    email_clean
                )

                st.session_state.otp_generated_at = (
                    datetime.now()
                )


                st.success(
                    f"OTP sent to {email_clean}"
                )


                # =================================================
                # PROTOTYPE OTP
                # =================================================
                # In production this should be replaced with an
                # actual email service such as SMTP, Resend,
                # SendGrid, AWS SES, etc.

                st.info(
                    f"🧪 Prototype OTP: **{otp}**"
                )


        # ========================================================
        # OTP VERIFICATION
        # ========================================================

        if st.session_state.otp:

            st.markdown("---")


            st.subheader(
                "🔢 Verify OTP"
            )


            st.caption(
                "Enter the 6-digit OTP sent to "
                f"**{st.session_state.otp_email}**"
            )


            entered_otp = st.text_input(
                "One-Time Password",
                max_chars=6,
                placeholder="123456"
            )


            col1, col2 = st.columns(2)


            with col1:

                if st.button(
                    "✅ Verify OTP",
                    use_container_width=True
                ):

                    otp_age = (
                        datetime.now()
                        - st.session_state.otp_generated_at
                    )


                    # OTP expires after 5 minutes
                    if otp_age > timedelta(minutes=5):

                        st.error(
                            "⏰ OTP expired. "
                            "Please request a new one."
                        )


                        st.session_state.otp = None


                    elif entered_otp == st.session_state.otp:

                        st.session_state.otp_verified = True


                        # Update profile with verified email
                        st.session_state.profile["email"] = (
                            st.session_state.otp_email
                        )


                        # Create a simple display name
                        # from the email address
                        email_username = (
                            st.session_state.otp_email
                            .split("@")[0]
                        )


                        st.session_state.profile["name"] = (
                            email_username
                        )


                        st.session_state.profile["role"] = (
                            "Student"
                        )


                        # Clear OTP after successful verification
                        st.session_state.otp = None

                        st.session_state.otp_generated_at = None


                        st.success(
                            "🎉 Email verified successfully!"
                        )


                        st.balloons()


                        st.rerun()


                    else:

                        st.error(
                            "❌ Incorrect OTP. "
                            "Please try again."
                        )


            with col2:

                if st.button(
                    "🔄 Resend OTP",
                    use_container_width=True
                ):

                    new_otp = str(
                        secrets.randbelow(900000) + 100000
                    )


                    st.session_state.otp = (
                        new_otp
                    )


                    st.session_state.otp_generated_at = (
                        datetime.now()
                    )


                    st.success(
                        "A new OTP has been generated."
                    )


                    # Prototype only
                    st.info(
                        f"🧪 Prototype OTP: "
                        f"**{new_otp}**"
                    )


    # ========================================================
    # LOGGED-IN PROFILE
    # ========================================================

    else:

        profile = st.session_state.profile


        display_name = profile.get(
            "name",
            "IBS Student"
        )


        display_email = profile.get(
            "email",
            ""
        )


        display_role = profile.get(
            "role",
            "Student"
        )


        display_dept = profile.get(
            "department",
            "Not specified"
        )


        display_batch = profile.get(
            "batch",
            "Not specified"
        )


        st.markdown(
            f"""
            <div class="card">

                <h2>{display_name}</h2>

                <p class="verified">
                    ✓ IBS Verified Profile
                </p>

                <p>
                    📧 {display_email}
                </p>

                <p>
                    🎓 {display_dept}
                    · Batch {display_batch}
                </p>

                <p>
                    👤 Role: {display_role}
                </p>

                <p>
                    ⭐ {st.session_state.points}
                    IBeX Points
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


        st.success(
            "🔐 Your email has been verified."
        )


        st.metric(
            "⭐ IBeX Points",
            st.session_state.points
        )


        st.markdown("---")


        st.subheader(
            "🔐 Trust & Privacy"
        )


        trust_col1, trust_col2 = st.columns(2)


        with trust_col1:

            st.write(
                "✓ IBS-only verified access"
            )

            st.write(
                "✓ Ratings and reviews"
            )

            st.write(
                "✓ OTP-based item handover"
            )

            st.write(
                "✓ Refundable rental deposits"
            )


        with trust_col2:

            st.write(
                "✓ Masked user identity"
            )

            st.write(
                "✓ Secure payment processing"
            )

            st.write(
                "✓ Payment details hidden from sellers"
            )

            st.write(
                "✓ Community accountability"
            )


        st.markdown("---")


        if st.button(
            "🚪 Logout"
        ):

            st.session_state.otp_verified = False

            st.session_state.otp = None

            st.session_state.otp_email = None

            st.session_state.otp_generated_at = None


            # Reset demo profile
            st.session_state.profile = {

                "name":
                    "IBS Student",

                "email":
                    "demo@ibsindia.org",

                "department":
                    "MBA",

                "batch":
                    "2026",

                "role":
                    "Student",
            }


            st.success(
                "You have been logged out."
            )


            st.rerun()


# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "IBeX — IBS Exchange | "
    "Customer-Facing Prototype | "
    "Secure • Sustainable • Community Driven"
)
