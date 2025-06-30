# Relatório Técnico — Reconhecimento de Dígitos com Keras

## Objetivo
Desenvolver um sistema de aprendizado de máquina capaz de reconhecer dígitos manuscritos (0 a 9) utilizando redes neurais com Keras e o dataset MNIST.

## Funcionamento
- `treinamento_mnist.py`: treina uma rede neural com duas camadas ocultas (128 e 64 neurônios).
- O modelo é salvo como `modelo_mnist.h5`.
- `reconhecimento_exemplo.py`: realiza a predição sobre uma imagem e exibe o resultado.

## Execução

Requisitos:
```bash
pip install tensorflow matplotlib
```

Treinamento:
```bash
python treinamento_mnist.py
```

Reconhecimento:
```bash
python reconhecimento_exemplo.py
```

## Exemplo
A imagem `digito_3.png` está incluída como exemplo de entrada.

## Autoria
Projeto acadêmico — Inteligência Artificial.
