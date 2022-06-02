from shutil import unregister_archive_format
from codigofacilito_ver.workshops import unreleased

if __name__ == '__main__':
    workshops = unreleased()
    print(workshops)