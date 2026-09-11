import streamlit as st
from PIL import Image
import uuid

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Waste to Wealth Management",
    page_icon="♻️",
    layout="wide"
)

# =========================================================
# TITLE
# =========================================================

st.title("♻️ Waste to Wealth Management")
st.subheader("Turn Waste into Value 🌱")

st.write(
    "A smart platform that helps users identify waste, understand "
    "its proper treatment, find waste collectors, discover DIY ideas, "
    "calculate environmental impact and understand the value of waste."
)

# =========================================================
# AWARENESS
# =========================================================

st.header("🌍 Waste Management Awareness")

st.info(
    "Proper waste management helps reduce pollution, save natural "
    "resources, protect our environment and create useful products "
    "from materials that would otherwise become waste."
)

# =========================================================
# IMAGE UPLOAD
# =========================================================

st.header("📷 Upload Waste Image")

uploaded_file = st.file_uploader(
    "Upload a picture of the waste item",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Waste Image",
        use_container_width=True
    )

    st.success("Waste image uploaded successfully! ✅")

# =========================================================
# WASTE WEIGHT
# =========================================================

st.header("⚖️ Waste Weight")

weight = st.number_input(
    "Enter approximate waste weight (kg)",
    min_value=0.0,
    step=0.1
)

if weight == 0:

    st.warning(
        "Please enter the approximate weight of the waste."
    )

# =========================================================
# MATERIAL
# =========================================================

st.header("🧱 Select Waste Material")

materials = [
    "Plastic",
    "Paper",
    "Cardboard",
    "Metal",
    "Glass",
    "Organic / Biodegradable",
    "Textile / Cloth",
    "E-waste",
    "Wood",
    "Other"
]

material = st.selectbox(
    "What type of material is the waste made from?",
    materials
)

# =========================================================
# WASTE ANALYSIS
# =========================================================

st.header("🔎 Waste Analysis")

if material == "Plastic":

    treatment = "♻️ Recyclable"

    why = (
        "Plastic should be recycled or reused because it can remain "
        "in the environment for a very long time."
    )

    benefits = (
        "Recycling plastic helps reduce pollution, save raw materials "
        "and reduce the amount of waste sent to landfills."
    )

elif material == "Paper":

    treatment = "♻️ Recyclable / 🌱 Biodegradable"

    why = (
        "Paper can usually be recycled and can also naturally "
        "decompose under suitable conditions."
    )

    benefits = (
        "Recycling paper helps save trees, water and energy."
    )

elif material == "Cardboard":

    treatment = "♻️ Recyclable / 🌱 Biodegradable"

    why = (
        "Cardboard can usually be recycled into new paper-based products."
    )

    benefits = (
        "Recycling cardboard reduces landfill waste and saves resources."
    )

elif material == "Metal":

    treatment = "♻️ Recyclable"

    why = (
        "Many metals can be recycled repeatedly without losing "
        "their basic properties."
    )

    benefits = (
        "Metal recycling saves energy, reduces mining and conserves "
        "natural resources."
    )

elif material == "Glass":

    treatment = "♻️ Recyclable"

    why = (
        "Glass can be recycled and converted into new glass products."
    )

    benefits = (
        "Glass recycling saves raw materials and reduces landfill waste."
    )

elif material == "Organic / Biodegradable":

    treatment = "🌱 Compostable / Biodegradable"

    why = (
        "Organic waste can naturally decompose and can also be "
        "converted into compost."
    )

    benefits = (
        "Composting produces useful organic manure for plants and gardens."
    )

elif material == "Textile / Cloth":

    treatment = "♻️ Reusable / Recyclable"

    why = (
        "Old clothes can often be reused, donated or converted "
        "into new useful products."
    )

    benefits = (
        "Reusing textiles reduces textile waste and saves resources."
    )

elif material == "E-waste":

    treatment = "♻️ Specialized Recycling"

    why = (
        "Electronic waste should be handled through appropriate "
        "e-waste recycling systems."
    )

    benefits = (
        "Proper e-waste recycling helps recover valuable materials "
        "and reduces environmental pollution."
    )

elif material == "Wood":

    treatment = "♻️ Reusable / 🌱 Biodegradable"

    why = (
        "Wood can often be reused, repaired or, when untreated, "
        "eventually decomposed."
    )

    benefits = (
        "Reusing wood reduces the need for new raw materials."
    )

else:

    treatment = "🔎 Depends on Material"

    why = (
        "The correct treatment depends on the exact material "
        "and condition of the item."
    )

    benefits = (
        "Correct segregation helps ensure that the waste is handled safely."
    )

st.success(
    f"Recommended Treatment: {treatment}"
)

st.write("### ❓ Why should it be treated this way?")

st.write(why)

st.write("### 🌱 How is it useful?")

st.write(benefits)

# =========================================================
# WASTE IMPACT CALCULATOR
# =========================================================

st.header("📊 Waste Impact Calculator")

st.write(
    "This section gives an approximate idea of how your waste "
    "can contribute to recycling, reuse and environmental protection."
)

# Approximate recyclable/reusable percentage
impact_percentages = {
    "Plastic": 90,
    "Paper": 85,
    "Cardboard": 90,
    "Metal": 95,
    "Glass": 90,
    "Organic / Biodegradable": 85,
    "Textile / Cloth": 75,
    "E-waste": 80,
    "Wood": 80,
    "Other": 50
}

impact_percentage = impact_percentages[material]

if weight > 0:

    useful_weight = weight * impact_percentage / 100
    landfill_reduction = useful_weight

    # Approximate environmental score
    environmental_score = min(
        100,
        round((weight * impact_percentage) * 2)
    )

    # Approximate economic value
    estimated_value_rates = {
        "Plastic": 20,
        "Paper": 10,
        "Cardboard": 8,
        "Metal": 45,
        "Glass": 5,
        "Organic / Biodegradable": 3,
        "Textile / Cloth": 15,
        "E-waste": 50,
        "Wood": 8,
        "Other": 2
    }

    estimated_rate = estimated_value_rates[material]
    estimated_value = weight * estimated_rate

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "♻️ Useful Waste",
            f"{useful_weight:.2f} kg"
        )

    with col2:

        st.metric(
            "🗑️ Landfill Reduction",
            f"{landfill_reduction:.2f} kg"
        )

    with col3:

        st.metric(
            "💰 Estimated Value",
            f"₹{estimated_value:.2f}"
        )

    with col4:

        st.metric(
            "🌍 Eco Score",
            f"{environmental_score}/100"
        )

    st.info(
        f"Approximately {impact_percentage}% of this type of waste "
        f"may be reusable, recyclable, compostable or recoverable "
        f"under suitable conditions."
    )

else:

    st.info(
        "Enter the waste weight above to calculate the estimated impact."
    )

# =========================================================
# WASTE STATISTICS DASHBOARD
# =========================================================

st.header("📈 Waste Statistics Dashboard")

if weight > 0:

    if material in [
        "Plastic",
        "Paper",
        "Cardboard",
        "Metal",
        "Glass",
        "Textile / Cloth",
        "E-waste",
        "Wood"
    ]:

        recyclable_weight = weight * impact_percentage / 100
        non_recyclable_weight = weight - recyclable_weight
        reusable_weight = weight * 0.30

    elif material == "Organic / Biodegradable":

        recyclable_weight = 0
        reusable_weight = weight * 0.85
        non_recyclable_weight = weight - reusable_weight

    else:

        recyclable_weight = weight * 0.50
        reusable_weight = weight * 0.25
        non_recyclable_weight = weight - recyclable_weight

    if non_recyclable_weight < 0:
        non_recyclable_weight = 0

    if reusable_weight > weight:
        reusable_weight = weight

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "⚖️ Total Waste",
            f"{weight:.2f} kg"
        )

    with col2:

        st.metric(
            "♻️ Recyclable / Recoverable",
            f"{recyclable_weight:.2f} kg"
        )

    with col3:

        st.metric(
            "🪴 Reusable / Useful",
            f"{reusable_weight:.2f} kg"
        )

    with col4:

        st.metric(
            "🗑️ Remaining Waste",
            f"{non_recyclable_weight:.2f} kg"
        )

    st.write("### 📊 Waste Distribution")

    chart_data = {
        "Category": [
            "Recyclable / Recoverable",
            "Reusable / Useful",
            "Remaining Waste"
        ],
        "Weight (kg)": [
            round(recyclable_weight, 2),
            round(reusable_weight, 2),
            round(non_recyclable_weight, 2)
        ]
    }

    st.bar_chart(
        chart_data,
        x="Category",
        y="Weight (kg)"
    )

else:

    st.info(
        "Enter waste weight to generate your waste statistics."
    )

# =========================================================
# WASTE HERO ACHIEVEMENT
# =========================================================

st.header("🏆 Waste Hero Achievement")

if weight > 0:

    if environmental_score >= 80:

        st.success(
            "🏆🌍 ECO WARRIOR"
        )

        st.write(
            "Amazing! Your waste has a high recovery potential. "
            "You are helping reduce waste and protect the environment. 💚"
        )

    elif environmental_score >= 50:

        st.success(
            "♻️🌱 RECYCLING HERO"
        )

        st.write(
            "Great job! Your waste can be given a useful second life "
            "through proper recycling or reuse. 🌱"
        )

    else:

        st.info(
            "🌱 WASTE MANAGEMENT BEGINNER"
        )

        st.write(
            "Every small step matters! Proper segregation is the "
            "first step towards a cleaner planet. 💚"
        )

    st.write(
        "🎖️ Achievement unlocked for taking action towards "
        "responsible waste management!"
    )

else:

    st.info(
        "Enter your waste weight to unlock your Waste Hero achievement. 🏆"
    )

# =========================================================
# DIY IDEAS
# =========================================================

diy_ideas = {

    "Plastic": [
        "🌱 Plastic Bottle Planter",
        "🪴 Hanging Bottle Garden",
        "🖊️ Plastic Bottle Pen Stand",
        "🐦 Plastic Bottle Bird Feeder",
        "💡 Plastic Bottle Lampshade",
        "🧺 Plastic Bottle Storage Container",
        "🌸 Plastic Bottle Flower Decoration",
        "🧹 Plastic Bottle Mini Broom",
        "🎨 Plastic Bottle Wall Decoration",
        "💧 Self-Watering Bottle Planter",
        "🧸 Plastic Bottle Toy",
        "📦 Plastic Bottle Organizer",
        "🕯️ Decorative Bottle Holder",
        "🌿 Vertical Bottle Garden",
        "🎨 Plastic Bottle Craft"
    ],

    "Paper": [
        "📔 Handmade Paper Notebook",
        "🌸 Paper Flower Decoration",
        "🖼️ Paper Photo Frame",
        "🎁 Paper Gift Box",
        "📜 Paper Wall Art",
        "🧺 Paper Storage Basket",
        "🦋 Paper Butterfly Decoration",
        "🌳 Paper Tree Decoration",
        "💌 Handmade Greeting Card",
        "🎨 Paper Collage Art",
        "⭐ Paper Star Decoration",
        "🏠 Paper Miniature House",
        "🎭 Paper Mask",
        "📚 Paper Bookmark",
        "🪅 Paper Decorative Hanging"
    ],

    "Cardboard": [
        "📚 Cardboard Book Organizer",
        "🏠 Cardboard Doll House",
        "🚗 Cardboard Toy Car",
        "🗂️ Cardboard Desk Organizer",
        "🖼️ Cardboard Photo Frame",
        "📦 Cardboard Storage Box",
        "💻 Cardboard Laptop Stand",
        "📱 Cardboard Mobile Stand",
        "🎨 Cardboard Wall Art",
        "🏰 Cardboard Mini Castle",
        "🐱 Cardboard Cat House",
        "🎯 Cardboard Board Game",
        "✏️ Cardboard Pen Holder",
        "🧩 Cardboard Puzzle",
        "🌸 Cardboard Flower Decoration"
    ],

    "Metal": [
        "🪴 Tin Can Planter",
        "🖊️ Metal Can Pen Stand",
        "🕯️ Tin Can Candle Holder",
        "💡 Tin Can Lantern",
        "🌸 Metal Can Flower Pot",
        "🧺 Metal Can Storage Container",
        "🎨 Painted Tin Can Decoration",
        "🐦 Metal Can Bird Feeder",
        "🧵 Metal Can Craft Organizer",
        "🏠 Metal Can Home Decoration",
        "🪴 Hanging Metal Planter",
        "🎨 Metal Wall Art",
        "🔔 Metal Can Wind Chime",
        "🧰 Small Metal Tool Organizer",
        "🌱 Mini Herb Garden"
    ],

    "Glass": [
        "🌸 Glass Jar Flower Vase",
        "🕯️ Glass Jar Candle Holder",
        "🌱 Glass Jar Plant Terrarium",
        "💡 Glass Jar Lantern",
        "🪴 Glass Jar Planter",
        "🍪 Glass Jar Storage Container",
        "🎨 Painted Glass Jar Decoration",
        "💰 Glass Jar Coin Bank",
        "🧂 Glass Jar Spice Container",
        "🌈 Colored Glass Jar Decoration",
        "🌿 Glass Jar Herb Garden",
        "🎁 Glass Jar Gift Container",
        "🖼️ Glass Jar Photo Decoration",
        "✨ Glass Jar Light Holder",
        "🏠 Glass Jar Home Decor"
    ],

    "Organic / Biodegradable": [
        "🌱 Homemade Compost",
        "🌿 Kitchen Waste Plant Fertilizer",
        "🌳 Banana Peel Plant Fertilizer",
        "🥬 Vegetable Scrap Compost",
        "🍊 Citrus Peel Cleaner",
        "🌱 Seed Starter",
        "🌿 Natural Plant Mulch",
        "🍌 Banana Peel Fertilizer",
        "🌾 Dry Leaves Garden Compost",
        "🌱 Kitchen Waste Compost Bin",
        "🌸 Flower Compost",
        "🌿 Vegetable Scrap Soil Mix",
        "🍂 Dry Leaf Decoration",
        "🌱 Homemade Organic Garden Mix",
        "♻️ Mini Home Compost System"
    ],

    "Textile / Cloth": [
        "👜 Old T-Shirt Tote Bag",
        "🧸 Cloth Scrap Soft Toy",
        "🌸 Fabric Flower Decoration",
        "🧺 Old Clothes Storage Basket",
        "🪴 Fabric Plant Holder",
        "🧣 Old Scarf Wall Decoration",
        "🛏️ Old Clothes Cushion Cover",
        "🎀 Fabric Hair Bows",
        "🧵 Patchwork Wall Hanging",
        "👜 Denim Jeans Bag",
        "📚 Fabric Book Cover",
        "🧸 Sock Puppet",
        "🌈 Cloth Scrap Rug",
        "🎨 Fabric Scrap Artwork",
        "🧺 Old T-Shirt Storage Bag"
    ],

    "E-waste": [
        "⌨️ Keyboard Key Art",
        "🖼️ Circuit Board Wall Art",
        "🧩 Computer Parts Decoration",
        "🕰️ Old Electronics Clock",
        "🎨 Circuit Board Frame",
        "🖊️ Electronics Desk Decoration",
        "💡 Safe Electronic Parts Art",
        "🧲 Old Hard Drive Decoration",
        "🖼️ Electronics Photo Frame",
        "🎨 Keyboard Key Artwork",
        "🏠 Old Computer Case Decoration",
        "📦 Electronics Parts Organizer",
        "🎭 Electronic Parts Art Project",
        "🖼️ Circuit Board Display",
        "♻️ Creative E-waste Art"
    ],

    "Wood": [
        "🪴 Wooden Planter",
        "📚 Wooden Book Shelf",
        "🖼️ Wooden Photo Frame",
        "🕯️ Wooden Candle Holder",
        "🪵 Wooden Wall Art",
        "🔑 Wooden Key Holder",
        "🪴 Wooden Plant Stand",
        "📱 Wooden Mobile Stand",
        "🖊️ Wooden Pen Holder",
        "🐦 Wooden Bird House",
        "🧺 Wooden Storage Box",
        "🎨 Painted Wooden Decoration",
        "🏠 Wooden Miniature House",
        "🧩 Wooden DIY Puzzle",
        "🪵 Wooden Wall Shelf"
    ],

    "Other": [
        "🎨 Waste Material Wall Art",
        "🪴 Recycled Material Planter",
        "📦 DIY Storage Organizer",
        "🖼️ Recycled Photo Frame",
        "🕯️ Decorative Waste Candle Holder",
        "🌸 Recycled Flower Decoration",
        "🎁 DIY Gift Box",
        "🧺 Waste Material Storage Basket",
        "🏠 Miniature Recycled House",
        "🎨 Waste Material Collage",
        "🧸 DIY Recycled Toy",
        "📱 DIY Mobile Stand",
        "🖊️ DIY Desk Organizer",
        "🌱 Recycled Garden Decoration",
        "♻️ Creative Recycled Art"
    ]
}

st.header("🎨 DIY & Upcycling Ideas")

ideas = diy_ideas[material]

for i in range(0, len(ideas), 3):

    cols = st.columns(3)

    for j in range(3):

        if i + j < len(ideas):

            with cols[j]:

                st.markdown(
                    f"""
                    <div style="
                        border: 1px solid #cccccc;
                        border-radius: 12px;
                        padding: 15px;
                        margin-bottom: 10px;
                        min-height: 75px;
                        background-color: #f7fff9;
                        color: #222222;
                    ">
                        <b>{ideas[i + j]}</b>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# =========================================================
# WASTE COLLECTORS
# =========================================================

st.header("📍 Find Nearby Waste Collectors")

location = st.text_input(
    "Enter your location",
    placeholder="Example: Hadapsar"
)

other_location = st.text_input(
    "Optional: Enter another location"
)

partners = {

    "Hadapsar": [
        {
            "name": "Green Earth Waste Collection",
            "type": "Recyclable Waste Collector"
        },
        {
            "name": "Eco Waste Solutions",
            "type": "Plastic & Paper Collector"
        }
    ],

    "Pune": [
        {
            "name": "Pune Green Recycling",
            "type": "Recycling Partner"
        },
        {
            "name": "Clean City Waste Management",
            "type": "Waste Collection Partner"
        }
    ],

    "Kharadi": [
        {
            "name": "Eco Kharadi Recycling",
            "type": "Recycling Partner"
        }
    ]
}

if st.button(
    "🔍 Find Waste Collectors",
    use_container_width=True
):

    search_location = location.strip().lower()

    found = False

    for area, partner_list in partners.items():

        if area.lower() in search_location:

            found = True

            st.success(
                f"Demo waste collectors available in {area}"
            )

            for partner in partner_list:

                st.markdown(
                    f"""
                    <div style="
                        border: 1px solid #cccccc;
                        border-radius: 12px;
                        padding: 15px;
                        margin-bottom: 10px;
                        background-color: #f7fff9;
                        color: #222222;
                    ">
                        <h4 style="color:#198754;">
                            ♻️ {partner["name"]}
                        </h4>

                        <p style="color:#333333;">
                            {partner["type"]}
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.button(
                    "📞 Contact Partner",
                    key=f"contact_{area}_{partner['name']}"
                )

    if not found:

        st.warning(
            "No demo partner found. Try Hadapsar, Pune or Kharadi."
        )

# =========================================================
# CUSTOMER PAYMENT
# =========================================================

st.header("💰 Customer Payment")

st.info(
    "This is a demo payment system for the project. "
    "It does not transfer real money."
)

payment_method = st.selectbox(
    "Select Payment Method",
    [
        "📷 Demo QR Payment",
        "💵 Cash on Delivery (COD)"
    ]
)

payment_material = st.selectbox(
    "Select Waste Material for Payment",
    materials,
    key="payment_material"
)

payment_weight = st.number_input(
    "Enter collected waste weight (kg)",
    min_value=0.0,
    step=0.1,
    key="payment_weight"
)

rate_per_kg = st.number_input(
    "Enter rate per kg (₹)",
    min_value=0.0,
    step=1.0,
    key="rate_per_kg"
)

payment_amount = payment_weight * rate_per_kg

st.metric(
    "💵 Customer Will Receive",
    f"₹{payment_amount:.2f}"
)

if payment_amount > 0:

    st.success(
        f"Customer will receive ₹{payment_amount:.2f} "
        f"for {payment_weight:.1f} kg of {payment_material}."
    )

# =========================================================
# QR PAYMENT
# =========================================================

if payment_method == "📷 Demo QR Payment":

    st.header("📷 Demo QR Customer Payment")

    st.warning(
        "⚠️ This is only a demo QR scanner. "
        "It does not access a real camera, bank account or UPI account."
    )

    if "customer_payment_id" not in st.session_state:

        st.session_state.customer_payment_id = None

    st.markdown(
        """
        <div style="
            border: 3px dashed #00b894;
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            margin-top: 10px;
            margin-bottom: 15px;
            background-color: #f1fff9;
            color: #222222;
        ">

            <div style="font-size: 65px;">
                ▦
            </div>

            <h3 style="color: #222222;">
                QR SCANNER
            </h3>

            <p style="color: #222222;">
                Place customer's QR code inside this scanner area
            </p>

            <p style="color: #222222;">
                🔐 Customer bank details remain private
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "📷 Scan Customer QR",
        use_container_width=True
    ):

        st.session_state.customer_payment_id = (
            "CUS-" + uuid.uuid4().hex[:8].upper()
        )

        st.success(
            "✅ Customer QR scanned successfully!"
        )

    if st.session_state.customer_payment_id:

        st.info(
            f"Customer ID: "
            f"**{st.session_state.customer_payment_id}**"
        )

        waste_collected = st.checkbox(
            "I confirm that the waste has been collected from the customer.",
            key="qr_waste_collected"
        )

        if st.button(
            "💳 Pay Customer",
            use_container_width=True
        ):

            if not waste_collected:

                st.error(
                    "Please confirm that the waste has been collected."
                )

            elif payment_weight <= 0:

                st.error(
                    "Please enter the waste weight."
                )

            elif rate_per_kg <= 0:

                st.error(
                    "Please enter the rate per kg."
                )

            else:

                transaction_id = (
                    "TXN-" + uuid.uuid4().hex[:10].upper()
                )

                st.success(
                    "🎉 Demo payment completed successfully!"
                )

                st.write(
                    f"**Material:** {payment_material}"
                )

                st.write(
                    f"**Weight:** {payment_weight:.1f} kg"
                )

                st.write(
                    f"**Amount:** ₹{payment_amount:.2f}"
                )

                st.write(
                    f"**Transaction ID:** {transaction_id}"
                )

                st.info(
                    "This is a simulated transaction for the project. "
                    "No real money was transferred."
                )

# =========================================================
# COD PAYMENT
# =========================================================

else:

    st.header("💵 Cash on Delivery (COD)")

    st.info(
        "The person buying/collecting the waste can pay the customer "
        "in cash after collecting the waste."
    )

    if payment_amount > 0:

        st.success(
            f"Cash payment amount: ₹{payment_amount:.2f}"
        )

    payment_proof = st.file_uploader(
        "Upload the picture for proof of payment",
        type=["jpg", "jpeg", "png"],
        key="cod_payment_proof"
    )

    if payment_proof is not None:

        proof_image = Image.open(payment_proof)

        st.image(
            proof_image,
            caption="Payment Proof",
            use_container_width=True
        )

        st.success(
            "Payment proof uploaded successfully! ✅"
        )

    else:

        st.warning(
            "Please upload payment proof."
        )

    payer_confirmation = st.checkbox(
        f"I confirm that I have paid ₹{payment_amount:.2f} to the customer.",
        key="payer_confirmation"
    )

    customer_confirmation = st.checkbox(
        f"I confirm that I have received ₹{payment_amount:.2f} "
        "from the person who collected/bought my waste.",
        key="customer_confirmation"
    )

    if st.button(
        "✅ Complete COD Payment",
        use_container_width=True
    ):

        if payment_proof is None:

            st.error(
                "Please upload payment proof."
            )

        elif not payer_confirmation:

            st.error(
                "Please confirm that the payment was made."
            )

        elif not customer_confirmation:

            st.error(
                "Please confirm that the customer received the payment."
            )

        elif payment_weight <= 0:

            st.error(
                "Please enter the waste weight."
            )

        elif rate_per_kg <= 0:

            st.error(
                "Please enter the rate per kg."
            )

        else:

            cod_transaction_id = (
                "COD-" + uuid.uuid4().hex[:10].upper()
            )

            st.success(
                "🎉 COD payment completed successfully!"
            )

            st.write(
                f"**Material:** {payment_material}"
            )

            st.write(
                f"**Weight:** {payment_weight:.1f} kg"
            )

            st.write(
                f"**Amount:** ₹{payment_amount:.2f}"
            )

            st.write(
                f"**Transaction ID:** {cod_transaction_id}"
            )

            st.success(
                "✅ Both payer and customer have confirmed the payment."
            )

            st.info(
                "This COD feature is a demo/project feature. "
                "It does not process real payments."
            )

# =========================================================
# WASTE TO WEALTH
# =========================================================

st.header("♻️ Waste to Wealth")

st.write(
    "Waste can become a valuable resource when it is properly "
    "segregated, recycled, reused or converted into useful products."
)

col1, col2, col3 = st.columns(3)

with col1:

    st.success("♻️ Recycling")

    st.write(
        "Recyclable materials can be processed and converted "
        "into new products."
    )

with col2:

    st.success("🌱 Composting")

    st.write(
        "Organic waste can be converted into useful compost "
        "for plants and agriculture."
    )

with col3:

    st.success("💰 Income")

    st.write(
        "Collected recyclable waste can have economic value "
        "when sold to appropriate collectors."
    )

# =========================================================
# CUSTOMER FEEDBACK
# =========================================================

st.header("⭐ Customer Feedback")

st.write(
    "Your feedback helps us improve the Waste to Wealth Management "
    "platform. Rating and feedback are completely optional."
)

rating = st.radio(
    "How would you rate your experience?",
    [
        "⭐ 1 - Very Poor",
        "⭐⭐ 2 - Poor",
        "⭐⭐⭐ 3 - Average",
        "⭐⭐⭐⭐ 4 - Good",
        "⭐⭐⭐⭐⭐ 5 - Excellent"
    ],
    index=None,
    horizontal=True
)

feedback = st.text_area(
    "💬 Share your feedback (Optional)",
    placeholder="Tell us what you liked or what we can improve...",
    height=120
)

# =========================================================
# SUBMIT & FINISH
# =========================================================

if st.button(
    "💚 Submit & Finish",
    use_container_width=True
):

    if rating is not None or feedback.strip() != "":

        st.success(
            "🎉 Thank you for your valuable feedback!"
        )

        if rating is not None:

            st.write(
                f"⭐ Your Rating: **{rating}**"
            )

        if feedback.strip() != "":

            st.write("💬 Your Feedback:")

            st.info(
                feedback
            )

    else:

        st.info(
            "No feedback submitted — that's completely okay! 😊"
        )

    st.balloons()

    # =====================================================
    # FINAL THANK YOU MESSAGE
    # =====================================================

    st.success(
        "🌱♻️ You did something wonderful today! 💚"
    )

    st.write(
        "✨ Your old item is getting a second chance "
        "instead of becoming waste. 🥰"
    )

    st.write(
        "🌍 Small choices like yours make our planet "
        "a little happier! 💚"
    )

    st.write(
        "🪴 Thank you for being a part of "
        "Waste to Wealth! ♻️"
    )

    st.write(
        "🌸 Keep reusing • Keep recycling • "
        "Keep making a difference! 🦋✨"
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.success(
    "🌱 Reduce • Reuse • Recycle • Recover • Rebuild"
)

st.caption(
    "Waste to Wealth Management Project ♻️"
)