import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'port': 3306,
    'database': 'bd_ADIS',
    'raise_on_warnings': True
}


#################################################################################################################
# connexion au serveur de la base de données
def connexion():
    cnx = ""
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Mauvais login ou mot de passe")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La Base de données n'existe pas.")
        else:
            print(err)
    return cnx


#################################################################################################################
# fermeture de la connexion au serveur de la base de données
def close_bd(cursor, cnx):
    cursor.close()
    cnx.close()


###################################################################################################
# récupère toutes les données de la table synopsis
def get_SynopsisData():
    try:
        cnx = connexion()
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM synopsis"
        cursor.execute(sql)
        res = cursor.fetchall()
        close_bd(cursor, cnx)
        msg = "ok"
    except mysql.connector.Error as err:
        res = None
        msg = "Failed get SynopsisData: {}".format(err)
    return msg, res


###################################################################################################
# met à jour un champ de la table synopsis
def update_SynopsisData(champ, id_synopsis, newValue):
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        sql = "UPDATE synopsis SET " + champ + " = %s WHERE synopsis.id_synopsis = %s;"
        param = (newValue, id_synopsis)
        cursor.execute(sql, param)
        cnx.commit()
        close_bd(cursor, cnx)
        msg = "ok"
    except mysql.connector.Error as err:
        msg = "Failed update SynopsisData : {}".format(err)
    return msg
