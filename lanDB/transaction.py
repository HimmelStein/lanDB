import records


def do_transaction(database, queryTranscation):
    db = records.Database(database)
    tx = db.transaction()
    try:
        print(queryTranscation)
        db.query(queryTranscation)
        tx.commit()
    except:
        tx.rollback()
        return False