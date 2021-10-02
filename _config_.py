#coding: utf-8

'''
Fichier pour l'adressage des différents équipement

'''

import platform
import subprocess

def myping(host):
    parameter = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', parameter, '1', host]
    response = subprocess.call(command)

    if response == 0:
        return True
    else: 
        return False

if myping('192.168.120.1') == True:
    _MCZip='192.168.120.1'
elif myping('192.168.244.1') == True:
    _MCZip='192.168.244.1'
else:
    exit()

_MQTT_ip='127.0.0.1'				#Adresse IP du broker mqtt
_MQTT_port=1883						#Port du broker mqtt
_MQTT_authentication=False          #Mqtt use authentication
_MQTT_user=''			            #Mqtt User name
_MQTT_pass=''			            #Mqtt password
_MQTT_TOPIC_SUB='SUBmcz'			#Topic général de souscription
_MQTT_TOPIC_PUB='PUBmcz'			#Topic général de publication
#_MCZip='192.168.120.1'				#Adresse IP du poêle
_MCZport='81'						#Port du serveur embarqué du poele
_VERSION='1.5'						#Version
_AUTHOR='Anthony L.'				#Auteur
