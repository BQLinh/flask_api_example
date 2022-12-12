from datetime import datetime, timedelta

import jwt
from models.user import User


class JWT_Token:

    secret_key = None
    alg = None

    def __init__(self):
        self.alg = 'HS256'
        self.secret_key = 'aadadhkadhakbdakjdha131b@!@#$'

    def generate_token(self, user):
        now = datetime.now()

        expired_time = now + timedelta(hours=6)
        
        payload = {
            'exp': expired_time,
            'email': user.email
        }

        return jwt.encode(payload, self.secret_key, algorithm=self.alg)

    def check_token(self, token):
        try:
            jwt_payload = jwt.decode(token, self.secret_key, algorithms=[self.alg])
            email = jwt_payload.get('email')
            user = User.query.filter_by(email=email).first()

            if user is not None:
                return {'result': 'ok'}
            return {'error': 'user not founded'}

        except jwt.ExpiredSignatureError:
            return {'error': 'token is expired'}
        except Exception as e:
            print(e)
            return {'error': 'error decoding token'}



# from jwt import JWT, jwk_from_dict
# from jwt.utils import get_int_from_datetime


# class JWT_Token:
#     instance = None

#     payload = None
#     signing_key = None

#     def __init__(self):
#         self.instance = JWT()

#         self.signing_key = jwk_from_dict({
#             "p": "_clYSsO_o60GQDm1k2Qynj58Omp7ZZvTLjWehIUcPrjCcbq1v6dE2NtJq1CV_DJi3ldYB3XAgDCW3tL_tAfS4_2uWfgrEPePN8BsD7nWTzYX_olCBdZDuEYWMRqtUjItKzqx4iZZ2aY6Vk3D-wo15B3w2ZmB_dgA0Sn5lLZtWP8",
#             "kty": "RSA",
#             "q": "nJ6kpISsmLR1TvC3Mox1m7UjNBXyD4c8e_E0Wojli2YvOYohJxQeV2hLoqKLQu7jWA6BC2w538snuJA4yxUpHnBFZnyqEn3yZ_FuIbDIfoVMsjCZVJaM1Z87CP3jXAwKNevrEvfzZwB9j6b4ZHDnf_8UrS7tZGw9BheiGH_F7J8",
#             "d": "G51S9hR86-NLGHepT43MYKVvRMQeqDao0xXPIHcVdRngWqG6WpYV6xXirpLfxnA9Dq1dOw-F6hY_G63F2EO4tvXMYL2vSK-bN2VnRkPPcuvYuVpKrJBLuOfSLOV5dNWODiRfFp1S4yiKeY4a9hRO05rJKKtXoW7zeBZO3oVsiRMOSuv5yOMzSmKFrXPb0V01ZulsTO2mWbHQ3B8CUFzlcziK414etADc-AJrIrP7cIoJuW-i0mgLVMitnQ_-a_ipFrr6Svb_VTB3X3KbaOvtMJccaX-b-Z_1T883VJYfHOcFZj8bSLxqmj2D_3XsHfLivwQVbzqnhe422aHmlvh8IQ",
#             "e": "AQAB",
#             "use": "sig",
#             "kid": "7CeYLPqs2c3l63sm_1gzoP6oD6NPPqzvkbjTlwqVV4k",
#             "qi": "pqsSS4O6f-yUYcie1ymWuYadEsKu_lrBHKJRu0gZPfbOwhUxDU5ADtiMKMVA_lUAgyeq3Gku40Aew3qnZQqyLTNy_YH1E7Ld7xcEJUhTANaH-GTohf8ajnx3Y1sEtGOhp4HbtNws73LpQ7ldCBPeGZokjOg2qYgxIC5qNtfAtH4",
#             "dp": "N7dgfumCxThTSv5gcr9orX0iYODHvoL7VgXHi2h9zvdZGQbYp_7dCo76GXZTt06Iji-2z8x2Oq5wMPM52BhvoEYtZOsq6UqwUpkYIEu4VSOXGPahXA6yR157uMQWkRka-YalTvUEfNgVrqTcBd0z_6TjH6Kn-0bUxxbkCFYUo5k",
#             "alg": "RS256",
#             "dq": "aeRBARLK9zwbjFHoKv8YjTw9Hvwvexw-YrZEZWnleQiPqWGg5KEPmp1jdgRcD9cgUusLiMOVpZ_frUOlgnk-Idxar95dxr7s5CYyBglWpWRO5LNDGBPqCIzuBzhRPmzNgoONnneSU_Pa8QM9Mfu8Kag3PJhb3OfponLcH6BUG5U",
#             "n": "m0P3SiKA-YDxrMbvd3V0zwS9-9uHYwmvvefNLwya4v6J2b4Lg_aF6Wr0U2fN9A1uJGx-sQmvYzArQ-3CoulbEsSCg_-mLgKLqZFHEJV5NSKEmDm4HLR0Kpka_Hpt3YpXlN_JEgTG6C37ek1ooq91uCw0yXR_fWvQXPx2h7zFzybWoMpCf1oN8Sj63xTzCO1AMRfb7cIK_2Wjx_Dh2ig4dxpkBOfQdtqDNxhFzdyBeDEtg2Vg8J_Wg3nEq2HdBqZgl9vg6pUOpGouAz8cDuN2VLOD71vppogkHf5Gp4gnBItqlCzkbE67Q0XT98PUwpqu1EEwDuTm74C2knK-GTBaYQ"
#         })

#     def generate_token(self, user):
#         now = datetime.now()

#         expired_time = now + timedelta(hours=6)
#         self.payload = {
#             'exp': get_int_from_datetime(expired_time),
#             'email': user.email if user is not None else None,
#         }
#         return self.instance.encode(self.payload, self.signing_key, alg='RS256')

#     def check_token(self, token):
#         try:
#             self.instance.decode(token, self.signing_key, do_time_check=True)
#             return True
#         except:
#             return False