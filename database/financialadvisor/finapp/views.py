from django.shortcuts import render
from django.http import JsonResponse

from financialadvisor.finapp.utilities import signup_u

import json

def signup(request):
    if request.method == "POST":
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")
    

            # Validate inputs
            if not all([username, email, password]):
                return JsonResponse({"status": "error", "message": "All fields are required!"})

            # Call the add_user function
            result = signup_u(username, email, password)
            return JsonResponse(result)

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON data!"})