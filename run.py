from pack.pack_manager import TestManager
import pytest
from multiprocessing import Pool

driver_infos = [
    ["chrome", "test_case/test_login.py", "test1"],
    ["chrome", "test_case/test_login2.py", "test2"]
]

def run_parallel(driver_info):
    pytest.main([driver_info[1],
                 f"--cmdopt={driver_info[0]}", "--alluredir",
                 f"./report/allure_result/{driver_info[0]}",])
    manager = TestManager()
    manager.generate_report(driver_info[2])


def pytest_start():
    with Pool(len(driver_infos)) as pool:
        pool.map(run_parallel, driver_infos)
        pool.close()
        pool.join()

if __name__ == '__main__':
    pytest_start()
