############################### RUNS THE SITE ###############################

# NOTE: KEEP THIS SCRIPT CLEAN AND BASICALLY IMPORT ALL METHODS FROM OTHER PYTHON FILES WE WRITE

############# IMPORTS#############
# LIBRARIES
from flask import Flask, render_template, request
from sqlalchemy import create_engine

# FILES
import landing

############# GLOBAL VARIABLES #############
# CONNECT TO DATABASE

############# METHODS #############

############# PAGES #############
app = Flask(__name__)

# landing page
@app.route('/')
def home():
    page = landing.main()
    return page
# above is format for all methods below:
    # actual render_template all done in main methods of individual py scripts
    # that is returned up to this central file


# sign up page
@app.route('/signup')
def sign_up():
    page = "Sign Up page"
    return page

# connect to IMDb
@app.route('/signup/imdb')
def sign_up_imdb():
    page = "Sign Up through IMDb page"
    return page

# connect to Netflix
@app.route('/signup/netflix')
def sign_up_netflix():
    page = "Sign Up through Netflix page"
    return page

# connect to other accounts?

# import watchlist - sign up version
@app.route('/signup/watchimport')
def sign_up_watchImport():
    page = "Sign Up through Importing list"
    return page

# sign up succeed page
@app.route('/signup/success')
def sign_up_success():
    page = "Sign Up success"
    return page




# log in page
@app.route('/login')
def login():
    page = "Login Page"
    return page



# movie/show search page
@app.route('/browse')
def browse():
    page = "Browse catalog page"
    return page

# movie/show profile page


# NOTE: IF CREATE PUBLIC PROFILE KIND OF THING, CHANGE BELOW "PROFILE" ALL INTO "SETTINGS"
# user profile main page
@app.route('/profile')
def profile():
    # auto route to edit profile page
    page = "Profile main page"
    return page

# user profile edit profile page
@app.route('/profile/edit')
def profile_edit():
    page = "Profile edit page"
    return page

# user profile history and watchlist page
@app.route('/profile/history')
def profile_history():
    page = "Profile history page"
    return page

# user profile security and login page
@app.route('/profile/security')
def profile_security():
    page = "Profile security page"
    return page

# user profile linked accounts page
@app.route('/profile/linked')
def profile_linked():
    page = "Profile linked page"
    return page

# user profile content preferences page
@app.route('/profile/preferences')
def profile_preferences():
    page = "Profile preferences page"
    return page

# import watchlist - user profile version
@app.route('/profile/import')
def profile_import():
    page = "Profile import page"
    return page

# watchlist pages
@app.route('/watchlist')
def profile_watchlist():
    # will have arguments in url for each unique watchlist
    page = "Profile watchlist page"
    return page

# streaming service recommendation
@app.route('/recommendation')
def profile_recommendation():
    page = "Profile recommendation page"
    return page

# refining user preference page
@app.route('/recommendation/refine')
def profile_recommendation_refine():
    page = "Profile recommentation refine page"
    return page

# results page



# OPTIONAL TEST PAGES
# about us page
@app.route('/about')
def about():
    page = "About page"
    return page

# contact us page
@app.route('/contact')
def contact():
    page = "Contacts page"
    return page

# privacy policy page
@app.route('/privacy')
def privacy():
    page = "Privacy Policy page"
    return page

# FAQ page
@app.route('/faq')
def faq():
    page = "FAQ page"
    return page

# Requires different template from above
# sitemap page
@app.route('/sitemap')
def sitemap():
    page = "Sitemap page"
    return page

# Requires different template form above
# Report bugs page
@app.route('/bugs')
def bugs():
    page = "Report bugs page"
    return page


###############################
app.run(host='0.0.0.0', port=5000, debug=True)