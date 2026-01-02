import os
from app import create_app
from app.config.database import init_db

app = create_app()

if __name__ == '__main__':
    # Initialize the database
    init_db(app)
    
    # Run the application
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
