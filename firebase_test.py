import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("hackverse-5ecdd-firebase-adminsdk-ftdmd-308179e4be.json")
app = firebase_admin.initialize_app(cred)
firestore_client = firestore.client()


details={
    "tittle": "Fire accident",
    "description": "A big building got large fire",
    "intensity": "7",
   
    "location": { "latitude": 13.009267, "longitude": 74.795371},
    "image":
      "https://bsmedia.business-standard.com/_media/bs/img/article/2022-05/13/full/1652462127-1638.jpg?im=Resize,width=480",
    #datetime: getCurrentDate(),
    "policehelp": True,
    "firehelp": True,
    "ambulancehelp": False,
    "otherhelp": False,
    "imageurl": "",
    "status": "NEW",
  }


doc_ref = firestore_client.collection("laptops").document()
doc_ref.set(
    details
)

