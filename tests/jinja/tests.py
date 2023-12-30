# Usage:
# [SNAPSHOT_UPDATE=true] pytest -ssvv tests/jinja/tests.py

import pytest
from jinja2 import Environment, FileSystemLoader
import yaml
import os
from typing import List, Tuple


def _render(path: str, file_name: str, context: str) -> str:
    """ Render a Jinja2 template """

    return Environment(
        loader=FileSystemLoader(path)
    ).get_template(file_name).render(context)


def _generate_test_params() -> List[Tuple[str, str]]:
    """ Generate the params for test_snapshot """
    context_dir = "tests/fixtures/contexts"
    expected_dir = "tests/fixtures/expected"
    test_params = []

    # Assume context and expected files follow the format:
    # <TEMPLATE_FILE_BASE_NAME>.<SOME_DESCRIPTION>.yaml
    #
    for context_file in os.listdir(context_dir):
        if context_file.endswith(".yaml"):
            base_name, description = context_file.rsplit(".", 2)[0:2]
            expected_file = f"{base_name}.{description}.yaml"
            test_params.append((base_name, description))

    return test_params


@pytest.mark.parametrize(
    "template_file_base_name, description",
    _generate_test_params()
)
def test_snapshot(
        template_file_base_name: str,
        description: str
    ) -> None:

    context_path = f"tests/fixtures/contexts/{template_file_base_name}.{description}.yaml"
    expected_path = f"tests/fixtures/expected/{template_file_base_name}.{description}.yaml"

    with open(context_path, "r", encoding="utf-8") as file_handle:
        context = yaml.safe_load(file_handle)

    template_dir = "./templates"
    template_file_name = f"{template_file_base_name}.j2"

    rendered = _render(
        template_dir,
        template_file_name,
        context
    )

    if os.getenv("SNAPSHOT_UPDATE", "").lower() == "true":
        print(f"Writing rendered text to {expected_path}")
        with open(expected_path, "w", encoding="utf-8") as file_handle:
            file_handle.write(rendered)                                                                      

    with open(expected_path, "r", encoding="utf-8") as file_handle:
        expected = file_handle.read()

    assert rendered == expected
