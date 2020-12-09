#!/usr/bin/env python3

from aws_cdk import core

from s3_static_hosting.s3_static_hosting_stack import S3StaticHostingStack


app = core.App()
S3StaticHostingStack(app, "s3-static-hosting")

app.synth()
