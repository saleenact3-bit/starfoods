from flask import Flask, render_template_string

app = Flask(__name__)

items = [
    {"name": "Chocolate Cake", "price": 450, "emoji": "🍫🍰"},
    {"name": "Birthday Cake", "price": 550, "emoji": "🎂"},
    {"name": "Red Velvet Cake", "price": 600, "emoji": "❤️🍰"},
    {"name": "Black Forest Cake", "price": 500, "emoji": "🍒🍰"},
    {"name": "Butter Cake", "price": 350, "emoji": "🧈🍰"},
    {"name": "Cream Cake", "price": 400, "emoji": "🍰✨"},
    {"name": "Banana Chips", "price": 120, "emoji": "🍌"},
    {"name": "Potato Chips", "price": 100, "emoji": "🥔"},
    {"name": "Murukku", "price": 150, "emoji": "🥨"},
    {"name": "Mixture", "price": 130, "emoji": "🥜"},
    {"name": "Nippattu", "price": 140, "emoji": "🍪"},
    {"name": "Sweet Cookies", "price": 180, "emoji": "🍪"},
]

HTML = """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Starfoods Bakery</title>

<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: Arial, sans-serif;
    background: #fff8f1;
    color: #3d2115;
    overflow-x: hidden;
}


/* ================= NAVBAR ================= */

.navbar {
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;

    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 18px 8%;

    background: rgba(255,255,255,0.90);
    backdrop-filter: blur(12px);

    box-shadow: 0 3px 20px rgba(0,0,0,0.08);
}

.logo {
    font-size: 30px;
    font-weight: 900;
    color: #d85b28;
    letter-spacing: 1px;
}

.logo span {
    color: #6b351e;
}

.nav-links {
    display: flex;
    gap: 30px;
}

.nav-links a {
    text-decoration: none;
    color: #4b2b20;
    font-weight: bold;
    transition: 0.3s;
}

.nav-links a:hover {
    color: #e7652d;
}


/* ================= HERO ================= */

.hero {
    min-height: 100vh;
    padding: 150px 8% 80px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    position: relative;
    overflow: hidden;

    background:
        radial-gradient(circle at 80% 20%, #ffd6b8, transparent 30%),
        linear-gradient(135deg, #fff7ef, #ffe3cf);
}

.hero-content {
    max-width: 600px;
    z-index: 2;

    animation: slideLeft 1s ease;
}

.hero h1 {
    font-size: 65px;
    line-height: 1.05;
    margin-bottom: 20px;
}

.hero h1 span {
    color: #df612b;
}

.hero p {
    font-size: 20px;
    line-height: 1.7;
    color: #765447;
    margin-bottom: 30px;
}

.hero-btn {
    display: inline-block;

    padding: 15px 30px;

    background: #df612b;
    color: white;

    border-radius: 30px;

    text-decoration: none;
    font-weight: bold;

    box-shadow: 0 10px 25px rgba(223,97,43,0.35);

    transition: 0.3s;
}

.hero-btn:hover {
    transform: translateY(-5px) scale(1.04);
}


/* ================= HERO CAKE ================= */

.hero-cake {
    position: relative;
    width: 400px;
    height: 400px;

    display: flex;
    align-items: center;
    justify-content: center;

    animation: cakeFloat 4s ease-in-out infinite;
}

.cake-circle {
    position: absolute;

    width: 350px;
    height: 350px;

    border-radius: 50%;

    background: #ffd0ad;

    box-shadow:
        0 20px 60px rgba(0,0,0,0.15),
        inset 0 0 40px rgba(255,255,255,0.5);
}

.cake-emoji {
    position: relative;
    z-index: 2;

    font-size: 180px;

    filter: drop-shadow(0 15px 15px rgba(0,0,0,0.15));
}


/* ================= FLOATING ITEMS ================= */

.float-item {
    position: absolute;
    font-size: 50px;
    z-index: 3;

    animation: floating 4s ease-in-out infinite;
}

.float1 {
    top: 20px;
    right: 40px;
}

.float2 {
    bottom: 50px;
    left: 10px;
    animation-delay: 1s;
}

.float3 {
    top: 100px;
    left: -20px;
    animation-delay: 2s;
}


/* ================= SECTION ================= */

.section {
    padding: 90px 8%;
}

.section-title {
    text-align: center;
    margin-bottom: 50px;
}

.section-title h2 {
    font-size: 40px;
    margin-bottom: 10px;
}

.section-title p {
    color: #87695c;
}


/* ================= FILTER BUTTONS ================= */

.filters {
    text-align: center;
    margin-bottom: 40px;
}

.filter-btn {
    border: none;
    padding: 12px 22px;
    margin: 5px;

    border-radius: 25px;

    background: #ffe2d0;
    color: #6b351e;

    cursor: pointer;
    font-weight: bold;

    transition: 0.3s;
}

.filter-btn:hover {
    background: #df612b;
    color: white;
    transform: translateY(-3px);
}


/* ================= FOOD CARDS ================= */

.food-grid {
    display: grid;

    grid-template-columns:
        repeat(auto-fit, minmax(220px, 1fr));

    gap: 25px;
}

.card {
    background: white;

    padding: 25px;

    border-radius: 25px;

    text-align: center;

    box-shadow:
        0 10px 30px rgba(70,35,20,0.08);

    transition: 0.4s;

    animation: cardAppear 0.8s ease both;
}

.card:hover {
    transform:
        translateY(-12px)
        rotate(1deg);

    box-shadow:
        0 20px 40px rgba(70,35,20,0.15);
}

.food-icon {
    font-size: 75px;

    margin-bottom: 18px;

    display: inline-block;

    transition: 0.4s;
}

.card:hover .food-icon {
    transform:
        scale(1.15)
        rotate(-5deg);
}

.card h3 {
    font-size: 21px;
    margin-bottom: 10px;
}

.price {
    color: #df612b;
    font-size: 21px;
    font-weight: bold;

    margin-bottom: 18px;
}

.order-btn {
    border: none;

    background: #6b351e;
    color: white;

    padding: 11px 25px;

    border-radius: 25px;

    cursor: pointer;

    font-weight: bold;

    transition: 0.3s;
}

.order-btn:hover {
    background: #df612b;
    transform: scale(1.05);
}


/* ================= ABOUT ================= */

.about {
    background: #6b351e;
    color: white;

    text-align: center;

    padding: 80px 10%;
}

.about h2 {
    font-size: 40px;
    margin-bottom: 20px;
}

.about p {
    max-width: 700px;
    margin: auto;

    line-height: 1.8;

    color: #f4ddd1;
}


/* ================= FOOTER ================= */

footer {
    background: #2b1710;

    color: white;

    text-align: center;

    padding: 35px;
}

footer h2 {
    color: #ff9b69;
    margin-bottom: 10px;
}


/* ================= ANIMATIONS ================= */

@keyframes slideLeft {

    from {
        opacity: 0;
        transform: translateX(-80px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }
}


@keyframes cakeFloat {

    0%, 100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-18px);
    }
}


@keyframes floating {

    0%, 100% {
        transform: translateY(0) rotate(0deg);
    }

    50% {
        transform: translateY(-20px) rotate(10deg);
    }
}


@keyframes cardAppear {

    from {
        opacity: 0;
        transform: translateY(30px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}


/* ================= MOBILE ================= */

@media (max-width: 768px) {

    .nav-links {
        display: none;
    }

    .hero {
        flex-direction: column;
        text-align: center;
        padding-top: 130px;
    }

    .hero h1 {
        font-size: 45px;
    }

    .hero-cake {
        width: 320px;
        height: 320px;
        margin-top: 40px;
    }

    .cake-circle {
        width: 280px;
        height: 280px;
    }

    .cake-emoji {
        font-size: 130px;
    }

}

</style>

</head>


<body>


<!-- NAVBAR -->

<nav class="navbar">

    <div class="logo">
        ⭐ Star<span>foods</span>
    </div>

    <div class="nav-links">
        <a href="#home">Home</a>
        <a href="#menu">Menu</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
    </div>

</nav>


<!-- HERO -->

<section class="hero" id="home">

    <div class="hero-content">

        <h1>
            Sweet Moments
            <br>
            Start With
            <span>Starfoods!</span>
        </h1>

        <p>
            Freshly baked cakes, crispy chips,
            traditional murukku and delicious
            bakery snacks made with love.
        </p>

        <a href="#menu" class="hero-btn">
            🍰 Explore Our Menu
        </a>

    </div>


    <div class="hero-cake">

        <div class="cake-circle"></div>

        <div class="cake-emoji">
            🎂
        </div>

        <div class="float-item float1">
            🍪
        </div>

        <div class="float-item float2">
            🥨
        </div>

        <div class="float-item float3">
            🍩
        </div>

    </div>

</section>


<!-- MENU -->

<section class="section" id="menu">

    <div class="section-title">

        <h2>🍰 Our Special Menu</h2>

        <p>
            Fresh cakes, crispy snacks and tasty treats
        </p>

    </div>


    <div class="filters">

        <button class="filter-btn"
                onclick="filterItems('all')">
            All
        </button>

        <button class="filter-btn"
                onclick="filterItems('cake')">
            🎂 Cakes
        </button>

        <button class="filter-btn"
                onclick="filterItems('snack')">
            🥨 Snacks
        </button>

        <button class="filter-btn"
                onclick="filterItems('chips')">
            🥔 Chips
        </button>

    </div>


    <div class="food-grid" id="foodGrid">

        {% for item in items %}

        <div class="card">

            <div class="food-icon">
                {{ item.emoji }}
            </div>

            <h3>
                {{ item.name }}
            </h3>

            <div class="price">
                ₹{{ item.price }}
            </div>

            <button class="order-btn"
                    onclick="orderItem('{{ item.name }}')">

                Order Now

            </button>

        </div>

        {% endfor %}

    </div>

</section>


<!-- ABOUT -->

<section class="about" id="about">

    <h2>⭐ Why Starfoods?</h2>

    <p>
        At Starfoods, we bring you delicious bakery
        products made with care. From celebration cakes
        to crispy banana chips and traditional murukku,
        every bite is made to bring a smile.
    </p>

</section>


<!-- FOOTER -->

<footer id="contact">

    <h2>⭐ Starfoods</h2>

    <p>
        Fresh • Tasty • Homemade Taste
    </p>

    <br>

    <p>
        📞 Contact: 98765 43210
    </p>

    <br>

    <p>
        © 2026 Starfoods Bakery
    </p>

</footer>


<script>

function orderItem(name) {

    alert(
        "🍰 " + name +
        " added to your order!\\n\\n" +
        "Thank you for choosing Starfoods ⭐"
    );

}


function filterItems(type) {

    const cards =
        document.querySelectorAll(".card");

    cards.forEach(card => {

        card.style.display = "block";

        if (type !== "all") {

            const name =
                card.querySelector("h3")
                    .innerText
                    .toLowerCase();

            if (type === "cake" &&
                !name.includes("cake")) {

                card.style.display = "none";

            }

            if (type === "chips" &&
                !name.includes("chips")) {

                card.style.display = "none";

            }

            if (type === "snack" &&
                (name.includes("cake") ||
                 name.includes("chips"))) {

                card.style.display = "none";

            }

        }

    });

}

</script>


</body>

</html>
"""


@app.route("/")
def home():
    return render_template_string(
        HTML,
        items=items
    )


if __name__ == "__main__":
    app.run(debug=True)
