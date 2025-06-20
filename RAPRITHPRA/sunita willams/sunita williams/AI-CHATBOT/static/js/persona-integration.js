/**
 * Persona Integration for Chat System
 * Connects the farmer persona system with the existing chat functionality
 */

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeFarmerPersonaSystem();
});

function initializeFarmerPersonaSystem() {
    console.log('🧑‍🌾 Initializing Farmer Persona System...');
    
    // Wait for the main persona system to load
    setTimeout(() => {
        if (window.farmerPersonaSystem) {
            console.log('✅ Farmer persona system loaded successfully');
            
            // Update chat suggestions for Indian farmers
            updateChatSuggestionsForPersona();
            
            // Add persona indicators to messages
            observeNewMessagesForPersona();

            // Integrate persona context with existing sendMessage function
            enhanceSendMessageWithPersona();
        } else {
            console.log('⏳ Waiting for persona system...');
            // Retry after a short delay
            setTimeout(initializeFarmerPersonaSystem, 500);
        }
    }, 100);
}

function updateChatSuggestionsForPersona() {
    const suggestions = document.querySelectorAll('.suggestion-chip');
    
    // Define persona-specific suggestions in Hindi-English mix (Indian farmer style)
    const personaSuggestions = {
        'experienced_traditional': [
            'पारंपरिक तरीकों से गेहूं कैसे उगाएं?',
            'How to save water in farming?',
            'बारिश के पानी का संरक्षण कैसे करें?',
            'Traditional pest control methods'
        ],
        'tech_savvy_modern': [
            'Drip irrigation system लगवाना है',
            'Best farming apps for Indian farmers',
            'Precision agriculture techniques',
            'Weather monitoring technology की जानकारी'
        ],
        'small_scale_organic': [
            'Organic fertilizer कैसे बनाएं?',
            'Natural pesticides घर पर कैसे बनाएं?',
            'Kitchen garden planning tips',
            'Compost making at home'
        ],
        'young_entrepreneur': [
            'Export market opportunities',
            'Agricultural business loans कैसे लें?',
            'Value addition in farming',
            'Digital marketing for farmers'
        ],
        'southern_progressive': [
            'Climate change adaptation strategies',
            'Research-based farming techniques',
            'Sustainable agriculture practices',
            'Scientific soil testing methods'
        ]
    };
    
    // Update suggestions when persona changes
    function updateSuggestions() {
        const currentPersona = window.farmerPersonaSystem?.currentPersona || 'experienced_traditional';
        const newSuggestions = personaSuggestions[currentPersona] || personaSuggestions['experienced_traditional'];
        
        suggestions.forEach((suggestion, index) => {
            if (newSuggestions[index]) {
                suggestion.textContent = newSuggestions[index];
                
                // Add click handler for persona suggestions
                suggestion.onclick = function() {
                    const userInput = document.getElementById('userMessage');
                    if (userInput) {
                        userInput.value = this.textContent;
                        // Trigger send message if the function exists
                        if (typeof sendMessage === 'function') {
                            sendMessage(this.textContent);
                        }
                    }
                };
            }
        });
    }
    
    // Update initially and when persona changes
    updateSuggestions();
    
    // Listen for persona changes
    document.addEventListener('personaChanged', updateSuggestions);
}

function observeNewMessagesForPersona() {
    const chatbox = document.getElementById('chatbox');
    if (!chatbox) return;
    
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            mutation.addedNodes.forEach(function(node) {
                if (node.nodeType === 1 && node.classList.contains('message') && node.classList.contains('assistant')) {
                    addPersonaIndicatorToMessage(node);
                }
            });
        });
    });
    
    observer.observe(chatbox, { childList: true, subtree: true });
}

function addPersonaIndicatorToMessage(messageElement) {
    // Wait for persona system to be loaded
    setTimeout(() => {
        if (!window.farmerPersonaSystem) return;
        
        const personaType = window.farmerPersonaSystem.currentPersona || 'auto';
        
        if (personaType !== 'auto' && window.farmerPersonaSystem.personas[personaType]) {
            const persona = window.farmerPersonaSystem.personas[personaType];
            const messageInfo = messageElement.querySelector('.message-info');
            
            if (messageInfo && !messageInfo.querySelector('.persona-indicator')) {
                const personaIndicator = document.createElement('span');
                personaIndicator.className = 'persona-indicator';
                personaIndicator.innerHTML = `${persona.avatar} ${persona.name}`;
                personaIndicator.style.cssText = `
                    font-size: 0.8rem;
                    color: var(--indian-saffron, #FF9933);
                    margin-left: 10px;
                    font-weight: 600;
                    padding: 2px 8px;
                    background: rgba(255, 153, 51, 0.1);
                    border-radius: 12px;
                    border: 1px solid var(--indian-saffron, #FF9933);
                    display: inline-block;
                `;
                messageInfo.appendChild(personaIndicator);
            }
        }
    }, 100);
}

function enhanceSendMessageWithPersona() {
    // Check if sendMessage function exists
    if (typeof window.sendMessage !== 'function') {
        console.log('⚠️ sendMessage function not found, will retry...');
        setTimeout(enhanceSendMessageWithPersona, 1000);
        return;
    }
    
    // Store original sendMessage function
    const originalSendMessage = window.sendMessage;
    
    // Enhance sendMessage with persona context
    window.sendMessage = function(message, imageFile = null) {
        let enhancedMessage = message;
        
        // Add persona context if available
        if (window.farmerPersonaSystem && window.farmerPersonaSystem.currentPersona !== 'auto') {
            const personaContext = {
                persona_type: window.farmerPersonaSystem.currentPersona,
                farming_region: window.farmerPersonaSystem.getFarmingRegion(),
                primary_crops: window.farmerPersonaSystem.getPrimaryCrops(),
                farming_style: window.farmerPersonaSystem.getFarmingStyle()
            };
            
            // Add context marker for backend processing
            enhancedMessage = `[PERSONA:${personaContext.persona_type}] ${message}`;
            
            console.log('📤 Sending message with persona context:', personaContext.persona_type);
        }
        
        // Call original function with enhanced message
        return originalSendMessage.call(this, enhancedMessage, imageFile);
    };
    
    console.log('✅ Enhanced sendMessage with persona context');
}

// Add welcome message with cultural touch
function addWelcomeMessage() {
    const chatbox = document.getElementById('chatbox');
    if (!chatbox) return;
    
    const welcomeMessage = document.createElement('div');
    welcomeMessage.className = 'message assistant cultural-welcome';
    welcomeMessage.innerHTML = `
        <div class="message-avatar">
            <i class="fas fa-seedling"></i>
        </div>
        <div class="message-bubble">
            <div class="message-info">
                <span class="message-sender">EDU SPARK Assistant</span>
                <span class="message-time">Just now</span>
            </div>
            <div class="message-content">
                <div class="cultural-greeting">
                    🙏 नमस्कार! Welcome to EDU SPARK! 🌾
                </div>
                <p>I'm here to help you with agricultural guidance in the true Indian farming spirit. You can choose from our experienced farmer personas who understand regional farming practices, seasonal patterns, and traditional wisdom combined with modern techniques.</p>
                <div class="cultural-element">
                    <div class="icon">🇮🇳</div>
                    <div class="text">
                        <strong>Choose your advisor above</strong> or let me auto-select based on your questions. Each persona brings decades of farming experience from different regions of India.
                    </div>
                </div>
            </div>
        </div>
    `;
    
    // Add cultural styling
    welcomeMessage.style.cssText = `
        background: linear-gradient(135deg, rgba(255,153,51,0.05), rgba(19,136,8,0.05));
        border-left: 4px solid var(--indian-saffron, #FF9933);
        margin: 10px 0;
        border-radius: 10px;
    `;
    
    // Insert after the default welcome message
    const existingWelcome = chatbox.querySelector('.welcome-message');
    if (existingWelcome) {
        existingWelcome.insertAdjacentElement('afterend', welcomeMessage);
    } else {
        chatbox.prepend(welcomeMessage);
    }
}

// Initialize cultural welcome message
setTimeout(addWelcomeMessage, 1000);

// Export functions for external use
window.personaIntegration = {
    updateChatSuggestionsForPersona,
    addPersonaIndicatorToMessage,
    enhanceSendMessageWithPersona
}; 