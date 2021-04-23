# sceptre-aws
Deploy and manage AWS account for Sceptre tests

## Workflow
The workflow to provision AWS resources is done using pull requests.
Request using PRs provide history, gating, reviewing and an approval
process.

## Requirements:
* Install [pre-commit](https://pre-commit.com/#install) app
* Clone this repo
* Run `pre-commit install` to install the git hook.

## Testing
As a pre-deployment step we syntatically validate our sceptre and
cloudformation yaml files with [pre-commit](https://pre-commit.com).

Please install pre-commit, once installed the file validations will
automatically run on every commit.  Alternatively you can manually
execute the validations by running `pre-commit run --all-files`.

## Continuous Integration
We have setup CI to deploy cloudformation template in this project on
mergees to master.
