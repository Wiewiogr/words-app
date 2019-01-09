import boto3
from botocore.client import Config


class SpacesClient:
    def __init__(self, access_key, secret_key, bucket, region_name, endpoint_url):
        self.session = boto3.session.Session()
        self.client = self.session.client(
            "s3",
            region_name=region_name,
            endpoint_url=endpoint_url,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )
        self.bucket = bucket

    def get_list(self, prefix):
        response = self.client.list_objects(Bucket=self.bucket, Prefix=prefix)
        return list(map(lambda key: key["Key"], response["Contents"]))

    def get_subtitles_as_string(self, key):
        return (
            self.client.get_object(Bucket=self.bucket, Key=key)["Body"]
            .read()
            .decode("utf-8")
        )


if __name__ == "__main__":
    client = SpacesClient()
    for a in client.get_list("new-data/2"):
        print(a)
        print(client.get_subtitles_as_string(a))

