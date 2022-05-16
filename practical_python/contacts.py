contacts = {
    "number":3,
    "students":
    [ 
        {"name": "Michael Scott", "email":"1234@email.com"},
        {"name": "Jim Halpert", "email":"bigbird@email.com"},
        {"name": "Pam Beasley", "email":"artist@email.com"}

    ]
}

for student in contacts["students"]:
    print(student["name"])
    print(student["email"])