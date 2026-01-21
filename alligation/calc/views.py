from django.shortcuts import render

def alligation_form(request):
    return render(request, 'calc/form.html')

def results(request):
    if request.method == "POST":
        try:
            high_strength = float(request.POST["high_strength"])
            low_strength = float(request.POST["low_strength"])
            desired_strength = float(request.POST["desired_strength"])
            total_volume = float(request.POST["total_volume"])

        except (KeyError, ValueError):
            return render(request, 
            "calc/form.html",
            {'error_message': "Please enter valid numbers"}
            )

        #validating non-percentage inputs
        if high_strength > 100 or low_strength > 100 or desired_strength > 100:
            return render(
                request,
                "calc/form.html",
                {"error_message": "Strength values must be percentages! (0-100)"}
            )

        #validating user input
        if not (high_strength > low_strength):
            return render(
                request,
                "calc/form.html",
                {"error_message": "High strength must be greater than low strength!"}
            )

        if not (low_strength < desired_strength < high_strength):
            return render(
                request,
                "calc/form.html",
                {"error_message": "Desired strength must be between low and high strengths!"}
            )


        #performing the calculations
        high_volume = total_volume * (desired_strength - low_strength) / (high_strength - low_strength)
        low_volume = total_volume - high_volume

        return render(
            request,
            "calc/results.html",
            {
                "high_volume": round(high_volume, 1),
                "low_volume": round(low_volume, 1),
                "total_volume": total_volume,
                "high_strenth": low_strength,
                "desired_strenth": desired_strength
            }
        )

    else:
        return render(request, 'calc/form.html')







