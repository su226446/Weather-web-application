from flask import Flask, request, redirect

app = Flask(__name__)

zip_code = -1

@app.route('/')
def index():
    return '<h1>Main Page</h1>'

@app.route('/city')
def city_entry():
    city_name = request.args.get('city_name')
    zip_code = find_zip_code(city_name)
    redirect('/result')
    return f"The zip code of {city_name} is {zip_code}."

@app.route('/result')
def result():
    return zip_code

def find_zip_code(city):
    city_to_zip_code = {"Milpitas": 95035, "Fremont": 94539, "cupertino": 95015, "Union City": 94536, "Redwood": 94061}
    return city_to_zip_code[city]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)