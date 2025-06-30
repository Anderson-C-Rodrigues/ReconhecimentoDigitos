# Reconhecimento de Dígitos com Keras (MNIST)

Este projeto realiza o treinamento de uma rede neural para reconhecer dígitos manuscritos de 0 a 9 usando o dataset MNIST.

## 📁 Conteúdo

- `treinamento_mnist.py`: código de treinamento do modelo
- `reconhecimento_exemplo.py`: exemplo de reconhecimento usando o modelo treinado
- `modelo_mnist.h5`: modelo treinado (gerado após rodar o script de treinamento)
- `relatorio.md`: explicação técnica do funcionamento
- `imagens_exemplo/digito_3.png`: imagem de exemplo de um dígito manuscrito (3)

## ⚙️ Como executar

### 1. Requisitos
Instale o Python 3.8 ou superior e as bibliotecas necessárias:

```bash
pip install tensorflow matplotlib
```

### 2. Treinamento do modelo
```bash
python treinamento_mnist.py
```
Isso irá gerar o arquivo `modelo_mnist.h5`.

### 3. Reconhecimento (Predição)
```bash
python reconhecimento_exemplo.py
```
Este script carregará o modelo salvo e fará uma predição da primeira imagem de teste da base MNIST.

## 💡 Observação importante

> ⚠️ Este projeto foi originalmente desenvolvido no **Google Colab**, mas funciona perfeitamente em qualquer computador com Python instalado.
> Basta instalar as bibliotecas necessárias, colocar os arquivos na mesma pasta e rodar os scripts normalmente.

## 🧪 Exemplo
A imagem real (`digito_3.png`) está disponível na pasta `imagens_exemplo/` para testes adicionais com imagens do MNIST.

## 👨‍🏫 Projeto Acadêmico
Este projeto foi desenvolvido para a disciplina de Inteligência Artificial.
