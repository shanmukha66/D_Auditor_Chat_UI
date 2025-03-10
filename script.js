document.addEventListener('DOMContentLoaded', function() {
    const taxPrompt = document.getElementById('taxPrompt');
    const sendBtn = document.getElementById('sendBtn');
    const cancelBtn = document.getElementById('cancelBtn');
    const responseArea = document.getElementById('responseArea');
    const queryTypeRadios = document.querySelectorAll('input[name="queryType"]');

    // Backend API endpoint
    const API_ENDPOINT = '/api/tax-chat';
    
    // List of tax-related keywords to validate questions
    const taxKeywords = [
        'tax', 'deduction', 'credit', 'irs', 'audit', 'filing',
        'income', 'expense', 'write-off', 'depreciation', 'withholding',
        'return', 'liability', 'exemption', 'compliance', 'section',
        'revenue', 'fiscal', 'taxation', 'payroll', 'vat', 'gst',
        '1040', 'w2', 'w4', 'schedule', '1099', 'fica'
    ];

    function isTaxRelatedQuestion(question) {
        const lowerQuestion = question.toLowerCase();
        return taxKeywords.some(keyword => lowerQuestion.includes(keyword));
    }
    
    sendBtn.addEventListener('click', async function() {
        const prompt = taxPrompt.value.trim();
        
        if (!prompt) {
            alert('Please enter a question');
            return;
        }

        // Validate if the question is tax-related
        if (!isTaxRelatedQuestion(prompt)) {
            responseArea.innerHTML = `<div class="error">This appears to be a non-tax related question. Please ask a question about taxes, deductions, credits, audits, or other tax-related topics.</div>`;
            return;
        }

        // Get the selected query type
        let queryType = 'business'; // Default
        queryTypeRadios.forEach(radio => {
            if (radio.checked) {
                queryType = radio.value;
            }
        });

        // Modify prompt based on query type if needed
        let finalPrompt = prompt;
        if (queryType === 'student' && !prompt.toLowerCase().includes('student')) {
            finalPrompt = `As a student, ${prompt}`;
        }
        
        try {
            // Disable button and show loading state
            sendBtn.disabled = true;
            responseArea.innerHTML = '<div class="loading">Processing your tax question...</div>';

            // Make the API request to our backend
            const response = await fetch(API_ENDPOINT, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    prompt: finalPrompt
                })
            });

            if (!response.ok) {
                throw new Error(`API request failed with status ${response.status}: ${response.statusText}`);
            }
            
            const data = await response.json();
            
            // Extract the response content
            const llmResponse = data.response;
            
            // Display the response
            responseArea.innerHTML = `<div class="success">${llmResponse.replace(/\n/g, '<br>')}</div>`;
            
        } catch (error) {
            console.error('Error:', error);
            responseArea.innerHTML = `<div class="error">Error: ${error.message || 'An unknown error occurred'}</div>`;
        } finally {
            // Re-enable the button
            sendBtn.disabled = false;
        }
    });

    // Add keyboard shortcut (Enter to send)
    taxPrompt.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendBtn.click();
        }
    });

    cancelBtn.addEventListener('click', function() {
        taxPrompt.value = '';
        responseArea.textContent = '';
    });
    
    // Update placeholder based on selected query type
    queryTypeRadios.forEach(radio => {
        radio.addEventListener('change', function() {
            if (this.value === 'student') {
                taxPrompt.placeholder = "Enter your student tax-related question here...";
                responseArea.innerHTML = '<div class="note">Enter any student or education-related tax question to get started.</div>';
            } else {
                taxPrompt.placeholder = "Enter your business tax-related question here...";
                responseArea.innerHTML = '<div class="note">Enter any business or client tax-related question to get started.</div>';
            }
        });
    });
    
    // Initial message
    responseArea.innerHTML = '<div class="note">Please enter a tax-related question about deductions, credits, compliance, or other tax matters.</div>';
}); 