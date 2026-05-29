import cv2 
import numpy as np

# Setando o caminho das imagens

SetaFrente = cv2.imread('cards/Seta frente.png', 0)
SetaEsquerda = cv2.imread('cards/Seta esquerda.png', 0)
NovaPilha = cv2.imread('cards/Nova pilha.png', 0)
EmpilharBloco= cv2.imread('cards/Empilhar bloco.png', 0)
EmpilharRobo= cv2.imread('cards/Empilhar robo.png', 0)

orb = cv2.ORB_create()

# Detectando os pontos chave e os descritores das imagens

ponto_chave1, descritores1 = orb.detectAndCompute(SetaFrente, None)
ponto_chave2, descritores2 = orb.detectAndCompute(SetaEsquerda, None)
ponto_chave3, descritores3 = orb.detectAndCompute(NovaPilha, None)
ponto_chave4, descritores4 = orb.detectAndCompute(EmpilharBloco, None)
ponto_chave5, descritores5 = orb.detectAndCompute(EmpilharRobo, None)

# Comparando os descritores das imagens usando o método de força bruta (Brute Force)

print(descritores3[0])

# bf = cv2.BFMatcher()

# matches1 = bf.match(descritores1, descritores1, k=2)

# boa = []

# for m, n in matches1:
#     if m.distance < 0.75 * n.distance:
#         boa.append([m])


# ImgPontoChave1 = cv2.drawKeypoints(SetaFrente, ponto_chave1,None)
# ImgPontoChave2 = cv2.drawKeypoints(SetaEsquerda, ponto_chave2,None)
# ImgPontoChave3 = cv2.drawKeypoints(NovaPilha, ponto_chave3,None)
# ImgPontoChave4 = cv2.drawKeypoints(EmpilharBloco, ponto_chave4,None)
# ImgPontoChave5 = cv2.drawKeypoints(EmpilharRobo, ponto_chave5,None)

# cv2.imshow('Pontos chave Seta Frente', ImgPontoChave1)
# cv2.imshow('Pontos chave Seta Esquerda', ImgPontoChave2)
# cv2.imshow('Pontos chave Nova pilha', ImgPontoChave3)
# cv2.imshow('Pontos chave Empilhar bloco', ImgPontoChave4)
# cv2.imshow('Pontos chave Empilhar robo', ImgPontoChave5)

cv2.imshow('Seta Frente', SetaFrente)
cv2.imshow('Seta Esquerda', SetaEsquerda)
cv2.imshow('Nova pilha', NovaPilha)
cv2.imshow('Empilhar bloco', EmpilharBloco)
cv2.imshow('Empilhar robo', EmpilharRobo)

cv2.waitKey(0)

print("Imagens carregadas com sucesso!")