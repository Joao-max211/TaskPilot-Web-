from sqlalchemy import create_engine

engine = create_engine('sqlite:////home/lucas/Estudos/Projetos/TaskPilot_web/back_end/database/database.db', echo=True)
