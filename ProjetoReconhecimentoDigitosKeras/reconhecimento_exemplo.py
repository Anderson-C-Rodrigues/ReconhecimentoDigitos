import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist

model = load_model('modelo_mnist.h5')
(_, _), (x_test, y_test) = mnist.load_data()
x = x_test[0] / 255.0
x_input = x.reshape(1, 28, 28)

pred = model.predict(x_input)
print("Dígito previsto:", np.argmax(pred))

plt.imshow(x, cmap='gray')
plt.title("Imagem usada para predição")
plt.axis('off')
plt.show()
