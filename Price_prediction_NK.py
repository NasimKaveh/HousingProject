import pandas as pd
import numpy as np
import xgboost
from xgboost import plot_importance
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from string_to_int import preprocess
import matplotlib.pyplot as plt

df_train = preprocess(df=pd.read_csv('train.csv'))
df_train.to_numpy()
y_set_train = (np.array(df_train.SalePrice)).reshape((1460,1))
x_set_train = (np.array(df_train.drop(['SalePrice'], axis = 1))).reshape((1460, 61))

df_test = preprocess(df=pd.read_csv('test.csv'))
df_test.to_numpy()
y_set_test = (np.array(df_train.SalePrice)).reshape((1460,1))
x_set_test = (np.array(df_train.drop(['SalePrice'], axis = 1))).reshape((1460, 61))


#To normalize the dataset
scaler = MinMaxScaler(feature_range=(0, 1))
x_set_train = scaler.fit_transform(x_set_train)
y_set_train = scaler.fit_transform(y_set_train)

x_set_test = scaler.fit_transform(x_set_test)
y_set_test = scaler.fit_transform(y_set_test)

#kfold
scores = []
best_svr = SVR(kernel='rbf')
cv = KFold(n_splits=10, random_state=42, shuffle=False)
for train_index, test_index in cv.split(x_set_train):
    print("Train Index: ", train_index, "\n")
    print("Test Index: ", test_index)

    X_train, X_test, y_train, y_test = x_set_train[train_index], x_set_train[test_index], y_set_train[train_index], y_set_train[test_index]
    best_svr.fit(X_train, y_train)
    scores.append(best_svr.score(X_test, y_test))

print(np.mean(scores))


#Linear regression
X_train, X_test, y_train, y_test = train_test_split(x_set_train, y_set_train, random_state=0)
linreg = LinearRegression().fit(X_train, y_train)

#XGBoost Regression
best_xgb_model = xgboost.XGBRegressor(colsample_bytree=0.4,
                 gamma=0,                 
                 learning_rate=0.07,
                 max_depth=3,
                 min_child_weight=1.5,
                 n_estimators=10000,                                                                    
                 reg_alpha=0.75,
                 reg_lambda=0.45,
                 subsample=0.6,
                 seed=42)
best_xgb_model.fit(x_set_train, y_set_train)

df_test['Prediction'] = np.expm1(best_xgb_model.predict(x_set_test))
filename = 'submission.csv'
pd.DataFrame({'Id': df_test.Id, 'SalePrice': df_test.Prediction}).to_csv(filename, index=False)