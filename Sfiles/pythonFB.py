import pyrebase

config = {
    'apiKey': "AIzaSyASZlbFTiUNd8_lm7r_ODqE9NSQDZR5Ojw",
    'authDomain': "neoneclipse-5f706.firebaseapp.com",
    'databaseURL': "https://neoneclipse-5f706-default-rtdb.europe-west1.firebasedatabase.app",
    'storageBucket': "neoneclipse-5f706.appspot.com",
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()


def setNetworkIpv4(ipv4):
    data = {'ipv4': ipv4}
    db.child('ipv4Network').set(data)


def setNetworkPort(port):
    data = {'port': port}
    db.child('NetworkPort').set(data)


def getNetworkIpv4():
    return db.child('ipv4Network').get().val().get('ipv4')


def getNetworkPort():
    return db.child('NetworkPort').get().val().get('port')