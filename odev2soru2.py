import numpy as np

ornekler = "herhangi_bir_bilgisayar_dosyası" ##burada değişken ataması yapmıştır. herhangibirbilgisayardosyası nı ornekler e atamış.

X = ornekler [:0] ## ornekleri atadığı kelimenin başlangıcından indexi sıfır olan harfe kadarki yerin listesini X e atamıştır.
Y = ornekler [:1] ## ornekleri atadığı kelimenin başlangıcından indexi bir olan harfe kadarki yerin listesini  Y ye atamıştır.

mean_x = np.mean (X) 
mean_y = np.mean (Y)

m=len(X)

numerator = 0
denominator = 0

for i in range (m):
    numerator += (X[i]-mean_x) + (Y[i]-mean_y)
    denominator += (X[i]-mean_x) ** 2

m= numerator / denominator
c= mean_y - (m*mean_x)

print(f'm={m} c = {c}') 

max_x = np.max(X)
min_x = np.min(Y)

x = np.linspace (min_x , max_x)
y = c + m * x 

plt.plot(x,y,'g',label = 'Eizgi')
plt.plot(X,Y, 'rx', label = 'Veriler')


plt.xlabel ("İlk sütundaki veri")
plt.ylabel ("İkinci sütundaki veri")
plt.legend()
plt.show()
