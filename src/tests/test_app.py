import os

from srctools import bsp


def test_app():
    for file in os.listdir(os.getcwd()):
        if file.endswith("test_packmap.bsp"):
            assert "models/props/portal_door_combined_new.mdl" not in bsp.BSP(
                os.path.join(os.getcwd(), "test_packmap.bsp")).pakfile.namelist()


test_app()
