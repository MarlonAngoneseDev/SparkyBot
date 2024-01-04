from app.classes.intention_identifier import IntentionIdentifier

data = IntentionIdentifier()

classifier = data.train_data()


while True:
    message = input()
    intent = data.predict_intent(message=message, classifier=classifier)
    print(f'Mensagem: "{message}" - Intenção: {intent}')