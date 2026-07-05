from fastapi import FastAPI
import requests
import json

app = FastAPI()

@app.get("/history")
def get_momo_history():
    url = "https://api.momo.vn/transhis/api/transhis/golden-pocket/trans/browse"

    headers = {
        "Host": "api.momo.vn",
        "sessionKey": "65c0f548-c301-4ddb-a8a4-c488470af591",
        "app_code": "5.11.0",
        "userId": "01682962182",
        "user_phone": "01682962182",
        "User-Agent": "MoMoPlatform Store/5.11.0.51100 CFNetwork/1410.1 Darwin/22.6.0 (iPhone X iOS/16.7.11) AgentID/110335164",
        "lang": "vi",
        "device_performance": "low-end",
        "app_version": "51100",
        "wbmky": "v2T7VFwlFi3ZNEAQ9OuN/ILUD8n6v6o5gPfKLAEPCs52/KpQGiiN4tpoio4FcC/mIt8DxNxGmAoLalbTEKYJmUJFnysGIZVzUnCftgDZK2oaH4nONn5lcBJGNvJ5bLYqY9V/+RTX/JvKICDmPqZuoQaA2FeFZTCNQbakMo7Vb92sgoGa48ppKViC4/k7/jfJYAScS87ZtuZb8wR/aPRZf/Brm60Wtni0ThpNGAhb2hH7PI+AThbALapUp8mASg3Wld7EG//A3TPgMy+buPYj62WD0IlbgPCgYzn/4knaarjPzj2YuIbyByOLTbBym6uNnBGwGnMC9ApfBGUzIjUM+g==",
        "Accept-Language": "vi-VN,vi;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "channel": "APP",
        "wbmtd": "/NYE/2lgrQKtHjMOmNbslEl6bqKLSyjUngA/seGyJfxzSF+mnBDySWJZoOBSZPd1B4pr5vIfO2ITBlXH7RNW0+mHvoAJeX2Nadmpsr7Gjigou2rq8/KcV/lViubElvlHBY3ABRFoCuhHVt01UBO4mcs3wphV/nbKiDN+NWY/5QjCEF8SOadwzweSZF58j2R0LqlZXj9kPX/uy8qbGQn4/Hu0rEbykGGiH45J2Whc2EKs/+X4MPII+Exmwqa88ezUhbMjQPQA11o4tiRW3tCUH59/wP+6a6GvhrIzG81ljAWKV8hLjHN3QGKz41qVwH73EGYvWAFCaRqxzJyNcXzUn6W1NKxxdNMKT/LM65AxVOfZ1bMLDdicQ1KmaOUqWx3mOqFmAT2+mCnoTn9i6Dw7+9Q0vxwc5UrbhfFYWm2oNMiTzP3P+tfGenK18Pgr8GaikPV/jSjxe5N93gFAFilZFHSc4sX/DXT2K/h4NCEISIxWTInmGFtytoCuxFIjvkkam8Dpjeu1HiGv67IBlN9nfPZEbnGpnq4kqIjm1EkC8xasoMKLo/XFMVqLxd7CcvnTlF2e5dXoQ5U52KqNB2xH+HhzzlNAb0NlLafnsNYwoXL1AYTl3TI8t5iKTjg1HXZ/oVb9KGLC0Hk0FMHG7OZq/poWU0Ut+rBUxKZJx8BPVnUSZ1ajI2Aye834tbnjTKQx9NjzLIVVcvqiDOJp78PMXff2F8MnRR5cT7cDN1P0mBYui+Bw2R5hZyGHI6G3eJUQE7bh1Wy98/m9aQ9zhaUJ5XO2RVc0s6vUcy9U1SuxztVUpFCmFEzy5KjE4VPTcqSvRilXBYmqtkEFBXHZSX4Dw9lJWOAv8MQmNlbPwlCjDcgTSV6zIBqCcMujT2O/1CLIYp/eJmt7oEzbAx041vGr61aILRWFSVH7Y1jAfEGWEDmOsJFe2Ofq7l0eKg9o0QRrX9LXaTzzz9yN7xiNcDHeWqTw6BBzNkEOoVyvj3svK7nsfK4M3jzb3qDBvSz3o1Ssf4sKOPqtK33/ZZpqIVYL+lfeOxu71XMR3p6vlfTWioNhEBmcfRa4V0mWkcXmbMB0PafxS7Qcl/wORdncwIWEpCGD10vfVvdz+KoAYdLCxAthI+5XrYUakJahawMVf/Da6gE9We892FoppPPs+Gg3M5Wv9OfqgFpozBRJPcKNhONIOnOKUKOVVTaTu3ZbbMM+9FzK5uU7zPcszaBO5TiIndabR5q9s1UAVRVe1Fvp0bcSDEsEPk/853lFOnvrI0X5dHqfrX2v5O9m/hmcBGcbyU+S6AKtRZb/uHNMb7MxfNTcC5WziGTd+Ezjfc7RnLUauTHoZ90G7bHYY3Zsp7M8jv8kiZfZjl3i65cInJ3x8iTcPtVFAqAzm12SIdp4gy1E",
        "momo-session-key-tracking": "8398DC87-02D6-4C22-91ED-4971EACB46F9",
        "wbCode": "0&1783239663515",
        "baggage": "sentry-environment=production,sentry-public_key=6e80c9f01f2440c9be5b37606028f996,sentry-release=vn.momo.platform.ios%405.11.0%2B51100,sentry-sample_rand=0.975339,sentry-sample_rate=0.050000,sentry-sampled=false,sentry-trace_id=f125956e01314eae894b064de8beca41,sentry-transaction=HomeSwiftViewController",
        "Connection": "keep-alive",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VyIjoiMDE2ODI5NjIxODIiLCJpbWVpIjoiNTAxMDMtMGUyYjQ4NTRkNzdhNTAyMWYzYTQ0N2JlN2ZkOTY1NGYwMDQ2ZDZjNDVkZWI0YWI5YzhiNjQwYjUwNzgxN2VlZiIsImhJbWVpIjoiQmV4RjYvbnliOW9mNlUySGVJZVBwQnBOvlY5dk1TZE1wRXZuMTdrVkY3bnpxWW1Sdis3dTRCMnVmTmFFLzV0TkswdTd0eEJKRG40S280bWRnVkRQV05wTVF4d01CZ3NvYUc1M3gzeGc3REU9IiwiTUFQX1NBQ09NX0NBUkQiOjAsIk5BTUUiOiJUcuG6p24gTmjhuq10IEhvw6BuZyIsIkRFVklDRV9PUyI6ImlvcyIsIkFQUF9WRVIiOjUxMTAwLCJhZ2VudF9pZCI6MTEwMzM1MTY0LCJzZXNzaW9uS2V5IjoiWVFQUjN0N01pUEt4L1hGa3ZHQ3RQeWhMc1lwLzBLWHdDWWJObEF1ZjNpUnh2VEZlRGRNSjNBPT0iLCJ1c2VyX3R5cGUiOjEsImtleSI6Im1vbW8iLCJyYXBpZF9pZCI6ImxKMHZSeFA5QjliNEhXQTRNTVIyZFZodGU5YUlXcDBmZ1dqWDhFTDdLRFI4TDZtRFM5UFFPVUdrbDE2enUzL0x4MUI4ZXUzYmIrVT0iLCJ1aWQiOiIwMTY4Mjk2MjE4MiIsImV4cCI6MTc4MzI0NTA0MX0.od8W8Yu31xTt6FDA0lHSDW0coa4MIaqdMNWZevo-aexW1GE9wLKe-igFCYquizB1EY-T3YKvp7FBKRZI8eGBl1pVy2o4T2aFCvjIDiWRPSGP7ZQFsu20yyqn9WmtZBsiAHHCuwiXgmEZeaFjPzYqrDEij2xhL6wRCQeVv_QL6D4ykIQQ_A7a84dG_saC38781z4x8UO0DDkmsoLJI45UQ-8c46PGNhSsYbPH9w9pe7PeJuC7PkY__hHNOx0T-GZFuIKIcI-1itEXhoqA_UPpO2jTc60aP7rtd_Ypif4vDvyBLRWe-dy6SIQ5OoL_w_xUbuRn0SJ-c5DIhmGRnlgtlg",
        "env": "production",
        "app_type": "production",
        "device_os": "IOS",
        "http-process-timestamp": "1783239663515",
        "timezone": "Asia/Ho_Chi_Minh",
        "Accept-Charset": "UTF-8",
        "Accept": "application/json",
        "agent_id": "110335164",
        "Content-Type": "application/json",
        "sentry-trace": "f125956e01314eae894b064de8beca41-f1e7ece697cc47f0-0",
        "wbSign": "z/UWXtMocpzA8BRxcmCB3DVhKfbzCaI+lGcmnChrQ9NJvoW86PW5oSKIcukXl/VR/IBLTmeCAWQW5WUT41vnriPE3sVUjdkW7qzLNXGPGxed",
        "platform-timestamp": "1783239663516"
    }

    payload = {
        "page": 1,
        "pageSize": 20,
        "offset": 0
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}
