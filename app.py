from flask import Flask, render_template
import game_of_life as gl

app = Flask(__name__)

@app.route('/')
def index():
    gl.GameOfLife(25, 25)
    return render_template('index.html')

@app.route('/live')
def live():
    ng = gl.GameOfLife()
    if ng.gen_number > 0:
        ng.form_new_generation()
    ng.gen_number += 1
    return render_template('live.html', new_gen=ng.world, gen_n= ng.gen_number, old_gen=ng.old_world)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)