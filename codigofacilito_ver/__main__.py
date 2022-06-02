import logging
from codigofacilito_ver import unreleased

"""
INFO -> 10
DEBUG -> 20
WARNING -> 30
ERROR -> 40
CRITICAL -> 50
"""

#logging.basicConfig(level=logging.DEBUG) # Para forzar a que se muestre por consola los DEBUG
logging.basicConfig(level=logging.WARNING) # Para forzar a que se muestre por consola los WARNING

if __name__ == '__main__':
    logging.debug('>>>> El paquete ha comnezado a ejecutarse.')

    workshops = unreleased()
    print(workshops)

    print('>>>> La ejecucion de este paquete ha finalizado.')