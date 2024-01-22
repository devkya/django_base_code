from rest_framework.response import Response


def success_response(*args):
    res_data = {"success": True}
    for arg in args:
        res_data.update(arg)
    return Response(res_data)
