from sklearn.preprocessing import OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class OneHotEncoder_Colunas(BaseEstimator, TransformerMixin):
    def __init__( self, colunas):
        self.colunas = colunas
        self.enc = OneHotEncoder()

    def fit(self, X, y = None ):
        self.enc.fit(X[self.colunas])
        return self 

    def transform(self, X, y = None):
      X_categoricas = pd.DataFrame(data=self.enc.transform(X[self.colunas]).toarray(),
                                  columns= self.enc.get_feature_names(self.colunas))
      X = pd.concat([X, X_categoricas], axis=1).drop(self.colunas, axis=1)
      return X