from urllib.request import Request,urlopen
from urllib.parse import quote,urlencode
import webbrowser
payload_dict={'loginfmt':'adu@noctrl.edu'}
encode_dict=urlencode(payload_dict).encode('utf-8')
request=Request("https://login.microsoftonline.com/common/oauth2/authorize?client_id=4345a7b9-9a63-4910-a426-35363201d503&redirect_uri=https%3A%2F"\
                "%2Fwww.office.com%2Flanding&response_type=code%20id_token&scope=openid%20profile&response_mode=form_post&nonce=63745473"\
                "0525395576.MzI0YTRiYjktMTNhMC00MzgwLWEzZTItMzI5YjM4MDc3ZjgzZDRlMDNhNTAtOGJhNC00OGFkLTg3YTYtMWRhNWZiYWQwZGJl"\
                "&ui_locales=en-US&mkt=en-US&client-request-id=da9c5a77-3c8a-4993-93da-60f53e645aab&state=23LgEQYe6pVNwQ9Mfa"\
               "zVQYu6wX7mKD_lCONVRsSgjn_aVEUOOo1yOyCgslrd_SrvEvd-6Pqpj1n8bPGhnyuHVnkSB6NyLxMaFU3TZAiLZpvDlnVOoX8M8TAsvd54759Fm0l-y6ZGR4-2luRo-CrrP8"\
                "Q8r9tYjshT3nQ3V2-ZuRmYyBH5-MjEID9nWyH9xag7ThCqpnqSeE1B356RDCere5vOx5KPqopSSb_QB6n8wO0tgEGCd-zhZDUfkuL1sfRS6ut4LRXRsh3pKsQhsIqR5A&x-"\
                "client-SKU=ID_NETSTANDARD2_0&x-client-ver=6.6.0.0#",headers={"Content-Type":"application/x-www-form-urlencoded"}
                ,data=encode_dict,method="POST")
response=urlopen(request)
print(response.url)
print(response.read().splitlines()[0:10])




