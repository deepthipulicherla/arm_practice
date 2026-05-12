import subprocess
import sys
import os
import shutil

def run(cmd):
    result = subprocess.run(cmd,shell=True)
    print(f"****Running {cmd} ******\n")
    if result.returncode != 0:
        sys.exit(result.returncode)

def generate_allure_report():
    """Generate allure-report folder without starting a server."""
    if os.path.exists("allure-report"):
        shutil.rmtree("allure-report")

    run("allure generate allure-results -o allure-report --clean")
def main():
    mode = sys.argv[1] if len(sys.argv)>1 else "default"

    if mode == "parallel":
        run("pytest -n 4 -vv -s --alluredir=allure-results")
        generate_allure_report()

    elif mode == "debug" :
        run("pytest -vv -s --pdb")

    elif mode == "regression":
        run("pytest -m regression -vv -s --alluredir=allure-results")
        generate_allure_report()

    elif mode == "smoke":
        run("pytest -m smoke -vv -s --alluredir=allure-results")
        run("allure serve allure-results")

    elif mode == "jenkins":
        print("Jenkins mode")
        run("pytest -vv -s  --alluredir=allure-results")
        generate_allure_report()

    else:
        run("pytest -vv -s --alluredir=allure-results")
        run("allure serve allure-results")

if __name__ == "__main__":
    main()

