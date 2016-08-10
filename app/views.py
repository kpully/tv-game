from flask import Flask, jsonify, render_template, request, redirect, flash, json
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from .forms import MyForm
from app import app

import numpy as np
import pandas as pd

import pandas as pd
import numpy as np
import random

conditions = pd.read_csv('data/conditions.csv')
alc_df = pd.read_csv('data/alc_general.csv')
states_df = pd.read_csv('data/drunks.csv')

alc_dict = alc_df.set_index('alc')['abv'].to_dict()
states_dict = states_df.set_index('label')['bac'].to_dict()
genders = {'male': 0.73, 'female': 0.66}
conditions_dict = conditions.set_index('Condition')['times_per_show'].to_dict()


#---------- URLS AND WEB PAGES -------------#

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/_create_game')
def game():
    user = {'nickname': 'Katherine'}  # fake user
    return render_template('game.html', user=user)

@app.route('/_index2', methods=["GET", "POST"])
def get_form():
    form = MyForm()

    alc = form.alc
    if request.method == "POST":
        name = request.form['firstname']
        name = name[0].upper()+name[1:]
        weight = request.form['weight']
        gender = request.form['gender']
        drunk = request.form['drunk']
        redWine, whiteWine, vodka, champagne, whiskey, beer= False, False, False, False, False, False
        if request.form.get("wine(red)"):
            redWine = True
        if request.form.get("wine(white)"):
            whiteWine = True
        if request.form.get("vodka"):
            vodka = True
        if request.form.get("champagne"):
            champagne = True
        if request.form.get("whiskey"):
            whiskey = True
        if request.form.get("beer"):
            beer = True
        s = 0
        l = {}
        while s <= 15:
            c = random.choice(conditions_dict.items())
            l[c[0]]=c[1]
            s = s + c[1]
        return render_template('results.html', name=name, conditions=json.dumps(l), weight=weight, gender=gender, drunk=drunk)
    elif request.method == "GET":
        return render_template('index_2.html', form=form)

@app.route('/_index3', methods=["GET", "POST"])
def get_form2():
    form = MyForm()
    weight = form.weight
    gender = form.gender
    alc = form.alc
    if request.method == "POST":
        name = request.form['firstname']
        return name
    elif request.method == "GET":
        return render_template('index_2.html', form=form)




