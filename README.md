# sceptre-aws
Deploy and manage AWS account for Sceptre tests

## Requirements:
* Install [pre-commit](https://pre-commit.com/#install) app
* Clone this repo
* Run `pre-commit install` to install the git hook.

## Testing
As a pre-deployment step we syntatically validate our sceptre and
CloudFormation YAML files with [pre-commit](https://pre-commit.com).

Please install pre-commit, once installed the file validations will
automatically run on every commit.  Alternatively you can manually
execute the validations by running `pre-commit run --all-files`.

## Continuous Integration
We have setup CI to deploy CloudFormation templates in this project
on mergees to master.

## Workflow
The workflow to provision AWS resources is done using pull requests.

1. Create a PR. This will trigger the CI to run a linter test job.
2. Review PR and verify tests passed.
3. Approve & Merge PR.

Once PR is merged the CI will run the deploy job to automatically
deploy the CloudFormation templates using sceptre.