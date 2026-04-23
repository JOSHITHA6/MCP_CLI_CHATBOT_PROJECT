import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")

docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}


@mcp.tool()
def read_doc(doc_id: str) -> str:
    """Read the contents of a document by its ID."""
    if doc_id not in docs:
        return f"Error: Document '{doc_id}' not found."
    return docs[doc_id]


@mcp.tool()
def edit_doc(doc_id: str, new_content: str) -> str:
    """Edit the contents of a document by its ID."""
    if doc_id not in docs:
        return f"Error: Document '{doc_id}' not found."
    docs[doc_id] = new_content
    return f"Document '{doc_id}' updated successfully."


@mcp.resource("docs://documents")
def list_documents() -> str:
    """Return all document IDs as a JSON list."""
    return json.dumps(list(docs.keys()))


@mcp.resource("docs://documents/{doc_id}")
def get_document(doc_id: str) -> str:
    """Return the contents of a specific document."""
    if doc_id not in docs:
        return f"Error: Document '{doc_id}' not found."
    return docs[doc_id]


@mcp.prompt()
def format_as_markdown(doc_id: str) -> str:
    """Rewrite a document in clean markdown format."""
    content = docs.get(doc_id, f"Document '{doc_id}' not found.")
    return f"Please rewrite the following document in clean, well-structured markdown:\n\n{content}"


@mcp.prompt()
def summarize(doc_id: str) -> str:
    """Summarize a document concisely."""
    content = docs.get(doc_id, f"Document '{doc_id}' not found.")
    return f"Please provide a concise summary of the following document:\n\n{content}"


if __name__ == "__main__":
    mcp.run(transport="stdio")