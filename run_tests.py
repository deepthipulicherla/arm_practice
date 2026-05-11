import subprocess
import sys

def run(cmd):
    result = subprocess.run(cmd,shell=True)
    print(f"****Running {cmd} ******\n")
    if result.returncode != 0:
        sys.exit(result.returncode)

def main():
    mode = sys.argv[1] if len(sys.argv)>1 else "default"

    if mode == "parallel":
        run("pytest -n 4 -vv -s --alluredir=allure-results")
        run("allure serve allure-results")

    elif mode == "debug" :
        run("pytest -vv -s --pdb")

    elif mode == "regression":
        run("pytest -m regression -vv -s --alluredir=allure-results")
        run("allure serve allure-results")

    elif mode == "smoke":
        run("pytest -m smoke -vv -s --allure-dir=allure-results")
        run("allure serve allure-results")

    elif mode == "jenkins":
        print("Jenkins mode")
        run("pytest -vv -s --alluredir=allure-results")

    else:
        run("pytest -vv -s  --allure-dir=allure-results")
        run("allure serve allure-results")

if __name__ == "__main__":
    main()

