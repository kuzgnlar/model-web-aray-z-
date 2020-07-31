from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline


class Sentiment():
    """
    Create Sentiment model from given Huggingface model
    """
    def __init__(self, model="kuzgunlar/electra-turkish-sentiment-analysis"):
        tokenizer = AutoTokenizer.from_pretrained(model)
        model = AutoModelForSequenceClassification.from_pretrained(model)

        self.sentiment_model = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

    def result(self, context):
        """Find and return sentiment for given context

        Args:
            context (str): Context

        Returns:
            arr: Result
        """
        return self.sentiment_model(context)


if __name__ == "__main__":
    sentiment = Sentiment()
    context = "Ahmet arkadaşları tarafından seviliyor."

    print(sentiment.result(context))