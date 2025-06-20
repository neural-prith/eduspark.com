/**
 * Chat Persona Integration
 * Connects farmer personas with chat functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize persona integration after a short delay
    setTimeout(initializePersonaIntegration, 500);
});

function initializePersonaIntegration() {
    console.log('🧑‍🌾 Initializing Persona Integration...');
    
    // Update chat suggestions with Indian farmer context
    updateSuggestionsForIndianFarmers();
    
    // Add cultural elements to chat
    addCulturalElements();
    
    // Monitor for persona changes
    monitorPersonaChanges();
}

function updateSuggestionsForIndianFarmers() {
    const suggestions = document.querySelectorAll('.suggestion-chip');
    
    const indianFarmerSuggestions = [
        'मेरी फसल में कीड़े लग रहे हैं (Pest problem)',
        'PM-KISAN scheme के बारे में बताएं',
        'Organic farming कैसे शुरू करें?',
        'Weather forecast और farming tips'
    ];
    
    suggestions.forEach((chip, index) => {
        if (indianFarmerSuggestions[index]) {
            chip.textContent = indianFarmerSuggestions[index];
        }
    });
}

function addCulturalElements() {
    // Add Indian flag and cultural symbols to the interface
    const chatHeader = document.querySelector('.chat-title');
    if (chatHeader) {
        const culturalBadge = document.createElement('div');
        culturalBadge.innerHTML = '🇮🇳 Made for Indian Farmers | भारतीय किसानों के लिए';
        culturalBadge.style.cssText = `
            font-size: 0.8rem;
            color: var(--indian-saffron, #FF9933);
            font-weight: 600;
            margin-top: 5px;
        `;
        chatHeader.appendChild(culturalBadge);
    }
}

function monitorPersonaChanges() {
    // Listen for persona selection events
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('persona-select-btn')) {
            const personaType = e.target.getAttribute('data-persona');
            if (personaType) {
                updateUIForPersona(personaType);
            }
        }
    });
}

function updateUIForPersona(personaType) {
    const personaNames = {
        'experienced_traditional': 'राम बाबू (Ram Babu)',
        'tech_savvy_modern': 'अनिल शर्मा (Anil Sharma)',
        'small_scale_organic': 'सुमित्रा देवी (Sumitra Devi)',
        'young_entrepreneur': 'विकास पटेल (Vikas Patel)',
        'southern_progressive': 'रमेश गौड़ा (Ramesh Gowda)'
    };
    
    // Update current persona display
    const currentPersona = document.getElementById('currentPersona');
    if (currentPersona && personaNames[personaType]) {
        const personaInfo = currentPersona.querySelector('.info h5');
        if (personaInfo) {
            personaInfo.textContent = personaNames[personaType];
        }
    }
    
    // Show success notification
    showNotification(`Selected: ${personaNames[personaType]} as your farming advisor!`, 'success');
}

function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `persona-notification ${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <span>${message}</span>
            <button class="notification-close">&times;</button>
        </div>
    `;
    
    // Styling
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: white;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 10000;
        max-width: 300px;
        animation: slideInRight 0.3s ease;
        border-left: 4px solid ${type === 'success' ? '#2ecc71' : '#3498db'};
    `;
    
    document.body.appendChild(notification);
    
    // Auto remove
    setTimeout(() => {
        if (notification.parentElement) {
            notification.remove();
        }
    }, 3000);
    
    // Manual close
    notification.querySelector('.notification-close').addEventListener('click', () => {
        notification.remove();
    });
}

// Add animation keyframes
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
`;
document.head.appendChild(style); 