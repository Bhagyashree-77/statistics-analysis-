from simple_image_download import simple_image_download as simpl

 
response = simpl.simple_image_download

 

keywords = ["Elon Musk", "mark twain"]

for kw in keywords:
    response.download(kw, 10)

