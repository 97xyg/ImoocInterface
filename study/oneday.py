import requests
import json
url = 'http://www.imooc.com/api3/updateversion'
get_url = 'https://www.imooc.com/apiw/logo?callback=jQuery210029960238633298286_1576376803442&_=1576376803443'
data = {
        "uid":"8227928",
        "v_code":"6030",
        "v":"6.0.3",
        "plat_id":"2",
        "secrect":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWUiOiI4MjI3OTI4IiwianRpIjoiZDVjZmM0ZTBkM2RjOGQ4Y2E2ZGQwNWM4MTc2YjVjMjUiLCJkZXZpY2UiOiJtb2JpbGUifQ.TyzNWHf4Lc8fvmopSWMd81ssAF3AT_cJFirfiE0OODs",
        "type":"0",
        "app_id":"1",
        "uuid":"d0d981e51ae08fd50b10425b8814c675",
        "timestamp":"1576384255815",
        "token":"cbef0c1931aa22c705386bcc82672155"
        }
res_text = requests.get(get_url).text
print(res_text)
#res = requests.post(url,data,verify=False)

#json_res = res.json()
#print(json.dumps(json_res,indent=4,ensure_ascii=False))
#print(res_text)