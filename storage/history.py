from firebase_admin import firestore


db = firestore.client()

def append(uid,role,content):
    doc_ref = db.collection("history").document(uid)
    doc_ref.set({"messages": []}, merge = True)
    doc_ref.update({
        "messages": firestore.ArrayUnion([{"role": role,"content": content}])
    })

def load(uid):
    doc_ref = db.collection("history").document(uid)
    doc = doc_ref.get()
    data = doc.to_dict()
    return data.get("messages",[])

def clear(uid):
    doc_ref = db.collection("history").document(uid)
    doc_ref.delete()


    