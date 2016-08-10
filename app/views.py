from flask import Flask, jsonify, render_template, request, redirect, flash, json
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from .forms import MyForm
from app import app

import numpy as np
import pandas as pd

import pandas as pd
import numpy as np
import random


alc_df = pd.read_csv('data/alc_general.csv')
states_df = pd.read_csv('data/drunks.csv')

alc_dict = alc_df.set_index('alc')['abv'].to_dict()
states_dict = states_df.set_index('label')['bac'].to_dict()
genders = {'male': 0.73, 'female': 0.66}



#---------- URLS AND WEB PAGES -------------#
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/_bip', methods=["GET", "POST"])
def get_form():
    form = MyForm()
    show="Bachelor in Paradise"
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
        conditions = pd.read_csv('data/conditions.csv')
        conditions_dict = conditions.set_index('Condition')['times_per_show'].to_dict()
        s = 0
        l = {}
        while s <= 15:
            c = random.choice(conditions_dict.items())
            l[c[0]]=c[1]
            s = s + c[1]
        return render_template('results.html', name=name, conditions=json.dumps(l), weight=weight, gender=gender, drunk=drunk, show=show)
    elif request.method == "GET":
        return render_template('bip.html', form=form)

@app.route('/_olympics', methods=["GET", "POST"])
def get_form_olympics():
    form = MyForm()
    show = "Olympics 2016"
    if request.method == "POST":
        name = request.form['firstname']
        name = name[0].upper()+name[1:]
        weight = request.form['weight']
        gender = request.form['gender']
        drunk = request.form['drunk']
        redWine, whiteWine, vodka, champagne, whiskey, beer= False, False, False, False, False, False
        sports = request.form.getlist('sports')        
        #alcs
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
        conditions = pd.read_csv('data/olympics.csv')
        conditions_dict = conditions.set_index('Condition')['sport'].to_dict()
        s = 0
        l = set()
        while s <= 25:
            el = random.choice(conditions_dict.items())
            curr =  el[1].split(',')
            for sport in curr:
                if sport.strip() in sports:
                    l.add(el[0])
                    s = s + 1
                    break
        return render_template('results.html', name=name, conditions=json.dumps(list(l)), weight=weight, gender=gender, drunk=drunk, show=show, sports=sports)
    elif request.method == "GET":
        return render_template('olympics.html', form=form)


