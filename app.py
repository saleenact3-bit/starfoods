from flask import Flask, render_template_string

app = Flask(__name__)

products = [
    {"name": "Banana Chips", "price": 120, "emoji": "🥔", "category": "chips"},
    {"name": "Potato Chips", "price": 100, "emoji": "🥔", "category": "chips"},
    {"name": "Spicy Murukku", "price": 150, "emoji": "🥨", "category": "snacks"},
    {"name": "Butter Murukku", "price": 160, "emoji": "🥨", "category": "snacks"},
    {"name": "Special Mixture", "price": 140, "emoji": "🥜", "category": "snacks"},
    {"name": "Nippattu", "price": 130, "emoji": "🍘", "category": "snacks"},
    {"name": "Masala Peanuts", "price": 110, "emoji": "🥜", "category": "snacks"},
    {"name": "Spicy Mixture", "price": 150, "emoji": "🌶️", "category": "snacks"},
]

HTML = """
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Starfoods | Crispy Snacks</title>

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
    background: #fff8ed;
    color: #35180d;
    overflow-x: hidden;
}


/* NAVBAR */

.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;

    padding: 18px 7%;

    display: flex;
    justify-content: space-between;
    align-items: center;

    background: rgba(255,255,255,0.92);
    backdrop-filter: blur(12px);

    z-index: 1000;

    box-shadow: 0 5px 25px rgba(0,0,0,0.08);
}

.logo {
    font-size: 30px;
    font-weight: 900;
    color: #d94d18;
}

.logo span {
    color: #442015;
}

.nav-links {
    display: flex;
    gap: 30px;
}

.nav-links a {
    text-decoration: none;
    color: #442015;
    font-weight: bold;
}

.nav-links a:hover {
    color: #e4581c;
}


/* HERO */

.hero {
    min-height: 100vh;

    padding: 150px 7% 80px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    position: relative;
    overflow: hidden;

    background:
        radial-gradient(circle at 80% 30%, #ffd09d, transparent 30%),
        linear-gradient(135deg, #fff8ed, #ffe1bd);
}

.hero-content {
    width: 50%;
    z-index: 5;

    animation: slideIn 1s ease;
}

.hero-content h1 {
    font-size: 68px;
    line-height: 1.05;
    margin-bottom: 20px;
}

.hero-content h1 span {
    color: #e0521b;
}

.hero-content p {
    font-size: 20px;
    line-height: 1.7;
    color: #765448;
    max-width: 550px;
    margin-bottom: 30px;
}

.hero-button {
    display: inline-block;

    padding: 15px 30px;

    background: #e0521b;
    color: white;

    text-decoration: none;

    border-radius: 30px;

    font-weight: bold;

    box-shadow: 0 12px 30px rgba(224,82,27,0.35);

    transition: 0.3s;
}

.hero-button:hover {
    transform: translateY(-5px) scale(1.05);
}


/* SNACK ANIMATION AREA */

.snack-scene {
    width: 48%;
    height: 480px;

    position: relative;

    display: flex;
    justify-content: center;
    align-items: center;
}


/* PLATE */

.plate {
    width: 330px;
    height: 330px;

    position: absolute;

    border-radius: 50%;

    background: #fff;

    border: 12px solid #f0e2d3;

    box-shadow:
        0 25px 50px rgba(80,40,15,0.2),
        inset 0 0 30px rgba(0,0,0,0.06);

    animation: plateFloat 4s ease-in-out infinite;
}


/* SNACKS */

.snack {
    position: absolute;

    font-size: 75px;

    z-index: 5;

    filter: drop-shadow(
        0 12px 10px rgba(0,0,0,0.18)
    );
}

.snack1 {
    top: 85px;
    left: 50px;

    animation: snackMove1 3s ease-in-out infinite;
}

.snack2 {
    top: 40px;
    right: 40px;

    animation: snackMove2 3.5s ease-in-out infinite;
}

.snack3 {
    bottom: 65px;
    left: 100px;

    animation: snackMove3 4s ease-in-out infinite;
}

.snack4 {
    bottom: 50px;
    right: 70px;

    animation: snackMove4 3.2s ease-in-out infinite;
}


/* FLOATING PARTICLES */

.particle {
    position: absolute;

    font-size: 30px;

    animation: particleFloat 5s ease-in-out infinite;
}

.p1 {
    top: 20px;
    left: 30%;
}

.p2 {
    top: 55%;
    right: 5%;
    animation-delay: 1s;
}

.p3 {
    bottom: 10px;
    left: 20%;
    animation-delay: 2s;
}

.p4 {
    top: 25%;
    right: 20%;
    animation-delay: 1.5s;
}


/* PRODUCTS */

.products {
    padding: 90px 7%;
}

.title {
    text-align: center;
    margin-bottom: 50px;
}

.title h2 {
    font-size: 42px;
    margin-bottom: 10px;
}

.title p {
    color: #87695d;
}


/* FILTERS */

.filters {
    text-align: center;
    margin-bottom: 35px;
}

.filter {
    border: none;

    background: #ffe0c4;

    color: #572719;

    padding: 12px 22px;

    margin: 5px;

    border-radius: 25px;

    cursor: pointer;

    font-weight: bold;

    transition: 0.3s;
}

.filter:hover {
    background: #e0521b;
    color: white;
    transform: translateY(-3px);
}


/* PRODUCT GRID */

.grid {
    display: grid;

    grid-template-columns:
        repeat(auto-fit, minmax(220px, 1fr));

    gap: 25px;
}

.card {
    background: white;

    padding: 28px;

    border-radius: 25px;

    text-align: center;

    box-shadow: 0 10px 30px rgba(70,30,10,0.08);

    transition: 0.4s;

    animation: cardIn 0.8s ease;
}

.card:hover {
    transform:
        translateY(-12px)
        rotate(1deg);

    box-shadow:
        0 20px 40px rgba(70,30,10,0.16);
}

.product-icon {
    font-size: 75px;

    margin-bottom: 18px;

    display: inline-block;

    transition: 0.4s;
}

.card:hover .product-icon {
    transform:
        scale(1.2)
        rotate(-8deg);
}

.card h3 {
    margin-bottom: 12px;
    font-size: 21px;
}

.price {
    color: #e0521b;

    font-size: 21px;

    font-weight: bold;

    margin-bottom: 18px;
}

.order {
    border: none;

    background: #4a2115;

    color: white;

    padding: 11px 25px;

    border-radius: 25px;

    cursor: pointer;

    font-weight: bold;

    transition: 0.3s;
}

.order:hover {
    background: #e0521b;
    transform: scale(1.08);
}


/* ABOUT */

.about {
    padding: 90px 10%;

    background: #4a2115;

    color: white;

    text-align: center;
}

.about h2 {
    font-size: 40px;
    margin-bottom: 20px;
}

.about p {
    max-width: 750px;

    margin: auto;

    line-height: 1.8;

    color: #ead7cd;
}


/* FOOTER */

footer {
    background: #24100a;

    color: white;

    text-align: center;

    padding: 35px;
}

footer h2 {
    color: #ff925d;
    margin-bottom: 10px;
}


/* ANIMATIONS */

@keyframes slideIn {

    from {
        opacity: 0;
        transform: translateX(-80px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }
}


@keyframes plateFloat {

    0%, 100% {
        transform: translateY(0) rotate(0deg);
    }

    50% {
        transform: translateY(-15px) rotate(4deg);
    }
}


@keyframes snackMove1 {

    0%, 100% {
        transform: translate(0,0) rotate(-10deg);
    }

    50% {
        transform: translate(15px,-25px) rotate(15deg);
    }
}


@keyframes snackMove2 {

    0%, 100% {
        transform: translate(0,0) rotate(10deg);
    }

    50% {
        transform: translate(-20px,-30px) rotate(-15deg);
    }
}


@keyframes snackMove3 {

    0%, 100% {
        transform: translate(0,0) rotate(5deg);
    }

    50% {
        transform: translate(20px,-20px) rotate(-10deg);
    }
}


@keyframes snackMove4 {

    0%, 100% {
        transform: translate(0,0) rotate(-5deg);
    }

    50% {
        transform: translate(-15px,-25px) rotate(12deg);
    }
}


@keyframes particleFloat {

    0%, 100% {
        transform: translateY(0);
        opacity: 0.7;
    }

    50% {
        transform: translateY(-30px);
        opacity: 1;
    }
}


@keyframes cardIn {

    from {
        opacity: 0;
        transform: translateY(35px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}


/* MOBILE */

@media (max-width: 800px) {

    .nav-links {
        display: none;
    }

    .hero {
        flex-direction: column;
        text-align: center;
    }

    .hero-content {
        width: 100%;
    }

    .hero-content h1 {
        font-size: 45px;
    }

    .snack-scene {
        width: 100%;
        height: 400px;
        margin-top: 30px;
    }

    .plate {
        width: 280px;
        height: 280px;
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

        <a href="#products">Snacks</a>

        <a href="#about">About</a>

        <a href="#contact">Contact</a>

    </div>

</nav>


<!-- HERO -->

<section class="hero" id="home">

    <div class="hero-content">

        <h1>
            Taste The
            <span>Crunch!</span>
        </h1>

        <p>
            Welcome to Starfoods — your place for
            crispy chips, traditional murukku,
            spicy mixture and delicious snacks.
        </p>

        <a class="hero-button" href="#products">
            🛍️ Explore Snacks
        </a>

    </div>


    <!-- ANIMATED SNACK SCENE -->

    <div class="snack-scene">

        <div class="plate"></div>

        <div class="snack snack1">
            🥔
        </div>

        <div class="snack snack2">
            🥨
        </div>

        <div class="snack snack3">
            🥜
        </div>

        <div class="snack snack4">
            🍘
        </div>


        <div class="particle p1">
            ✨
        </div>

        <div class="particle p2">
            ⭐
        </div>

        <div class="particle p3">
            ✨
        </div>

        <div class="particle p4">
            🟠
        </div>

    </div>

</section>


<!-- PRODUCTS -->

<section class="products" id="products">

    <div class="title">

        <h2>🔥 Starfoods Snacks</h2>

        <p>
            Crispy. Fresh. Delicious.
        </p>

    </div>


    <div class="filters">

        <button
            class="filter"
            onclick="filterProducts('all')">

            All

        </button>

        <button
            class="filter"
            onclick="filterProducts('chips')">

            🥔 Chips

        </button>

        <button
            class="filter"
            onclick="filterProducts('snacks')">

            🥨 Snacks

        </button>

    </div>


    <div class="grid">

        {% for product in products %}

        <div
            class="card"
            data-category="{{ product.category }}">

            <div class="product-icon">

                {{ product.emoji }}

            </div>

            <h3>

                {{ product.name }}

            </h3>

            <div class="price">

                ₹{{ product.price }}

            </div>

            <button
                class="order"
                onclick="orderProduct('{{ product.name }}')">

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
        Starfoods brings you crispy and tasty snacks
        made for every occasion. From crunchy chips
        to traditional murukku and spicy mixtures,
        every packet is packed with flavour.
    </p>

</section>


<!-- FOOTER -->

<footer id="contact">

    <h2>⭐ Starfoods</h2>

    <p>
        Crispy • Fresh • Tasty
    </p>

    <br>

    <p>
        📞 Contact: 98765 43210
    </p>

    <br>

    <p>
        © 2026 Starfoods
    </p>

</footer>


<script>


function orderProduct(name) {

    alert(
        "🛍️ " + name +
        " added to your order!\\n\\n" +
        "Thank you for choosing Starfoods ⭐"
    );

}


function filterProducts(category) {

    const cards =
        document.querySelectorAll(".card");


    cards.forEach(card => {

        const productCategory =
            card.getAttribute("data-category");


        if (category === "all") {

            card.style.display = "block";

        }

        else if (productCategory === category) {

            card.style.display = "block";

        }

        else {

            card.style.display = "none";

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
        products=products
    )


if __name__ == "__main__":
    app.run(debug=True)
