# https://cs50.harvard.edu/python/2022/psets/1/extensions/

filename = input("File name: ").strip().lower()

if filename.endswith(".gif"):
    print("image/gif")
elif filename.endswith((".jpeg", ".jpg")):
    print("image/jpeg")
elif filename.endswith(".png"):
    print("image/png")
elif filename.endswith(".pdf"):
    print("application/pdf")
elif filename.endswith(".txt"):
    print("text/plain")
elif filename.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
