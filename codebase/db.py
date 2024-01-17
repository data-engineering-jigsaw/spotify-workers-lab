from sqlalchemy import create_engine


def build_eng():
    host = 'localhost'
    port = '5432'
    database = 'spotify'
    engine = create_engine(f'postgresql+psycopg2://@{host}:{port}/{database}')
    return engine

engine = build_eng()