// Configuration for different environments
const config = {
    // GitHub Pages deployment
    production: {
        apiBaseUrl: 'https://student-management-system-backend.onrender.com/api', // Update this with your backend URL
        isDemoMode: false
    },
    // Demo mode (no backend required)
    demo: {
        apiBaseUrl: '',
        isDemoMode: true
    },
    // Local development
    development: {
        apiBaseUrl: `${window.location.protocol}//${window.location.host}/api`,
        isDemoMode: false
    }
};

// Auto-detect environment
function getEnvironment() {
    const hostname = window.location.hostname;
    
    // Check if running on GitHub Pages
    if (hostname.includes('github.io')) {
        return 'production';
    }
    
    // Check if localhost
    if (hostname === 'localhost' || hostname === '127.0.0.1') {
        return 'development';
    }
    
    // Default to demo mode for other cases
    return 'demo';
}

// Get current configuration
const currentEnv = getEnvironment();
const appConfig = config[currentEnv];

// Export configuration
window.APP_CONFIG = appConfig;

console.log(`Running in ${currentEnv} mode`, appConfig);