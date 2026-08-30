
import streamlit as st
import pandas as pd
import uuid
from datetime import datetime


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="IBeX | IBS Exchange",
    page_icon="🟣",
    layout="wide"
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
        '<div class="main-title">🟣 IBeX</div>',
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

nav6, nav7, nav8, nav9 = st.columns(4)


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
        "🎁 IBeX Freemium Model: "
        "Initial listings are free. "
        "Additional listings can be supported through "
        "paid listing plans/subscriptions."
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


    if st.button("📤 Publish Listing"):

        if item_name.strip() == "":

            st.warning(
                "Please enter the item name."
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


# ============================================================
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

                request = {

                    "Task":
                        request_type,

                    "Pickup":
                        pickup,

                    "Drop":
                        drop,

                    "Reward":
                        fee,

                    "Status":
                        "Open"
                }


                st.session_state.help_requests.append(
                    request
                )


                st.success(
                    "✅ Your request has been posted."
                )


    with tab2:

        sample_tasks = [

            {
                "Task":
                    "Parcel Pickup",

                "Pickup":
                    "IBS Main Gate",

                "Drop":
                    "ABCD Block",

                "Reward":
                    20,

                "Status":
                    "Open"
            },

            {
                "Task":
                    "Snack Pickup",

                "Pickup":
                    "Campus Store",

                "Drop":
                    "QRS Block",

                "Reward":
                    15,

                "Status":
                    "Open"
            }
        ]


        all_tasks = (
            sample_tasks
            + st.session_state.help_requests
        )


        for i, task in enumerate(all_tasks):

            st.markdown(
                f"### {task['Task']}"
            )


            st.write(
                f"📍 {task['Pickup']} "
                f"→ {task['Drop']}"
            )


            st.write(
                f"💰 Student Reward: "
                f"₹{task['Reward']}"
            )


            if st.button(
                "🤝 Accept Task",
                key=f"task_{i}"
            ):

                st.session_state.points += 30


                st.success(
                    "✅ Task accepted!"
                )


                st.info(
                    "⭐ You earned 30 IBeX points "
                    "for helping the community."
                )


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
        "Suggested Helper Reward (₹)",
        min_value=0,
        max_value=200,
        value=20
    )


    if st.button("🏥 Request Assistance"):

        st.success(
            f"✅ Request posted for {need}."
        )


        st.info(
            "Only verified IBS users can respond."
        )


# ============================================================
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
            "1 Free Listing — 750 Points",
            "Priority Listing — 1000 Points"
        ]
    )


    if st.button("Redeem Reward"):

        st.info(
            "Prototype demonstration: "
            "the reward would be applied to "
            "the user's IBeX account."
        )


# ============================================================
# PROFILE
# ============================================================

elif st.session_state.current_page == "Profile":

    st.title("👤 My IBeX Profile")


    st.markdown("""
    <div class="card">

    <h2>IBX Student 001</h2>

    <p class="verified">
    ✓ IBS Verified Profile
    </p>

    <p>
    ⭐ 4.8 User Rating
    </p>

    <p>
    🔄 16 Successful Transactions
    </p>

    <p>
    🏆 Trusted Community Member
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.metric(
        "⭐ IBeX Points",
        st.session_state.points
    )


    st.markdown("---")


    st.subheader("🔐 Trust & Privacy")


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


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "IBeX — IBS Exchange | "
    "Customer-Facing Prototype | "
    "Secure • Sustainable • Community Driven"
)
