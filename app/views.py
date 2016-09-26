from flask import Flask, jsonify, render_template, request, redirect, flash, json
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from .forms import MyForm, OlympicForm
from app import app

import numpy as np
import math

import pandas as pd
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
def get_form_bip():
    form = MyForm()
    show="Bachelor in Paradise"
    if form.validate_on_submit():
        name = form.name.data
        name = name[0].upper()+name[1:]
        weight = float(form.weight.data)
        hours = float(form.time.data)
        gen_temp = request.form['gender']
        if gen_temp == 'male':
            gender = 0.73
        else:
            gender = 0.66
        state = float(form.drunk.data)
        alc = float(form.alc.data)
        conditions = pd.read_csv('data/bip.csv')
        conditions_dict = conditions.set_index('Condition')['chance_of_condition'].to_dict()
        oz = math.floor((weight*gender*(state + 0.015*hours))/(5.14*alc))
        keys = conditions_dict.keys()
        random.shuffle(keys)
        game = {}
        imbibed = 0
        for key in keys:
            if int(imbibed) < oz:
                if conditions_dict[key] == "low":
                    imbibed = imbibed + 0.12*8
                    game[key] = 'chug'
                elif conditions_dict[key] == "normal":
                    imbibed = imbibed + 0.12*3
                    game[key] = "gulp"
                elif conditions_dict[key] == "high":
                    imbibed = imbibed + 0.12*1.5
                    game[key] = "sip"
        return render_template('results.html', name=name, conditions=json.dumps(game), show=show, oz=oz)
    return render_template('bip.html', form=form)

@app.route('/_debate', methods=["GET", "POST"])
def get_form_debate():
    form = MyForm()
    show="Presidential Debates"
    if form.validate_on_submit():
        name = form.name.data
        name = name[0].upper()+name[1:]
        weight = float(form.weight.data)
        hours = float(form.time.data)
        gen_temp = form.gender.data
        if gen_temp == 'male':
            gender = 0.73
        else:
            gender = 0.66
        state = float(form.drunk.data)
        alc = float(form.alc.data)
        conditions = pd.read_csv('data/debates.csv')
        conditions_dict = conditions.set_index('Condition')['chance_of_condition'].to_dict()
        oz = math.floor((weight*gender*(state + 0.015*hours))/(5.14*alc))
        keys = conditions_dict.keys()
        random.shuffle(keys)
        game = {}
        imbibed = 0
        for key in keys:
            if int(imbibed) < oz:
                if conditions_dict[key] == "low":
                    imbibed = imbibed + 0.12*8
                    game[key] = 'chug'
                elif conditions_dict[key] == "normal":
                    imbibed = imbibed + 0.12*3
                    game[key] = "gulp"
                elif conditions_dict[key] == "high":
                    imbibed = imbibed + 0.12*1.5
                    game[key] = "sip"
        return render_template('results.html', name=name, conditions=json.dumps(game), show=show, oz=oz)
    return render_template('debate.html', form=form)


@app.route('/_create', methods=["GET", "POST"])
def get_form_custom():
    form = MyForm()
    return render_template('custom.html', form=form)
    if request.method == "POST":
        show = request.form['show']
        name = request.form['firstname']
        name = name[0].upper()+name[1:]
        weight = float(request.form['weight'])
        hours = float(request.form['hours'])
        gen_temp = request.form['gender']
        if gen_temp == 'male':
            gender = 0.73
        else:
            gender = 0.66
        alc = float(request.form['alc'])
        state = float(request.form['drunk'])
        conditions=requests.form['custom']
        oz = math.floor((weight*gender*(state + 0.015*hours))/(5.14*alc))
        return render_template('results.html', name=name, conditions=json.dumps(game), show=show, oz=oz)

@app.route('/_olympics', methods=["GET", "POST"])
def get_form_olympics():
    form = OlympicForm()
    show = "Olympics 2016"
    if request.method == "POST":
        name = request.form['firstname']
        name = name[0].upper()+name[1:]
        weight = float(request.form['weight'])
        hours = float(request.form['hours'])
        gen_temp = request.form['gender']
        if gen_temp == 'male':
            gender = 0.73
        else:
            gender = 0.66
        alc = float(request.form['alc'])
        state = float(request.form['drunk'])
        sports = request.form.getlist('sports')        
        conditions = pd.read_csv('data/olympics.csv')
        conditions_dict = conditions.set_index('Condition')['chance_of_condition'].to_dict()
        categories = conditions.set_index('Condition')['sport'].to_dict()
        filtered = []
        for c in categories.items():
            curr = c[1].split(',')
            for s in curr:
                if s.strip() in sports:
                    filtered.append(c[0])
        oz = math.floor((weight*gender*(state + 0.015*hours))/(5.14*alc))
        filtered_d = dict((key, value) for key, value in conditions_dict.items() if key in filtered)
        keys = filtered_d.keys()
        random.shuffle(keys)
        game = {}
        imbibed = 0
        for key in keys:
            if int(imbibed) < oz:
                if filtered_d[key] == "low":
                    imbibed = imbibed + 0.12*8
                    game[key] = 'chug'
                elif filtered_d[key] == "normal":
                    imbibed = imbibed + 0.12*3
                    game[key] = "gulp"
                elif filtered_d[key] == "high":
                    imbibed = imbibed + 0.12*1.5
                    game[key] = "sip"
        return render_template('results.html', name=name, conditions=json.dumps(game), show=show, sports=sports, oz=oz)
    elif request.method == "GET":
        return render_template('olympics.html', form=form)



