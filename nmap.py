import os
import mysql.connector
import subprocess

red="200.33.171.20"

output = os.popen('nmap -sT ' + red).readlines()
puertos = output[5:len(output)-2]

# DB
db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  passwd = "",
  database = "web"
)

cursor = db.cursor()

for obj in puertos:
  fields = obj.split()
  sql = "INSERT INTO puertos (puerto, estado, servicio) VALUES (%s, %s, %s)"
  val = (fields[0], fields[1], fields[2])
  cursor.execute(sql, val)

db.commit()