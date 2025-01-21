import typer
from typing import Optional
from typing import List  # Ensure you import List from typing if not already imported
from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2 
from phi.embedder.openai import OpenAIEmbedder
import os
from dotenv import load_dotenv
import phi.utils

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
embedder = OpenAIEmbedder(
        openai_api_key=os.getenv('OPENAI_API_KEY'))

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector2(collection = "recipes",
    db_url = db_url),
    embedder=embedder
)   

knowledge_base.load()

storage = PgAssistantStorage(table_name="pdf_assist" , db_url=db_url)

def pdf_assist(new: bool =False , user : str = "user"):
    run_id : Optional[str] = None

    if not new:
        existing_run_ids: List[str] = storage.get_all_run_ids(user)
        if len(existing_run_ids) > 0:
            run_id = existing_run_ids[0]
    assistant = Assistant(
        run_id=run_id,
        user_id=user,
        knowledge_base=knowledge_base,
        storage=storage,    
        show_tool_calls=True,
        search_knowledge=True,
        read_chat_history=True,
    )
    if run_id is None:
        run_id = assistant.run_id
        print("Starting new assistant run with run_id: ", run_id)
    else:
        print("Continuing assistant run with run_id: ", run_id)
    
    assistant.cli_app(markdown=True)

if __name__ == "__main__":
    typer.run(pdf_assist)
    