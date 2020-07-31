# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

import numpy as np
import pandas as pd

from ner_lib import Ner
from question_answer_lib import QuentionAnswer

import random

external_stylesheets = [
    # dbc
    dbc.themes.BOOTSTRAP,
    # Loading screen CSS
    'https://codepen.io/chriddyp/pen/brPBPO.css',
    # W3 CSS Library
    'https://www.w3schools.com/w3css/4/w3.css',
    # Lato fonts
    "https://fonts.googleapis.com/css?family=Lato",
    # Font Awesome
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)

app.title = 'Model Interface'


def header():
    return \
        html.Div(id="header", className="bgimg-1 w3-display-container w3-opacity-min", children=[
            html.Div(style={'whiteSpace': 'nowrap', 'margin-top': '10vh'}, className="w3-display-topmiddle", children=[
                html.Span(className='w3-padding-large w3-black w3-xlarge w3-wide w3-animate-opacity w3-hide-small', children='MODEL WEB ARAYÜZÜ')
            ])
        ])

def description():
    return \
        html.Div(id="description", className="w3-center w3-padding-large", children=[
            html.P("Bu araç Kuzgunlar ekibi tarafından Acikhack2 Türkçe Doğal Dil İşleme yarışması için hazırlanmıştır."),
            html.P("Amacı son kullanıcılara, uygun bir Q&A ve NER test ortamı sunmaktır."),
            html.Br(className='w3-margin-top'),
            html.P("EKİP", className='w3-margin-top'),
            html.Div(className="w3-row", children=[
                html.Div(className="w3-display-container w3-col m6", children=[
                    html.P("Hüseyin ERDEM"),
                    html.Div(className="w3-xlarge w3-section", children=[
                        html.A(href='https://twitter.com/rootofarch', target='_blank', children=[
                            html.I(className="fa fa-twitter w3-padding-large"),
                        ]),
                        html.A(href='https://linkedin.com/in/rootofarch', target='_blank', children=[
                            html.I(className="fa fa-linkedin w3-padding-large"),
                        ]),
                        html.A(href='https://github.com/rootofarch', target='_blank', children=[
                            html.I(className="fa fa-github w3-padding-large"),
                        ]),
                    ]),
                ]),
                html.Div(className="w3-display-container w3-col m6", children=[
                    html.P("Behçet ŞENTÜRK"),
                    html.Div(className="w3-xlarge w3-section", children=[
                        html.A(href='https://twitter.com/behetsenturk', target='_blank', children=[
                            html.I(className="fa fa-twitter w3-padding-large"),
                        ]),
                        html.A(href='https://linkedin.com/in/behçet-şentürk', target='_blank', children=[
                            html.I(className="fa fa-linkedin w3-padding-large"),
                        ]),
                        html.A(href='https://github.com/bhctsntrk', target='_blank', children=[
                            html.I(className="fa fa-github w3-padding-large"),
                        ]),
                    ]),
                ]),
            ]),
        ])

def modeldef():
    return \
        html.Div(id="model_def", className="w3-padding-large", children=[

            html.Div(className="w3-row", children=[
                html.Div(id='model_inputs', style={'height': '50vh'}, className="w3-opacity-min w3-display-container w3-col m6 w3-padding-large", children=[
                    html.Div(className='w3-display-middle', children=[
                        html.Div(className='w3-container w3-center w3-padding-large', children=[
                            html.Span(className='w3-padding w3-black w3-xlarge w3-wide', children='NER MODELİ'),
                            html.Br(),
                            dcc.Input(
                                value='kuzgunlar/electra-turkish-ner',
                                style={'width': '500px'}, id='ner_input'),
                        ]),
                        html.Br(),
                        html.Br(),
                        html.Div(className='w3-container w3-center w3-padding-large', children=[
                            html.Span(className='w3-padding w3-black w3-xlarge w3-wide', children='Q&A MODELİ'),
                            html.Br(),
                            dcc.Input(
                                value='kuzgunlar/electra-turkish-qa',
                                style={'width': '500px'}, id='qa_input'),
                        ])
                    ])
                ]),

                html.Div(style={'height': '50vh'}, className="w3-display-container w3-col m6 w3-padding-large", children=[
                    html.Div(className='w3-display-middle w3-xlarge', children=[
                        html.P("İstediğiniz bir NER yahut Q&A modelini kullanabilirsiniz."),
                        html.P("İndirme hızınıza göre ilk çalıştırmada bir süre beklemeniz gerekecek.")
                    ])
                ]),  
            ])
        ])

def question_answer():
    return \
        html.Div(id="qa_section", className="w3-padding-large ", children=[
            html.Div(className='w3-center w3-opacity w3-padding w3-black w3-xlarge w3-wide', children='Q&A BÖLÜMÜ'),
            html.Div(className="w3-row", children=[
                html.Div(id='qa_input_sec', style={'height': '50vh'}, className="w3-opacity-min w3-display-container w3-col m6 w3-padding-large", children=[
                    html.Div(className='w3-display-middle', children=[
                        html.Div(className='w3-container w3-center w3-padding-large', children=[
                            html.Span(className='w3-padding w3-black w3-xlarge w3-wide', children='İÇERİK'),
                            html.Br(),
                            dcc.Textarea(
                                style={'height': '130px', 'width':'400px'},
                                id='qaContextTextArea'
                            ),
                        ]),
                        html.Br(),
                        html.Br(),
                        html.Div(className='w3-container w3-center w3-padding-large', children=[
                            html.Span(className='w3-padding w3-black w3-xlarge w3-wide', children='SORU'),
                            html.Br(),
                            dcc.Textarea(
                                style={'height': '50px', 'width':'400px'},
                                id='qaQuestionTextArea'
                            ),
                        ]),
                    ])
                ]),
                html.Div(style={'height': '50vh'}, className="w3-display-container w3-col m6 w3-padding-large", children=[
                    html.Div(className='w3-display-middle', children=[
                        html.Div(className='w3-container w3-center', children=[
                            html.Textarea(
                                style={'height': '130px', 'width':'400px'},
                                disabled=True,
                                id='qaAnswerInput'
                            ),
                            html.Br(),
                            html.Br(),
                            dbc.Button(
                                color="dark", 
                                id='qaGetAnswerButton',
                                n_clicks=0,
                                children='CEVABI BUL',
                            ),
                        ]),
                    ]),
                ]),
            ])
        ])

def ner():
    return \
        html.Div(id="ner_section", className="w3-padding-large", children=[
            html.Div(className='w3-center w3-opacity w3-padding w3-black w3-xlarge w3-wide', children='NER BÖLÜMÜ'),
            html.Div(className="w3-row", children=[
                html.Div(id='ner_input_sec', style={'height': '50vh'}, className="w3-opacity-min w3-display-container w3-col m6 w3-padding-large", children=[
                    html.Div(className='w3-display-middle', children=[
                        html.Div(className='w3-container w3-center w3-padding-large', children=[
                            html.Span(className='w3-padding w3-black w3-xlarge w3-wide', children='İÇERİK'),
                            html.Br(),
                            dcc.Textarea(
                                style={'height': '130px', 'width':'400px'},
                                id='nerContextTextArea'
                            ),
                        ]),
                    ])
                ]),
                html.Div(style={'height': '50vh'}, className="w3-display-container w3-col m6 w3-padding-large", children=[
                    html.Div(className='w3-display-middle', children=[
                        html.Div(
                            className='w3-border',
                            style={'height': '130px', 'width':'400px', 'overflow': 'scroll'},
                            id='nerLabelsTextArea'
                        ),
                        html.Br(),
                        html.Br(),
                        html.Div(className='w3-container w3-center', children=[
                            dbc.Button(
                                color="dark", 
                                id='nerGetLabelsButton',
                                n_clicks=0,
                                children='ETİKETLERİ BUL',
                            ),
                        ]),
                    ]),
                ]),
            ])
        ])

def footer():
    return \
        html.Div(className='w3-center w3-opacity-min w3-padding w3-black w3-wide', children=[
            html.A(className='w3-hover-opacity w3-margin-right', href='https://www.acikhack.com/', target='_blank', children=[
                html.Img(src="/assets/logo_acikhack.png", width=75, height=20),
            ]),
            html.A(className='w3-hover-opacity w3-margin-left', href='https://www.teknofest.org/', target='_blank', children=[
                html.Img(src="/assets/logo_teknofest.png", width=75, height=45),
            ]),
        ])


def mainPage():
    return \
        html.Div(id='body', children=[
            header(),
            description(),
            modeldef(),
            question_answer(),
            ner(),
            footer()
        ])


app.layout = mainPage()


@app.callback(
    Output("qaAnswerInput", "value"),
    [Input("qaGetAnswerButton", "n_clicks")],
    [State('qa_input', 'value'),
     State("qaContextTextArea", "value"),
     State("qaQuestionTextArea", "value")],
)
def getAnswer(n_clicks, model_name, context, question):
    if n_clicks is None or n_clicks == 0:
        raise PreventUpdate

    qa = QuentionAnswer(model_name)
    answer_data = qa.answer(question, context)

    answer = answer_data['answer']

    return answer


def fancyNER(context, entities):
    entities_list = [e['entity_group'] for e in entities]

    # Create random colors for unique entities
    entity_color_map = {}
    for e in set(entities_list):
        entity_color_map[e] = 'hsl(0, 0%, '+str(random.randint(0,70))+'%)'

    # Split context from entities
    for e in entities:
        #e['word'] = e['word'].replace("##", "")  # Remove dashes if there are
        context = context.replace(e['word']+' ', '-ENTITIY-'+e['entity_group']+'-ENTITIY-'+e['word']+'-ENTITIY- ')
    splitted_context = context.split('-ENTITIY-')
    
    # Change entities with span element
    result = []
    i = 0
    while i < len(splitted_context):
        if splitted_context[i].strip() not in entities_list:
            result.append(splitted_context[i])
        else:
            word = splitted_context[i+1]
            entity = splitted_context[i]
            color = entity_color_map[entity]

            word_entity = word+'('+entity+')'

            span_element = html.Span(word_entity, className='w3-padding-small', style={'background-color':color, 'color':'white'})

            result.append(span_element)

            i += 1  # Pass e['word']
        i += 1 
    return result


@app.callback(
    Output("nerLabelsTextArea", "children"),
    [Input("nerGetLabelsButton", "n_clicks")],
    [State('ner_input', 'value'),
     State("nerContextTextArea", "value")],
)
def getEntities(n_clicks, model_name, context):
    if n_clicks is None or n_clicks == 0:
        raise PreventUpdate

    ner = Ner(model_name)
    entities = ner.entities(context)

    return fancyNER(context, entities)


if __name__ == '__main__':
    app.run_server(debug=False)
