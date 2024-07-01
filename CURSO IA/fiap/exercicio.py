from sklearn.datasets import load_breast_cancer, load_diabetes
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Carregar os conjuntos de dados
cancer_data = load_breast_cancer()
diabetes_data = load_diabetes()

# Visualização de exemplo dos dados de câncer de mama
print("Características do câncer de mama:", cancer_data.feature_names)
print("Classes do câncer de mama:", cancer_data.target_names)

# Visualização de exemplo dos dados de diabetes
print("Características do diabetes:", diabetes_data.feature_names)

# Dividir o conjunto de dados de câncer de mama em treinamento e teste
X_train_can, X_test_can, y_train_can, y_test_can = train_test_split(
    cancer_data.data, cancer_data.target, stratify=cancer_data.target, random_state=42
)

# Dividir o conjunto de dados de diabetes em treinamento e teste
X_train_dia, X_test_dia, y_train_dia, y_test_dia = train_test_split(
    diabetes_data.data, diabetes_data.target, random_state=42
)

# SVM com diferentes kernels
training_accuracy_svm = []
test_accuracy_svm = []

kernels = ['linear', 'rbf', 'sigmoid']
for kernel in kernels:
    svm_model = svm.SVC(kernel=kernel)
    svm_model.fit(X_train_can, y_train_can)
    training_accuracy_svm.append(svm_model.score(X_train_can, y_train_can))
    test_accuracy_svm.append(svm_model.score(X_test_can, y_test_can))

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(kernels, training_accuracy_svm, label='Acurácia no conj. treino (SVM)')
plt.plot(kernels, test_accuracy_svm, label='Acurácia no conj. teste (SVM)')
plt.ylabel('Acurácia')
plt.xlabel('Kernels')
plt.title('Curvas de Aprendizado para SVM com Kernels diferentes')
plt.legend()

# Árvore de decisão com diferentes profundidades máximas
training_accuracy_tree = []
test_accuracy_tree = []

prof_max = range(1, 10)
for md in prof_max:
    tree = DecisionTreeClassifier(max_depth=md, random_state=0)
    tree.fit(X_train_can, y_train_can)
    training_accuracy_tree.append(tree.score(X_train_can, y_train_can))
    test_accuracy_tree.append(tree.score(X_test_can, y_test_can))

plt.subplot(1, 2, 2)
plt.plot(prof_max, training_accuracy_tree, label='Acurácia no conj. treino (Árvore de Decisão)')
plt.plot(prof_max, test_accuracy_tree, label='Acurácia no conj. teste (Árvore de Decisão)')
plt.ylabel('Acurácia')
plt.xlabel('Profundidade Máxima')
plt.title('Curvas de Aprendizado para Árvore de Decisão com Profundidades diferentes')
plt.legend()

plt.tight_layout()
plt.show()

training_error = []
test_error = []

# Testar com e sem intercepto
for intercept in [True, False]:
    regr = LinearRegression(fit_intercept=intercept)
    regr.fit(X_train_dia, y_train_dia)
    training_error.append(mean_absolute_error(y_train_dia, regr.predict(X_train_dia)))
    test_error.append(mean_absolute_error(y_test_dia, regr.predict(X_test_dia)))

# Plotar os resultados
plt.plot(["Com Intercepto", "Sem Intercepto"], training_error, label='Erro no conj. treino')
plt.plot(["Com Intercepto", "Sem Intercepto"], test_error, label='Erro no conj. teste')
plt.ylabel('Erro Absoluto Médio')
plt.xlabel('Fit Intercept')
plt.title('Erro do Modelo de Regressão Linear com e sem Intercepto')
plt.legend()
plt.show()

