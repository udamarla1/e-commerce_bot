import gradio as gr
from src.main import retrieval_chain, client


def final_response(user_query):
    # Invoking the retrieval chain with the user's query to fetch relevant product information
    response = retrieval_chain.invoke({"input": user_query})['answer']

    # Creating a prompt to instruct the AI to format the response properly
    # The prompt asks the AI to extract only product names from the retrieved response
    prompt = f"Format the responses properly in {response}. Just return the product names, no other text"

    # Sending the formatted prompt to the GPT-4o-mini model for processing
    openai_response = client.chat.completions.create(
        model='gpt-4o-mini',  # Using GPT-4o-mini model for response generation
        messages=[{'role': 'user', 'content': prompt}]  # Providing the prompt to the model
    )

    # Extracting and returning the AI-generated response containing only the product names
    return openai_response.choices[0].message.content


demo = gr.Interface(
    fn=final_response,
    inputs=gr.Textbox(label="Product search", placeholder="What product are you looking for?"),
    outputs=gr.Textbox(label="Recommended products"),
    title="E-commerce Product Search",
)


if __name__ == "__main__":
    demo.launch()