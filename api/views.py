import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


ANNA = {
    "uuid": "68af402f-1084-40a4-b9b2-6bb5c2d11559",
    "name": "Anna",
    "yearsOfExperience": 5,
    "languages": ["python", "c"],
    "newOpportunities": True,
}

LOUIS = {
    "uuid": "0d1bd106-c585-4d6b-b3a4-d72dedf7190e",
    "name": "Louis",
    "yearsOfExperience": 3,
    "languages": ["java"],
    "newOpportunities": True,
}

MARCUS = {
    "uuid": "129e8cb2-d19c-41ad-9921-cea329bed7f0",
    "name": "Marcus",
    "yearsOfExperience": 4,
    "languages": ["c"],
    "newOpportunities": False,
}

DEVS = [ANNA, LOUIS, MARCUS]


def root(request):
    return HttpResponse(
        "<h2>DEPRECATED: ScanAPI Demo API</h2>"
        "<p>DEPRECATED: this is the old demo API. We are leaving it here only to avoid breaking external code that depends on it.</p>"
        "<p><strong>Please, use the new one</strong> <a href=https://demo.scanapi.dev/>https://demo.scanapi.dev/</a></p>"
        "<a href=https://demo.scanapi.dev/api/health>https://demo.scanapi.dev/api/health</a> (GET)<br>"
        "<a href=https://demo.scanapi.dev/api/devs>https://demo.scanapi.dev/api/devs</a> (GET, POST)<br>"
        "<a href=https://demo.scanapi.dev/api/devs?newOpportunities=true>https://demo.scanapi.dev/api/devs?newOpportunities=true</a> (GET)<br>"
        "<a href=https://demo.scanapi.dev/api/devs?newOpportunities=false>https://demo.scanapi.dev/api/devs?newOpportunities=false</a> (GET)<br>"
        "<a href=https://demo.scanapi.dev/api/languages>https://demo.scanapi.dev/api/languages</a> (GET)<br>"
        "<a href=https://demo.scanapi.dev/api/devs/129e8cb2-d19c-41ad-9921-cea329bed7f0>https://demo.scanapi.dev/api/devs/129e8cb2-d19c-41ad-9921-cea329bed7f0</a> (GET, DELETE)<br>"
        "<a href=https://demo.scanapi.dev/api/devs/129e8cb2-d19c-41ad-9921-cea329bed7f0/languages>https://demo.scanapi.dev/api/devs/129e8cb2-d19c-41ad-9921-cea329bed7f0/languages</a> (GET)<br>"
    )


def health(request):
    if request.method == "GET":
        return HttpResponse("OK!")

    return http_method_now_allowed(request.method)


@csrf_exempt
def dev_list(request):
    if request.method == "GET":
        newOpportunities = request.GET.get("newOpportunities")
        devs = filter_devs_by_new_opportunities(newOpportunities)

        return JsonResponse(devs, safe=False)

    if request.method == "POST":
        if is_not_authenticated(request):
            return not_authenticated()

        body = json.loads(str(request.body, encoding="utf-8"))
        return JsonResponse(body, status=201, safe=False)

    return http_method_now_allowed(request.method)


@csrf_exempt
def dev_details(request, identifier):
    uuid = str(identifier)
    dev = get_dev(uuid)
    if request.method == "GET":
        if not dev:
            return dev_not_found(uuid)

        return JsonResponse(dev, status=200, safe=False)

    if request.method == "DELETE":
        if is_not_authenticated(request):
            return not_authenticated()

        if not dev:
            return dev_not_found(uuid)

        return JsonResponse({"deleted": f"{uuid}"}, status=200, safe=False)

    return http_method_now_allowed(request.method)


def dev_details_languages(request, identifier):
    uuid = str(identifier)
    dev = get_dev(uuid)
    if request.method == "GET":
        if not dev:
            return dev_not_found(uuid)

        return JsonResponse(dev["languages"], status=200, safe=False)

    return http_method_now_allowed(request.method)


def language_list(request):
    return JsonResponse(["c", "go", "java", "python", "ruby"], safe=False)


def is_not_authenticated(request):
    api_key = request.headers.get("x-api-key")

    return api_key != "demoKEY123"


def not_authenticated():
    return HttpResponse(f"Failed to authenticate", status=401)


def filter_devs_by_new_opportunities(newOpportunities):
    if newOpportunities in ("False", "false", 0):
        return [dev for dev in DEVS if dev["newOpportunities"] == False]

    if newOpportunities in ("True", "true", 1):
        return [dev for dev in DEVS if dev["newOpportunities"] == True]

    return DEVS


def get_dev(uuid):
    for dev in DEVS:
        if uuid == dev["uuid"]:
            return dev


def dev_not_found(uuid):
    return HttpResponse(f"uuid {uuid} not found", status=404)


def http_method_now_allowed(request_method):
    return JsonResponse({"error": f"{request_method} Method not allowed"})
