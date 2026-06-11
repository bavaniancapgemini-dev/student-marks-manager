import json

from database_v2 import (
    view_students_db
)

def export_json():

    data = view_students_db()

    file = open(
        "students_export.json",
        "w"
    )

    json.dump(
        data,
        file,
        indent=4
    )

    file.close()

    print(
        "JSON Exported"
    )