from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('list.html', items=load_candidates_from_json())


@app.route('/candidate/<idi>')
def candidate(idi):
    if idi == "8":
        return render_template('anketa.html')
    return render_template('single.html', data=get_candidate(idi))


@app.route('/candidate/')
def candidate_list():
    return render_template('list.html', items=load_candidates_from_json())


@app.route("/search/<name>")
def searche_name(name):
    return render_template("search.html", items=get_candidates_by_name(name), num=len(get_candidates_by_name(name)))


@app.route("/search/")
def search():
    return render_template('list.html', items=load_candidates_from_json())


@app.route("/skill/")
def skill():
    return render_template('list.html', items=load_candidates_from_json())


@app.route("/skill/<skilll>")
def skill_search(skilll):
    return render_template('skill.html', items=get_candidates_by_skill(skilll), skill=skilll,
                           num=len(get_candidates_by_skill(skilll)))


app.run('127.0.0.1', 5000)
