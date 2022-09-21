# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:01:52 2022

@author: maria
"""
#INSTALAR PIP INSTALL STREAMLIT_AGRAPH


# karate_club_graph.py
# An example of basic and common interoperability between 
# streamlit-agraph and networkx.
#
# Use the following command to launch the app
# streamlit run <path-to-script>.py

import networkx as nx
import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from PIL import Image


#https://streamlit.io/

def create_karateClub():
    image = Image.open('karate_club.jpg')
    
    G = nx.karate_club_graph()
    color_node = {'Mr. Hi': 'red', 'Officer': 'blue'}
    nodes = [Node(id=i, label=str(i) ,color = color_node[G.nodes[i]['club']], size=10) for i in range(len(G.nodes))]
    edges = [Edge(source=i, target=j, type="CURVE_SMOOTH") for (i,j) in G.edges]
    return image, nodes, edges

def create_davis():
    image = Image.open('davis_women.jpg')
    
    G = nx.davis_southern_women_graph()
    nodes = [Node(id=node, label=node , size=10) for node in G.nodes]
    edges = [Edge(source=i, target=j, type="CURVE_SMOOTH") for (i,j) in G.edges]
    return image, nodes, edges


def create_florentine():
    image = Image.open('italy.png')
    G = nx.florentine_families_graph()
    nodes = [Node(id=node, label=node , size=10) for node in G.nodes]
    edges = [Edge(source=i, target=j, type="CURVE_SMOOTH") for (i,j) in G.edges]
    return image, nodes, edges
    
st.sidebar.header('Visualização de grafo')    
tipo_grafo = st.sidebar.selectbox(
    'Escolha o seu grafo',
    ('Karate Clube', 'Davis Southern Women Graph', 'Florentine Families'))

if(tipo_grafo == 'Karate Clube'):
    image, nodes,  edges = create_karateClub()
elif(tipo_grafo == 'Davis Southern Women Graph'):
    image, nodes,  edges = create_davis()
else:
    image, nodes,  edges= create_florentine()



config = Config(width=500, 
                 height=500, 
                 directed=True,
                 nodeHighlightBehavior=True, 
                 highlightColor="#F7A7A6",
                 collapsible=True,
                 node={'labelProperty':'label'},
                 link={'labelProperty': 'label', 'renderLabel': True}
                 ) 

col1, col2, col3 = st.columns(3)

with col1:
   st.image(image)

with col2:
    st.title(tipo_grafo)
    

return_value = agraph(nodes=nodes, edges=edges,  config=config)

