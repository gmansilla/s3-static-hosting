from aws_cdk import core

from aws_cdk import (
    aws_s3 as s3,
    core as cdk,
)

from aws_cdk.aws_s3_deployment import BucketDeployment, Source



class S3StaticHostingStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        website_bucket = s3.Bucket(self, 
            "MyHostingBucketMF",
            versioned=True,
            public_read_access=True,
            website_index_document="index.html",
            removal_policy=cdk.RemovalPolicy.DESTROY
        )

        BucketDeployment(self, "DeployStaticWebsite",
            sources=[Source.asset("./website-dist")],
            destination_bucket=website_bucket
        )