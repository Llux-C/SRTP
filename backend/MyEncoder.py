import json
import numpy as np

class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        """
        只要检查到了是bytes类型的数据就把它转为str类型
        :param obj:
        :return:
        """
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        elif isinstance(obj, np.int64):
            return int(obj)
        return json.JSONEncoder.default(self, obj)
