from flask import Flask, render_template_string

app = Flask(__name__)

foods = [
    {"name": "Chicken Biriyani", "price": 180, "emoji": "🍗"},
    {"name": "Beef Biriyani", "price": 200, "emoji": "🥩"},
    {"name": "Chicken Fried Rice", "price": 160, "emoji": "🍚"},
    {"name": "Porotta & Chicken", "price": 150, "emoji": "🍛"},
    {"name": "Shawarma", "price": 120, "emoji": "🌯"},
    {"name": "Burger", "price": 140, "emoji": "🍔"},
    {"name": "Pizza", "price": 220, "emoji": "🍕"},
    {"name": "Fresh Juice", "price": 80, "emoji": "🥤"},
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>starfoods - Food Delivery</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, sans-serif;
            background: #fff8f0;
            color: #333;
        }

        nav {
            background: #ff5a1f;
            color: white;
            padding: 18px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        nav h1 {
            font-size: 28px;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin-left: 25px;
            font-weight: bold;
        }

        .hero {
            padding: 70px 8%;
            text-align: center;
            background: linear-gradient(135deg, #ff7a18, #ff3d00);
            color: white;
        }

        .hero h2 {
            font-size: 45px;
            margin-bottom: 15px;
        }

        .hero p {
            font-size: 20px;
            margin-bottom: 25px;
        }

        .btn {
            display: inline-block;
            background: white;
            color: #ff4d00;
            padding: 13px 25px;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
        }

        .foods {
            padding: 50px 8%;
        }

        .foods h2 {
            text-align: center;
            margin-bottom: 35px;
            font-size: 32px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 25px;
        }

        .card {
            background: white;
            border-radius: 18px;
            padding: 25px;
            text-align: center;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-8px);
        }

        .emoji {
            font-size: 70px;
            margin-bottom: 15px;
        }

        .card h3 {
            font-size: 21px;
            margin-bottom: 10px;
        }

        .price {
            color: #ff4d00;
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 15px;
        }

        .order {
            background: #ff5a1f;
            color: white;
            border: none;
            padding: 11px 22px;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
        }

        footer {
            margin-top: 30px;
            background: #222;
            color: white;
            text-align: center;
            padding: 25px;
        }
    </style>
</head>

<body>

<nav>
    <h1>🍴 Foodie</h1>

    <div>
        <a href="/">Home</a>
        <a href="#menu">Menu</a>
        <a href="#contact">Contact</a>
    </div>
</nav>

<section class="hero">
    <h2>Delicious Food, Delivered Fast!</h2>
    <p>Fresh • Tasty • Affordable</p>
    <a href="#menu" class="btn">View Menu</a>
</section>

<section class="foods" id="menu">
    <h2>🔥 Popular Foods</h2>

    <div class="grid">

        {% for food in foods %}
        <div class="card">

            <div class="emoji">
                {{ food.emoji }}
            </div>

            <h3>{{ food.name }}</h3>

            <div class="price">
                ₹{{ food.price }}
            </div>

            <button class="order"
                    onclick="alert('{{ food.name }} added to your order!')">
                Order Now
            </button>

        </div>
        {% endfor %}

    </div>
</section>

<footer id="contact">
    <p>📞 Contact: 9656640161</p>
    <p>© 2026 Foodie. All Rights Reserved.</p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, foods=foods)


if __name__ == "__main__":
    app.run(debug=True)
