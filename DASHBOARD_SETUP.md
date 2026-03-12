# Subscription Dashboard Setup Guide

## Dashboard Features

The dashboard includes:
✅ **Add Subscription Form** - Create new subscriptions with service name, cost, type, dates, and auto-pay option
✅ **Subscriptions Table** - View all subscriptions with status, days remaining, and auto-pay status
✅ **Edit & Delete Buttons** - Modify or remove subscriptions
✅ **Total Monthly Spend Display** - Shows aggregated monthly costs
✅ **Upcoming Renewals Section** - Displays subscriptions expiring soon with countdown
✅ **Statistics Cards** - Quick overview of total subscriptions and active subscriptions

## How to Run

### Prerequisites
- Python 3.8+
- Virtual environment (venv) activated

### Step 1: Start the Backend API

```powershell
# Navigate to the project directory
cd "c:\Users\TS6208_TEJASHWANI\Desktop\Subscription project_git"

# Activate virtual environment (if not already activated)
.\venv\Scripts\Activate.ps1

# Install dependencies (if not already installed)
pip install fastapi uvicorn sqlalchemy

# Run the FastAPI server
uvicorn main:app --reload
```

The API will start at: `http://localhost:8000`

### Step 2: Access the Dashboard

Once the backend is running, you can access the dashboard in two ways:

**Option 1: Open the HTML file directly**
- Navigate to: `c:\Users\TS6208_TEJASHWANI\Desktop\Subscription project_git\index.html`
- Double-click to open in your default browser

**Option 2: Access via FastAPI**
- Go to: `http://localhost:8000/dashboard-ui`
- The API serves the dashboard directly

### API Endpoints Available

- `GET /dashboard` - Get dashboard data with all stats
- `GET /subscriptions/{id}` - Get a specific subscription
- `POST /subscriptions` - Create a new subscription
- `PUT /subscriptions/{id}` - Update a subscription
- `DELETE /subscriptions/{id}` - Delete a subscription
- `GET /subscriptions/search?title=search_term` - Search subscriptions

## Dashboard Usage

### Adding a Subscription
1. Fill in the form on the left side:
   - Service Name (e.g., Netflix, Spotify)
   - Monthly Cost
   - Type (Monthly/Yearly/Weekly)
   - Start and End dates
   - Toggle Auto-Pay if applicable
2. Click "Add Subscription"
3. The dashboard updates automatically

### Editing a Subscription
1. Click the "Edit" button in the Actions column
2. Update the fields in the modal
3. Click "Update Subscription"

### Deleting a Subscription
1. Click the "Delete" button in the Actions column
2. Confirm the deletion

### Dashboard Statistics
- **Total Monthly Spend**: Sum of all active monthly subscriptions
- **Total Subscriptions**: Count of all subscriptions
- **Active Subscriptions**: Count of currently active subscriptions

### Upcoming Renewals
- Shows subscriptions expiring within the next 30 days
- Displays the exact number of days until renewal
- Sorted by renewal date (soonest first)

## Troubleshooting

### CORS Errors
If you see CORS errors in the browser console, ensure the backend is running with CORS enabled (already configured in main.py).

### Cannot Connect to API
- Verify the backend is running: `http://localhost:8000/docs`
- Check that the API is running on port 8000
- Ensure firewall isn't blocking localhost connections

### Dashboard Not Loading Data
1. Open browser DevTools (F12)
2. Check the Console tab for errors
3. Verify the API endpoint is correct in the browser console
4. Check that the database has been initialized

## File Structure

```
├── index.html          # Main dashboard UI
├── main.py             # FastAPI application with CORS
├── models.py           # SQLAlchemy models
├── schemas.py          # Pydantic schemas
├── crud.py             # Database operations
├── database.py         # Database configuration
├── requirements.txt    # Python dependencies
└── DASHBOARD_SETUP.md  # This file
```

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Performance Notes

- Dashboard loads with initial API call to `/dashboard`
- Auto-refresh happens when adding/editing/deleting subscriptions
- Table updates dynamically without page reload

## Future Enhancements

Consider adding:
- Subscription filtering by type
- Export to CSV functionality
- Recurring reminder notifications
- Dark mode toggle
- Mobile app version
