from pixflow import (
    read_image, save_image,
    resize_image, transfer_histogram, find_difference,
    plot_image, plot_result, plot_histogram
)

# 🔹 Leitura das imagens
image1 = read_image('flor1.jpg')               # Flor rosa
image2 = read_image('flor2.jpg')               # Flor laranja
image3 = read_image('flor1_alterada.jpg')      # Flor rosa com alteração (riscos)

# 🔸 Redimensionamento
resized = resize_image(image1, proportion=0.5)
plot_image(resized, title="Redimensionamento")
# save_image(resized, 'resized_image.jpg')       # Salvar imagem redimensionada

# 🔸 Transferência de histograma
matched = transfer_histogram(image1, image2)
plot_result(image1, image2, matched, title="Transferência de Histograma")           # Visualizar resultado
# save_image(matched, 'histogram_matched.jpg')   # Salvar resultado opcionalmente

# 🔸 Diferença estrutural (entre flor rosa e flor laranja — estruturas diferentes)
difference1 = find_difference(image1, image2)
plot_result(image1, image3, difference1, title="Diferença Estrutural")
# save_image(difference1, 'difference_1.jpg')

# 🔸 Diferença estrutural (entre flor rosa e flor rosa alterada — faz sentido)
difference2 = find_difference(image1, image3)
plot_result(image1, image3, difference2, title="Diferença Estrutural")
# save_image(difference2, 'difference_2.jpg')

# 🔸 Plotar histograma da flor original
plot_histogram(image1)

print("Test completed successfully! 🚀")
