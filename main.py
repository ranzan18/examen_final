from database.conector import *
from modelo.infante import centro deportivo


def ejecutador_clase():

    Base.metadata.create_all(engine)

    cd1 = ct (nombre="centro deportivo", direccion="Vista alegre")

    cd_p1 = centro deportivo (centro deportivo, direccion="Vista alegre", telefono="60254714", encargado="Ice D")

    session.add_all([cd1, cd_p1])
    session.commit()


if __name__ == '__main__':
    print("centro deporivo")
    app.run()
