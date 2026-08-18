from flask import Flask, render_template_string

app = Flask(__name__)

products = [
    ("Banana Chips", "₹120", "static/micher.png"),
    ("Spicy Chips", "₹140", "static/micher.png"),
    ("Murukku", "₹150", "static/micher.png"),
    ("Special Mixture", "₹160", "static/micher.png"),
    ("Masala Peanuts", "₹130", "static/micher.png"),
    ("Nippattu", "₹140", "static/micher.png"),
]

HTML = """
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Starfoods</title>

<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background: #fff8ed;
    color: #32150c;
    overflow-x: hidden;
}


/* NAVBAR */

nav {
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;

    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 18px 7%;

    background: rgba(255,255,255,0.9);
    backdrop-filter: blur(12px);

    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
}

.logo {
    font-size: 30px;
    font-weight: 900;
    color: #d84d19;
}

.logo span {
    color: #3b1c12;
}

nav a {
    text-decoration: none;
    color: #3b1c12;
    font-weight: bold;
    margin-left: 25px;
}

nav a:hover {
    color: #d84d19;
}


/* HERO */

.hero {
    min-height: 100vh;

    padding: 130px 7% 60px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    background:
        radial-gradient(circle at 80% 30%,
        #ffd6a8,
        transparent 35%),
        linear-gradient(135deg,
        #fff8ed,
        #ffe0bd);

    overflow: hidden;
}

.hero-text {
    width: 45%;
    z-index: 10;

    animation: textIn 1s ease;
}

.hero-text h1 {
    font-size: 68px;
    line-height: 1.05;
}

.hero-text h1 span {
    color: #df531c;
}

.hero-text p {
    margin-top: 20px;

    font-size: 20px;
    line-height: 1.7;

    color: #755448;
}

.button {
    display: inline-block;

    margin-top: 30px;

    padding: 15px 30px;

    background: #df531c;
    color: white;

    border-radius: 30px;

    text-decoration: none;
    font-weight: bold;

    box-shadow: 0 12px 30px rgba(223,83,28,.35);
}


/* ANIMATION SCENE */

.scene {
    width: 52%;
    height: 560px;

    position: relative;
}


/* REALISTIC PLATE IMAGE */

.plate {
    position: absolute;

    width: 390px;

    left: 50%;
    bottom: 50px;

    transform: translateX(-50%);

    z-index: 2;

    filter:
        drop-shadow(0 25px 20px rgba(0,0,0,.25));

    animation: plateMove 4s ease-in-out infinite;
}


/* REALISTIC PACKET */

.packet {
    position: absolute;

    width: 260px;

    right: 70px;
    top: 40px;

    z-index: 8;

    filter:
        drop-shadow(0 20px 15px rgba(0,0,0,.25));

    transform-origin: bottom center;

    animation: packetPour 4s ease-in-out infinite;
}


/* CHIPS FALLING FROM PACKET */

.chip {
    position: absolute;

    width: 48px;

    z-index: 6;

    opacity: 0;

    filter:
        drop-shadow(0 8px 5px rgba(0,0,0,.25));
}


/* EACH CHIP HAS DIFFERENT PATH */

.chip1 {
    right: 230px;
    top: 190px;

    animation: fall1 4s infinite;
}

.chip2 {
    right: 250px;
    top: 190px;

    animation: fall2 4s .15s infinite;
}

.chip3 {
    right: 270px;
    top: 190px;

    animation: fall3 4s .3s infinite;
}

.chip4 {
    right: 245px;
    top: 190px;

    animation: fall4 4s .45s infinite;
}

.chip5 {
    right: 280px;
    top: 190px;

    animation: fall5 4s .6s infinite;
}


/* CRUMBS */

.crumb {
    position: absolute;

    width: 12px;
    height: 12px;

    background: #d78b32;

    border-radius: 50%;

    opacity: 0;

    animation: crumbFall 4s infinite;
}


/* ANIMATIONS */

@keyframes packetPour {

    0%, 15% {
        transform: rotate(0deg);
    }

    25%, 65% {
        transform: rotate(-25deg) translate(-15px,20px);
    }

    75%, 100% {
        transform: rotate(0deg);
    }
}


@keyframes plateMove {

    0%, 100% {
        transform: translateX(-50%) translateY(0);
    }

    50% {
        transform: translateX(-50%) translateY(-8px);
    }
}


@keyframes fall1 {

    0%, 20% {
        opacity: 0;
        transform: translate(0,0) rotate(0);
    }

    30% {
        opacity: 1;
    }

    70% {
        opacity: 1;
        transform: translate(-120px,250px) rotate(300deg);
    }

    80%,100% {
        opacity: 0;
        transform: translate(-125px,280px) rotate(360deg);
    }
}


@keyframes fall2 {

    0%, 20% {
        opacity: 0;
    }

    30% {
        opacity: 1;
    }

    70% {
        opacity: 1;
        transform: translate(-100px,270px) rotate(-280deg);
    }

    80%,100% {
        opacity: 0;
        transform: translate(-105px,285px) rotate(-360deg);
    }
}


@keyframes fall3 {

    0%, 20% {
        opacity: 0;
    }

    30% {
        opacity: 1;
    }

    70% {
        opacity: 1;
        transform: translate(-80px,245px) rotate(250deg);
    }

    80%,100% {
        opacity: 0;
        transform: translate(-85px,280px) rotate(320deg);
    }
}


@keyframes fall4 {

    0%, 20% {
        opacity: 0;
    }

    30% {
        opacity: 1;
    }

    70% {
        opacity: 1;
        transform: translate(-145px,260px) rotate(-250deg);
    }

    80%,100% {
        opacity: 0;
        transform: translate(-150px,280px) rotate(-320deg);
    }
}


@keyframes fall5 {

    0%, 20% {
        opacity: 0;
    }

    30% {
        opacity: 1;
    }

    70% {
        opacity: 1;
        transform: translate(-65px,280px) rotate(400deg);
    }

    80%,100% {
        opacity: 0;
        transform: translate(-70px,290px) rotate(450deg);
    }
}


@keyframes crumbFall {

    0%,20% {
        opacity: 0;
        transform: translateY(0);
    }

    35% {
        opacity: 1;
    }

    70% {
        opacity: 1;
        transform: translate(-100px,270px);
    }

    80%,100% {
        opacity: 0;
    }
}


@keyframes textIn {

    from {
        opacity: 0;
        transform: translateX(-70px);
    }

    to {
        opacity: 1;
        transform: translateX(0);
    }
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
}

.title p {
    margin-top: 10px;
    color: #806357;
}

.grid {
    display: grid;

    grid-template-columns:
        repeat(auto-fit,minmax(220px,1fr));

    gap: 25px;
}

.card {
    background: white;

    padding: 30px;

    border-radius: 25px;

    text-align: center;

    box-shadow:
        0 10px 30px rgba(60,25,10,.08);

    transition: .4s;
}

.card:hover {
    transform: translateY(-12px);
}

.card img {
    width: 130px;
    height: 130px;

    object-fit: contain;

    margin-bottom: 15px;
}

.card h3 {
    margin-bottom: 10px;
}

.price {
    color: #df531c;

    font-size: 20px;

    font-weight: bold;

    margin-bottom: 15px;
}

.order {
    border: none;

    padding: 11px 25px;

    border-radius: 25px;

    background: #3b1c12;

    color: white;

    cursor: pointer;

    font-weight: bold;
}

.order:hover {
    background: #df531c;
}


/* FOOTER */

footer {
    padding: 40px;

    background: #251009;

    color: white;

    text-align: center;
}

footer h2 {
    color: #ff9564;
    margin-bottom: 10px;
}


/* MOBILE */

@media(max-width:800px) {

    nav a {
        display: none;
    }

    .hero {
        flex-direction: column;
        text-align: center;
    }

    .hero-text {
        width: 100%;
    }

    .hero-text h1 {
        font-size: 45px;
    }

    .scene {
        width: 100%;
        height: 450px;
        margin-top: 30px;
    }

    .packet {
        width: 190px;
        right: 20px;
    }

    .plate {
        width: 280px;
    }

}

</style>

</head>


<body>


<nav>

    <div class="logo">
        Star<span>foods</span>
    </div>

    <div>
        <a href="#home">Home</a>
        <a href="#products">Products</a>
        <a href="#contact">Contact</a>
    </div>

</nav>


<section class="hero" id="home">

    <div class="hero-text">

        <h1>
            Feel The
            <span>Crunch.</span>
        </h1>

        <p>
            Fresh crispy chips, traditional murukku
            and delicious snacks from Starfoods.
        </p>

        <a href="#products" class="button">
            Explore Starfoods
        </a>

    </div>


    <div class="scene">

        <!-- REAL PACKET IMAGE -->

        <img
            src="/static/micher.png"
            class="packet"
        >


        <!-- REAL PLATE IMAGE -->

        <img
            src="/static/micher.png"
            class="plate"
        >


        <!-- REAL CHIP IMAGES -->

        <img
            src="/static/micher.png"
            class="chip chip1"
        >

        <img
            src="/static/micher.png"
            class="chip chip2"
        >

        <img
            src="/static/micher.png"
            class="chip chip3"
        >

        <img
            src="/static/micher.png"
            class="chip chip4"
        >

        <img
            src="/static/micher.png"
            class="chip chip5"
        >

    </div>

</section>


<section class="products" id="products">

    <div class="title">

        <h2>Starfoods Snacks</h2>

        <p>
            Crispy. Fresh. Delicious.
        </p>

    </div>


    <div class="grid">

        {% for name, price, image in products %}

        <div class="card">

            <img
                src="/static/images/{{ image }}"
            >

            <h3>
                {{ name }}
            </h3>

            <div class="price">
                {{ price }}
            </div>

            <button
                class="order"
                onclick="alert('Added {{ name }} to your order!')">

                Order Now

            </button>

        </div>

        {% endfor %}

    </div>

</section>


<footer id="contact">

    <h2>Starfoods</h2>

    <p>
        Crispy • Fresh • Tasty
    </p>

    <br>

    <p>
        Contact: 98765 43210
    </p>

    <br>

    <p>
        © 2026 Starfoods
    </p>

</footer>


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
