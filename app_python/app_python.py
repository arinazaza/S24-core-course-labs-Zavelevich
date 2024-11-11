from flask import Flask, request
from datetime import datetime
import pytz

app = Flask(__name__)

# File to store the visit count
VISITS_FILE = 'visits.txt'


def read_visits():
    try:
        with open(VISITS_FILE, 'r+') as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def write_visits(count):
    with open(VISITS_FILE, "r+", encoding="utf-8") as file:
        file.seek(0)
        file.write(str(count))


@app.route('/')
def msc_time():
    msc = pytz.timezone('Europe/Moscow')
    cur_time = datetime.now(msc).strftime('%Y-%m-%d %H:%M:%S')

    # Increment the visit count
    write_visits(read_visits() + 1)

    return f"{cur_time}"


@app.route('/visits')
def visits():
    visit_count = read_visits()
    return f"Total Visits: {visit_count}"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)