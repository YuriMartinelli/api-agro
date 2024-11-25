import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desabilita o rastreamento de modificações (para otimização)
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
