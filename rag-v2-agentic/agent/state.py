class AgentState:
    def __init__(self, question: str):
        self.question = question
        self.sub_questions = []
        self.retrieved_chunks = []
        self.answers = []
        self.finished = False

    def add_sub_question(self, sq: str):
        self.sub_questions.append(sq)

    def add_retrieved_chunks(self, chunks: list[str]):
        self.retrieved_chunks.extend(chunks)

    def add_answer(self, answer: str):
        self.answers.append(answer)

    def mark_finished(self):
        self.finished = True
