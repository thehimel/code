# AWS S3

## Setup

### Install

> Must have Python install as AWS CLI is written in Python.
* Install with `brew install awscli`
* Source: https://formulae.brew.sh/formula/awscli

### Get Credentials

* Got to IAM and create a user by attaching a policy like `S3FullAccess`.
* Generate access key for that user. It will provide access key and secret access key.

### Login

* Enter `aws configure`.
* Provide the access key and secret access key.
* Enter region name, for example, `us-east-1`.
* Enter a default output format, for example, `json`.
* Test the connection with a command, for example, `aws s3api list-buckets`.
