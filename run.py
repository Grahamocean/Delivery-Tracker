# from app import create_app  # <-- use app. since run.py is in root

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)


from app import create_app
from flask import request, redirect

app = create_app()

@app.before_request
def redirect_to_www_and_https():
    # Redirect to www if not present
    if request.host == "tracknavi.com":
        return redirect(request.url.replace("tracknavi.com", "www.tracknavi.com"), code=301)
    
    # Redirect to HTTPS if using HTTP
    if request.url.startswith("http://"):
        return redirect(request.url.replace("http://", "https://"), code=301)

if __name__ == '__main__':
    app.run(debug=True)
