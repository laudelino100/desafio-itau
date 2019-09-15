import twitter
import csv
import os
from heapq import nlargest
from operator import itemgetter
import http.server
import socketserver

def mensagens_por_tag(filename,data):
    print("Mensagens")
    csvFile = open(filename+".csv", 'a')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["Nome de Usuario","Criado em","Hashtag", "Texto"])
    for topic in data:
        tweets = api.GetSearch(term=topic, count=100)
        print("Salvango mensagens relativas ao topico", topic)
        for data in tweets:
            csvWriter.writerow([data.user.screen_name,data.created_at, topic ,data.text.encode('utf-8')])


def numero_seguidores(filename,data):
    print("Seguidores")
    csvFile = open(filename+".csv", 'a')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["Nome","Numero de Seguidores"])
    numero_de_followers = {}
    for topic in data:
        tweets = api.GetSearch(term=topic, count=100)
        lista_de_usuarios = []
        for data in tweets:
            lista_de_usuarios.append(data.user.id)
    dicionario_usuario = {}
    lista_de_usuarios = set(lista_de_usuarios)
    for user in lista_de_usuarios:
        dicionario_usuario[api.GetUser(user).name] = api.GetUser(user).followers_count
    for nome, n_seguidores in nlargest(5, dicionario_usuario.items(), key=itemgetter(1)):
        csvWriter.writerow([nome,n_seguidores])


api = twitter.Api(consumer_key=os.environ['consumer_key'],
                  consumer_secret=os.environ['consumer_secret'],
                  access_token_key=os.environ['token_key'],
                  access_token_secret=os.environ['token_secret'])
#cloud, #container, #devops, #aws, #microservices,
#docker, #openstack, #automation, #gcp, #azure,
#istio, #sre
hashtags = ['#cloud','#container', '#devops','#aws','#microservices', '#docker', '#openstack', '#automation', '#gcp', '#azure', '#istio', '#sre']
#users = ['ruthwignall']
mensagens_por_tag("mensagens",hashtags)
numero_seguidores("top_usuarios",hashtags)

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    with open('top_usuarios.csv', 'rt') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            print(line[0], line[1], PORT)
    #print("Top 5 seguidores\n"+ , PORT)
    httpd.serve_forever()



