import random

#DEFAULT NAME 
print (" _ __ | |__  _ ___| |__   ___ _ _")
print("  | '_ \\| '_ \\| / __| '_ \\ / _ \\ '__|")
print(" _| |_) | | | | \\__ \\ | | |  __/ |")
print(" /.__/|_| |_|_|___/_| |_|\\___|_|")
print("  | | ")
print("  |_|         ...                Version : 1.0.0")

print ("     ")
print ("     ")
print ("     ")
print ("     ")
print ("     ")
print ("ⓘWarning about the Illegality of Fraud Through Fake Emails")

print("Using fake emails to commit fraud is an illegal activity and severely punished by law. Some of these are:")
print("")
print("/ⓘphishing")
print("/ⓘIdentity theft ")
print("/ⓘSending malware")
print ("")
print ("")
#OPTIONS
print("1.ACCOUNT GENERATE(HOTMAIL.COM, GMAIL.COM, OUTLOOK.COM)")
options = int(input("SELECT AN OPTION:"))
if options == 1:
    caracteres_contraseña = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/"

    # Función para generar una dirección de correo electrónico
    def generar_correo(nombre_usuario, dominio):
        return nombre_usuario + "@" + dominio

    # Función para generar un nombre de usuario aleatorio
    def generar_nombre_usuario(longitud=8):
        caracteres_usuario = "1234567890AnaMaríaJuanCarlosSofíaMiguelLauraPedroLucíaAndrésValeriaJorgeCamilaFernandoIsabelLuisGabrielaRicardoElenaDanielaMartínPaulaRobertoClaraDiegoMartaSantiagoAlejandraHugoPatriciaIvánRosaManuelTeresaAdriánBeatrizAlbertoVictoriaRaúlCristinaEnriqueSilviaÓscarNataliaJavierLorenaAntonioCarmenEduardoSaraFelipeInésMarcosAliciaPabloVerónicaÁlvaroEstherRubénIreneMarioÁngelaRamónNuriaGonzaloEvaFranciscoJuliaRafaelMónicaJesúsMarinaJohanso"
        nombre_usuario = ''.join(random.choice(caracteres_usuario) for i in range(longitud))
        return nombre_usuario

    # Función para generar una contraseña aleatoria
    def generar_contraseña(longitud=12):
        contraseña = ''.join(random.choice(caracteres_contraseña) for i in range(longitud))
        return contraseña

    # Lista de dominios
    dominios = ["hotmail.com", "gmail.com", "outlook.com"]

    # Generar correos electrónicos y contraseñas
    for dominio in dominios:
        nombre_usuario = generar_nombre_usuario()
        correo = generar_correo(nombre_usuario, dominio)
        contraseña = generar_contraseña()
        print("Correo: " + correo + ", Contraseña: " + contraseña, "")
