import boto3
from datetime import datetime
from shop_diary.config import (
    DDB_TABLE_NAME,
    DDB_TABLE_REGION
)


class ShopDiaryDB():
    def __init__(self):
        self.TABLE_NAME = DDB_TABLE_NAME
        self.ddb = boto3.resource(
            'dynamodb',
            region_name=DDB_TABLE_REGION
        )

    def _post_item(self, table_name, args):
        tb = self.ddb.Table(table_name)
        return tb.put_item(**args)

    def make_entry(self, shop_object, args):
        args['object'] = shop_object
        args['date'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self._post_item(self.TABLE_NAME, {"Item": args})
