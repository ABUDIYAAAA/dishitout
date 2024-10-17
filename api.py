from flask import Flask, jsonify, send_file, render_template
import random
import os
from markupsafe import escape


app = Flask(__name__)

# Assume we have a directory called 'dishes' with images of dishes
DISHES_DIR = "dishes"


@app.route("/dish/<course>", methods=["GET"])
def dish(course):
    try:
        course = course
        u = f"./static/images/{course}"
        images = os.listdir(u)
        image = random.choice(images)
        image_url = f"./static/images/{course}/{image}"
        return send_file(image_url)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/random-dish", methods=["GET"])
def random_dish():
    try:
        courses = os.listdir("./static/images")
        course = random.choice(courses)
        print(course)
        u = f"./static/images/{course}"
        print(u)
        images = os.listdir(u)
        image = random.choice(images)
        image_url = f"./static/images/{course}/{image}"
        return send_file(image_url)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/all-dishes", methods=["GET"])
def all_dish():
    try:
        dishes = ""
        for course in os.listdir("static/images"):
            course_url = f"./static/images/{course}"
            for image in os.listdir(course_url):
                dishes += image.rstrip(".jpg")
        return jsonify(
            {
                "dishes": [
                    ["paneer-tikka", "soup", "spring-rolls"],
                    ["dal makhani", "paneer butter masala", "butter chicken"],
                    ["ice cream", "gulab jamun", "pastry"],
                ]
            }
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
