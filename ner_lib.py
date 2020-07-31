from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline


class Ner():
    """
    Create NER model from given Huggingface model
    """
    def __init__(self, model="kuzgunlar/electra-turkish-ner"):
        tokenizer = AutoTokenizer.from_pretrained(model)
        model = AutoModelForTokenClassification.from_pretrained(model)

        self.ner_model = pipeline("ner", model=model, tokenizer=tokenizer, grouped_entities=True)

    def entities(self, context):
        """Find and return entities in given context

        Args:
            context (str): Context

        Returns:
            arr: Entities
        """
        return self.ner_model(context)


if __name__ == "__main__":
    ner = Ner()
    context = "Metehan gelmiş geçmiş en büyük Moğol İmparatorluğunu kurdu."

    print(ner.entities(context))
