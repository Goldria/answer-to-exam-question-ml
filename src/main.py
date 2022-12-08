import streamlit as st
from transformers import pipeline


def get_context():
    return st.text_area(
        label="Введите текст:",
        placeholder="My name is Wolfgang and I live in Berlin"
    )


def get_question():
    return st.text_area(
        label="Введите вопрос:",
        placeholder="Where do I live?"
    )


def main():
    st.title(
        "Генератор возможных ответов на вопросы по тексту ЕГЭ (английский язык, 12-18 задания)"
    )

    context_input = get_context()
    question_input = get_question()

    model_name = "deepset/roberta-base-squad2"

    nlp = pipeline("question-answering",
                   model=model_name,
                   tokenizer=model_name
                   )

    if context_input != "" and question_input != "":
        qa_input = {
            "question": question_input,
            "context": context_input
        }
        result = nlp(qa_input)

        st.caption("**Результат, сгенерированный на основе текста, на вопрос:**")
        st.write(result["answer"])
    elif context_input != "" and question_input == "":
        st.caption("**Вопрос обработан:**")
        st.write(context_input)
    elif context_input == "" and question_input != "":
        st.caption("**Текст обработан:**")
        st.write(question_input)


if __name__ == "__main__":
    main()