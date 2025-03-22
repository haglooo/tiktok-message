from requests import post
from pyproto import ProtoBuf
from json import loads

sessionid = ''
send_to = '1234'
self = '123'
message = 'test'


class PbEnc:
    @staticmethod
    def encrypt_pb_payload(payload: str) -> str:
        try:
            return ProtoBuf(payload).toBuf()
        except Exception:
            return None
    
    @staticmethod
    def pb_get_raw_body(data: bytes, a: int, b: int) -> str:
        return ''.join(ProtoBuf(data).getProtoBuf(a).getBytes(b)).decode("utf-8")
    
    @staticmethod
    def get_rresp(response_body: str) -> str:
        try:
            json_res = response_body[response_body.find('['):]
            parse_m = loads(json_res)
            return {"rresp": parse_m[1]}
        except ValueError:
            return None


payload = {
    1: 100,
    2: 627793,
    3: "local",
    4: "",
    5: 1,
    6: 0,
    7: "0",
    8: {
        100: {
        1: f"0:1:{send_to}:{self}",
        2: 1,
        3: 65346,
        4: f"{{\"text\":\"{message}\",\"is_card\":true,\"reference_scene\":0,\"sendStartTime\":1,\"aweType\":700}}",
        6: 7,
        }
    },
    9: "213",
    10: "googleplay",
    11: "android",
    12: "G011A",
    13: "7.1.2",
    14: "124124",
    18: 0,
    21: ""
}

url = 'https://api32-normal-no1a.tiktokv.eu/v1/message/send?aid=1233'
headers = {
    "cookie": f"sessionid={sessionid}",
    "Content-Type": "application/x-protobuf",
    "Accept": "application/json"
}

payload = PbEnc().encrypt_pb_payload(payload)

r = post(url, headers=headers, data=payload)
print(r.text)
