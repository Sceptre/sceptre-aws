# sceptre-aws
This project is setup to deploy and manage resources in an AWS account
for executing Sceptre tests.

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
We have setup CI to deploy CloudFormation templates.  The templates
are used to setup cloud infrastructure for testing Sceptre.

### Setup AWS account
Instructions to bootstrap an AWS account for [GH actions OIDC access].

1. Login to AWS as the root user.
2. Goto the cloudformation console
3. Deploy the [oidc-provider.yaml](templates/oidc-provider.yaml) template to setup
an OIDC provider in the AWS account.  Use the following Sceptre template config
```yaml
template:
  path: oidc-provider.yaml
stack_name: oidc-provider
parameters:
  ThumbprintList:
    - "6938fd4d98bab03faadb97b34396831e3780aea1"
    - "1c58a3a8518e8759bf075b76b750d4f2df264fcd"
  Url: "https://token.actions.githubusercontent.com"
```
4. Deploy the [github-oidc-provider.j2](templates/github-oidc-provider.j2) to
allow a Github repository OIDC access the AWS account. For an example view the
[gh-oidc-sceptre-aws.yaml](config/prod/gh-oidc-sceptre-aws.yaml) file.


### Workflow
The workflow to provision additoinal AWS resources is done using pull requests.

1. Create a PR. This will trigger the CI to run a linter test job.
2. Review PR and verify tests passed.
3. Approve & Merge PR.

Once PR is merged the CI will run the deploy job to automatically
deploy the CloudFormation templates using sceptre.


[GH actions OIDC access]: https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services
