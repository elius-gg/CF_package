import logging
from codigofacilito_ver import unreleased

logging.basicConfig(level=logging.WARNING) # Para forzar a que se muestre por consola a partir de los WARNING
"""
INFO -> 10
DEBUG -> 20
WARNING -> 30
ERROR -> 40
CRITICAL -> 50
"""

if __name__ == '__main__':
    logging.debug('>>>> El paquete ha comnezado a ejecutarse.')

    workshops = unreleased()
    print(workshops)

    print('>>>> La ejecucion de este paquete ha finalizado.')