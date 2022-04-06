def handle_uploaded_file(f):
    with open("parth_app/static/parth_app/uploads"+f.name,"wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    