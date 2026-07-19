import resend

resend.api_key = "re_RXx2iwED_JhrTBF55wVXLbVbUKDw4icK"

try:
    response = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": ["g40834942@gmail.com"],
        "subject": "Test",
        "text": "Hello from Resend!"
    })
    print(response)
except Exception as e:
    print(e)