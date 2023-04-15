import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from google.cloud import storage
from google.oauth2 import service_account
from firebase_admin import credentials, storage





cred = credentials.Certificate("hackverse-5ecdd-firebase-adminsdk-ftdmd-308179e4be.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'hackverse-5ecdd.appspot.com'})



def write_to_firestore(colection_name: str, details: dict):
    # app = firebase_admin.initialize_app(cred)
    
    firestore_client = firestore.client()
    doc_ref = firestore_client.collection(colection_name).document()
    doc_ref.set(
        details
    )
    



def upload_blob(bucket_name, source_file_name, destination_blob_name):
    # cred = credentials.Certificate("hackverse-5ecdd-firebase-adminsdk-ftdmd-308179e4be.json")
    bucket = storage.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")
    blob.make_public()
    print(blob.public_url)



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



# Example usage
upload_blob('hackverse-5ecdd.appspot.com', 'wordle.png', 'wordle.png')
# write_to_firestore('fire', details)

