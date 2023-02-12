from rest_framework.throttling import UserRateThrottle


class ApplyRateThrottle(UserRateThrottle):
    scope = "apply"
