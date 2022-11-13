import boto3
import json

s3 = boto3.resource("s3")
client = boto3.client("rekognition")

def detecta_faces():
  faces_detectadas = client.index_faces(
    CollectionId="faces",
    DetectionAttributes=[
      "DEFAULT"
    ],
    ExternalImageId="TEMPORARIA",
    Image={
      "S3Object": {
        "Bucket": "lambda-imagens-alura",
        "Name": "_analise.png",
      }
    },
  )
  return faces_detectadas


def cria_lista_faceId_detectadas(faces_detectadas):
  faceId_detectadas = []
  for imagem in range(len(faces_detectadas["FaceRecords"])):
    faceId_detectadas.append(faces_detectadas["FaceRecords"][imagem]["Face"]["FaceId"])
  return faceId_detectadas


def compara_imagens(faceId_detectadas):
  resultado_comparacao = []
  for ids in faceId_detectadas:
    resultado_comparacao.append(
      client.search_faces(
        CollectionId='faces',
        FaceId=ids,
        MaxFaces=10,
        FaceMatchThreshold=80
      )
    )
  return resultado_comparacao
   

faces_detectadas = detecta_faces()
faceId_detectadas = cria_lista_faceId_detectadas(faces_detectadas)
resultado_comparacao = compara_imagens(faceId_detectadas)
print(json.dumps(
  resultado_comparacao, indent=4
))