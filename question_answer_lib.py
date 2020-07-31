from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline


class QuentionAnswer():
    """
    Create Question Answer model from given Huggingface model
    """
    def __init__(self, model="kuzgunlar/electra-turkish-qa"):
        tokenizer = AutoTokenizer.from_pretrained(model)
        model = AutoModelForQuestionAnswering.from_pretrained(model)

        self.question_answer_model = pipeline("question-answering", model=model, tokenizer=tokenizer)

    def answer(self, question, context):
        """Create answer from context for given question

        Args:
            question (str): Question
            context (str): Context

        Returns:
            dict: Answer
        """
        inputs = {
            "question": question,
            "context": context
        }
        return self.question_answer_model(inputs)


if __name__ == "__main__":
    qa = QuentionAnswer()
    context = "Metehan gelmiş geçmiş en büyük Moğol imparatorluğunu kurdu."
    question = "Metehan kimdir?"

    print(qa.answer(question, context))
