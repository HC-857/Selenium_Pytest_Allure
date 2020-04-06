from pack.pack_manager import TestManager
import pytest
from multiprocessing import Pool

driver_infos = [
    "chrome",
    "firefox"
]

def run_parallel(driver_info):
    pytest.main([f"--cmdopt={driver_info}", "--alluredir",
                 f"./report/allure_result/{driver_info}"])
    manager = TestManager()
    manager.generate_report(driver_info)


def pytest_start():
    with Pool(len(driver_infos)) as pool:
        pool.map(run_parallel, driver_infos)
        pool.close()
        pool.join()

if __name__ == '__main__':
    pytest_start()
