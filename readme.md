# LangGraph Samples

A collection of practical examples and samples demonstrating how to build intelligent agents and workflows using [LangGraph](https://github.com/langchain-ai/langgraph).

## Overview

This repository contains various sample implementations showcasing different patterns, techniques, and use cases for building with LangGraph. Whether you're just getting started or looking to implement advanced agent architectures, you'll find useful examples here.

## What is LangGraph?

LangGraph is a library for building stateful, multi-actor applications with LLMs. It allows you to create complex workflows with branching logic, loops, and state management—perfect for building autonomous agents and interactive systems.

## Repository Structure

```
langgraph-samples/
├── agents/          # Example agent implementations
├── workflows/       # Workflow pattern examples
├── tools/           # Custom tool implementations
└── readme.md        # This file
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip or conda for package management

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ahmedsaud-01/langgraph-samples.git
cd langgraph-samples
```

2. Install dependencies:
```bash
pip install langgraph langchain openai
```

3. Set up your environment variables:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Examples Included

### Agents
- Basic agent implementations
- Multi-tool agents
- Specialized agent patterns

### Workflows
- Sequential workflows
- Conditional logic flows
- Parallel execution patterns

### Tools
- Tool integration examples
- Custom tool creation

## Usage

Each example is self-contained and can be run independently. Refer to individual files for specific instructions.

Example:
```python
from langgraph.graph import Graph

# Create and configure your graph
graph = Graph()
# ... add nodes and edges
# ... execute

result = graph.invoke({"input": "your prompt"})
print(result)
```

## Documentation

For detailed documentation on LangGraph:
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)

## Contributing

Contributions are welcome! If you have examples or improvements you'd like to share:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-example`)
3. Commit your changes (`git commit -am 'Add new example'`)
4. Push to the branch (`git push origin feature/your-example`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation and examples
- Refer to the official LangGraph repository

## Author

**Ahmed Saud** - [GitHub Profile](https://github.com/ahmedsaud-01)

---

Happy building with LangGraph! 🚀
