import plotext as plt

path = plt.file.join_paths(plt.file.script_folder(), 'image.jpg')

size = [100,100]
size = plt.image_plot(path, size = size, keep_ratio = True)

plt.plotsize(*size)
plt.title("I USE FEDORA BTW")
plt.show()
