from django.shortcuts import render

def club_matching_view(request):
    if request.method == 'POST':
        # Process form submission
        question1_answer = request.POST.get('question1')
        question2_answer = request.POST.get('question2')
        question3_answer = request.POST.get('question3')

        # Calculate scores based on user's answers
        clubs = {"CODEESI": 0, "CLICK": 0, "ADE": 0, "JCMP": 0}
        if question1_answer == 'introvert':
            clubs["CODEESI"] += 5
            clubs["CLICK"] += 5
        elif question1_answer == 'extrovert':
            clubs["ADE"] += 5
            clubs["JCMP"] += 5

        if question2_answer == 'technical':
            clubs["CODEESI"] += 5
            clubs["CLICK"] += 5
        elif question2_answer == 'soft':
            clubs["ADE"] += 5
            clubs["JCMP"] += 5
        elif question2_answer == 'both':
            clubs["CODEESI"] += 3
            clubs["CLICK"] += 3
            clubs["ADE"] += 3
            clubs["JCMP"] += 3

        if question3_answer == 'yes':
            clubs["CODEESI"] += 5
            clubs["CLICK"] += 5

        # Determine the recommended club(s)
        max_score = max(clubs.values())
        recommended_clubs = [club for club, score in clubs.items() if score == max_score]

        # Render the recommendation template with the recommended club(s)
        return render(request, 'clubmatching/recommendation.html', {'recommended_clubs': recommended_clubs})

    else:
        # Render the template containing the questions, extending from base.html
        return render(request, 'clubmatching/questions.html')
