/**
 * Indian Farmer Persona System JavaScript
 * Handles persona selection, government schemes, and seasonal advice interactions
 */

class FarmerPersonaSystem {
    constructor() {
        this.currentPersona = 'auto';
        this.personas = {
            'experienced_traditional': {
                name: 'राम बाबू (Ram Babu)',
                avatar: '🧑‍🌾',
                region: 'Punjab/Haryana',
                experience: '35 years',
                specialization: ['wheat', 'rice', 'traditional methods']
            },
            'tech_savvy_modern': {
                name: 'अनिल शर्मा (Anil Sharma)',
                avatar: '👨‍💻',
                region: 'Maharashtra/Karnataka',
                experience: '12 years',
                specialization: ['precision agriculture', 'technology', 'irrigation']
            },
            'small_scale_organic': {
                name: 'सुमित्रा देवी (Sumitra Devi)',
                avatar: '👩‍🌾',
                region: 'Uttar Pradesh/Bihar',
                experience: '20 years',
                specialization: ['organic farming', 'natural pesticides', 'sustainability']
            },
            'young_entrepreneur': {
                name: 'विकास पटेल (Vikas Patel)',
                avatar: '🚀',
                region: 'Gujarat/Rajasthan',
                experience: '8 years',
                specialization: ['commercial farming', 'export markets', 'business']
            },
            'southern_progressive': {
                name: 'रमेश गौड़ा (Ramesh Gowda)',
                avatar: '🔬',
                region: 'Karnataka/Tamil Nadu',
                experience: '18 years',
                specialization: ['scientific methods', 'research', 'innovation']
            }
        };
        this.initializeEventListeners();
        this.loadCurrentPersona();
    }

    initializeEventListeners() {
        // Persona modal controls
        const showPersonasBtn = document.getElementById('showPersonasBtn');
        const personaModal = document.getElementById('personaModal');
        const closePersonaModal = document.getElementById('closePersonaModal');

        if (showPersonasBtn) {
            showPersonasBtn.addEventListener('click', () => this.showPersonaModal());
        }

        if (closePersonaModal) {
            closePersonaModal.addEventListener('click', () => this.hidePersonaModal());
        }

        // Persona selection buttons
        const personaSelectBtns = document.querySelectorAll('[data-persona]');
        personaSelectBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                const personaType = e.target.getAttribute('data-persona');
                this.selectPersona(personaType);
            });
        });

        // Government schemes modal
        const govtSchemesBtn = document.getElementById('govtSchemesBtn');
        const govtSchemesModal = document.getElementById('govtSchemesModal');
        const closeGovtSchemesModal = document.getElementById('closeGovtSchemesModal');

        if (govtSchemesBtn) {
            govtSchemesBtn.addEventListener('click', () => this.showGovtSchemesModal());
        }

        if (closeGovtSchemesModal) {
            closeGovtSchemesModal.addEventListener('click', () => this.hideGovtSchemesModal());
        }

        // Seasonal advice modal
        const seasonalAdviceBtn = document.getElementById('seasonalAdviceBtn');
        const seasonalAdviceModal = document.getElementById('seasonalAdviceModal');
        const closeSeasonalAdviceModal = document.getElementById('closeSeasonalAdviceModal');

        if (seasonalAdviceBtn) {
            seasonalAdviceBtn.addEventListener('click', () => this.showSeasonalAdviceModal());
        }

        if (closeSeasonalAdviceModal) {
            closeSeasonalAdviceModal.addEventListener('click', () => this.hideSeasonalAdviceModal());
        }

        // Close modals when clicking outside
        window.addEventListener('click', (e) => {
            if (e.target.classList.contains('persona-modal') ||
                e.target.classList.contains('govt-schemes-modal') ||
                e.target.classList.contains('seasonal-advice-modal')) {
                this.hideAllModals();
            }
        });

        // Scheme application buttons
        const schemeApplyBtns = document.querySelectorAll('.scheme-apply-btn');
        schemeApplyBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                const schemeCard = e.target.closest('.scheme-card');
                const schemeName = schemeCard.querySelector('h4').textContent;
                this.handleSchemeApplication(schemeName);
            });
        });
    }

    showPersonaModal() {
        const modal = document.getElementById('personaModal');
        if (modal) {
            modal.style.display = 'flex';
            modal.classList.add('show');
            this.updatePersonaModalSelection();
        }
    }

    hidePersonaModal() {
        const modal = document.getElementById('personaModal');
        if (modal) {
            modal.style.display = 'none';
            modal.classList.remove('show');
        }
    }

    showGovtSchemesModal() {
        const modal = document.getElementById('govtSchemesModal');
        if (modal) {
            modal.style.display = 'flex';
            modal.classList.add('show');
        }
    }

    hideGovtSchemesModal() {
        const modal = document.getElementById('govtSchemesModal');
        if (modal) {
            modal.style.display = 'none';
            modal.classList.remove('show');
        }
    }

    showSeasonalAdviceModal() {
        const modal = document.getElementById('seasonalAdviceModal');
        if (modal) {
            modal.style.display = 'flex';
            modal.classList.add('show');
            this.loadSeasonalData();
        }
    }

    hideSeasonalAdviceModal() {
        const modal = document.getElementById('seasonalAdviceModal');
        if (modal) {
            modal.style.display = 'none';
            modal.classList.remove('show');
        }
    }

    hideAllModals() {
        this.hidePersonaModal();
        this.hideGovtSchemesModal();
        this.hideSeasonalAdviceModal();
    }

    selectPersona(personaType) {
        this.currentPersona = personaType;
        this.updateCurrentPersonaDisplay();
        this.savePersonaPreference();
        this.hidePersonaModal();
        
        // Show success message
        this.showNotification(`Persona selected: ${this.personas[personaType].name}`, 'success');
        
        // Send update to backend
        this.updateBackendPersona(personaType);
    }

    updateCurrentPersonaDisplay() {
        const currentPersonaElement = document.getElementById('currentPersona');
        if (!currentPersonaElement) return;

        if (this.currentPersona === 'auto') {
            currentPersonaElement.innerHTML = `
                <div class="avatar traditional">🧑‍🌾</div>
                <div class="info">
                    <h5>Auto-Selected Persona</h5>
                    <div class="details">Based on your query | आपके सवाल के अनुसार</div>
                </div>
            `;
        } else {
            const persona = this.personas[this.currentPersona];
            currentPersonaElement.innerHTML = `
                <div class="avatar">${persona.avatar}</div>
                <div class="info">
                    <h5>${persona.name}</h5>
                    <div class="details">${persona.region} | ${persona.experience}</div>
                </div>
            `;
        }
    }

    updatePersonaModalSelection() {
        const personaCards = document.querySelectorAll('.persona-card');
        personaCards.forEach(card => {
            const personaType = card.getAttribute('data-persona');
            const selectBtn = card.querySelector('.persona-select-btn');
            
            if (personaType === this.currentPersona) {
                selectBtn.classList.add('selected');
                selectBtn.textContent = 'Selected | चुना गया';
            } else {
                selectBtn.classList.remove('selected');
                selectBtn.textContent = selectBtn.textContent.replace('Selected | चुना गया', 'Select');
            }
        });
    }

    loadCurrentPersona() {
        const saved = localStorage.getItem('farmer_persona');
        if (saved) {
            this.currentPersona = saved;
            this.updateCurrentPersonaDisplay();
        }
    }

    savePersonaPreference() {
        localStorage.setItem('farmer_persona', this.currentPersona);
    }

    async updateBackendPersona(personaType) {
        try {
            const response = await fetch('/api/set_persona', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    persona_type: personaType,
                    farming_region: this.getFarmingRegion(),
                    primary_crops: this.getPrimaryCrops(),
                    farming_style: this.getFarmingStyle()
                })
            });

            if (!response.ok) {
                throw new Error('Failed to update persona');
            }

            const result = await response.json();
            console.log('Persona updated successfully:', result);
        } catch (error) {
            console.error('Error updating persona:', error);
            this.showNotification('Failed to update persona preference', 'error');
        }
    }

    async loadSeasonalData() {
        try {
            const response = await fetch('/api/seasonal_advice');
            if (response.ok) {
                const data = await response.json();
                this.updateSeasonalDisplay(data);
            }
        } catch (error) {
            console.error('Error loading seasonal data:', error);
        }
    }

    updateSeasonalDisplay(data) {
        const currentSeasonElement = document.getElementById('currentSeason');
        const seasonalCropsElement = document.getElementById('seasonalCrops');
        const currentActivitiesElement = document.getElementById('currentActivities');

        if (currentSeasonElement) {
            currentSeasonElement.textContent = `${data.current_season.charAt(0).toUpperCase() + data.current_season.slice(1)} Season`;
        }

        if (seasonalCropsElement && data.recommended_crops) {
            seasonalCropsElement.innerHTML = data.recommended_crops
                .map(crop => `<span class="crop-tag">${crop.charAt(0).toUpperCase() + crop.slice(1)}</span>`)
                .join('');
        }

        if (currentActivitiesElement && data.current_activities) {
            currentActivitiesElement.innerHTML = data.current_activities
                .map(activity => `<li>${activity.charAt(0).toUpperCase() + activity.slice(1)}</li>`)
                .join('');
        }
    }

    handleSchemeApplication(schemeName) {
        this.showNotification(`Opening ${schemeName} application information...`, 'info');
        
        // Open relevant government website or show more information
        const schemeUrls = {
            'PM-KISAN': 'https://pmkisan.gov.in/',
            'Fasal Bima': 'https://pmfby.gov.in/',
            'Soil Health Card': 'https://soilhealth.dac.gov.in/',
            'KCC': 'https://www.nabard.org/auth/writereaddata/tender/1608180417Kisan%20Credit%20Card.pdf',
            'e-NAM': 'https://enam.gov.in/',
            'PMFBY': 'https://pmfby.gov.in/'
        };

        if (schemeUrls[schemeName]) {
            window.open(schemeUrls[schemeName], '_blank');
        }
    }

    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <span>${message}</span>
                <button class="notification-close">&times;</button>
            </div>
        `;

        document.body.appendChild(notification);

        // Auto remove after 5 seconds
        setTimeout(() => {
            if (notification.parentElement) {
                notification.remove();
            }
        }, 5000);

        // Manual close
        notification.querySelector('.notification-close').addEventListener('click', () => {
            notification.remove();
        });
    }

    getFarmingRegion() {
        return localStorage.getItem('farming_region') || 'general';
    }

    getPrimaryCrops() {
        const saved = localStorage.getItem('primary_crops');
        return saved ? JSON.parse(saved) : [];
    }

    getFarmingStyle() {
        return localStorage.getItem('farming_style') || 'mixed';
    }
}

// Initialize the persona system when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.farmerPersonaSystem = new FarmerPersonaSystem();
    
    // Add persona context to chat messages
    if (typeof window.sendMessage === 'function') {
        const originalSendMessage = window.sendMessage;
        window.sendMessage = function(message) {
            // Add persona context to the message
            const personaContext = {
                persona_type: window.farmerPersonaSystem.currentPersona,
                farming_region: window.farmerPersonaSystem.getFarmingRegion(),
                primary_crops: window.farmerPersonaSystem.getPrimaryCrops(),
                farming_style: window.farmerPersonaSystem.getFarmingStyle()
            };
            
            // Call original function with enhanced context
            return originalSendMessage.call(this, message, personaContext);
        };
    }
});

// CSS for notifications
const notificationStyles = `
    .notification {
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
    }
    
    .notification.success {
        border-left: 4px solid #2ecc71;
    }
    
    .notification.error {
        border-left: 4px solid #e74c3c;
    }
    
    .notification.info {
        border-left: 4px solid #3498db;
    }
    
    .notification-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 10px;
    }
    
    .notification-close {
        background: none;
        border: none;
        font-size: 18px;
        cursor: pointer;
        color: #666;
    }
    
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
    
    /* Modal Styles */
    .persona-modal,
    .govt-schemes-modal,
    .seasonal-advice-modal {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.5);
        z-index: 9999;
        justify-content: center;
        align-items: center;
        padding: 20px;
    }
    
    .modal-content {
        background: white;
        border-radius: 15px;
        max-width: 90vw;
        max-height: 90vh;
        overflow-y: auto;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        animation: modalFadeIn 0.3s ease;
    }
    
    .modal-header {
        padding: 20px 30px;
        border-bottom: 1px solid #eee;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .modal-header h3 {
        margin: 0;
        color: var(--indian-green);
        font-size: 1.5rem;
    }
    
    .close-btn {
        background: none;
        border: none;
        font-size: 24px;
        cursor: pointer;
        color: #666;
        padding: 5px;
    }
    
    .modal-body {
        padding: 30px;
    }
    
    @keyframes modalFadeIn {
        from {
            opacity: 0;
            transform: scale(0.9);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
`;

// Inject styles
const styleSheet = document.createElement('style');
styleSheet.textContent = notificationStyles;
document.head.appendChild(styleSheet); 