import boto3

s3 = boto3.resource("s3")
client = boto3.client("rekognition")
response=client.create_collection(CollectionId='faces')

def lista_imagens():
  imagens = []
  bucket = s3.Bucket("lambda-imagens-alura")
  for imagem in bucket.objects.all():
    imagens.append(imagem.key)
  print(imagens)
  return imagens


def indexa_colecao(imagens):
  for imagem in imagens:
    response = client.index_faces(
      CollectionId="faces",
      DetectionAttributes=[
      ],
      ExternalImageId=imagem[:-4],
      Image={
        "S3Object": {
          "Bucket": "lambda-imagens-alura",
          "Name": imagem,
        }
      },
    )
    print('response: ', response)


imagens = lista_imagens()
indexa_colecao(imagens)
