# D Auditor Chat UI - Tax Consultation Interface

## Overview
This project implements an interactive chat interface for Deloitte auditors to get instant, accurate responses to tax-related queries. The system uses the Groq API to provide detailed tax information, compliance guidance, and professional tax advice.

## Features
- Real-time tax consultation interface
- Business/Client focused tax queries
- Strict tax-related query validation
- Professional Deloitte branding and UI
- Responsive design for various screen sizes
- Interactive chat with instant responses
- Comprehensive tax knowledge base

## Technical Stack
- Frontend: HTML5, CSS3, JavaScript
- Backend: Python Flask
- API: Groq LLM API
- Database: SQLite (for conversation history)

## Prerequisites
- Python 3.x
- Flask
- Groq API key
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd deloitte-auditor-chat-ui
```

2. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # For Unix/MacOS
# or
.venv\Scripts\activate  # For Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with:
```
GROQ_API_KEY=your_api_key_here
```

## Running the Application

1. Start the Flask server:
```bash
python3 app.py
```

2. Access the application:
Open your browser and navigate to `http://localhost:5001`

## Usage Guidelines

### Valid Tax-Related Queries
The system accepts questions related to:
- Tax deductions and credits
- Business tax compliance
- International tax implications
- Tax documentation requirements
- Audit preparation
- Tax code interpretations

### Example Queries
✅ Valid Questions:
- "What documentation should I maintain for business expense deductions to prevent audit risks?"
- "What are the tax implications for my business if we have international subsidiaries?"
- "How do the recent changes in Section 80D affect my company's health insurance tax deductions?"

❌ Invalid Questions:
- "What's the best restaurant for a business lunch?"
- "How do I improve workplace culture?"
- "What's the best software for project management?"

## Features Demonstrated in Screenshots

![images](/working/1.png)

## Security and Best Practices
- API key protection through environment variables
- Input validation for tax-related queries
- Error handling for API requests
- Professional response formatting
- Secure data handling

## Troubleshooting
1. If the application doesn't start:
   - Check if Python and required packages are installed
   - Verify the virtual environment is activated
   - Ensure the GROQ_API_KEY is properly set

2. If queries aren't working:
   - Verify internet connection
   - Check API key validity
   - Ensure query contains tax-related keywords

## Contributing
Please follow the project's coding standards and submit pull requests for any enhancements.
