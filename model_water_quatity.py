import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import sklearn.preprocessing as sklp
from sklearn.model_selection import train_test_split

df = pd.read_csv('water_potability.csv')

# Danh gia du lieu dau vao x

# for label in df[df.columns[:-1]]:
#     plt.hist(df[df['Potability']==1][label],label ='Drinkable',alpha = 0.7,density = True)
#     plt.hist(df[df['Potability']==0][label],label ='Should Not Drink',alpha = 0.7,density = True)
#     plt.xlabel(label)
#     plt.ylabel('Potability')
#     plt.legend()
#     plt.show()

#Xu ly du lieu

# 'feature':label,
#         'count nan':df[label].isnull().sum(),
#Dem xem co bao nhieu du lieu o cac cot chua duoc xac dinh
print('So du lieu bi loi trong tap du lieu la ')
error = pd.DataFrame()
for label in df.columns:
    error = pd.concat([error, pd.DataFrame({
        'feature':label,
        'count nan':df[label].isnull().sum(),
    },index=[0])],ignore_index=True)

print(error)

# Thay the cac gia tri nan ban gia tri trung binh cot
df.fillna(df.mean(), inplace=True)

train, test = train_test_split(df, train_size = 0.7, random_state= 50)


def scale_data(dataframe):
    X = dataframe[dataframe.columns[:-1]]
    Y = dataframe[dataframe.columns[-1]]

    scaler = sklp.StandardScaler()

    X = scaler.fit_transform(X)

    return X,Y

X_train, y_train = scale_data(train)
X_test, y_test = scale_data(test)

# Xem du lieu duoc lay o tap train co mat can bang
print('\n\nDữ liệu ở các lớp ở tập train')
print(f'Train: {np.sum(y_train == 0)}')
print(f'Test: {np.sum(y_train == 1)}')


#Trien khai cac mo hinh
#SVM
from sklearn.svm import SVC
svc_model = SVC()

svc_model.fit(X_train,y_train)

y_pred = svc_model.predict(X_test)
svm_acc_score = accuracy_score(y_test,y_pred)

print('\n\nĐánh giá mô hình SVM với các tham số mặc đinh')
print(classification_report(y_test,y_pred))

#Toi uu hoa cac tham so

#Kernel and C prameter
kernels = ['linear','poly','rbf','sigmoid']
Cs = np.arange(0.1,3,0.1)


for ker in kernels:
    for c in Cs:
        svc_test = SVC(kernel=ker,C=c)
        svc_test.fit(X_train,y_train)
        y_pred_test = svc_model.predict(X_test)
        svm_acc_test = accuracy_score(y_test,y_pred_test)
        if(svm_acc_test>svm_acc_score):
            svc_model = svc_test
            svm_acc_score = svm_acc_test

print('\n\nĐánh giá mô hình SVM với các tham số sau khi tối ưu')
print(classification_report(y_test,svc_model.predict(X_test)))

#Logistic
from sklearn.linear_model import LogisticRegression
lg_model = LogisticRegression()
lg_model.fit(X_train,y_train)
y_pred = lg_model.predict(X_test)

lg_acc_score = accuracy_score(y_test,y_pred)

print('\n\nĐánh giá mô hình Logistic Regrssion')
print(classification_report(y_test,y_pred))


#Navies Bays
from sklearn.naive_bayes import GaussianNB
bayes_model = GaussianNB()
bayes_model.fit(X_train,y_train)
y_pred = bayes_model.predict(X_test)
bayes_accc_score = accuracy_score(y_test,y_pred)

print('\n\nĐánh giá mô hình Navies Bayes')
print(classification_report(y_test,y_pred))

#Perceptron
from sklearn.linear_model import Perceptron
per_model = Perceptron()
per_model.fit(X_train,y_train)
y_pred = per_model.predict(X_test)
per_acc_score = accuracy_score(y_test,y_pred)

print('\n\nĐánh giá mô hình Perceptron')
print(classification_report(y_test,y_pred))

#Danh gia hieu suat cua 4 mo hinh tren
model_acc = pd.DataFrame({
    'model':[ 'SVM model','Logistic model','Navies Bayes model','Perceptron'],
    'accuracy':[svm_acc_score*100,lg_acc_score*100,bayes_accc_score*100,per_acc_score*100],
}).sort_values(by='accuracy',ascending=False)
print('Hiệu suất của các mô hình sau huấn luyện là')
print(model_acc)

#Ket hop 3 mo hinh co hieu suat cao nhat mong muon dat mot hieu suat cao hon
from sklearn.ensemble import VotingClassifier
voting_model =VotingClassifier(estimators=[('SVM',svc_model),('Logistic',lg_model),('Navies Bayes',bayes_model)],voting='hard')
voting_model.fit(X_train,y_train)

y_pred = voting_model.predict(X_test)
#Hiệu suất sau khi kết hợp 3 mô hình
print(f'Đánh giá sau khi kết hợp 3 mô hình Logsitic, SVM, Navies Bayes')
print(classification_report(y_test,y_pred))