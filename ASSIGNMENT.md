# Deloitte Auditor Chat UI - Assignment Documentation

## Assignment Requirements

### Scenario
As part of the Deloitte Auditor team that specializes in development of Audit for commercial companies and individuals, we need a web interface to help auditors with US Tax law and tax deductions to benefit clients.

### Technology Requirements
- Develop a web interface with RESTful connectivity
- Limit prompts to tax-related questions using prompt engineering
- Store responses in the client's local system

## Implementation Details

### 1. User Interface
The implementation includes a clean, responsive UI with Deloitte branding that matches the provided mockup:
- Header with "Deloitte Auditor Enterprise Chat UI" title and Deloitte logo
- Tax Prompt input area for entering questions
- Send and Cancel buttons with appropriate styling
- Response area to display AI-generated answers
- Chat History section to view previous conversations

### 2. RESTful API Integration
The application integrates with the Grok AI API using RESTful principles:
- HTTP POST requests to the API endpoint
- JSON request and response format
- Proper authentication using API keys
- Error handling for API responses

### 3. Prompt Engineering
To ensure the system only handles tax-related questions:
- Client-side validation checks if the question contains tax-related keywords
- System prompt instructs the AI to only answer tax-related questions
- AI is configured to politely decline non-tax questions
- Specialized tax advisor persona is established in the system prompt

### 4. Local Storage
All conversations are saved to the client's local system using:
- Browser's localStorage API
- Structured data format with timestamps
- Limit of 50 conversations to prevent excessive storage use
- Persistent storage that survives page refreshes

### 5. Error Handling
The application includes comprehensive error handling:
- Validation for empty inputs
- API error detection and display
- Network error handling
- User-friendly error messages

### 6. Technologies Used
- HTML5, CSS3, JavaScript for frontend development
- Vite for modern bundling and development
- Fetch API for RESTful communication
- LocalStorage API for client-side data persistence

## How to Run the Application
1. Install dependencies: `npm install`
2. Configure the API key in the `.env` file
3. Start the development server: `npm run dev`
4. Access the application at http://localhost:3001 (or another available port)

## Testing the Application
1. Enter a tax-related question (e.g., "What are the tax deductions available for small businesses?")
2. Click "Send" or press Enter
3. View the AI-generated response
4. Check that the conversation is saved in the Chat History section
5. Try a non-tax question to verify the filtering works

## Conclusion
This implementation successfully meets all the requirements specified in the assignment. It provides a user-friendly interface for Deloitte auditors to ask tax-related questions, receive accurate responses, and store the conversation history locally. 