# MCP CLI Chatbot

A CLI-based chatbot built with the Model Context Protocol (MCP), powered by Databricks-hosted Claude.

## Project Structure

```
mcp_project/
├── core/
│   ├── __init__.py
│   ├── chat.py            # Base chat loop logic
│   ├── cli.py             # Terminal UI with autocomplete
│   ├── cli_chat.py        # CLI-specific chat with resource/prompt support
│   ├── databricks_llm.py  # Databricks LLM client (drop-in for Anthropic)
│   └── tools.py           # MCP tool execution manager
├── .env                   # Your API keys (never commit this!)
├── .gitignore
├── main.py                # Entry point
├── mcp_client.py          # MCP client wrapper
├── mcp_server.py          # MCP server with tools, resources, prompts
├── requirements.txt
└── README.md
```

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure your API key

Edit `.env` and paste your Databricks token:

```
DATABRICKS_TOKEN=your_actual_token_here
```

### 3. Run the chatbot

```bash
python main.py
```

## Usage

Once running, you'll see a `>` prompt. You can:

- **Ask questions**: just type naturally
- **Mention a document**: use `@filename` e.g. `what is @report.pdf about?`
- **Use a prompt command**: type `/` to see available commands e.g. `/summarize report.pdf`

Press `Ctrl+C` to exit.

## Available Documents

The server comes preloaded with these sample documents:

| Document | Description |
|---|---|
| `deposition.md` | Testimony of Angela Smith, P.E. |
| `report.pdf` | State of a 20m condenser tower |
| `financials.docx` | Project budget and expenditures |
| `outlook.pdf` | Projected future performance |
| `plan.md` | Project implementation steps |
| `spec.txt` | Technical equipment requirements |