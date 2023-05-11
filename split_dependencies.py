from typing import Callable

DEV_REQUIREMENTS = ["autopep8", "black", "flake8", "pytest-asyncio", "pytest", "Faker"]


def run():
    dependencies = clean_list(load_requirements())
    dev_dependencies = extract(is_dev_requirement, dependencies)
    prod_dependencies = extract(is_prod_requirement, dependencies)
    save_requirements("requirements-dev.txt", prepare_data(dev_dependencies))
    save_requirements("requirements.txt", prepare_data(prod_dependencies))


def extract(criteria: Callable, data: list) -> list:
    return list(filter(lambda item: criteria(item), data))


def is_dev_requirement(item: str) -> bool:
    package_name, version = item.split("==")
    return package_name in DEV_REQUIREMENTS


def is_prod_requirement(item: str) -> bool:
    return not is_dev_requirement(item)


def load_requirements(fname="requirements.txt") -> list:
    with open(fname, "r") as f:
        dependencies = f.readlines()
    return dependencies


def save_requirements(fname: str, data: str) -> None:
    with open(fname, "w") as f:
        f.write(data)


def prepare_data(data: list) -> str:
    return "\n".join(data) + "\n"


def clean_list(items: list) -> list:
    return list(map(lambda item: item.strip(), items))


if __name__ == "__main__":
    run()
